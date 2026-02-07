from .utils import percent_error

from .resistors import (
    parallel_resistors,
    series_resistors,
    resistor_power,
)

from .capacitors import (
    parallel_capacitors,
    series_capacitors,
)

from .voltage_dividers import (
    voltage_divider,
    current_through_voltage_divider,
    transfer_function_voltage_divider,
)

from .filters_lowpass import *
from .filters_highpass import *
from .filters_bandpass import *

from .bode_plot import *

from .opamps import *

__all__ = [
    "percent_error",
    "parallel_resistors",
    "series_resistors",
    "resistor_power",
    "parallel_capacitors",
    "series_capacitors",
    "voltage_divider",
    "current_through_voltage_divider",
    "transfer_function_voltage_divider",
    "bode_plot",
    "opamp_gain_magnitude"
]
