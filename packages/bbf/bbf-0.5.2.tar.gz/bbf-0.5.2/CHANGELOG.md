# Changelog

This documents the changes in `bbf` releases. Version numbers follows [semantic
versioning](https://semver.org/).


## bbf-0.5.2

`gaiaxpy` is now an optionnal dependency, install it with `pip install
bbf[gaia]` or a separate `pip install gaiaxpy`. See
[#17](https://gitlab.in2p3.fr/lemaitre/bbf/-/issues/17)


## bbf-0.5.1

* Fixed a regression introduced in `bbf-0.5.0` (removed
  `bspline.Bspline{2D}.__eq__` method making the class unhashable)


## bbf-0.5.0

* Incompatible with `python-3.13`. See
    [#16](https://gitlab.in2p3.fr/lemaitre/bbf/-/issues/16)
* Added `bbf.stellarlib.gaia`
* Fixed a bug when using `CompositeBandpass` without specifying a `sensor_id`
  (issue 15).
* Removed useless parameter in `bspline.lgram`
* Deprecated property `BSpline.nj` and `BSpline2D.nj`, use `__len__` instead.
* Code cleanup (PEP8)


## bbf-0.4.0

* Added a `filterlib.CompositeBandpasses` class to simplifies the management of
  bandpasses that depends on the `sensor_id`.
* Comes with some simplifications in Filterlib and FluxArgs.


## bbf-0.3.2

Fix several regressions introduced in `bbf-0.3.0`

* `BSpline` instances can be pickled
* Sparse matrices returned by `BSpline` instances are `csr_matrix` (was `csr_array`)
* Reintroduction of `BSpline.nj`


## bbf-0.3.1

* Bugfixes

  * Fixed a bug with `OpenMP` instructions in C code. The bug impacted the
    `clang` compiler while `gcc` compiled code was fine.


## bbf-0.3.0

* Improvments

  * Uses `nanobind` instead of `ctypes` to wrap the bsplines C extension. This
    allows for a simple cross-platforms installation of the package. See
    [#6](https://gitlab.in2p3.fr/lemaitre/bbf/-/issues/6).
  * Few unit tests (about bsplines) under continuous integration.


## bbf-0.2.0

First public release.
