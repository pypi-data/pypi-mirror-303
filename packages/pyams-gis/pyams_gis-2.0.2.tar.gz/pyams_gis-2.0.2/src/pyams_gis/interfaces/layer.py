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

from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import Attribute
from zope.location.interfaces import IContained
from zope.schema import Bool, Choice, Int, Text, TextLine
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from pyams_gis.interfaces import LAYER_CRS_VOCABULARY
from pyams_gis.schema import GeoAreaField
from pyams_i18n.schema import I18nTextLineField

__docformat__ = 'restructuredtext'

from pyams_gis import _


#
# Leaflet map layers interfaces
#

PYAMS_GIS_LAYERS_VOCABULARY = 'pyams_gis.layers'


class IMapLayer(IContained, IAttributeAnnotatable):
    """Base map layer interface"""

    factory = Attribute("Layer factory name")

    depends = Attribute("List of layer factory dependent objects")

    name = TextLine(title=_("Layer name"),
                    required=True)

    layer_type = Attribute("Layer type")

    layer_icon = Attribute("Layer icon")

    title = I18nTextLineField(title=_("Layer title"),
                              description=_("Full layer title"),
                              required=True)

    min_zoom = Int(title=_("Minimum zoom level"),
                   description=_("Minimum zoom level at which layer is displayed"),
                   default=0,
                   required=True)

    max_zoom = Int(title=_("Maximum zoom level"),
                   description=_("Maximum zoom level at which layer is displayed"),
                   default=18,
                   required=True)

    def get_configuration(self):
        """Get layer configuration mapping"""


class IGeoJSONLayer(IMapLayer):
    """GeoJSON map layer interface"""

    url = TextLine(title=_("Layer URL"),
                   description=_("URL used to get access to JSON data"),
                   required=True)

    style = Text(title=_("Layer style"),
                 description=_("Layer style, provided in Leaflet JSON format"),
                 required=False)


class IBaseTileMapLayer(IMapLayer):
    """Base tiles map layer interface"""

    attribution = TextLine(title=_("Layer attribution"),
                           description=_("String used by the attribution control"),
                           required=False)

    bounds = GeoAreaField(title=_("Layer bounds"),
                          description=_("Geographical bounds into which layer tiles are displayed"),
                          required=False)


class ITileMapLayer(IBaseTileMapLayer):
    """Tiles map layer interface"""

    url = TextLine(title=_("URL template"),
                   description=_("URL template used to get layer tiles (see leaflet.js docs)"),
                   default='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                   required=True)


class IWMSMapLayer(ITileMapLayer):
    """WMS map layer interface"""

    crs = Choice(title=_("CRS"),
                 description=_("Coordinates reference system to use for map requests; defaults to map request"),
                 vocabulary=LAYER_CRS_VOCABULARY,
                 required=False)

    layers = TextLine(title=_("Layers"),
                      description=_("Comma-separated list of WMS layers to show"),
                      required=False)

    styles = TextLine(title=_("Styles"),
                      description=_("Comma-separated list of WMS styles"),
                      required=False)

    format = TextLine(title=_("Layer format"),
                      description=_("WMS image format; use 'image/png' for layers with transparency"),
                      required=True,
                      default='image/png')

    transparent = Bool(title=_("Transparent?"),
                       description=_("If 'yes', the WMS services will return images with transparency"),
                       required=True,
                       default=False)

    version = TextLine(title=_("Version"),
                       description=_("Version of the WMS service to use"),
                       required=True,
                       default='1.1.1')

    uppercase = Bool(title=_("Uppercase?"),
                     description=_("If 'yes', WMS request parameters keys will be uppercase"),
                     required=True,
                     default=False)


class IGeoportalMapLayer(IBaseTileMapLayer):
    """French IGN map layer interface"""

    api_key = TextLine(title=_("API key"),
                       description=_("Key used to access layer data"),
                       required=True)

    layer_name = TextLine(title=_("IGN layer name"),
                          description=_("Name of layer in IGN format"),
                          required=True)

    crs = Choice(title=_("CRS"),
                 description=_("Coordinates reference system to use for map requests; defaults to map request"),
                 vocabulary=LAYER_CRS_VOCABULARY,
                 required=False)


class IEsriBaseMapLayer(ITileMapLayer):
    """ESRI map layer interface"""


class IEsriFeatureMapLayer(IMapLayer):
    """ESRI feature layer interface"""

    url = TextLine(title=_("Layer URL"),
                   description=_("URL used to get the feature layer"),
                   required=True)

    token = TextLine(title=_("Token"),
                     description=_("Token used in all service requests"),
                     required=False)

    where = TextLine(title=_("Where condition"),
                     description=_("Optional expression used to filter features"),
                     required=False)


GOOGLE_MAP_TYPES = {'roadmap': _("Roads map"),
                    'satellite': _("Satellite"),
                    'hybrid': _("Hybrid"),
                    'terrain': _("Terrain")}


GOOGLE_MAP_TYPES_VOCABULARY = SimpleVocabulary([
    SimpleTerm(v, title=t)
    for v, t in GOOGLE_MAP_TYPES.items()
])


class IGoogleMapLayer(IMapLayer):
    """Google Maps layer"""

    api_key = TextLine(title=_("API key"),
                       description=_("Google API key used to access maps data"),
                       required=True)

    type = Choice(title=_("Map type"),
                  description=_("Type of GoogleMaps layer type"),
                  vocabulary=GOOGLE_MAP_TYPES_VOCABULARY,
                  default='roadmap',
                  required=True)
