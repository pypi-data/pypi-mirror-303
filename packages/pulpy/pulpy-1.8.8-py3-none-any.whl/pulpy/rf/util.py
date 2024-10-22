# -*- coding: utf-8 -*-
"""MRI RF utilities.
"""

import numpy as np

__all__ = ["b12wbs", "calc_kbs", "dinf", "wbs2b1"]


def b12wbs(bs_offset, b1):
    """Calculate bloch-siegert shift for a given frequency offset and field
    strength. Note that this is NOT the first-order approximation given by Sacolick.
    Args:
        bs_offset (float or array): offset from larmor frequency in Hz.
        b1 (float or array): transmit field strength in G.

    Returns:
        wbs (float): Bloch-Siegert shift in Hz.

    References:
        Ramsey, N. F. (1955). Resonance Transitions Induced by Perturbations at
        Two or More Different Frequencies. Phys. Rev., 100(4): 1191-1194.
    """

    gam = 4258
    rfp_modulation = bs_offset * ((1 + (gam * b1) ** 2 / bs_offset**2) ** (1 / 2) - 1)

    return rfp_modulation


def wbs2b1(bs_offset, wrf):
    """Calculate the transmit field strength required to produce a given
    Bloch-Siegert shift wrf, for a pulse with an offset from larmor bs_offset
    Args:
        bs_offset (float or array): offset from larmor frequency in Hz.
        wrf (float or array): Bloch-Siegert shift in Hz.

    Returns:
        b1 (float): transmit field strength in G.

    References:
        Ramsey, N. F. (1955). Resonance Transitions Induced by Perturbations at
        Two or More Different Frequencies. Phys. Rev., 100(4): 1191-1194.
    """

    gam = 4258
    b1 = (wrf / gam) * np.sqrt((1 + bs_offset / wrf) ** 2 - 1)

    return b1


def calc_kbs(b1, wrf, T):
    """Calculate Kbs for a given pulse shape. Kbs is a constant that describes
    the phase shift (radians/Gauss^2) for a given RF pulse.
    Args:
        b1 (array): RF amplitude modulation, normalized.
        wrf (array): frequency modulation (Hz).
        T (float): pulse length (s)

    Returns:
        kbs (float): kbs constant for the input pulse, rad/gauss**2/msec

    References:
        Sacolick, L; Wiesinger, F; Hancu, I.; Vogel, M. (2010).
        B1 Mapping by Bloch-Siegert Shift. Magn. Reson. Med., 63(5): 1315-1322.
    """

    # squeeze just to ensure 1D
    b1 = np.squeeze(b1)
    wrf = np.squeeze(wrf)

    gam = 42.5657 * 2 * np.pi * 10**6  # rad/T
    t = np.linspace(0, T, np.size(b1))

    kbs = np.trapz(((gam * b1) ** 2 / ((2 * np.pi * wrf) * 2)), t)
    kbs /= 10000 * 10000  # want out rad/G**2

    return kbs


def dinf(d1=0.01, d2=0.01):
    """Calculate D infinity for a linear phase filter.

    Args:
        d1 (float): passband ripple level in M0**-1.
        d2 (float): stopband ripple level in M0**-1.

    Returns:
        float: D infinity.

    References:
        Pauly J, Le Roux P, Nishimra D, Macovski A. Parameter relations for the
        Shinnar-Le Roux selective excitation pulse design algorithm.
        IEEE Tr Medical Imaging 1991; 10(1):53-65.

    """

    a1 = 5.309e-3
    a2 = 7.114e-2
    a3 = -4.761e-1
    a4 = -2.66e-3
    a5 = -5.941e-1
    a6 = -4.278e-1

    l10d1 = np.log10(d1)
    l10d2 = np.log10(d2)

    d = (a1 * l10d1 * l10d1 + a2 * l10d1 + a3) * l10d2 + (
        a4 * l10d1 * l10d1 + a5 * l10d1 + a6
    )

    return d
