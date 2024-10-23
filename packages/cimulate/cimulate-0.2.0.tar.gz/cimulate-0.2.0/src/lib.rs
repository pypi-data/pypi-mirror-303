use std::{f64::consts::PI, sync::Arc};

use fft::{fft, fftfreq};
use num_complex::Complex;

pub mod elements;
pub mod fft;

#[cfg(feature = "python")]
mod py;

pub trait CircuitModel {
    fn voltage(&self, current: Vec<f64>, sample_rate: f64) -> Vec<f64>;
    fn current(&self, voltage: Vec<f64>, sample_rate: f64) -> Vec<f64>;
}

pub trait ImpedanceModel {
    fn impedance(&self, omega: f64) -> Complex<f64>;
    fn admittance(&self, omega: f64) -> Complex<f64> {
        1. / self.impedance(omega)
    }

    fn series<T: ImpedanceModel + Send + Sync + 'static>(self: Self, other: T) -> SeriesCircuit
    where
        Self: Sized + Send + Sync + 'static,
    {
        SeriesCircuit::new(vec![Arc::new(self), Arc::new(other)])
    }

    fn parallel<T: ImpedanceModel + Send + Sync + 'static>(self: Self, other: T) -> ParallelCircuit
    where
        Self: Sized + Send + Sync + 'static,
    {
        ParallelCircuit::new(vec![Arc::new(self), Arc::new(other)])
    }
}

impl<T: ?Sized + ImpedanceModel> CircuitModel for T {
    fn voltage(&self, current: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        let mut current_fft: Vec<Complex<f64>> =
            current.iter().map(|i| Complex::new(*i, 0.)).collect();
        fft(&mut current_fft);

        let freqs = fftfreq(current.len(), sample_rate);
        let omega = freqs.iter().map(|f| 2. * PI * f);
        let impedance = omega.map(|w| self.impedance(w));

        let mut voltage: Vec<Complex<f64>> = impedance
            .zip(current_fft.iter())
            .map(|(z, i)| z * i)
            .collect();
        fft(&mut voltage);
        voltage.iter().map(|v| v.re).collect()
    }

    fn current(&self, voltage: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        let mut voltage_fft: Vec<Complex<f64>> =
            voltage.iter().map(|v| Complex::new(*v, 0.)).collect();
        fft(&mut voltage_fft);

        let freqs = fftfreq(voltage.len(), sample_rate);
        let omega = freqs.iter().map(|f| 2. * PI * f);
        let impedance = omega.map(|w| self.impedance(w));

        let mut current: Vec<Complex<f64>> = impedance
            .zip(voltage_fft.iter())
            .map(|(z, i)| z * i)
            .collect();
        fft(&mut current);
        current.iter().map(|i| i.re).collect()
    }
}

pub struct SeriesCircuit {
    elements: Vec<Arc<dyn ImpedanceModel + Send + Sync>>,
}

impl SeriesCircuit {
    pub fn new(elements: Vec<Arc<dyn ImpedanceModel + Send + Sync>>) -> Self {
        SeriesCircuit { elements }
    }
}

impl ImpedanceModel for SeriesCircuit {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        self.elements.iter().map(|e| e.impedance(omega)).sum()
    }

    fn series<T: ImpedanceModel + Send + Sync + 'static>(
        mut self: Self,
        other: T,
    ) -> SeriesCircuit {
        self.elements.push(Arc::new(other));
        self
    }
}

pub struct ParallelCircuit {
    elements: Vec<Arc<dyn ImpedanceModel + Send + Sync>>,
}

impl ParallelCircuit {
    pub fn new(elements: Vec<Arc<dyn ImpedanceModel + Send + Sync>>) -> Self {
        ParallelCircuit { elements }
    }
}

impl ImpedanceModel for ParallelCircuit {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        let admittance: Complex<f64> = self.elements.iter().map(|e| e.admittance(omega)).sum();
        1. / admittance
    }

    fn parallel<T: ImpedanceModel + Send + Sync + 'static>(
        mut self: Self,
        other: T,
    ) -> ParallelCircuit {
        self.elements.push(Arc::new(other));
        self
    }
}
