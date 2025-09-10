#!/home/kir2351763/RRA/other trainings/DSCBI/nightlight-analysis-alleluiaMireilleKirezi/.venv-ntl/bin/python3.11

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.ogrmerge as a convenience to use as a script
from osgeo_utils.ogrmerge import *  # noqa
from osgeo_utils.ogrmerge import main

deprecation_warn("ogrmerge")
sys.exit(main(sys.argv))
