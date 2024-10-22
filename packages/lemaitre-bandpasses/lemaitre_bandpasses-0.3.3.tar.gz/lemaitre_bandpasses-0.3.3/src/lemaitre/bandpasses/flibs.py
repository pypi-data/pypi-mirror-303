"""Standard filterlibs

We may want to add this to a sncosmo-like registry. Not sure we really need
that.

"""

import hashlib
import importlib.resources
import logging

import numpy as np

import bbf


# TODO(mbernard) this should not be defined here because it may overload a
# logger already configured at application level
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


# TODO(mbernard) at some point we may want to clean the cache from deprecated
# filterlib files automatically (idea: remove the files with bad hash older
# than n days, add this as a kwargs?)
def get_filterlib(rebuild=False):
    """Returns the lemaitre filterlib as a `bbf.FilterLib` instance

    When `rebuild` is True, the filterlib is built and saved into a local cache
    for further reuse. When `rebuild` is False, the filterlib if first looked
    into the cache and rebuilt then saved if missing.

    To ensure the cached filterlib file matches the current version of this
    package, a hash value is computed from the package content (both code and
    data) and is compared to the hash stored in the file. In case of mismatch,
    the filterlib is rebuilt.

    The cache folder can be defined using the BBF_CACHE_DIR environment
    variable. By default, a platform dependent folder is chosen.

    """
    # retrieve the list of cached filterlibs
    cache_dir = bbf.get_cache_dir()
    cached_flibs = list(cache_dir.glob('lemaitre_flib.*.pkl'))
    logger.debug(
        'found %s versions of lemaitre filterlib in cache',
        len(cached_flibs))

    package_hash = _get_package_hash()

    flib_file = cache_dir / f'lemaitre_flib.{package_hash}.pkl'
    if flib_file.is_file() and not rebuild:
        logger.info('loading lemaitre filterlib from %s', flib_file)
        return bbf.FilterLib.load(flib_file)

    # warn the user in case of mismatch
    if cached_flibs and not rebuild:
        logger.warning(
            'mismatch between the lemaitre.bandpasses package and cached '
            'filterlib in %s, rebuilding filterlib', cache_dir)

    flib = _build_filterlib()
    logger.info('saving lemaitre filterlib to %s', flib_file)
    flib.save(flib_file)

    return flib


def _ccdid_qid_to_rcid(ccdid, qid):
    """Stolen from ztfimg.tools"""
    # Would love to use the original, but dask deps...
    return 4 * (ccdid - 1) + qid - 1


def _get_package_hash():
    """Compute a SHA256 digest (aka hash) of the lemaitre.bandpasses package"""
    hasher = hashlib.sha256()

    # for each source and data file in the lemaitre.bandpasses package, feed
    # the hasher with it's content
    for package_file in (
            list(importlib.resources.files(__package__).glob('**/*.py')) +
            list(importlib.resources.files(__package__).glob('**/data/*'))):
        with open(package_file, 'rb') as fh:
            hasher.update(fh.read())

    # hexadecimal digest of the concatenation of all the files
    return hasher.hexdigest()


