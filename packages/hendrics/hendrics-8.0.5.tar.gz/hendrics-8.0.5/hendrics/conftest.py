# This file is used to configure the behavior of pytest when using the Astropy
# test infrastructure. It needs to live inside the package in order for it to
# get picked up when running the tests inside an interpreter using
# packagename.test

import os

from astropy.version import version as astropy_version

try:
    from pytest_astropy_header.display import (
        PYTEST_HEADER_MODULES,
        TESTED_VERSIONS,
    )

    ASTROPY_HEADER = True
except ImportError:
    ASTROPY_HEADER = False


try:
    import matplotlib
except ImportError:
    pass
else:
    matplotlib.use("Agg")


def pytest_configure(config):
    if ASTROPY_HEADER:
        config.option.astropy_header = True

        # Customize the following lines to add/remove entries from the list of
        # packages for which version numbers are displayed when running the tests.
        PYTEST_HEADER_MODULES.pop("Pandas", None)
        PYTEST_HEADER_MODULES["scikit-image"] = "skimage"

        from . import __version__

        packagename = os.path.basename(os.path.dirname(__file__))
        TESTED_VERSIONS[packagename] = __version__
