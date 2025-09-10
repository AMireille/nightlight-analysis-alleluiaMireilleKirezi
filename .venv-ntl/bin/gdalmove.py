#!/home/kir2351763/RRA/other trainings/DSCBI/nightlight-analysis-alleluiaMireilleKirezi/.venv-ntl/bin/python3.11

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdalmove as a convenience to use as a script
from osgeo_utils.gdalmove import *  # noqa
from osgeo_utils.gdalmove import main

deprecation_warn("gdalmove")
sys.exit(main(sys.argv))
