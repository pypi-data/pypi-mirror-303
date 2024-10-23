from __future__ import absolute_import

import pkg_resources
from bmi_geotiff import BmiGeoTiff as GeoTiff

GeoTiff.__name__ = "GeoTiff"
GeoTiff.METADATA = pkg_resources.resource_filename(__name__, "data/GeoTiff")

__all__ = [
    "GeoTiff",
]
