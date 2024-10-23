"""
# `cimulate`

The `cimulate` package allows for easy simulation of electrical circuits. It has
a backend written in Rust and should therefore be performant enough to run
larger optimization algorithms on.
"""

from abc import ABC, abstractmethod
from typing import List, Sequence

class CircuitModel(ABC):
    """
    @private
    Abstract base class for electrical circuit models.

    This class defines the interface for circuit models that can calculate
    voltage from current and vice versa.
    """

    @abstractmethod
    def voltage(self, current: Sequence[float], sample_rate: float) -> List[float]:
        """
        Calculates the voltage based on the given current.

        Args:
            current: A sequence of current values.
            sample_rate: The sample rate of the signal.

        Returns:
            A list of voltage values corresponding to the input current.
        """
        ...
    @abstractmethod
    def current(self, voltage: Sequence[float], sample_rate: float) -> List[float]:
        """
        Calculates the current based on the given voltage.

        Args:
            voltage: A sequence of voltage values.
            sample_rate: The sample rate of the signal.

        Returns:
            A list of current values corresponding to the input voltage.
        """
        ...

class ImpedanceModel(CircuitModel):
    """
    Abstract base class for impedance models.

    This is implemented by all circuit elements and subsequently all circuits.
    You can also create custom circuit elements by subclassing this abstract
    class. You need only implement an `impedance` method.

    > CURRENT LIMITATION: Currently, you cannot implement a custom __init__
      method. I'm working on finding a fix for this, but for the time being
      you'll have to declare the attributes in the base of the class instead.

    `ImpedanceModel` implements `__add__` and `__truediv__`, which it uses to
    create series and parallel circuit connections, respectively.

    ```python
    # These all implement ImpedanceModel
    r = Resistor(100)  # 100 Ohms
    c = Capacitor(1e-6)  # 1 µF
    l = Inductor(1e-3)  # 1 mH

    # Components can be combined in series (+) and/or parallel (/)
    circuit = r + c / l
    ```
    """

    @abstractmethod
    def impedance(self, omega: float) -> complex:
        """
        Calculates the impedance at a specified angular frequency.

        Args:
            omega: The angular frequency of the signal.

        Returns:
            The impedance of the component as a complex number.
        """
        ...

    def admittance(self, omega: float) -> complex:
        """
        Calculates the admittance at a specified angular frequency.

        Args:
            omega: The angular frequency of the signal.

        Returns:
            The admittance of the component as a complex number.
        """
        ...
    def voltage(self, current: Sequence[float], sample_rate: float) -> List[float]: ...
    def current(self, voltage: Sequence[float], sample_rate: float) -> List[float]: ...
    def __add__(self, other): ...
    def __truediv__(self, other): ...

class Resistor(ImpedanceModel):
    """
    Represents a resistor in an electrical circuit.

    $$ Z(ω) = R, $$

    where $R$ is the resistance.
    """

    def __init__(self, resistance: float):
        """
        Initializes a Resistor instance.

        Args:
            resistance: The resistance value in Ohms.
        """
        ...
    def impedance(self, omega: float) -> complex: ...
    def __add__(self, other: ImpedanceModel) -> ImpedanceModel: ...
    def __truediv__(self, other: ImpedanceModel) -> ImpedanceModel: ...

class Capacitor(ImpedanceModel):
    """
    Represents a capacitor in an electrical circuit.

    $$ Z(ω) = \\frac{1}{iCω}, $$

    where $C$ is the capacitance.
    """

    def __init__(self, capacitance: float):
        """
        Initializes a Capacitor instance.

        Args:
            capacitance: The capacitance value in Farads.
        """
        ...
    def impedance(self, omega: float) -> complex: ...
    def __add__(self, other: ImpedanceModel) -> ImpedanceModel: ...
    def __truediv__(self, other: ImpedanceModel) -> ImpedanceModel: ...

class Inductor(ImpedanceModel):
    """
    Represents an inductor in an electrical circuit.

    $$ Z(ω) = iLω, $$

    where $L$ is the inductance.
    """
    def __init__(self, inductance: float):
        """
        Initializes an Inductor instance.

        Args:
            inductance: The inductance value in henries.
        """
        ...
    def impedance(self, omega: float) -> complex: ...
    def __add__(self, other: ImpedanceModel) -> ImpedanceModel: ...
    def __truediv__(self, other: ImpedanceModel) -> ImpedanceModel: ...

class Warburg(ImpedanceModel):
    """
    Represents a Warburg element in an electrical circuit.

    $$ Z(ω) = \\frac{W}{\\sqrt{ω}} + \\frac{W}{i\\sqrt{ω}}, $$

    where $W$ is the Warburg constant.
    """
    def __init__(self, w: float):
        """
        Initializes a Warburg instance.

        Args:
            w: The Warburg parameter.
        """
        ...
    def impedance(self, omega: float) -> complex: ...
    def __add__(self, other: ImpedanceModel) -> ImpedanceModel: ...
    def __truediv__(self, other: ImpedanceModel) -> ImpedanceModel: ...
