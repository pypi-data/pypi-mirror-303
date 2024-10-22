"""Reference flux with the bbf integrators
"""

import numpy as np
import astropy.constants as const

from bbf.bspline import BSpline, lgram, refine_grid


__all__ = ['SpecMagsys', 'SNMagSys', 'ab_reference_spectrum', 'get_reference_spectrum']


def ab_reference_spectrum(wavelength):
    """return the AB reference SED as a function of wavelength

    Parameters
    ----------
    wavelength (float): wavelength, in Angstrom

    Returns
    -------
    S_AB in erg s^-1 cm^-2 A^-1
    """
    norm = (const.c * 1.E10).to_value()
    return 10. ** (-19.44) * norm / wavelength ** 2


# TODO: implement this as a stellarlib
def get_reference_spectrum(name='AB'):
    """
    """
    if name == 'AB':
        return ab_reference_spectrum
    raise KeyError('unknown spectrum')


class SpecMagsys:
    """Compute the reference spectrum broadband fluxes in a set of passbands1
    """
    def __init__(self, basis=None, ref_spectrum=ab_reference_spectrum):
        """
        """
        if isinstance(basis, np.ndarray):
            self.basis = BSpline(basis)
        elif isinstance(basis, BSpline):
            self.basis=basis
        else:
            self.basis = self._default_basis()

        self.ref_spectrum = ref_spectrum
        self.coeffs = self._project()

    def __len__(self):
        return 1

    def _default_basis(self):
        return BSpline(np.arange(3000., 11010., 10.))

    def _project(self):
        """
        """
        wave = refine_grid(self.basis.grid, scale=0.25)
        flx = self.ref_spectrum(wave)
        return self.basis.linear_fit(wave, flx, beta=1.E-8).reshape((-1, 1))

    def ref_broadbandflux(self, flib, star, band, x=None, y=None, sensor_id=None,
                          filter_frame=False):
        """
        """
        # basis = flib.basis if self.basis is None else self.basis
        #G = lspec_gram(flib.basis, basis, self.ref_spectrum)
        s = np.zeros_like(star)
        flx = flib.flux(self, s, band, x=x, y=y, sensor_id=sensor_id,
                        filter_frame=filter_frame)
        return flx

    def zero_points(self, flib, star, band, x=None, y=None, sensor_id=None,
                    filter_frame=False):
        """return the zero point of the local mag system
        """
        rbbflx = self.ref_broadbandflux(flib, star, band, x=x, y=y, sensor_id=sensor_id,
                                        filter_frame=filter_frame)
        return 2.5 * np.log10(rbbflx)

    def mag(self, flib, stellarlib, star, band, x=None, y=None, sensor_id=None, filter_frame=False):
        """
        """
        flx = flib.flux(stellarlib, star, band, x=x, y=y, sensor_id=sensor_id,
                        filter_frame=filter_frame)
        mag = -2.5 * np.log10(flx)
        zp = self.zero_points(flib, star, band, x=x, y=y, sensor_id=sensor_id,
                              filter_frame=filter_frame)
        return mag + zp


class SNMagSys:
    """Temporary class, to compute the zero points for a SN filter set
    """
    def __init__(self, snfilterset, ref_spectrum=ab_reference_spectrum, basis=None):
        """
        """
        self.snfilterset = snfilterset

        if isinstance(basis, np.ndarray):
            self.basis = BSpline(basis)
        elif isinstance(basis, BSpline):
            self.basis=basis
        else:
            self.basis = snfilterset.basis

        # reference spectrum
        if isinstance(ref_spectrum, str):
            self.ref_spectrum = get_reference_spectrum(ref_spectrum)
        else:
#               assert isinstance(ref_spectrum, function)
            self.ref_spectrum = ref_spectrum

        # project the reference spectrum
        self.coeffs = self._project()

    def _project(self):
        """
        """
        wave = refine_grid(self.basis.grid, scale=0.25)
        flx = self.ref_spectrum(wave)
        return self.basis.linear_fit(wave, flx, beta=1.E-8).reshape((-1, 1))

    def ref_broadband_flux(self, tr, z=0.):
        """
        """
        # t, basis = self.snfilterset[(tr, z)]
        tr_data = self.snfilterset[(tr, z)]
        G = lgram(tr_data.basis, self.basis).tocsr()
        flux = (tr_data.tq @ G @ self.coeffs).squeeze()
        return flux

    def get_zp(self, tr, z=0.):
        """
        """
        ref_bb_flux = self.ref_broadband_flux(tr, z=z)
        return -2.5 * np.log10(ref_bb_flux)
