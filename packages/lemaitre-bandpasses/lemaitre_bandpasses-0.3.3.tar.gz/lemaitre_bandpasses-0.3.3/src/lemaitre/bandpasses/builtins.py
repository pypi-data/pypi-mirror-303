"""Registration of Lemaitre passband loaders into `sncosmo`

Importing this module register the Lemaitre passband loaders into the `sncosmo`
registry system.

"""

import importlib.resources
import h5py
from sncosmo.bandpasses import (
    Bandpass,
    GeneralBandpassInterpolator,
    Transforms,
    _BANDPASSES,
    _BANDPASS_INTERPOLATORS)

# this module does not export any symbols
__all__ = []


def _load_general_bandpass_interpolator(filename, band, version, name=None):
    """load the general functions"""
    with h5py.File(filename, 'r') as f:
        static = f['static']
        static_transmissions = [static[k][...] for k in static]

        if 'qe' in f:
            specific_sensor_qe = {
                int(k): v[...] for k, v in f['/qe/map'].items()}
        else:
            specific_sensor_qe = None

        to_focalplane = {
            int(k): v[...] for k, v in f['/transforms/to_focalplane'].items()}

        to_filter = {
            int(k): v[...] for k, v in f['/transforms/to_filter'].items()}

        transforms = Transforms(to_focalplane, to_filter)

        g = f['bandpasses'][band]
        if 'radii' in g:
            vtrans = g['radii'][...], g['wave'][...], g['trans'][...]
            return GeneralBandpassInterpolator(
                static_transmissions=static_transmissions,
                specific_sensor_qe=specific_sensor_qe,
                variable_transmission=vtrans,
                transforms=transforms,
                bounds_error=False,
                fill_value=0.)
        if 'X' in g and 'Y' in g:
            vtrans = g['X'][...], g['Y'][...], g['wave'][...], g['trans'][...]
            return GeneralBandpassInterpolator(
                static_transmissions=static_transmissions,
                specific_sensor_qe=specific_sensor_qe,
                variable_transmission=vtrans,
                transforms=transforms,
                bounds_error=False,
                fill_value=0.)

        return {}


def _load_default_bandpasses(filename, band, version, name=None):
    """load the default bandpasses"""
    with h5py.File(filename, 'r') as f:
        bandpass = f['averaged_bandpasses'][band]
        return Bandpass(
            bandpass['wave'][...],
            bandpass['trans'][...],
            name=name)


def _get_package_file(filename):
    filename = importlib.resources.files(__package__) / 'data' / filename

    if not h5py.is_hdf5(filename):
        raise RuntimeError(f'{filename} is not a valid HDF5 file')

    return filename


# ZTF variable bandpasses
for band in ('g', 'r', 'I'):
    _BANDPASS_INTERPOLATORS.register_loader(
        'ztf::' + band,
        _load_general_bandpass_interpolator,
        args=(_get_package_file('ztf_v0.hdf5'), band),
        version='0.1',
        meta={
            'filterset': 'ztf',
            'retrieved': '22 December 2023',
            'description': (
                'A re-determination of the ZTF filters by P. Rosnet et al '
                '(ZTF-II IN2P3 participation group)')})


# ZTF default bandpasses
for band in ('g', 'r', 'I'):
    _BANDPASSES.register_loader(
        'ztf::' + band,
        _load_default_bandpasses,
        args=(_get_package_file('ztf_v0.hdf5'), band, ),
        version='0.1',
        meta={
            'filterset': 'ztf',
            'retrieved': '22 December 2023',
            'description': (
                'A re-determination of the ZTF filters by P. Rosnet et al '
                '(ZTF-II IN2P3 participation group) - focal plane average')})


# megacam6 (re-measurements of the decommissioned MegaCam filters @ LMA)
for band in ('g', 'r', 'i', 'i2', 'z'):
    _BANDPASS_INTERPOLATORS.register_loader(
        'megacam6::' + band,
        _load_general_bandpass_interpolator,
        args=(_get_package_file('megacam6_v0.hdf5'), band),
        version='0.1',
        meta={
            'filterset': 'megacam6',
            'retrieved': '22 December 2023',
            'description': (
                'A re-determination of the decommissioned MegaCam '
                'filters by M. Betoule and LMA '),
            'reference': 'XX'})


# megacam6 default bandpasses
for band in ('g', 'r', 'i', 'i2', 'z'):
    _BANDPASSES.register_loader(
        'megacam6::' + band,
        _load_default_bandpasses,
        args=(_get_package_file('megacam6_v0.hdf5'), band),
        version='0.1',
        meta={
            'filterset': 'megacam6',
            'retrieved': '22 December 2023',
            'description': (
                'A re-determination of the decommissioned MegaCam '
                'filters by M. Betoule and LMA')})


# HSC - Tanaki  version
for band in ('g', 'r', 'r2', 'i', 'i2', 'z', 'Y'):
    _BANDPASS_INTERPOLATORS.register_loader(
        'hsc::' + band,
        _load_general_bandpass_interpolator,
        args=(_get_package_file('hsc_v0.hdf5'), band),
        version='0.1',
        meta={
            'filterset': 'hsc',
            'retrieved': '22 December 2023',
            'description': (
                'A model of the HSC filters - '
                'built on a series of measurements by et al.'),
            'reference': 'XX'})


for band in ('g', 'r', 'r2', 'i', 'i2', 'z', 'Y'):
    _BANDPASSES.register_loader(
        'hsc::' + band,
        _load_default_bandpasses,
        args=(_get_package_file('hsc_v0.hdf5'), band),
        version='0.1',
        meta={
            'filterset': 'hsc',
            'retrieved': '22 December 2023',
            'description': (
                'A model of the HSC filters - '
                'built on a series of measurements by et al. -- '
                'focal plane average'),
            'reference': 'XX'})
