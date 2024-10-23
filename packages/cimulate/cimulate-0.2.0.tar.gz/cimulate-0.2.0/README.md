# `cimulate`

`cimulate` is a Rust crate for modeling electrical components and circuits,
featuring Python bindings for easy integration. Combine components to create
complex circuits and perform simulations with built-in electrical elements.

## Installation

Install the Python package via pip:

```
$ pip install cimulate
```

For Rust usage, include it in your `Cargo.toml`:

```toml
[dependencies]
cimulate = "0.2"  # Replace with the current version
```

## Example

```python
from cimulate import Resistor, Capacitor, Inductor
import numpy as np

# Create components
r = Resistor(100)  # 100 Ohms
c = Capacitor(1e-6)  # 1 µF
l = Inductor(1e-3)  # 1 mH

# Combine components in series (+) and parallel (/)
circuit = r + c / l

# You can calculate the impedance (remember to use angular frequency)
frequency = np.geomspace(0.001, 1000, 1000)  # 1 mHz to 1 kHz
omega = 2 * np.pi * frequency
impedance = [circuit.impedance(w) for w in omega]

# You can even simulate voltages with a driving current
time = np.linspace(0, 60, 1000)
current = time / 6
voltage = circuit.voltage(current)
```
