import numpy as np
from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt

def bode_plot(
    freqs: Union[np.ndarray, list],
    mags: Union[np.ndarray, list],
    phase: Optional[Union[np.ndarray, list]] = None,
    title: str = "Bode Plot",
    xlabel: str = "Frequency (Hz)",
    mag_label: Optional[str] = None,
    phase_label: Optional[str] = None,
    mag_scale: str = "dB",           # "dB" or "linear"
    marker: str = "o",
    line_style: str = "-",
    grid: bool = True,
    figsize: Tuple[float, float] = (8, 6),
) -> Tuple[plt.Figure, Union[plt.Axes, Tuple[plt.Axes, plt.Axes]]]:
    """
    Create a Bode plot (magnitude and optional phase).

    Parameters:
    - freqs: frequencies (Hz)
    - mags: magnitude (linear, not dB)
    - phase: optional phase in degrees
    - title: overall title
    - xlabel: x-axis label (defaults to "Frequency (Hz)")
    - mag_label: y-label for magnitude (defaults to "Magnitude (dB)" or "Magnitude")
    - phase_label: y-label for phase (defaults to "Phase (deg)")
    - mag_scale: "dB" to plot 20*log10(mags) or "linear" to plot mags directly
    - marker, line_style: plotting styles for measured points/line
    - grid: show grid on axes
    - figsize: figure size

    Returns:
    - fig, ax (or (ax_mag, ax_phase) if phase provided)
    """
    freqs = np.asarray(freqs, dtype=float)
    mags = np.asarray(mags, dtype=float)
    if freqs.size != mags.size:
        raise ValueError("freqs and mags must have the same length")
    if phase is not None:
        phase = np.asarray(phase, dtype=float)
        if phase.size != freqs.size:
            raise ValueError("phase must have same length as freqs and mags")

    # sort by frequency
    order = np.argsort(freqs)
    freqs = freqs[order]
    mags = mags[order]
    if phase is not None:
        phase = phase[order]

    # prepare magnitude data
    if mag_scale == "dB":
        mag_plot = 20.0 * np.log10(np.clip(mags, a_min=1e-30, a_max=None))
        mag_label = mag_label or "Magnitude (dB)"
    else:
        mag_plot = mags
        mag_label = mag_label or "Magnitude"

    phase_label = phase_label or "Phase (deg)"

    # build figure and axes
    if phase is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        ax.semilogx(freqs, mag_plot, marker=marker, linestyle=line_style)
        ax.set_ylabel(mag_label)
        ax.set_title(title)
        ax.grid(grid, which="both", linestyle="--", linewidth=0.5)
        ax.set_xlabel(xlabel)
        # decade ticks
        min_dec = int(np.floor(np.log10(max(freqs.min(), 1e-30))))
        max_dec = int(np.ceil(np.log10(freqs.max())))
        xticks = np.logspace(min_dec, max_dec, max_dec - min_dec + 1)
        ax.set_xticks(xticks)
        ax.set_xlim(freqs.min(), freqs.max())
        ax.set_xscale("log")
        # nicer x tick labels (Hz -> kHz/MHz)
        def _fmt_xtick(v):
            if v >= 1e6:
                return f"{v/1e6:g} MHz"
            if v >= 1e3:
                return f"{v/1e3:g} kHz"
            return f"{int(v)} Hz"
        ax.set_xticklabels([_fmt_xtick(t) for t in xticks])
        return fig, ax
    else:
        fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True, figsize=figsize, gridspec_kw={"height_ratios": [2, 1]})
        ax_mag.semilogx(freqs, mag_plot, marker=marker, linestyle=line_style)
        ax_mag.set_ylabel(mag_label)
        ax_mag.set_title(title)
        ax_mag.grid(grid, which="both", linestyle="--", linewidth=0.5)

        ax_phase.semilogx(freqs, phase, marker=marker, linestyle=line_style, color="tab:orange")
        ax_phase.set_ylabel(phase_label)
        ax_phase.set_xlabel(xlabel)
        ax_phase.grid(grid, which="both", linestyle="--", linewidth=0.5)

        # decade ticks
        min_dec = int(np.floor(np.log10(max(freqs.min(), 1e-30))))
        max_dec = int(np.ceil(np.log10(freqs.max())))
        xticks = np.logspace(min_dec, max_dec, max_dec - min_dec + 1)
        ax_phase.set_xticks(xticks)
        ax_phase.set_xlim(freqs.min(), freqs.max())
        ax_phase.set_xscale("log")

        def _fmt_xtick(v):
            if v >= 1e6:
                return f"{v/1e6:g} MHz"
            if v >= 1e3:
                return f"{v/1e3:g} kHz"
            return f"{int(v)} Hz"
        ax_phase.set_xticklabels([_fmt_xtick(t) for t in xticks])

        fig.tight_layout()
        return fig, (ax_mag, ax_phase)