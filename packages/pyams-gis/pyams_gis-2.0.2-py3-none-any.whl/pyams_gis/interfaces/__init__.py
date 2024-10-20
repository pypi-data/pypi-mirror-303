#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_gis.interfaces module

This module defines main package interfaces.
"""

from enum import Enum

from zope.interface import Attribute, Interface, Invalid, invariant
from zope.schema import Choice
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from pyams_utils.list import is_not_none
from pyams_utils.schema import DottedDecimalField

from pyams_gis import _


REST_POINT_TRANSFORM_ROUTE = 'pyams_gis.rest.transform.point'
REST_POINT_TRANSFORM_ROUTE_SETTING = f'{REST_POINT_TRANSFORM_ROUTE}_route.path'
REST_POINT_TRANSFORM_PATH = '/api/gis/rest/transform/point'

REST_AREA_TRANSFORM_ROUTE = 'pyams_gis.rest.transform.area'
REST_AREA_TRANSFORM_ROUTE_SETTING = f'{REST_AREA_TRANSFORM_ROUTE}_route.path'
REST_AREA_TRANSFORM_PATH = '/api/gis/rest/transform/area'


#
# Custom permissions
#

MANAGE_MAPS_PERMISSION = 'pyams.ManageMaps'
'''Permission required to manage default maps configuration and layers'''


#
# Main maps CRS
#

class CRS(Enum):
    """Common CRS values"""
    WGS84 = 4326
    WGS84WM = 3857
    RGF93 = 2154
    LAMBERT_IIE = 27572
    UTM_20N = 4559
    UTM_22N = 2972
    UTM_38S = 4471
    UTM_40S = 2975


COORDINATES_PROJECTIONS = {
    CRS.WGS84.value: _("WGS84 (GPS)"),
    CRS.WGS84WM.value: _("WGS84 Web Mercator"),
    CRS.RGF93.value: _("Lambert 93 (Metropolitan France)"),
    CRS.LAMBERT_IIE.value: _("Extended Lambert II (Metropolitan France)"),
    CRS.UTM_20N.value: _("UTM Zone 20N (Martinique, Guadeloupe)"),
    CRS.UTM_22N.value: _("UTM Zone 22N (Guyane)"),
    CRS.UTM_38S.value: _("UTM Zone 38S (Mayotte)"),
    CRS.UTM_40S.value: _("UTM Zone 40S (La Réunion)")
}


COORDINATES_PROJECTION_VOCABULARY = SimpleVocabulary([
    SimpleTerm(v, title=t)
    for v, t in COORDINATES_PROJECTIONS.items()
])


LAYER_CRS = {
    CRS.WGS84.value: 'L.CRS.EPSG4326',
    CRS.WGS84WM.value: 'L.CRS.EPSG3857',
    CRS.RGF93.value: 'L.geoportalCRS.EPSG2154',
    CRS.LAMBERT_IIE.value: 'L.geoportalCRS.EPSG27572'
}

LAYER_CRS_VOCABULARY = SimpleVocabulary([
    SimpleTerm(t, title=COORDINATES_PROJECTIONS[v])
    for v, t in LAYER_CRS.items()
])


class IGeoInfo(Interface):
    """Base geographic information interface"""

    def to_json(self):
        """Return JSON representation of current object"""


class IGeoPoint(IGeoInfo):
    """GeoPoint attribute interface"""

    longitude = DottedDecimalField(title=_("Longitude"),
                                   required=False)

    latitude = DottedDecimalField(title=_("Latitude"),
                                  required=False)

    projection = Choice(title=_("Projection system"),
                        vocabulary=COORDINATES_PROJECTION_VOCABULARY,
                        default=CRS.WGS84.value,
                        required=True)

    @invariant
    def check_coordinates(self):
        """Point coordinates checker"""
        data = tuple(map(is_not_none, (self.longitude, self.latitude)))
        if len(data) != 2:
            raise Invalid(_("You must set longitude and latitude, or None!"))
        if self.longitude and not self.projection:
            raise Invalid(_("You can't set coordinates without setting projection!"))

    def get_coordinates(self, projection=CRS.WGS84.value):
        """Get coordinates translated to given projection"""

    wgs_coordinates = Attribute("Coordinates tuple in WGS84 projection")


class IGeoPointZ(IGeoPoint):
    """GeoPointZ attribute interface"""

    altitude = DottedDecimalField(title=_("Altitude"),
                                  required=False)


class IGeoArea(IGeoInfo):
    """Geographic area defined by a rectangle"""

    x1 = DottedDecimalField(title=_("West limit"),
                            required=False)

    y1 = DottedDecimalField(title=_("South limit"),
                            required=False)

    x2 = DottedDecimalField(title=_("East limit"),
                            required=False)

    y2 = DottedDecimalField(title=_("North limit"),
                            required=False)

    projection = Choice(title=_("Projection system"),
                        vocabulary=COORDINATES_PROJECTION_VOCABULARY,
                        default=CRS.WGS84.value,
                        required=True)

    @invariant
    def check_coordinates(self):
        """Area coordinates checker"""
        data = tuple(map(is_not_none, (self.x1, self.x2, self.y1, self.y2)))
        if len(data) != 4:
            raise Invalid(_("You must set all coordinates or None!"))
        if self.x1 and not self.projection:
            raise Invalid(_("You can't set coordinates without setting projection!"))

    def get_coordinates(self, projection=CRS.WGS84.value):
        """Get coordinates translated to given projection"""

    wgs_coordinates = Attribute("Coordinates in WGS84 projection")
