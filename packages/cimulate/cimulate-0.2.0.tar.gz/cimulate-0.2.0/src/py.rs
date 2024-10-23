use std::sync::Arc;

use num_complex::Complex;
use pyo3::prelude::*;

use crate::{
    elements::{Capacitor, Inductor, Resistor, Warburg},
    CircuitModel, ImpedanceModel, ParallelCircuit, SeriesCircuit,
};

#[pyclass(subclass, name = "CircuitModel")]
struct PyCircuitModel {
    inner: Arc<dyn CircuitModel + Send + Sync>,
}

#[pymethods]
impl PyCircuitModel {
    fn voltage(&self, current: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        self.inner.voltage(current, sample_rate)
    }

    fn current(&self, voltage: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        self.inner.current(voltage, sample_rate)
    }
}

#[pyclass(subclass, name = "ImpedanceModel")]
struct PyImpedanceModel {
    inner: Option<Arc<dyn ImpedanceModel + Send + Sync>>,
}

impl PyImpedanceModel {
    fn inner(slf: Bound<'_, Self>) -> Arc<dyn ImpedanceModel + Send + Sync> {
        if let Some(inner) = slf.borrow().inner.clone() {
            inner
        } else {
            Arc::new(slf.unbind())
        }
    }
}

#[pymethods]
impl PyImpedanceModel {
    #[new]
    pub fn new() -> Self {
        Self { inner: None }
    }

    fn voltage(slf: Bound<'_, Self>, current: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        Self::inner(slf).voltage(current, sample_rate)
    }

    fn current(slf: Bound<'_, Self>, voltage: Vec<f64>, sample_rate: f64) -> Vec<f64> {
        Self::inner(slf).current(voltage, sample_rate)
    }

    fn impedance(slf: Bound<'_, Self>, omega: f64) -> Complex<f64> {
        Self::inner(slf).impedance(omega)
    }

    fn admittance(slf: Bound<'_, Self>, omega: f64) -> Complex<f64> {
        Self::inner(slf).admittance(omega)
    }

    fn __add__(slf: Bound<'_, Self>, other: Bound<'_, Self>) -> PyResult<Self> {
        Ok(PyImpedanceModel {
            inner: Some(Arc::new(SeriesCircuit::new(vec![
                Self::inner(slf),
                Self::inner(other),
            ]))),
        })
    }

    fn __truediv__(slf: Bound<'_, Self>, other: Bound<'_, Self>) -> PyResult<Self> {
        Ok(PyImpedanceModel {
            inner: Some(Arc::new(ParallelCircuit::new(vec![
                Self::inner(slf),
                Self::inner(other),
            ]))),
        })
    }
}

impl ImpedanceModel for Py<PyImpedanceModel> {
    fn impedance(&self, omega: f64) -> Complex<f64> {
        Python::with_gil(|py| {
            self.into_py(py)
                .call_method1(py, "impedance", (omega,))
                .unwrap()
                .extract(py)
                .unwrap()
        })
    }
}

#[pyclass(extends = PyImpedanceModel, name = "Resistor")]
struct PyResistor;

#[pymethods]
impl PyResistor {
    #[new]
    pub fn new(resistance: f64) -> (Self, PyImpedanceModel) {
        (
            Self,
            PyImpedanceModel {
                inner: Some(Arc::new(Resistor { resistance })),
            },
        )
    }
}

#[pyclass(extends = PyImpedanceModel, name = "Capacitor")]
struct PyCapacitor;

#[pymethods]
impl PyCapacitor {
    #[new]
    pub fn new(capacitance: f64) -> (Self, PyImpedanceModel) {
        (
            Self,
            PyImpedanceModel {
                inner: Some(Arc::new(Capacitor { capacitance })),
            },
        )
    }
}

#[pyclass(extends = PyImpedanceModel, name = "Inductor")]
struct PyInductor;

#[pymethods]
impl PyInductor {
    #[new]
    pub fn new(inductance: f64) -> (Self, PyImpedanceModel) {
        (
            Self,
            PyImpedanceModel {
                inner: Some(Arc::new(Inductor { inductance })),
            },
        )
    }
}

#[pyclass(extends = PyImpedanceModel, name = "Warburg")]
struct PyWarburg;

#[pymethods]
impl PyWarburg {
    #[new]
    pub fn new(w: f64) -> (Self, PyImpedanceModel) {
        (
            Self,
            PyImpedanceModel {
                inner: Some(Arc::new(Warburg { w })),
            },
        )
    }
}

#[pymodule]
fn cimulate(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PyCircuitModel>()?;
    m.add_class::<PyImpedanceModel>()?;
    m.add_class::<PyResistor>()?;
    m.add_class::<PyCapacitor>()?;
    m.add_class::<PyInductor>()?;
    m.add_class::<PyWarburg>()?;
    Ok(())
}
