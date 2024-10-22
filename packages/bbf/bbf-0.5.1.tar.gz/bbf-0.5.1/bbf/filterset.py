"""
"""

import numpy as np
import pylab as pl

from bbf.utils import check_sequence
from bbf.bspline import BSpline, Projector


__all__ = ['FilterSet']


class FilterSet:
    """A set of band passes, projected on a spline basis
    """
    def __init__(self, bandpasses, basis, grid=None, project=True, names=None):
        """Constructor. Build an internal basis and project the filters on it
        """
        self.bandpasses = np.atleast_1d(bandpasses)
        self.basis = None
        if basis is not None:
            self.basis = basis
        elif grid is not None:
            self.basis = BSpline(grid)
        if project:
            self.coeffs = self.project()
        if project:
            self.coeffs = self.project()

    @property
    def names(self):
        return [bp.name for bp in self.bandpasses]

    def __len__(self):
        return self.bandpasses.shape[0]

    def __getitem__(self, i):
        return self.bandpasses[i]

    def _refine_grid(self):
        """
        """
        g = self.basis.grid
        return 0.5 * (g[1:] + g[:-1])

    def _compress(self, coeffs, thresh=1.E-9):
        """suppress the very small coefficients of the projection
        """
        if thresh <= 0.:
            return
        c = coeffs / coeffs.max(axis=0)
        idx = np.abs(c) < thresh
        coeffs[idx] = 0.
        return coeffs

    def project(self, wave=None, compress_thresh=1.E-9):
        """project the
        """
        proj = Projector(self.basis)
        coeffs = proj(self.bandpasses, x=wave)
        coeffs = self._compress(coeffs, compress_thresh)
        return coeffs

    def mean_wave(self):
        """return the mean wavelengh of the input filters
        """
        # if list of band passes, just call 'wave_eff' for each one
        if check_sequence(self.bandpasses, lambda x: hasattr(x, 'wave_eff')):
            return np.array([b.wave_eff for b in self.bandpasses])

        # if a 2D table, compute the mean wavelengths
        tr = self.bandpasses
        wl = self.wave
        return (tr * wl).sum(axis=0) / tr.sum(axis=0)

    def plot_transmissions(self, **kw):
        """Plot the contents of the filter set"""
        figsize = kw.get('figsize', (8,4.5))
        cmap = kw.get('cmap', pl.cm.jet)

        pl.figure(figsize=figsize)
        #     bands = [band_name] if band_name is not None else self.names

        wl = self.mean_wave()

        for i in range(len(self)):
            xx = self._refine_grid()
            J = self.basis.eval(xx)
            col = int(255 * (wl[i]-3000.) / (11000.-3000.))
            pl.plot(xx, J @ self.coeffs[:,i], ls='-', color=cmap(col))
        pl.xlabel(r'$\lambda [\AA]$')

    def plot(self, **kw):
        """Plot the contents of the filter set"""
        figsize = kw.get('figsize', (8,9))
        cmap = kw.get('cmap', pl.cm.jet)

        pl.figure(figsize=figsize)
        #     bands = [band_name] if band_name is not None else self.names
        pl.imshow(self.coeffs, aspect='auto', interpolation='nearest')
        pl.colorbar()
        pl.xlabel('band')
        pl.ylabel(r'$\lambda$')
