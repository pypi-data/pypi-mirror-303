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

import json
from zope.interface import Interface, alsoProvides, implementer_only

from pyams_form.browser.object import ObjectWidget
from pyams_form.interfaces import IObjectFactory
from pyams_form.interfaces.form import IForm
from pyams_form.interfaces.widget import IFieldWidget
from pyams_form.widget import FieldWidget
from pyams_gis.interfaces import IGeoPoint, IGeoPointZ
from pyams_gis.interfaces.widget import IGeoPointWidget, IGeoPointZWidget
from pyams_gis.schema import IGeoPointField, IGeoPointZField
from pyams_layer.interfaces import IFormLayer
from pyams_utils.adapter import adapter_config
from pyams_utils.factory import get_interface_name, get_object_factory
from pyams_utils.interfaces.data import IObjectData


#
# GeoPoint widget
#

@adapter_config(name=get_interface_name(IGeoPoint),
                required=(Interface, IFormLayer, IForm, IGeoPointWidget),
                provides=IObjectFactory)
def geo_point_object_widget_factory(*args):  # pylint: disable=unused-argument
    """GeoPoint object factory"""
    return get_object_factory(IGeoPoint)


@implementer_only(IGeoPointWidget)
class GeoPointWidget(ObjectWidget):
    """GeoPoint widget"""

    def update_widgets(self, set_errors=True):
        super().update_widgets(set_errors)
        widgets = self.widgets
        for name in ('longitude', 'latitude'):
            widget = widgets.get(name)
            if widget is not None:
                widget.readonly = 'readonly'
                widget.label_css_class = 'control-label col-md-3'
                widget.input_css_class = 'col-md-4'
        projection = widgets.get('projection')
        if projection is not None:
            projection.label_css_class = 'control-label col-md-3'
            projection.input_css_class = 'col-md-4'
            projection.object_data = {
                'ams-events-handlers': {
                    'select2:selecting': 'MyAMS.gis.position.beforeProjectionChange',
                    'change.select2': 'MyAMS.gis.position.changedProjection'
                }
            }
            alsoProvides(projection, IObjectData)

    @property
    def wgs_coordinates(self):
        value = self.field.get(self.field.interface(self.context))
        if not value:
            return json.dumps({
                'longitude': None,
                'latitude': None
            })
        point = value.wgs_coordinates
        return json.dumps({
            'longitude': float(point[0]),
            'latitude': float(point[1])
        })


@adapter_config(required=(IGeoPointField, IFormLayer),
                provides=IFieldWidget)
def GeoPointFieldWidget(field, request):
    """GeoPoint field widget factory"""
    return FieldWidget(field, GeoPointWidget(request))


#
# GeoPointZ widget
#

@adapter_config(name=get_interface_name(IGeoPointZ),
                required=(Interface, IFormLayer, IForm, IGeoPointZWidget),
                provides=IObjectFactory)
def geo_pointz_object_widget_factory(context, request, form, widget):
    """GeoPointZ object factory"""
    return get_object_factory(IGeoPointZ)


@implementer_only(IGeoPointZWidget)
class GeoPointZWidget(GeoPointWidget):
    """GeoPointZ widget"""

    def update_widgets(self, set_errors=True):
        super().update_widgets(set_errors)
        altitude = self.widgets.get('altitude')
        if altitude is not None:
            altitude.label_css_class = 'control-label col-md-3'
            altitude.input_css_class = 'col-md-2'

    @property
    def wgs_coordinates(self):
        value = self.field.get(self.field.interface(self.context))
        if not value:
            return json.dump({
                'longitude': None,
                'latitude': None,
                'altitude': None
            })
        point = value.wgs_coordinates
        return json.dumps({
            'longitude': float(point[0]),
            'latitude': float(point[1]),
            'altitude': value.altitude
        })


@adapter_config(required=(IGeoPointZField, IFormLayer),
                provides=IFieldWidget)
def GeoPointZFieldWidget(field, request):
    """GeoPointZ field widget factory"""
    return FieldWidget(field, GeoPointZWidget(request))
