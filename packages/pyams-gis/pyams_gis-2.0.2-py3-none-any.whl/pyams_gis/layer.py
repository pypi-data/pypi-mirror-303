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

import json
from persistent import Persistent
from zope.container.contained import Contained
from zope.interface import implementer
from zope.schema.fieldproperty import FieldProperty
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from pyams_gis import esri_leaflet, leaflet_google_mutant, leaflet_gp
from pyams_gis.interfaces.layer import IBaseTileMapLayer, IEsriFeatureMapLayer, IGeoJSONLayer, IGeoportalMapLayer, \
    IGoogleMapLayer, IMapLayer, ITileMapLayer, IWMSMapLayer, PYAMS_GIS_LAYERS_VOCABULARY
from pyams_gis.interfaces.utility import IMapManager
from pyams_i18n.interfaces import II18n
from pyams_utils.dict import update_dict
from pyams_utils.factory import factory_config
from pyams_utils.fanstatic import get_resource_path
from pyams_utils.registry import get_utility
from pyams_utils.request import check_request
from pyams_utils.vocabulary import vocabulary_config

__docformat__ = 'restructuredtext'

from pyams_gis import _


@vocabulary_config(name=PYAMS_GIS_LAYERS_VOCABULARY)
class MapLayersVocabulary(SimpleVocabulary):
    """Map layers vocabulary"""

    def __init__(self, context):
        request = check_request()
        manager = get_utility(IMapManager)
        super().__init__([
            SimpleTerm(layer.__name__,
                       title=II18n(layer).query_attribute('title',
                                                          request=request))
            for layer in manager.values()
        ])


@implementer(IMapLayer)
class MapLayer(Persistent, Contained):
    """Base tile map layer persistent class"""

    factory = None
    depends = {}
    layer_type = None
    layer_icon = None

    name = FieldProperty(IMapLayer['name'])
    title = FieldProperty(IMapLayer['title'])
    min_zoom = FieldProperty(IMapLayer['min_zoom'])
    max_zoom = FieldProperty(IMapLayer['max_zoom'])

    def get_configuration(self):
        """Get configuration mapping"""
        result = {
            'name': self.name,
            'title': II18n(self).query_attribute('title')
        }
        update_dict(result, 'factory', self.factory)
        update_dict(result, 'minZoom', self.min_zoom)
        update_dict(result, 'maxZoom', self.max_zoom)
        if self.depends:
            depends = {}
            for name, resource in self.depends.items():
                depends[name] = get_resource_path(resource)
            update_dict(result, 'dependsOn', depends)
        return result


class GeoJSONLayer(MapLayer):
    """GeoJSON layer"""

    factory = 'MyAMS.gis.factory.GeoJSON'
    layer_type = _("GeoJSON")

    url = FieldProperty(IGeoJSONLayer['url'])
    style = FieldProperty(IGeoJSONLayer['style'])

    def get_configuration(self):
        result = super(GeoJSONLayer, self).get_configuration()
        update_dict(result, 'url', self.url)
        if self.style:
            update_dict(result, 'style', json.loads(self.style))
        return result


class BaseTileMapLayer(MapLayer):
    """Base tile map layer"""

    attribution = FieldProperty(IBaseTileMapLayer['attribution'])
    bounds = FieldProperty(IBaseTileMapLayer['bounds'])

    def get_configuration(self):
        result = super(BaseTileMapLayer, self).get_configuration()
        update_dict(result, 'attribution', self.attribution)
        if self.bounds:
            point1, point2 = self.bounds.wgs_coordinates
            result['bounds'] = [{
                'lat': float(point1[1]),
                'lon': float(point1[0])
            }, {
                'lat': float(point2[1]),
                'lon': float(point2[0])
            }]
        return result


