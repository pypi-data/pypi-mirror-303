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

"""PyAMS GIS package

PyAMS GIS extension package
"""

__docformat__ = 'restructuredtext'

from fanstatic import Library, Resource
from pyramid.i18n import TranslationStringFactory

from pyams_utils.fanstatic import ExternalResource

_ = TranslationStringFactory('pyams_gis')


library = Library('pyams_gis', 'resources')

leaflet_css = Resource(library, 'css/leaflet-1.9.4.css',
                       minified='css/leaflet-1.9.4.min.css')

leaflet = Resource(library, 'js/leaflet-1.9.4.js',
                   minified='js/leaflet-1.9.4.min.js',
                   depends=[leaflet_css, ],
                   bottom=True)

esri_leaflet_gp = Resource(library, 'js/esri-leaflet-gp-3.0.0.js',
                           depends=[leaflet, ],
                           bottom=True)

esri_leaflet = Resource(library, 'js/esri-leaflet-3.0.12.js',
                        depends=[leaflet, ],
                        bottom=True)

leaflet_google = ExternalResource(library, 'https://maps.googleapis.com/maps/api/js',
                                  bottom=True)

leaflet_gp = Resource(library, 'js/GpPluginLeaflet.js',
                      minified='js/GpPluginLeaflet.min.js',
                      depends=[leaflet, ],
                      bottom=True)

leaflet_google_mutant = Resource(library, 'js/Leaflet.GoogleMutant.js',
                                 minified='js/Leaflet.GoogleMutant.min.js',
                                 depends=[leaflet, ],
                                 bottom=True)

pyams_gis = Resource(library, 'js/pyams_gis.js',
                     minified='js/pyams_gis.min.js',
                     depends=[leaflet, ],
                     bottom=True)


def includeme(config):
    """pyams_gis features include"""
    from .include import include_package  # pylint: disable=import-outside-toplevel
    include_package(config)
