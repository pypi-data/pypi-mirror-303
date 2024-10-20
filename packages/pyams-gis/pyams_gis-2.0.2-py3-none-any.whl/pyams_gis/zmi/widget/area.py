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
from pyams_gis.interfaces import IGeoArea
from pyams_gis.interfaces.widget import IGeoAreaWidget
from pyams_gis.schema import IGeoAreaField
from pyams_layer.interfaces import IFormLayer
from pyams_utils.adapter import adapter_config
from pyams_utils.factory import get_interface_name, get_object_factory
from pyams_utils.interfaces.data import IObjectData


#
# GeoArea widget
#

@adapter_config(name=get_interface_name(IGeoArea),
                required=(Interface, IFormLayer, IForm, IGeoAreaWidget),
                provides=IObjectFactory)
def geo_area_object_widget_factory(*args):  # pylint: disable=unused-argument
    """GeoArea object factory"""
    return get_object_factory(IGeoArea)


@implementer_only(IGeoAreaWidget)
class GeoAreaWidget(ObjectWidget):
    """GeoArea widget"""
    
    def update_widgets(self, set_errors=True):
        super().update_widgets(set_errors)
        widgets = self.widgets
        for name in ('x1', 'y1', 'x2', 'y2'):
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
                    'select2:selecting': 'MyAMS.gis.area.beforeProjectionChange',
                    'change.select2': 'MyAMS.gis.area.changedProjection'
                }
            }
            alsoProvides(projection, IObjectData)
    
    @property
    def wgs_coordinates(self):
        value = self.field.get(self.field.interface(self.context))
        if not value:
            return json.dumps({
                'x1': None,
                'y1': None,
                'x2': None,
                'y2': None
            })
        point1, point2 = value.wgs_coordinates
        return json.dumps({
            'x1': float(point1[0]),
            'y1': float(point1[1]),
            'x2': float(point2[0]),
            'y2': float(point2[1])
        })


@adapter_config(required=(IGeoAreaField, IFormLayer),
                provides=IFieldWidget)
def GeoAreaFieldWidget(field, request):
    """GeoArea field widget factory"""
    return FieldWidget(field, GeoAreaWidget(request))
