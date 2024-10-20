"""
Hyo2-Package
ABC 2
"""

import logging
import os

from hyo2.abc2.lib.package.pkg_info import PkgInfo

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

name = "ABC"
__version__ = "2.3.10"
__license__ = "LGPLv3 license"
__copyright__ = "Copyright 2024 University of New Hampshire, Center for Coastal and Ocean Mapping"

pkg_info = PkgInfo(
    name=name,
    version=__version__,
    author="Giuseppe Masetti(UNH,JHC-CCOM)",
    author_email="gmasetti@ccom.unh.edu",
    lic="LGPLv2.1 or CCOM-UNH Industrial Associate license",
    lic_url="https://www.hydroffice.org/license/",
    path=os.path.abspath(os.path.dirname(__file__)),
    url="https://www.hydroffice.org/abc/",
    manual_url="https://www.hydroffice.org/manuals/abc2/index.html",
    support_email="info@hydroffice.org",
    latest_url="https://www.hydroffice.org/latest/abc.txt",
    deps_dict={
        "gdal": "osgeo",
        "numpy": "numpy",
        "PySide6": "PySide6"
    }
)
