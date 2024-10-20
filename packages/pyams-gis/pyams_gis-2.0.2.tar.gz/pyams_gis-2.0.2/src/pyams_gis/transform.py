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

__docformat__ = 'restructuredtext'

from decimal import Decimal

try:
    from osgeo.osr import SpatialReference, CoordinateTransformation
    have_gdal = True
except ImportError:
    have_gdal = False


def transform(point, from_srid, to_srid):
    """Transform point coordinates from source projection to another projection

    :param point: source point coordinates; can be given as a (longitude, latitude) tuple
        or as a mapping containing both keys
    :param from_srid: source coordinates system given as SRID
    :param to_srid: target coordinates system given as SRID
    :return: mapping with new 'point' coordinates containing transformed coordinates, and 'projection'
        key containing SRID of result projection system
    """
    longitude = None
    latitude = None
    if isinstance(point, (list, tuple)):
        longitude, latitude = map(float, point)
    elif isinstance(point, dict):
        longitude = float(point['longitude'])
        latitude = float(point['latitude'])
    from_srid = int(from_srid)
    to_srid = int(to_srid)
    if (not have_gdal) or (from_srid == to_srid):
        return {
            'point': {
                'longitude': longitude,
                'latitude': latitude
            },
            'srid': from_srid
        }
    source = SpatialReference()
    source.ImportFromEPSG(from_srid)
    destination = SpatialReference()
    destination.ImportFromEPSG(to_srid)
    transformed = CoordinateTransformation(source, destination).TransformPoint(longitude, latitude)
    return {
        'point': {
            'longitude': transformed[0],
            'latitude': transformed[1]
        },
        'srid': to_srid
    }
