import logging
import os

from lemaitre import bandpasses


def test_filterlib(caplog, tmpdir):
    # capture log messages up to DEBUG level and setup a temp cache folder
    caplog.set_level(logging.DEBUG)
    os.environ['BBF_CACHE_DIR'] = str(tmpdir / 'cache')

    # build and write in cache
    flib1 = bandpasses.get_filterlib()
    assert 'found 0 versions of lemaitre filterlib in cache' in caplog.text
    assert 'loading lemaitre filterlib from ' not in caplog.text
    assert 'building lemaitre filterlib' in caplog.text

    caplog.clear()

    # read from cache
    flib2 = bandpasses.get_filterlib()
    assert 'found 1 versions of lemaitre filterlib in cache' in caplog.text
    assert 'loading lemaitre filterlib from ' in caplog.text
    assert 'building lemaitre filterlib' not in caplog.text

    caplog.clear()

    # force rebuild
    flib3 = bandpasses.get_filterlib(rebuild=True)
    assert 'found 1 versions of lemaitre filterlib in cache' in caplog.text
    assert 'loading lemaitre filterlib from ' not in caplog.text
    assert 'building lemaitre filterlib' in caplog.text

    # there is no implementation of flib.__eq__ so we fallback bandpass names
    assert (
        flib1.bandpass_names ==
        flib2.bandpass_names ==
        flib3.bandpass_names)
