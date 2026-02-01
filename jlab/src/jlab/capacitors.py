from __future__ import annotations
from typing import Iterable

# ----------- Capacitor Calculations -----------
def parallel_capacitors(capacitors: Iterable[float]) -> float:
    """
    Calculate the equivalent capacitance of capacitors in parallel.

    Parameters:
    capacitors (list): A list of capacitance values in farads.

    Returns:
    float: The equivalent capacitance in farads.
    """
    return sum(capacitors)

def series_capacitors(capacitors: Iterable[float]) -> float:
    """
    Calculate the equivalent capacitance of capacitors in series.

    Parameters:
    capacitors (list): A list of capacitance values in farads.

    Returns:
    float: The equivalent capacitance in farads.
    """
    if not capacitors:
        return 0.0
    reciprocal_sum = sum(1.0 / c for c in capacitors if c != 0)
    if reciprocal_sum == 0:
        return float('inf')  # Infinite capacitance if all capacitors are open circuits
    return 1.0 / reciprocal_sum