def _build_filterlib():
    """Build and return the lemaitre filterlib"""
    logger.info('building lemaitre filterlib')
    fl = bbf.FilterLib(basis=np.arange(3000., 11010., 10.))

    # MegaCam6: the only tricky part is g, which requires a higher resolution
    # for the spatial spline basis
    logger.debug('megacam6')
    fl.insert(fl.fetch('megacam6::g', xy_size=40, xy_order=4),  'megacam6::g')
    fl.insert(fl.fetch('megacam6::r', xy_size=20, xy_order=2),  'megacam6::r')
    fl.insert(fl.fetch('megacam6::i', xy_size=20, xy_order=2),  'megacam6::i')
    fl.insert(fl.fetch('megacam6::i2', xy_size=20, xy_order=2), 'megacam6::i2')
    fl.insert(fl.fetch('megacam6::z', xy_size=20, xy_order=2),  'megacam6::z')

    logger.debug('megacam6 default (averaged) bandpasses')
    fl.insert(fl.fetch('megacam6::g', average=True),  'megacam6::g', average=True)
    fl.insert(fl.fetch('megacam6::r', average=True),  'megacam6::r', average=True)
    fl.insert(fl.fetch('megacam6::i', average=True),  'megacam6::i', average=True)
    fl.insert(fl.fetch('megacam6::i2', average=True), 'megacam6::i2', average=True)
    fl.insert(fl.fetch('megacam6::z', average=True),  'megacam6::z', average=True)

    logger.debug('megacampsf default (averaged) bandpasses [used in JLA]')
    fl.insert(fl.fetch('megacampsf::g', average=True, radius=0.),  'megacampsf::g', average=True)
    fl.insert(fl.fetch('megacampsf::r', average=True, radius=0.),  'megacampsf::r', average=True)
    fl.insert(fl.fetch('megacampsf::i', average=True, radius=0.), 'megacampsf::i', average=True)
    fl.insert(fl.fetch('megacampsf::z', average=True, radius=0.),  'megacampsf::z', average=True)

    logger.debug('HSC')
    fl.insert(fl.fetch('hsc::g', xy_size=20, xy_order=2), 'hsc::g')
    fl.insert(fl.fetch('hsc::r', xy_size=20, xy_order=2), 'hsc::r')
    fl.insert(fl.fetch('hsc::r2', xy_size=20, xy_order=2), 'hsc::r2')
    fl.insert(fl.fetch('hsc::i', xy_size=20, xy_order=2), 'hsc::i')
    fl.insert(fl.fetch('hsc::i2', xy_size=20, xy_order=2), 'hsc::i2')
    fl.insert(fl.fetch('hsc::z', xy_size=20, xy_order=2), 'hsc::z')
    fl.insert(fl.fetch('hsc::Y', xy_size=20, xy_order=2), 'hsc::Y')

    logger.debug('HSC default (averaged) bandpasses')
    fl.insert(fl.fetch('hsc::g', average=True), 'hsc::g', average=True)
    fl.insert(fl.fetch('hsc::r', average=True), 'hsc::r', average=True)
    fl.insert(fl.fetch('hsc::r2', average=True), 'hsc::r2', average=True)
    fl.insert(fl.fetch('hsc::i', average=True), 'hsc::i', average=True)
    fl.insert(fl.fetch('hsc::i2', average=True), 'hsc::i2', average=True)
    fl.insert(fl.fetch('hsc::z', average=True), 'hsc::z', average=True)
    fl.insert(fl.fetch('hsc::Y', average=True), 'hsc::Y', average=True)

    # for ZTF, we have basically two models: one for single coatings and
    # another for the double coatings. Both include the transforms for the
    # entire filter set.
    logger.debug('ZTF')

    # single coating
    sid = _ccdid_qid_to_rcid(1, 1) + 1
    bp_g_single = fl.fetch('ztf::g', xy_size=20, xy_order=2, sensor_id=sid)
    bp_r_single = fl.fetch('ztf::r', xy_size=20, xy_order=2, sensor_id=sid)
    bp_i_single = fl.fetch('ztf::I', xy_size=20, xy_order=2, sensor_id=sid)
    sensors_single = [
        _ccdid_qid_to_rcid(ccdid, qid) + 1
        for qid in range(1, 5)
        for ccdid in [1, 2, 3, 4, 13, 14, 15, 16]]

    # double coating
    sid = _ccdid_qid_to_rcid(5, 1) + 1
    bp_g_double = fl.fetch('ztf::g', xy_size=20, xy_order=2, sensor_id=sid)
    bp_r_double = fl.fetch('ztf::r', xy_size=20, xy_order=2, sensor_id=sid)
    bp_i_double = fl.fetch('ztf::I', xy_size=20, xy_order=2, sensor_id=sid)
    sensors_double = [
        _ccdid_qid_to_rcid(ccdid, qid) + 1
        for qid in range(1, 5)
        for ccdid in [5, 6, 7, 8, 9, 10, 11, 12]]

    for b_single, b_double, b_name in zip(
            [bp_g_single, bp_r_single, bp_i_single],
            [bp_g_double, bp_r_double, bp_i_double],
            ['ztf::g', 'ztf::r', 'ztf::I']):
        keys = sensors_single + sensors_double
        values = (
            [b_single] * len(sensors_single) +
            [b_double] * len(sensors_double))
        fl.insert(dict(zip(keys, values)), b_name)

    logger.debug('ZTF default (averaged) bandpasses')
    fl.insert(fl.fetch('ztf::g', average=True), 'ztf::g', average=True)
    fl.insert(fl.fetch('ztf::r', average=True), 'ztf::r', average=True)
    fl.insert(fl.fetch('ztf::I', average=True), 'ztf::I', average=True)

    # the sncosmo version of various filters
    fl.insert(fl.fetch('ztfg', average=True), 'ztfg', average=True)
    fl.insert(fl.fetch('ztfr', average=True), 'ztfr', average=True)
    fl.insert(fl.fetch('ztfi', average=True), 'ztfi', average=True)

    fl.insert(fl.fetch('lsstu', average=True), 'lsstu', average=True)
    fl.insert(fl.fetch('lsstg', average=True), 'lsstg', average=True)
    fl.insert(fl.fetch('lsstr', average=True), 'lsstr', average=True)
    fl.insert(fl.fetch('lssti', average=True), 'lssti', average=True)
    fl.insert(fl.fetch('lsstz', average=True), 'lsstz', average=True)
    fl.insert(fl.fetch('lssty', average=True), 'lssty', average=True)

    return fl
