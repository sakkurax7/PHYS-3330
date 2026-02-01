from __future__ import annotations
from typing import List

# ----------- Voltage Divider Calculations -----------
def voltage_divider(v_in: float, resistors: List[float]) -> List[float]:
    """
    Calculate the output voltages at each node of a voltage divider. Should ignore the first node (input voltage).

    Parameters:
    v_in (float): The input voltage in volts.
    resistors (list): A list of resistance values in ohms.

    Returns:
    list: A list of output voltages at each node in volts.
    """
    total_resistance = sum(resistors)
    voltages = []
    v_out = v_in
    for r in resistors[:-1]:
        v_drop = (r / total_resistance) * v_in
        v_out -= v_drop
        voltages.append(v_out)
        total_resistance -= r
    return voltages
    

def current_through_voltage_divider(v_in: float, resistors: List[float]) -> float:
    """
    Calculate the current through a voltage divider.

    Parameters:
    v_in (float): The input voltage in volts.
    resistors (list): A list of resistance values in ohms.

    Returns:
    float: The current in amperes.
    """
    total_resistance = sum(resistors)
    if total_resistance == 0:
        return float('inf')  # Infinite current if total resistance is zero
    return v_in / total_resistance

def transfer_function_voltage_divider(resistors: List[float]) -> List[float]:
    """
    Calculate the transfer function (voltage ratios) of a voltage divider.

    Parameters:
    resistors (list): A list of resistance values in ohms.

    Returns:
    list: A list of voltage ratios at each node.
    """
    total_resistance = sum(resistors)
    transfer_functions = []
    v_out = total_resistance
    for r in resistors[1:]:
        tf = r / v_out
        transfer_functions.append(tf)
        v_out -= r
    return transfer_functions