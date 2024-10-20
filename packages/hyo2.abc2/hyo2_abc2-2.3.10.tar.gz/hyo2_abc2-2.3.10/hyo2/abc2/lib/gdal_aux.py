import logging
import os
from typing import Optional

import pyproj
import pyproj.datadir
from osgeo import gdal
from osgeo import ogr
from osgeo import osr

from hyo2.abc2.lib.package.pkg_helper import PkgHelper

logger = logging.getLogger(__name__)


class GdalAux:
    """ Auxiliary class to manage GDAL stuff """

    error_loaded = False
    gdal_data_fixed = False
    proj4_data_fixed = False

    ogr_formats = {
        'ESRI Shapefile': 0,
        'KML': 1,
        'CSV': 2,
    }

    ogr_exts = {
        'ESRI Shapefile': '.shp',
        'KML': '.kml',
        'CSV': '.csv',
    }

    @classmethod
    def current_gdal_version(cls) -> int:
        return int(gdal.VersionInfo('VERSION_NUM'))

    @classmethod
    def get_ogr_driver(cls, ogr_format):

        try:
            driver_name = [key for key, value in GdalAux.ogr_formats.items() if value == ogr_format][0]

        except IndexError:
            raise RuntimeError("Unknown ogr format: %s" % ogr_format)

        drv = ogr.GetDriverByName(driver_name)
        if drv is None:
            raise RuntimeError("Ogr failure > %s driver not available" % driver_name)

        return drv

    @classmethod
    def create_ogr_data_source(cls, ogr_format: str, output_path: str, epsg: Optional[int] = 4326):
        drv = cls.get_ogr_driver(ogr_format)
        output_file = output_path + cls.ogr_exts[drv.GetName()]
        # logger.debug("output: %s" % output_file)
        if os.path.exists(output_file):
            os.remove(output_file)

        ds = drv.CreateDataSource(output_file)
        if ds is None:
            raise RuntimeError("Ogr failure in creation of data source: %s" % output_path)

        if ogr_format == cls.ogr_formats['ESRI Shapefile']:
            cls.create_prj_file(output_path, epsg=epsg)

        return ds

    @classmethod
    def create_prj_file(cls, output_path: str, epsg: Optional[int] = 4326) -> None:
        """Create an ESRI lib file (geographic WGS84 by default)"""
        spatial_ref = osr.SpatialReference()
        spatial_ref.ImportFromEPSG(epsg)

        spatial_ref.MorphToESRI()
        fid = open(output_path + '.prj', 'w')
        fid.write(spatial_ref.ExportToWkt())
        fid.close()

    @staticmethod
    def list_ogr_drivers():
        """ Provide a list with all the available OGR drivers """

        cnt = ogr.GetDriverCount()
        driver_list = []

        for i in range(cnt):

            driver = ogr.GetDriver(i)
            driver_name = driver.GetName()
            if driver_name not in driver_list:
                driver_list.append(driver_name)

        driver_list.sort()  # Sorting the messy list of ogr drivers

        for i, drv in enumerate(driver_list):
            print("%3s: %25s" % (i, drv))

    @classmethod
    def gdal_error_handler(cls, err_class, err_num, err_msg) -> None:
        """GDAL Error Handler, to test it: gdal.Error(1, 2, b'test error')"""

        err_type = {
            gdal.CE_None: 'None',
            gdal.CE_Debug: 'Debug',
            gdal.CE_Warning: 'Warning',
            gdal.CE_Failure: 'Failure',
            gdal.CE_Fatal: 'Fatal'
        }
        try:
            err_msg = err_msg.replace('\n', ' ')
        except Exception as e:
            logger.warning("skip the new-line replacement: %s" % e)
        err_class = err_type.get(err_class, 'None')
        if err_class in ["Failure", "Fatal"]:
            raise RuntimeError("%s: gdal error %s > %s" % (err_class, err_num, err_msg))
        logger.info("%s: gdal error %s > %s" % (err_class, err_num, err_msg))

    @classmethod
    def push_gdal_error_handler(cls) -> None:
        """ Install GDAL error handler """
        if cls.error_loaded:
            return

        gdal.PushErrorHandler(cls.gdal_error_handler)

        gdal.UseExceptions()
        ogr.UseExceptions()
        osr.UseExceptions()

        cls.error_loaded = True

    @classmethod
    def check_gdal_data(cls, verbose: bool = False) -> None:
        """ Check the correctness of gdal data folder """

        if cls.gdal_data_fixed:
            if verbose:
                logger.debug("already fixed gdal data folder: %s" % gdal.GetConfigOption('GDAL_DATA'))
            return

        # avoid to rely on env vars
        env_vars = ('GDAL_DATA', 'GDAL_DRIVER_PATH')
        for env_var in env_vars:
            if env_var in os.environ:
                del os.environ[env_var]
                if verbose:
                    logger.debug("removed %s env var" % env_var)

        # check if the gdal data folder is already set
        try:
            gdal_path = gdal.GetConfigOption('GDAL_DATA')
            if not os.path.exists(gdal_path):
                raise RuntimeError("Unable to locate %s" % gdal_path)
            cls.gdal_data_fixed = True
            if verbose:
                logger.debug("already set gdal data folder = %s" % gdal_path)
            return
        except Exception:
            logger.info("attempting to fix unset gdal data folder")

        cand_data_folders = [
            os.path.join(os.path.dirname(gdal.__file__), 'data'),
            os.path.join(os.path.dirname(gdal.__file__), 'data', 'gdal'),
            os.path.join(os.path.dirname(gdal.__file__), 'osgeo', 'data'),
            os.path.join(os.path.dirname(gdal.__file__), 'osgeo', 'data', 'gdal'),
            os.path.join(PkgHelper.python_path(), 'Library', 'data'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'Library', 'share'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'Library', 'share', 'gdal'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'share'),  # anaconda (Linux)
            os.path.join(PkgHelper.python_path(), 'share', 'gdal'),  # anaconda (Linux)
        ]

        # checking each folder
        for cand_data_folder in cand_data_folders:

            s57_agencies_path = os.path.join(cand_data_folder, 's57agencies.csv')
            if os.path.exists(s57_agencies_path):

                gdal.SetConfigOption('GDAL_DATA', cand_data_folder)
                cls.gdal_data_fixed = True
                cls.push_gdal_error_handler()
                if verbose:
                    logger.debug("set gdal data folder = %s" % cand_data_folder)
                return

        raise RuntimeError("Unable to locate gdal data at:\n%s" % "\n - ".join(cand_data_folders))

    @classmethod
    def check_proj4_data(cls, verbose: bool = False) -> None:
        """ Check the correctness of proj data folder """

        if cls.proj4_data_fixed:
            if verbose:
                logger.debug("already fixed proj data folder: %s" % pyproj.datadir.get_data_dir())
            return

        # avoid to rely on env vars
        env_vars = ('PROJ_DATA', 'PROJ_LIB')
        for env_var in env_vars:
            if env_var in os.environ:
                del os.environ[env_var]
                if verbose:
                    logger.debug("removed %s env var" % env_var)

        # check if the proj data folder is already set
        try:
            proj4_path = pyproj.datadir.get_data_dir()
            cls.proj4_data_fixed = True
            if verbose:
                logger.debug("already set proj data folder = %s" % proj4_path)
            return
        except Exception:
            logger.info("attempting to fix unset proj data folder")

        # list all the potential proj data folders
        cand_data_folders = [
            os.path.join(os.path.dirname(pyproj.__file__), 'data'),
            os.path.join(PkgHelper.python_path(), 'Library', 'data'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'Library', 'share'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'Library', 'share', 'proj'),  # anaconda (Win)
            os.path.join(PkgHelper.python_path(), 'share'),  # anaconda (Linux)
            os.path.join(PkgHelper.python_path(), 'share', 'proj'),  # anaconda (Linux)
        ]

        # checking each folder
        for cand_data_folder in cand_data_folders:

            proj_db_path = os.path.join(cand_data_folder, 'proj.db')
            if os.path.exists(proj_db_path):

                pyproj.datadir.set_data_dir(cand_data_folder)
                cls.proj4_data_fixed = True
                if verbose:
                    logger.debug("set proj data folder = %s" % cand_data_folder)
                return

        raise RuntimeError("Unable to locate proj data at:\n%s" % "\n - ".join(cand_data_folders))

    @classmethod
    def crs_id(cls, wkt: str) -> Optional[int]:
        srs = osr.SpatialReference()
        srs.ImportFromWkt(wkt)
        srs.AutoIdentifyEPSG()
        return srs.GetAuthorityCode(None)

    @classmethod
    def lat_long_to_zone_number(cls, lat, long):
        if 56 <= lat < 64 and 3 <= long < 12:
            return 32

        if 72 <= lat <= 84 and long >= 0:
            if long < 9:
                return 31
            elif long < 21:
                return 33
            elif long < 33:
                return 35
            elif long < 42:
                return 37

        return int((long + 180) / 6) + 1
