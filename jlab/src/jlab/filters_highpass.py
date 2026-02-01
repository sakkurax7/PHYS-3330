import numpy as np

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