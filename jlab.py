"""
Python script to import useful functions for J-Lab
"""

import numpy as np


# ---------- Multi-use functions ----------

def percent_error(measured: float, theoretical: float) -> float:
    """
    Calculate the percent error between measured and theoretical values.

    Parameters:
    measured (float): The measured value.
    theoretical (float): The theoretical value.

    Returns:
    float: The percent error.
    """
    if theoretical == 0:
        return float('inf')  # Infinite percent error if theoretical value is zero
    return abs((measured - theoretical) / theoretical) * 100.0

# ----------- Resistor Calculations -----------
def parallel_resistors(resistors: list) -> float:
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

def series_resistors(resistors: list) -> float:
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

# ----------- Capacitor Calculations -----------
def parallel_capacitors(capacitors: list) -> float:
    """
    Calculate the equivalent capacitance of capacitors in parallel.

    Parameters:
    capacitors (list): A list of capacitance values in farads.

    Returns:
    float: The equivalent capacitance in farads.
    """
    return sum(capacitors)

def series_capacitors(capacitors: list) -> float:
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

# ----------- Voltage Divider Calculations -----------
def voltage_divider(v_in: float, resistors: list) -> list:
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
    

def current_through_voltage_divider(v_in: float, resistors: list) -> float:
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

def transfer_function_voltage_divider(resistors: list) -> list:
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


# ----------- Lowpass Filter Calculations -----------
def lowpass_transfer_function(R: float, C: float, f: float) -> complex:
    """
    Calculate the transfer function of a lowpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    complex: The transfer function H(f).
    """
    omega = 2 * np.pi * f
    return 1 / (1 + 1j * omega * R * C)

def lowpass_gain(R: float, C: float, f: float) -> float:
    """
    Calculate the gain of a lowpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The gain (magnitude of transfer function).
    """
    omega = 2 * np.pi * f
    return 1 / np.sqrt(1 + (omega * R * C) ** 2)

def lowpass_delta_angle(R: float, C: float, f: float) -> float:
    """
    Calculate the phase shift of a lowpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The phase shift in radians.
    """
    omega = 2 * np.pi * f
    return -np.arctan(omega * R * C)

def lowpass_cutoff_frequency(R: float, C: float) -> float:
    """
    Calculate the cutoff frequency of a lowpass RC filter.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.

    Returns:
    float: The cutoff frequency in hertz.
    """
    return 1 / (2 * np.pi * R * C)

# ----------- Highpass Filter Calculations -----------
def highpass_transfer_function(R: float, C: float, f: float) -> complex:
    """
    Calculate the transfer function of a highpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    complex: The transfer function H(f).
    """
    omega = 2 * np.pi * f
    return (1j * omega * R * C) / (1 + 1j * omega * R * C)

def highpass_gain(R: float, C: float, f: float) -> float:
    """
    Calculate the gain of a highpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The gain (magnitude of transfer function).
    """
    omega = 2 * np.pi * f
    return (omega * R * C) / np.sqrt(1 + (omega * R * C) ** 2)

def highpass_delta_angle(R: float, C: float, f: float) -> float:
    """
    Calculate the phase shift of a highpass RC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The phase shift in radians.
    """
    omega = 2 * np.pi * f
    return np.arctan(1 / (omega * R * C))

def highpass_cutoff_frequency(R: float, C: float) -> float:
    """
    Calculate the cutoff frequency of a highpass RC filter.

    Parameters:
    R (float): Resistance in ohms.
    C (float): Capacitance in farads.

    Returns:
    float: The cutoff frequency in hertz.
    """
    return 1 / (2 * np.pi * R * C)

# ----------- Bandpass Filter Calculations -----------
def bandpass_transfer_function(R: float, L: float, C: float, f: float) -> complex:
    """
    Calculate the transfer function of a bandpass RLC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    L (float): Inductance in henrys.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    complex: The transfer function H(f).
    """
    omega = 2 * np.pi * f
    numerator = 1j * omega * L / R
    denominator = 1 - omega**2 * L * C + 1j * omega * L / R
    return numerator / denominator

def bandpass_gain(R: float, L: float, C: float, f: float) -> float:
    """
    Calculate the gain of a bandpass RLC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    L (float): Inductance in henrys.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The gain (magnitude of transfer function).
    """
    omega = 2 * np.pi * f
    numerator = omega * L / R
    denominator = np.sqrt((1 - omega**2 * L * C) ** 2 + (omega * L / R) ** 2)
    return numerator / denominator

def bandpass_delta_angle(R: float, L: float, C: float, f: float) -> float:
    """
    Calculate the phase shift of a bandpass RLC filter at frequency f.

    Parameters:
    R (float): Resistance in ohms.
    L (float): Inductance in henrys.
    C (float): Capacitance in farads.
    f (float): Frequency in hertz.

    Returns:
    float: The phase shift in radians.
    """
    omega = 2 * np.pi * f
    return np.arctan((omega * L / R) / (1 - omega**2 * L * C))

def bandpass_center_frequency(L: float, C: float) -> float:
    """
    Calculate the center frequency of a bandpass RLC filter.

    Parameters:
    L (float): Inductance in henrys.
    C (float): Capacitance in farads.

    Returns:
    float: The center frequency in hertz.
    """
    return 1 / (2 * np.pi * np.sqrt(L * C))