use num_complex::Complex;

use crate::ImpedanceModel;

#[derive(Clone, Copy)]
pub struct Resistor {
    pub resistance: f64,
}

impl ImpedanceModel for Resistor {
    fn impedance(&self, _omega: f64) -> Complex<f64> {
        Complex::new(self.resistance, 0.)
    }
}

#[derive(Clone, Copy)]
pub struct Capacitor {
    pub capacitance: f64,
}

impl ImpedanceModel for Capacitor {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        if omega == 0. {
            Complex::new(f64::INFINITY, f64::INFINITY)
        } else {
            1. / Complex::new(0., self.capacitance * omega)
        }
    }
}

#[derive(Clone, Copy)]
pub struct Inductor {
    pub inductance: f64,
}

impl ImpedanceModel for Inductor {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        Complex::new(0., self.inductance * omega)
    }
}

#[derive(Clone, Copy)]
pub struct Warburg {
    pub w: f64,
}

impl ImpedanceModel for Warburg {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        if omega == 0. {
            Complex::new(f64::INFINITY, f64::INFINITY)
        } else {
            let comp = self.w / omega.sqrt();
            comp + comp / Complex::i()
        }
    }
}
