# bandpasses

[![PyPI - Version](https://img.shields.io/pypi/v/lemaitre-bandpasses.svg)](https://pypi.org/project/lemaitre-bandpasses)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lemaitre-bandpasses.svg)](https://pypi.org/project/lemaitre-bandpasses)


The bandpasses of the instrument involved in the Lemaitre dataset: MeagCam, HSC
and ZTF.

 - The MegaCam bandpasses were re-determined from the decommissioned MegaCam
  filters by M. Betoule and a team from the Laboratoire des matériaux avancés
  (LMA). These determinations differ slightly from the passband models that were
  published along with the SNLS and JLA papers. They are all non-radial. They do
  not (yet?) include per-CCD quantum efficiency determinations.

 - The ZTF bandpasses were re-assembled by P. Rosnet from a series of bench
 measurements sent by the ZTF team at Caltech. These passbands differ from the
 `models` sncosmo (`ztfg`, `ztfr` and `ztfi`), which contains only averaged
 passbands, which account for (1) the QE difference betweem the single- and
 double-coated CCDs (2) the passband radial variations due to the coating
 non-uniformities and to the variations of the incident beam angle w.r.t. the
 filter surface.

 - The HSC passbands are based on the measurements performed by Kawanomoto et
 al. These passband models are radial. They do not (yet?) include any per-CCD
 quantum efficiency determinations.

The passband models are distributed with `sncosmo`. We use a slightly patched
version of `sncosmo`, able to handle non-radial variations as well as per-CCD
quantum efficiencies.

This module contains the raw measurements and the code that was used to prepare
the sncosmo release. It also contain code that automatically registers the
Lemaitre passbands in sncosmo when the module is imported.

We also use the `bbf` module for fast computation of broadband fluxes. Within
`bbf`, the passbands are projected on a wavelength and position-dependent spline
basis, which is cached as a binary hdf5 file. The `bbf` module is


## Getting started

### Installation

conda packages for `bandpasses` are in preparation (but not ready yet). If you are
working within a conda environnment, we recommend that you install these conda
packages first:

```bash
conda install bbf ipython numpy scipy matplotlib scikit-sparse sparse_dot_mkl pandas h5py
```
Then install our temporary fork of `sncosmo`:

``` bash
pip install git+https://github.com/nregnault/sncosmo.git
```

Finally install this package:

```bash
pip install lemaitre-bandpasses
```

Or, for an installation from sources:

``` bash
git clone git@gitlab.in2p3.fr:lemaitre/bandpasses.git
cd bandpasses
pip install -e .
```

### Instantiating bandpasses from `sncosmo`

``` python
# registers the bandpasses into sncosmo
# when the filters will be public and sncosmo merged,
# this step won't be necessary anymore

from lemaitre import bandpasses

# getting the average ZTF/MegaCam6/HSC passbands

for name in ['ztf::g', 'ztf::r', 'ztf::I']:
    band = sncosmo.get_passband(name)
for name in ['megacam6::' + b for b in ['g', 'r', 'i2', 'z']]:
    band sncosmo.get_passband(name)
for name in [hsc::' + b for b in ['g', 'r', 'r2', 'i', 'i2', 'z', 'Y']]:
    band sncosmo.get_passband(name)

# getting, e.g. the ZTF r-passband at a given position
r = sncosmo.get_passband('ztf::r', x=724, y=2829, sensor_id=55)

# this function can be vectorized:
r = sncosmo.get_passband('ztf::r', x=[724., 1802, 222.], y=[42., 58., 2512], sensor_id=[5, 42, 22])
```

### Working with `bbf.FilterLib`s

``` python
from lemaitre import bandpasses

flib = bandpasses.get_filterlib(rebuild=False)
```

The filterlib contains all the lemaitre passbands, projected on specific
(adapted) spline bases. Then it is possible to use it to compute efficiently
broadband fluxes.

First, load a stellar library. A stellar library is like a FilterLib: it
consists in a collection of spectra, projected on a spline basis:

``` python
import bbf.stellarlib.pickles
pickles = bbf.stellarlib.pickles.fetch()
```

With that in hand, one can compute broadband fluxes on all (average passbands)
in the library:

``` python
fluxes = bbf.flux(flib, pickles)
```

``` python
from bbf.magsys import SpecMagSys

ms = SpecMagSys('AB')
mags = bbf.mag(flib, pickles, magsys=ms)

# or just
mags = bbf.mag(flib, pickles, 'AB')
```

We may be in a situation where we have actually one passband instance per
measurement. `bbf` handles that:

``` python
nmeas = 10_000

star = np.random.choice(np.arange(len(pickles)), size=nmeas
x = np.random.rand(3000., 3000., nmeas)
y = np.random.rand(3000., 3000., nmeas)
sensor_id = np.random.choice(np.arange(64), size=nmeas)

mags = bbf.mags(flib, pickles, star, x, y, sensor_id, magsys='AB')
```
