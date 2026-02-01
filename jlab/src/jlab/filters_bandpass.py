import numpy as np

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