from __future__ import annotations

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