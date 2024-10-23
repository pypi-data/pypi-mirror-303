#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_geotiff").version


from .bmi import GeoTiff

__all__ = [
    "GeoTiff",
]
