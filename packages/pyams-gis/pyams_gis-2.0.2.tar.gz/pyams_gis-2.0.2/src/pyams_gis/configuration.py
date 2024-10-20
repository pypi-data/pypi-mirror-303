# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

__docformat__ = 'restructuredtext'

from persistent import Persistent
from zope.container.contained import Contained
from zope.schema.fieldproperty import FieldProperty

from pyams_gis.interfaces.configuration import IMapConfiguration, IMapConfigurationTarget, MAP_CONFIGURATION_KEY
from pyams_gis.interfaces.utility import IMapManager
from pyams_utils.adapter import adapter_config, get_annotation_adapter
from pyams_utils.factory import factory_config
from pyams_utils.registry import get_utility


@factory_config(IMapConfiguration)
class MapConfiguration(Persistent, Contained):
    """Map configuration persistent class"""

    crs = FieldProperty(IMapConfiguration['crs'])
    layers = FieldProperty(IMapConfiguration['layers'])
    auto_adjust = FieldProperty(IMapConfiguration['auto_adjust'])
    zoom_level = FieldProperty(IMapConfiguration['zoom_level'])
    initial_center = FieldProperty(IMapConfiguration['initial_center'])
    initial_bounds = FieldProperty(IMapConfiguration['initial_bounds'])
    attribution_control = FieldProperty(IMapConfiguration['attribution_control'])
    zoom_control = FieldProperty(IMapConfiguration['zoom_control'])
    fullscreen_control = FieldProperty(IMapConfiguration['fullscreen_control'])
    layer_control = FieldProperty(IMapConfiguration['layer_control'])
    keyboard = FieldProperty(IMapConfiguration['keyboard'])
    scroll_wheel_zoom = FieldProperty(IMapConfiguration['scroll_wheel_zoom'])

    def get_configuration(self):
        result = {
            'crs': self.crs,
            'layerControl': self.layer_control,
            'attributionControl': self.attribution_control,
            'zoomControl': self.zoom_control,
            'fullscreenControl': self.fullscreen_control,
            'keyboard': self.keyboard,
            'scrollWheelZoom': self.scroll_wheel_zoom,
            'zoom': self.zoom_level
        }
        if self.auto_adjust:
            result['adjust'] = 'auto'
        if self.initial_center:
            gps_location = self.initial_center.wgs_coordinates
            result['center'] = {
                'lat': float(gps_location[1]),
                'lon': float(gps_location[0])
            }
        elif self.initial_bounds:
            point1, point2 = self.initial_bounds.wgs_coordinates
            result['bounds'] = [{
                'lat': float(point1[1]),
                'lon': float(point1[0])
            }, {
                'lat': float(point2[1]),
                'lon': float(point2[0])
            }]
        else:
            # Near center default location
            result['center'] = {
                'lat': 45,
                'lon': 5.0
            }
        if self.layers:
            manager = get_utility(IMapManager)
            layers = []
            for name in self.layers:
                layer = manager.get(name)
                if layer is not None:
                    layers.append(layer.get_configuration())
            result['layers'] = layers
        return result


@adapter_config(required=IMapConfigurationTarget,
                provides=IMapConfiguration)
def map_configuration(context):
    """Map configuration adapter"""
    return get_annotation_adapter(context, MAP_CONFIGURATION_KEY, IMapConfiguration)
