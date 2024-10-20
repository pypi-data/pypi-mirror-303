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

"""PyAMS_gis.interfaces.configuration module

This module defines interface of map configuration.
"""

from zope.interface import Interface
from zope.schema import Bool, Choice, Int, List

from pyams_gis.interfaces import CRS, LAYER_CRS, LAYER_CRS_VOCABULARY
from pyams_gis.interfaces.layer import PYAMS_GIS_LAYERS_VOCABULARY
from pyams_gis.schema import GeoAreaField, GeoPointField

__docformat__ = 'restructuredtext'

from pyams_gis import _


MAP_CONFIGURATION_KEY = 'pyams_gis.configuration'


class IMapConfiguration(Interface):
    """Map configuration interface"""

    crs = Choice(title=_("CRS"),
                 description=_("Coordinates reference system to use for the map"),
                 vocabulary=LAYER_CRS_VOCABULARY,
                 default=LAYER_CRS[CRS.WGS84WM.value],
                 required=True)

    layers = List(title=_("Layers list"),
                  description=_("List of available layers displayed into this map"),
                  value_type=Choice(vocabulary=PYAMS_GIS_LAYERS_VOCABULARY),
                  required=False)

    auto_adjust = Bool(title=_("Adjust bounds to markers layer"),
                       description=_("If 'yes', map area will be automatically adjusted "
                                     "to markers layer(s), if any"),
                       required=True,
                       default=True)

    zoom_level = Int(title=_("Initial zoom level"),
                     description=_("Zoom level at which to display map, if auto-adjust is "
                                   "disabled or if there is only one marker"),
                     min=0,
                     max=18,
                     default=11,
                     required=False)

    initial_center = GeoPointField(title=_("Initial center"),
                                   description=_("Initial map location center"),
                                   required=False)

    initial_bounds = GeoAreaField(title=_("Initial bounds"),
                                  description=_("Initial map location bounds, if auto-adjust or "
                                                "initial center are disabled"),
                                  required=False)

    attribution_control = Bool(title=_("Attribution control?"),
                               description=_("If 'yes', an attribution control is added to map"),
                               required=True,
                               default=True)

    zoom_control = Bool(title=_("Zoom control?"),
                        description=_("If 'yes', a zoom control is added to map"),
                        required=True,
                        default=True)

    fullscreen_control = Bool(title=_("Fullscreen control?"),
                              description=_("If 'yes', a fullscreen control is added to map"),
                              required=True,
                              default=False)

    layer_control = Bool(title=_("Layers control?"),
                         description=_("If 'yes', a layer selection control is added to map"),
                         required=True,
                         default=False)

    keyboard = Bool(title=_("Keyboard navigation?"),
                    description=_("If 'yes', makes the map focusable and allows users to "
                                  "navigate with keyboard arrows and +/- keys; this option "
                                  "will not be activated on mobile devices"),
                    required=True,
                    default=True)

    scroll_wheel_zoom = Bool(title=_("Scroll wheel zoom?"),
                             description=_("If 'yes', the map can be zoomed using the mouse "
                                           "wheel; this should be avoided to get a good "
                                           "responsive behaviour and handle gestures"),
                             required=True,
                             default=False)

    def get_configuration(self):
        """Get map layers configuration"""


class IMapConfigurationTarget(Interface):
    """Map configuration target marker interface"""
