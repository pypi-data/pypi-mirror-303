# Broadband fluxes (`bbf`)

[![PyPI - Version](https://img.shields.io/pypi/v/bbf.svg)](https://pypi.org/project/bbf)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/bbf.svg)](https://anaconda.org/conda-forge/bbf)
[![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/bbf.svg)](https://anaconda.org/conda-forge/bbf)

-----

**Table of contents**
- [Installation](#installation)
- [Getting started](#getting started)
- [License](#license)

A module to evaluate the broadband fluxes and magnitudes of spectrophotometric
standards.


# Installation

The `bbf` package works on `python>=3.9<3.13` for Linux and macos. It should
work on Windows too, but it has not been tested.

| :warning: `bbf` relies for the moment on a [modified version of `sncosmo`](https://github.com/nregnault/sncosmo) that must be installed separatly |
|---|


## Install using conda (recommended)

```bash
conda install -c conda-forge bbf
pip install git+https://github.com/nregnault/sncosmo
```


## Install using pip

* Installing `bbf` from `pip` requires to install
  [SuiteSparse](http://www.suitesparse.com) which is not installable from `pip`.
  On Debian/Ubuntu systems, the command `sudo apt install libsuitesparse-dev`
  suffices. Or you can compile `SuiteSparse` from
  [sources](https://github.com/DrTimothyAldenDavis/SuiteSparse). Or a simpler
  alternative is to install `scikit-sparse` from `conda`:

  ```bash
  conda install -c conda-forge scikit-sparse
  ```

* `cmake` and a C++ compiler with `OpenMP` support are required. On Linux, `gcc`
  supports `OpenMP` out of the box, and `cmake` is installed as needed during
  `bbf` installation. On macos an extra installation is required:

  ```bash
  # for macos only
  conda install cmake llvm-openmp
  ```

* `sncosmo` fork must be installed separatly with:

  ```bash
  pip install bbf git+https://github.com/nregnault/sncosmo
  ```

* Finally install `bbf`:

  ```bash
  pip install bbf
  ```

## Install from sources

* If you prefer installing from sources, ensure **git lfs** is installed (have a
  `git lfs`, if the command is missing install it with `conda install git-lfs;
  git lfs install`).

* Then follow the steps from the [Install using pip](#install using pip)
  section, and replace the last step with:

  ```bash
  git clone clone git@gitlab.in2p3.fr:lemaitre/bbf.git
  cd bbf
  pip install -e .
  ```

* To run the tests suite, install the required dependencies, then run `pytest`:

  ```bash
  pip install -e .[test]
  pytest
  ```

* If you are a developper and want to work on the `bbf` C/C++ extension,
  insall the package with:

  ```bash
  pip install nanobind ninja scikit-build-core[pyproject]
  VERBOSE=1 pip install --no-build-isolation -Ceditable.rebuild=true -ve .
  ```

## Installing the Lemaitre bandpasses

If you plan to use the latest version of the megacam6*, *ztf* and *hsc*
passbands, install the `lemaitre.bandpasses` package:

```bash
pip install lemaitre-bandpasses
```

or

```bash
git clone https://gitlab.in2p3.fr/lemaitre/lemaitre/bandpasses
cd bandpasses
git lfs pull
pip install .
```


# Getting started

The goal of `bbf` is to efficiently compute broadband fluxes and magnitudes,
i.e. quantities of the form:

$$f_{xys} = \int S(\lambda) \lambda T_{xys}(\lambda) d\lambda$$

where $\lambda$ is the SED of an object, $T_{xyz}(\lambda)$ is the bandpass of
the instrument used to observe it. $T$ may depend on the focal plane position of
the object and, if the focal plane is a mosaic of sensors, on the specific
sensor $s$ where the observation is made. In practice, $x,y$ are coordinates, in
pixels, in the sensor frame, and $s$ is a unique sensor index (or amplifier
index).

Computing magnitudes requires an additional ingredient: the flux of a reference
spectrum $S_{ref}(\lambda)$, usually the AB spectrum, integrated in the same
passband (same sensor, same position).

$$m = -2.5 \log_{10} \left(\frac{\int S(\lambda) \lambda T_{xyz}(\lambda) d\lambda}{\int S_{ref}(\lambda) \lambda T_{xyz}(\lambda) d\lambda}\right)$$

To compute these integrales, `bbf` uses the technique implemented in `nacl`,
which consists in projecting the bandpasses and SED on spline bases:

$$S(\lambda) = \sum_i \theta_i {\cal B}_i(\lambda)$$

and

$$T(\lambda) = \sum_j t_j {\cal B}_j(\lambda)$$

If we precompute the products $G_{ij} = \int \lambda {\cal B}_i(\lambda) {\cal B}_j(\lambda) d\lambda$
the integrals above can be expressed as a simple contraction:

$$f = \theta_i G_{ij} t_j$$

where $G$ is very sparse, since the B-Splines ${\cal B}_i$ have a compact
support. If the bandpass $T$ is spatially variable, the $t_j$ coefficients are
themselves developped on a spatial spline basis.

$$t_j = \sum_{kj} \tau_{kj} {\cal K}(x,y)$$

The contraction above is then of the form: ...


## FilterSets and StellarLibs

`bbf` implements two main kind of objects: `FilterLib`, which holds a set of
band passes, projected on spline bases (${\cal K_j(x,y)}$ and ${\cal
B}_i_(\lambda)$), and `StellarLib` which manages a set of spectra, also
projected on a spline basis (not necessily the splines used for the filters).


## Loading a filter lib

Building a complete version of a `FilterLib` requires some care. The standard
`FilterLib` used in the Lemaître analysis is build and maintained within the
package `lemaitre.bandpasses`. To access it:

``` python
from lemaitre import bandpasses

flib = bandpasses.get_filterlib()
```
The first time this function is called, the `FilterLib`` is built and cached. The subsequent calls
access the cached version, and never take more than a few milliseconds.


## Loading Stellar Libraries

As of today, `bbf` implements two kinds of StellarLibs: pickles and Calspec. An
interface to gaiaXP is in development.

To load the pickles library:

``` python

import bbf.stellarlib.pickles
pickles = bbf.stellarlib.pickles.fetch()
```

To load the most recent version of Calspec:

``` python
import bbf.stellarlib.calspec
calspec = bbf.stellarlib.calspec.fetch()
```


## Computing Broadband fluxes

With a `FilterSet` and a `StellarLib` in hand, one can compute broadband fluxes
and broadband mags.


### Broadband fluxes

``` python
import bbf.stellarlib.pickles
from lemaitre import bandpasses

flib = bandpasses.get_filterlib()
pickles = bbf.stellarlib.pickles.fetch()

# number of measurements
nmeas = 100_000

# which stars ?
star = np.random.choice(np.arange(0, len(pickles)), size=nmeas)

# in which band ?
band = np.random.choice(['ztf::g', 'ztf::r', 'ztf::I'], size=nmeas)

# observation positions
x = np.random.uniform(0., 3072., size=nmeas)
y = np.random.uniform(0., 3080., size=nmeas)
sensor_id = np.random.choice(np.arange(1, 65), size=nmeas)

fluxes = flib.flux(pickles, star, band, x=x, y=y, sensor_id=sensor_id)
```


### Broadband magnitudes

To convert broadband fluxes into broadband magnitudes, we need to compute the
reference fluxes, in the same effective measurement band passes. This is done
using an auxiliary object called `MagSys`:

``` python

from bbf.magsys import SpecMagSys
import bbf.stellarlib.pickles
from lemaitre import bandpasses

flib = bandpasses.get_filterlib()
pickles = bbf.stellarlib.pickles.fetch()

# number of measurements
nmeas = 100_000

# which stars ?
star = np.random.choice(np.arange(0, len(pickles)), size=nmeas)

# in which band ?
band = np.random.choice(['ztf::g', 'ztf::r', 'ztf::I'], size=nmeas)

# observation positions
x = np.random.uniform(0., 3072., size=nmeas)
y = np.random.uniform(0., 3080., size=nmeas)
sensor_id = np.random.choice(np.arange(1, 65), size=nmeas)

ms = SpecMagSys('AB')
mags = ms.mag(pickles, star, band, x=x, y=y, sensor_id=sensor_id)
```


# License

`bbf` is distributed under the terms of the
[MIT](https://spdx.org/licenses/MIT.html) license.
