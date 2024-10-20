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

"""PyAMS_gis.zmi.configuration module

This module define PyAMS_gis default maps configuration management components.
"""

from pyramid.view import view_config
from zope.interface import Interface

from pyams_form.ajax import ajax_form_config
from pyams_form.field import Fields
from pyams_form.interfaces.form import IFormContent
from pyams_gis.interfaces import MANAGE_MAPS_PERMISSION
from pyams_gis.interfaces.configuration import IMapConfiguration
from pyams_gis.interfaces.utility import IMapManager
from pyams_gis.zmi.interfaces import IMapManagerMenu
from pyams_layer.interfaces import IPyAMSLayer
from pyams_utils.adapter import adapter_config
from pyams_utils.registry import query_utility
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.form import AdminEditForm
from pyams_zmi.interfaces import IAdminLayer
from pyams_zmi.zmi.viewlet.menu import NavigationMenuItem

__docformat__ = 'restructuredtext'

from pyams_gis import _


@view_config(name='get-map-configuration.json',
             context=Interface, request_type=IPyAMSLayer,
             renderer='json', xhr=True)
def get_map_configuration(request):
    """Get map configuration in JSON format"""
    manager = query_utility(IMapManager)
    if manager is not None:
        configuration = IMapConfiguration(manager)
        if configuration is not None:
            return configuration.get_configuration()


@viewlet_config(name='map-manager-configuration.menu',
                context=IMapManager, layer=IAdminLayer,
                manager=IMapManagerMenu, weight=10,
                permission=MANAGE_MAPS_PERMISSION)
class MapManagerConfigurationMenu(NavigationMenuItem):
    """Map manager configuration menu"""

    label = _("Default configuration")
    href = '#configuration.html'


@ajax_form_config(name='configuration.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class MapManagerConfigurationEditForm(AdminEditForm):
    """Map manager configuration edit form"""

    title = _("Map manager default configuration")
    legend = _("Default map configuration")

    fields = Fields(IMapConfiguration)


@adapter_config(required=(IMapManager, IAdminLayer, MapManagerConfigurationEditForm),
                provides=IFormContent)
def map_manager_configuration_content(context, request, form):
    """Map manager configuration content"""
    return IMapConfiguration(context)
