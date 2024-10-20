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

"""PyAMS_gis.zmi module

This module defines main maps manager layers view.
"""

from pyramid.decorator import reify
from pyramid.view import view_config
from zope.interface import Interface, implementer

from pyams_gis.interfaces import MANAGE_MAPS_PERMISSION
from pyams_gis.interfaces.utility import IMapManager
from pyams_gis.zmi.interfaces import IMapManagerLayersTable, IMapManagerLayersView, IMapManagerMenu
from pyams_layer.interfaces import IPyAMSLayer
from pyams_pagelet.pagelet import pagelet_config
from pyams_site.interfaces import ISiteRoot
from pyams_table.interfaces import IColumn, IValues
from pyams_utils.adapter import ContextRequestViewAdapter, adapter_config
from pyams_utils.factory import factory_config
from pyams_utils.registry import get_utility, query_utility
from pyams_utils.url import absolute_url
from pyams_viewlet.manager import viewletmanager_config
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.interfaces import IAdminLayer
from pyams_zmi.interfaces.table import ITableElementEditor
from pyams_zmi.interfaces.viewlet import IControlPanelMenu
from pyams_zmi.table import IconColumn, NameColumn, Table, TableAdminView, TableElementEditor, TrashColumn
from pyams_zmi.zmi.viewlet.menu import NavigationMenuItem

__docformat__ = 'restructuredtext'

from pyams_gis import _


@adapter_config(required=(IMapManager, IAdminLayer, Interface),
                provides=ITableElementEditor)
class MapManagerTableElementEditor(TableElementEditor):
    """Maps manager table element editor"""
    
    view_name = 'admin#map-layers.html'
    modal_target = False
    
    def __new__(cls, context, request, view):
        if not request.has_permission(MANAGE_MAPS_PERMISSION, context=context):
            return None
        return TableElementEditor.__new__(cls)
    
    
@viewlet_config(name='maps.menu',
                context=ISiteRoot, layer=IAdminLayer,
                manager=IControlPanelMenu, weight=60,
                permission=MANAGE_MAPS_PERMISSION)
class MapManagerMenu(NavigationMenuItem):
    """Maps manager menu"""
    
    label = _("map-manager-menu", default="Maps manager")
    icon_class = 'fas fa-map-marker'
    
    def __new__(cls, context, request, view, manager):
        manager = query_utility(IMapManager)
        if (manager is None) or not manager.show_home_menu:
            return None
        return NavigationMenuItem.__new__(cls)
    
    def get_href(self):
        """Menu URL getter"""
        manager = get_utility(IMapManager)
        return absolute_url(manager, self.request, 'admin')


@viewletmanager_config(name='map-layers.menu',
                       context=IMapManager, layer=IAdminLayer,
                       manager=IControlPanelMenu, weight=60,
                       permission=MANAGE_MAPS_PERMISSION,
                       provides=IMapManagerMenu)
class MapManagerLayersMenu(NavigationMenuItem):
    """Maps manager layers menu"""
    
    label = _("Maps manager")
    icon_class = 'fas fa-map-marker'
    
    href = '#map-layers.html'


@pagelet_config(name='map-layers.html',
                context=IMapManager, layer=IPyAMSLayer,
                permission=MANAGE_MAPS_PERMISSION)
@implementer(IMapManagerLayersView)
class MapManagerLayersView(TableAdminView):
    """Map manager layers view"""

    title = _("Maps manager layers")
    table_class = IMapManagerLayersTable
    table_label = _("List of maps layers")

    @property
    def back_url(self):
        """Form back URL getter"""
        return absolute_url(self.request.root, self.request, 'admin#utilities.html')

    back_url_target = None


@factory_config(IMapManagerLayersTable)
class MapManagerLayersTable(Table):
    """Maps manager layers table"""
    
    display_if_empty = True
    
    @reify
    def data_attributes(self):
        attributes = super().data_attributes
        manager = get_utility(IMapManager)
        attributes['table'].update({
            'data-ams-location': absolute_url(manager, self.request),
            'data-ams-order': '1,asc'
        })
        return attributes


@adapter_config(required=(IMapManager, IAdminLayer, IMapManagerLayersTable),
                provides=IValues)
class MapManagerLayersValues(ContextRequestViewAdapter):
    """Maps manager layers table values"""

    @property
    def values(self):
        """Maps manager layers table values getter"""
        yield from self.context.values()


@adapter_config(name='icon',
                required=(IMapManager, IAdminLayer, IMapManagerLayersTable),
                provides=IColumn)
class MapManagerLayersIconColumn(IconColumn):
    """Maps manager layers icon column"""

    weight = 1

    def get_icon_class(self, item):
        """Icon class getter"""
        return item.layer_icon

    def get_icon_hint(self, item):
        """Icon hint getter"""
        translate = self.request.localizer.translate
        return translate(item.layer_type)


@adapter_config(name='name',
                required=(IMapManager, IAdminLayer, IMapManagerLayersTable),
                provides=IColumn)
class MapManagerLayersNameColumn(NameColumn):
    """Maps manager layers name column"""


@adapter_config(name='trash',
                required=(IMapManager, IAdminLayer, IMapManagerLayersTable),
                provides=IColumn)
class MapManagerLayersTrashColumn(TrashColumn):
    """Maps manager layers trash column"""

    permission = MANAGE_MAPS_PERMISSION


@view_config(name='delete-element.json',
             context=IMapManager, request_type=IPyAMSLayer,
             permission=MANAGE_MAPS_PERMISSION, renderer='json', xhr=True)
def delete_map_layer(request):
    """Delete map layer"""
    return delete_map_layer(request)
