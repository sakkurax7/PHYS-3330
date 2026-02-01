import numpy as np

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