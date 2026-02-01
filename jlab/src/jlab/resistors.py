from __future__ import annotations
from typing import Iterable

# ----------- Resistor Calculations -----------
def parallel_resistors(resistors: Iterable[float]) -> float:
    """
    Calculate the equivalent resistance of resistors in parallel.

    Parameters:
    resistors (list): A list of resistance values in ohms.

    Returns:
    float: The equivalent resistance in ohms.
    """
    if not resistors:
        return 0.0
    reciprocal_sum = sum(1.0 / r for r in resistors if r != 0)
    if reciprocal_sum == 0:
        return float('inf')  # Infinite resistance if all resistors are open circuits
    return 1.0 / reciprocal_sum

def series_resistors(resistors: Iterable[float]) -> float:
    """
    Calculate the equivalent resistance of resistors in series.

    Parameters:
    resistors (list): A list of resistance values in ohms.

    Returns:
    float: The equivalent resistance in ohms.
    """
    return sum(resistors)

def resistor_power(voltage: float, resistance: float) -> float:
    """
    Calculate the power dissipated by a resistor.

    Parameters:
    voltage (float): The voltage across the resistor in volts.
    resistance (float): The resistance in ohms.

    Returns:
    float: The power dissipated in watts.
    """
    if resistance == 0:
        return float('inf')  # Infinite power if resistance is zero
    return (voltage ** 2) / resistance