@factory_config(ITileMapLayer)
class TileMapLayer(BaseTileMapLayer):
    """Base tile map layer persistent class"""

    factory = 'MyAMS.gis.factory.TileLayer'
    layer_type = _("Tile layer")
    layer_icon = 'fas fa-layer-group'

    url = FieldProperty(ITileMapLayer['url'])

    def get_configuration(self):
        result = super(TileMapLayer, self).get_configuration()
        update_dict(result, 'url', self.url)
        return result


@factory_config(IWMSMapLayer)
class WMSMapLayer(TileMapLayer):
    """WMS map mayer persistent class"""

    factory = 'MyAMS.gis.factory.WMS'
    layer_type = _("WMS layer")
    layer_icon = 'fas fa-map'

    crs = FieldProperty(IWMSMapLayer['crs'])
    layers = FieldProperty(IWMSMapLayer['layers'])
    styles = FieldProperty(IWMSMapLayer['styles'])
    format = FieldProperty(IWMSMapLayer['format'])
    transparent = FieldProperty(IWMSMapLayer['transparent'])
    version = FieldProperty(IWMSMapLayer['version'])
    uppercase = FieldProperty(IWMSMapLayer['uppercase'])

    def get_configuration(self):
        result = super(WMSMapLayer, self).get_configuration()
        update_dict(result, 'crs', self.crs)
        update_dict(result, 'layers', self.layers)
        update_dict(result, 'styles', self.styles)
        update_dict(result, 'format', self.format)
        update_dict(result, 'transparent', self.transparent)
        update_dict(result, 'version', self.version)
        update_dict(result, 'uppercase', self.uppercase)
        return result


@factory_config(IGeoportalMapLayer)
class GeoportalMapLayer(BaseTileMapLayer):
    """Geoportal map layer persistent class"""

    factory = 'MyAMS.gis.factory.Geoportal.WMS'
    depends = {
        'L.geoportalLayer.WMS': leaflet_gp
    }
    layer_type = _("GeoPortal layer")
    layer_icon = 'far fa-map'

    api_key = FieldProperty(IGeoportalMapLayer['api_key'])
    layer_name = FieldProperty(IGeoportalMapLayer['layer_name'])
    crs = FieldProperty(IGeoportalMapLayer['crs'])

    def get_configuration(self):
        result = super(GeoportalMapLayer, self).get_configuration()
        update_dict(result, 'apiKey', self.api_key)
        update_dict(result, 'layer', self.layer_name)
        update_dict(result, 'crs', self.crs)
        return result


@factory_config(IEsriFeatureMapLayer)
class EsriFeatureMapLayer(MapLayer):
    """ESRI feature map layer"""

    factory = 'MyAMS.gis.factory.ESRI.Feature'
    depends = {
        'L.esri.featureLayer': esri_leaflet
    }
    layer_type = _("ESRI features layer")
    layer_icon = 'fas fa-map-signs'

    url = FieldProperty(IEsriFeatureMapLayer['url'])
    token = FieldProperty(IEsriFeatureMapLayer['token'])
    where = FieldProperty(IEsriFeatureMapLayer['where'])

    def get_configuration(self):
        result = super(EsriFeatureMapLayer, self).get_configuration()
        update_dict(result, 'url', self.url)
        update_dict(result, 'token', self.token)
        update_dict(result, 'where', self.where)
        return result


@factory_config(IGoogleMapLayer)
class GoogleMapLayer(MapLayer):
    """Google maps layer"""

    factory = 'MyAMS.gis.factory.Google'
    depends = {
        'L.gridLayer.googleMutant': leaflet_google_mutant
    }
    layer_type = _("Google Maps layer")
    layer_icon = 'fas fa-map-marker'

    api_key = FieldProperty(IGoogleMapLayer['api_key'])
    type = FieldProperty(IGoogleMapLayer['type'])

    def get_configuration(self):
        result = super(GoogleMapLayer, self).get_configuration()
        update_dict(result, 'apiKey', self.api_key)
        update_dict(result, 'type', self.type)
        return result
