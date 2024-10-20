#
# Copyright (c) 2015-2024 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_*** module

"""

try:
    from osgeo.osr import SpatialReference, CoordinateTransformation
    have_gdal = True
except ImportError:
    have_gdal = False

from decimal import Decimal

from persistent import Persistent
from zope.schema.fieldproperty import FieldProperty

from pyams_gis.interfaces import CRS, IGeoPoint, IGeoPointZ
from pyams_utils.factory import factory_config
from pyams_utils.list import is_not_none

__docformat__ = 'restructuredtext'


@factory_config(IGeoPoint)
class GeoPoint(Persistent):
    """GeoPoint attribute object"""

    longitude = FieldProperty(IGeoPoint['longitude'])
    latitude = FieldProperty(IGeoPoint['latitude'])
    projection = FieldProperty(IGeoPoint['projection'])

    def __init__(self, data=None, **kwargs):
        super().__init__()
        if 'longitude' in kwargs:
            self.longitude = Decimal(kwargs['longitude'])
        if 'latitude' in kwargs:
            self.latitude = Decimal(kwargs['latitude'])
        if 'projection' in kwargs:
            self.projection = kwargs['projection']

    def __bool__(self):
        return len(tuple(map(is_not_none, (self.longitude, self.latitude)))) == 2

    def get_coordinates(self, projection=CRS.WGS84.value):
        if projection == self.projection:
            return self.longitude, self.latitude
        if (not have_gdal) or not self:
            return None, None
        source = SpatialReference()
        source.ImportFromEPSG(self.projection)
        destination = SpatialReference()
        destination.ImportFromEPSG(projection)
        transformation = CoordinateTransformation(source, destination)
        return transformation.TransformPoint(float(self.longitude), float(self.latitude))[0:2]

    @property
    def wgs_coordinates(self):
        return self.get_coordinates(CRS.WGS84.value)

    def to_json(self):
        if not self:
            return None
        return {
            'lon': float(self.longitude),
            'lat': float(self.latitude),
            'crs': float(self.projection)
        }


@factory_config(IGeoPointZ)
class GeoPointZ(GeoPoint):
    """GeoPointZ attribute object"""

    altitude = FieldProperty(IGeoPointZ['altitude'])

    def __init__(self, data=None, **kwargs):
        super().__init__(data, **kwargs)
        if 'altitude' in kwargs:
            self.altitude = Decimal(kwargs['altitude'])

    def to_json(self):
        result = super().to_json()
        if result:
            result.update({
                'alt': float(self.altitude)
            })
        return result
