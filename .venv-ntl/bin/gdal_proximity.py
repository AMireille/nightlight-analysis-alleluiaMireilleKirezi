#!/home/kir2351763/RRA/other trainings/DSCBI/nightlight-analysis-alleluiaMireilleKirezi/.venv-ntl/bin/python3.11

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdal_proximity as a convenience to use as a script
from osgeo_utils.gdal_proximity import *  # noqa
from osgeo_utils.gdal_proximity import main

deprecation_warn("gdal_proximity")
sys.exit(main(sys.argv))
