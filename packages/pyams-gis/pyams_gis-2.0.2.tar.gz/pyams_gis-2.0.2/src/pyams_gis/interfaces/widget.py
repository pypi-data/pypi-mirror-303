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
from pyams_form.interfaces import INPUT_MODE
from pyams_form.interfaces.widget import IObjectWidget
from pyams_form.template import widget_template_config
from pyams_layer.interfaces import IFormLayer, IPyAMSLayer

__docformat__ = 'restructuredtext'


@widget_template_config(mode=INPUT_MODE,
                        template='templates/geopoint-input.pt',
                        layer=IPyAMSLayer)
class IGeoPointWidget(IObjectWidget):
    """GeoPoint widget interface"""


class IGeoPointZWidget(IGeoPointWidget):
    """GeoPointZ widget interface"""


@widget_template_config(mode=INPUT_MODE,
                        template='templates/geoarea-input.pt',
                        layer=IPyAMSLayer)
class IGeoAreaWidget(IObjectWidget):
    """GeoArea widget interface"""
