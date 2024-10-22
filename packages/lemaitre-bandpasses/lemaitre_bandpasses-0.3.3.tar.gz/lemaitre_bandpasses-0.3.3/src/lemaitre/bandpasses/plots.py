"""General standard
"""

import numpy as np
import matplotlib.pyplot as plt
# import builtins
# import sncosmo

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO)


colors = {'g': 'b', 'r': 'g', 'r2': 'aquamarine',
          'i': 'yellow', 'i2': 'gold', 'z': 'r', 'Y': 'purple',
          'I': 'r'}


def hsc_xyccd(delta=200, nx=None, ny=None):
    """
    """
    # x, y = np.mgrid[:2048:delta, :4177:delta]
    nx = nx if nx is not None else int(np.floor(2048/delta))
    ny = ny if ny is not None else int(np.floor(4177/delta))
    x, y = np.meshgrid(np.linspace(0, 2048, nx),
                       np.linspace(0, 4177, ny))
    ccd = list(range(104))
    ccd.remove(9)
    ccd = np.tile(ccd, len(x.ravel()))
    x = np.repeat(x.ravel(), 103)
    y = np.repeat(y.ravel(), 103)

    return x, y, ccd


def megacam_xyccd(delta=200, nx=None, ny=None):
    """
    """
    # x, y = np.mgrid[:2048:delta, :4608:delta]
    nx = nx if nx is not None else int(np.floor(2048/delta))
    ny = ny if ny is not None else int(np.floor(4608/delta))
    x, y = np.meshgrid(np.linspace(0, 2048, nx),
                       np.linspace(0, 4608, ny))

    ccd = np.tile(np.arange(36), len(x.ravel()))
    x = np.repeat(x.ravel(), 36)
    y = np.repeat(y.ravel(), 36)

    return x, y, ccd


def ztf_xyccd(delta=200, nx=None, ny=None):
    #       xx,yy = np.mgrid[:3001+delta:delta, :3001+delta:delta]
    nx = nx if nx is not None else int(np.floor(3072/delta))
    ny = ny if ny is not None else int(np.floor(3080/delta))
    x, y = np.meshgrid(np.linspace(0, 3072, nx),
                       np.linspace(0, 3080, ny))

    # ccd, qid = np.mgrid[1:17,1:5]
    # key = np.repeat(np.vstack((ccd.ravel(), qid.ravel())).T, len(xx.ravel()), axis=0)
    rcid = np.repeat(np.arange(1,65), len(x.ravel()))

    x = np.tile(x.ravel(), 64)
    y = np.tile(y.ravel(), 64)

    return x, y, rcid


def mean_wavelength(wl, tr):
    return (tr * wl).sum(axis=1) / tr.sum(axis=1)


def mean_wavelength_vs_position(band, x, y, ccd, wl=None, relative=False, title='', markersize=5):
    """
    """
    if type(band) is str:
        from sncosmo.bandpasses import _BANDPASS_INTERPOLATORS
        band = _BANDPASS_INTERPOLATORS.retrieve(band)

    XX, YY = band.transforms.to_focalplane(x, y, ccd)

    if wl is None:
        wl = np.linspace(band.minwave(), band.maxwave())

    tr = band.eval_at(x, y, ccd, wl)
    mapmwl = mean_wavelength(wl, tr)

    idx = ~np.isnan(mapmwl)
    mean_wl = mapmwl[idx].mean()

    if relative:
        mapmwl -= mean_wl

    plt.figure(figsize=(11,8))
    plt.plot(XX, YY, marker='.', color='gray', alpha=0.25, ls='')
    plt.scatter(XX[idx], YY[idx], c=mapmwl[idx], zorder=100, s=markersize,
                label=f'$\lambda={mean_wl:.1f}$')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.colorbar()
    plt.legend(loc='upper right')

    return mapmwl


def average_bands(bp_interpolator, wl, xyccd, ax=None):
    """
    """
    averaged_bands = {}
    for band, bpi in bp_interpolator.items():
        x, y, sensor_id = xyccd(delta=100)
        tr = bpi.eval_at(x, y, sensor_id, wl=wl)

        # some of the transmissions are equal to zero
        # we need to remove them from the average
        idx = tr.sum(axis=1) == 0.
        logging.info(f'{idx.sum()}/{len(idx)} passbands evaluated to zero - removed from the mean')
        tr = tr[~idx,:]
        trans = tr.mean(axis=0)
        idx = trans == 0.
        wl_min, wl_max = wl[~idx].min()-20., wl[~idx].max()+20.
        idx = (wl>wl_min) & (wl<wl_max)
        logging.info(f'{band}: {wl_min}, {wl_max}')
        averaged_bands[band] = (wl[idx], trans[idx])
        if ax is not None:
            ax.plot(wl[idx], trans[idx], color=colors[band], marker='.')

    return averaged_bands
