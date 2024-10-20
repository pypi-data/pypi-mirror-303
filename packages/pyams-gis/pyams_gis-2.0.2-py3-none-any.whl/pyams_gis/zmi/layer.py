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

"""PyAMS_gis.zmi.layer module

This module defines map layers management components.
"""

from pyramid.events import subscriber
from zope.interface import Interface, Invalid, implementer

from pyams_form.ajax import ajax_form_config
from pyams_form.field import Fields
from pyams_form.interfaces import DISPLAY_MODE
from pyams_form.interfaces.form import IAJAXFormRenderer, IDataExtractedEvent
from pyams_gis.interfaces import MANAGE_MAPS_PERMISSION
from pyams_gis.interfaces.layer import IEsriFeatureMapLayer, IGeoportalMapLayer, IGoogleMapLayer, IMapLayer, \
    ITileMapLayer, IWMSMapLayer
from pyams_gis.interfaces.utility import IMapManager
from pyams_gis.layer import EsriFeatureMapLayer, GeoportalMapLayer, GoogleMapLayer, TileMapLayer, WMSMapLayer
from pyams_gis.zmi.interfaces import IMapManagerLayersTable, IMapLayerAddForm
from pyams_i18n.interfaces import II18n
from pyams_layer.interfaces import IPyAMSLayer
from pyams_security.interfaces import IViewContextPermissionChecker
from pyams_skin.interfaces.view import IModalEditForm
from pyams_skin.viewlet.menu import MenuItem
from pyams_utils.adapter import ContextAdapter, ContextRequestViewAdapter, adapter_config
from pyams_utils.interfaces import MISSING_INFO
from pyams_utils.registry import get_utility, query_utility
from pyams_utils.traversing import get_parent
from pyams_utils.url import absolute_url
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.form import AdminModalAddForm, AdminModalEditForm
from pyams_zmi.helper.event import get_json_table_row_add_callback, get_json_table_row_refresh_callback
from pyams_zmi.interfaces import IAdminLayer, IObjectLabel, TITLE_SPAN_BREAK
from pyams_zmi.interfaces.form import IFormTitle
from pyams_zmi.interfaces.table import ITableElementEditor
from pyams_zmi.interfaces.viewlet import IContextAddingsViewletManager
from pyams_zmi.table import TableElementEditor
from pyams_zmi.utils import get_object_label

__docformat__ = 'restructuredtext'

from pyams_gis import _


class MapLayerAddMenu(MenuItem):
    """Map layer add menu"""

    modal_target = True

    def get_href(self):
        manager = get_utility(IMapManager)
        return absolute_url(manager, self.request, self.href)


@implementer(IMapLayerAddForm)
class MapLayerAddForm(AdminModalAddForm):
    """Map layer add form"""

    @property
    def subtitle(self):
        translate = self.request.localizer.translate
        return translate(_("New layer: {}")).format(translate(self.content_label))

    legend = _("New layer properties")
    content_factory = None
    content_label = MISSING_INFO

    @property
    def fields(self):
        return Fields(self.content_factory).omit('__name__', '__parent__')

    def add(self, obj):
        self.context[obj.name] = obj


@subscriber(IDataExtractedEvent, form_selector=IMapLayerAddForm)
def handle_new_map_layer_data(event):
    """Handle new layer data extraction"""
    manager = query_utility(IMapManager)
    name = event.data.get('name')
    if name in manager:
        event.form.widgets.errors += (Invalid(_("Specified layer name already exists!")))


@adapter_config(required=(IMapManager, IAdminLayer, IMapLayerAddForm),
                provides=IAJAXFormRenderer)
class MapLayerAddFormRenderer(ContextRequestViewAdapter):
    """Map layer add form AJAX renderer"""

    def render(self, changes):
        """AJAX form renderer"""
        if changes is None:  # WARNING: creating an empty container will return a "false" value!
            return None
        manager = get_utility(IMapManager)
        return {
            'callbacks': [
                get_json_table_row_add_callback(manager, self.request,
                                                IMapManagerLayersTable, changes)
            ]
        }


@adapter_config(required=(IMapLayer, IPyAMSLayer),
                provides=IObjectLabel)
def map_layer_label(context, request):
    """Map layer label adapter"""
    return II18n(context).query_attribute('title', request=request)


@adapter_config(required=(IMapLayer, IAdminLayer, Interface),
                provides=ITableElementEditor)
class MapLayerEditor(TableElementEditor):
    """Map layer editor adapter"""


@adapter_config(required=IMapLayer,
                provides=IViewContextPermissionChecker)
class MapLayerPermissionChecker(ContextAdapter):
    """Map layer permission checker"""

    edit_permission = MANAGE_MAPS_PERMISSION


class MapLayerPropertiesEditForm(AdminModalEditForm):
    """Map layer properties edit form"""

    legend = _("Layer properties")
    content_factory = None
    content_label = MISSING_INFO

    @property
    def fields(self):
        return Fields(self.content_factory).omit('__name__', '__parent__')

    def update_widgets(self, prefix=None):
        super().update_widgets()
        name = self.widgets.get('name')
        if name is not None:
            name.mode = DISPLAY_MODE


@adapter_config(required=(IMapLayer, IAdminLayer, IModalEditForm),
                provides=IFormTitle)
def map_layer_edit_form_title(context, request, form):
    """Map layer edit form title"""
    translate = request.localizer.translate
    manager = get_utility(IMapManager)
    layer = get_parent(context, IMapLayer)
    return TITLE_SPAN_BREAK.format(
        get_object_label(manager, request, form),
        translate(_("Layer: {} ({})")).format(get_object_label(layer, request, form),
                                              translate(layer.layer_type)))


@adapter_config(required=(IMapLayer, IAdminLayer, IModalEditForm),
                provides=IAJAXFormRenderer)
class MapLayerPropertiesAJAXRenderer(ContextRequestViewAdapter):
    """Map layer properties AJAX renderer"""

    def render(self, changes):
        """AJAX form renderer"""
        if not changes:
            return None
        manager = get_utility(IMapManager)  # pylint: disable=invalid-name
        return get_json_table_row_refresh_callback(manager, self.request,
                                                   IMapManagerLayersTable, self.context)


#
# Tile layers components
#

@viewlet_config(name='add-tile-layer.menu',
                context=IMapManager, layer=IAdminLayer, view=IMapManagerLayersTable,
                manager=IContextAddingsViewletManager, weight=10,
                permission=MANAGE_MAPS_PERMISSION)
class TileLayerAddMenu(MapLayerAddMenu):
    """Tile layer add menu"""

    label = _("Add tile layer...")
    href = 'add-tile-layer.html'
    icon_class = TileMapLayer.layer_icon


class TileLayerMixinForm:
    """Tile layer mixin form"""

    content_factory = ITileMapLayer
    content_label = TileMapLayer.layer_type


@ajax_form_config(name='add-tile-layer.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class TileLayerAddForm(TileLayerMixinForm, MapLayerAddForm):
    """Tile layer add form"""


@ajax_form_config(name='properties.html',
                  context=ITileMapLayer, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class TileLayerPropertiesEditForm(TileLayerMixinForm, MapLayerPropertiesEditForm):
    """Tile layer properties edit form"""


#
# WMS layers components
#

@viewlet_config(name='add-wms-layer.menu',
                context=IMapManager, layer=IAdminLayer, view=IMapManagerLayersTable,
                manager=IContextAddingsViewletManager, weight=20,
                permission=MANAGE_MAPS_PERMISSION)
class WMSLayerAddMenu(MapLayerAddMenu):
    """WMS layer add menu"""

    label = _("Add WMS layer...")
    href = 'add-wms-layer.html'
    icon_class = WMSMapLayer.layer_icon


class WMSLayerMixinForm:
    """WMS layer mixin form"""

    content_factory = IWMSMapLayer
    content_label = WMSMapLayer.layer_type


@ajax_form_config(name='add-wms-layer.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class WMSLayerAddForm(WMSLayerMixinForm, MapLayerAddForm):
    """WMS layer add form"""


@ajax_form_config(name='properties.html',
                  context=IWMSMapLayer, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class WMSLayerPropertiesEditForm(WMSLayerMixinForm, MapLayerPropertiesEditForm):
    """WMS layer properties edit form"""


#
# Geoportal layers components
#

@viewlet_config(name='add-geoportal-layer.menu',
                context=IMapManager, layer=IAdminLayer, view=IMapManagerLayersTable,
                manager=IContextAddingsViewletManager, weight=30,
                permission=MANAGE_MAPS_PERMISSION)
class GeoportalLayerAddMenu(MapLayerAddMenu):
    """Geoportal layer add menu"""

    label = _("Add Geoportal layer...")
    href = 'add-geoportal-layer.html'
    icon_class = GeoportalMapLayer.layer_icon


class GeoportalLayerMixinForm:
    """Geoportal layer mixin form"""

    content_factory = IGeoportalMapLayer
    content_label = GeoportalMapLayer.layer_type


@ajax_form_config(name='add-geoportal-layer.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class GeoportalLayerAddForm(GeoportalLayerMixinForm, MapLayerAddForm):
    """Geoportal layer add form"""


@ajax_form_config(name='properties.html',
                  context=IGeoportalMapLayer, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class GeoportalLayerPropertiesEditForm(GeoportalLayerMixinForm, MapLayerPropertiesEditForm):
    """Geoportal layer properties edit form"""


#
# ESRI feature layers components
#

@viewlet_config(name='add-esri-feature-layer.menu',
                context=IMapManager, layer=IAdminLayer, view=IMapManagerLayersTable,
                manager=IContextAddingsViewletManager, weight=40,
                permission=MANAGE_MAPS_PERMISSION)
class EsriFeatureLayerAddMenu(MapLayerAddMenu):
    """ESRI feature layer add menu"""

    label = _("Add ESRI feature layer...")
    href = 'add-esri-feature-layer.html'
    icon_class = EsriFeatureMapLayer.layer_icon


class EsriFeatureLayerMixinForm:
    """ESRI feature layer mixin form"""

    content_factory = IEsriFeatureMapLayer
    content_label = EsriFeatureMapLayer.layer_type


@ajax_form_config(name='add-esri-feature-layer.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class EsriFeatureLayerAddForm(EsriFeatureLayerMixinForm, MapLayerAddForm):
    """ESRI feature layer add form"""


@ajax_form_config(name='properties.html',
                  context=IEsriFeatureMapLayer, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class EsriFeatureLayerPropertiesEditForm(EsriFeatureLayerMixinForm, MapLayerPropertiesEditForm):
    """ESRI feature layer properties edit form"""


#
# Google layers components
#

@viewlet_config(name='add-google-layer.menu',
                context=IMapManager, layer=IAdminLayer, view=IMapManagerLayersTable,
                manager=IContextAddingsViewletManager, weight=50,
                permission=MANAGE_MAPS_PERMISSION)
class GoogleLayerAddMenu(MapLayerAddMenu):
    """Google layer add menu"""

    label = _("Add Google layer...")
    href = 'add-google-layer.html'
    icon_class = GoogleMapLayer.layer_icon


class GoogleLayerMixinForm:
    """Google layer mixin form"""

    content_factory = IGoogleMapLayer
    content_label = GoogleMapLayer.layer_type


@ajax_form_config(name='add-google-layer.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class GoogleLayerAddForm(GoogleLayerMixinForm, MapLayerAddForm):
    """Google layer add form"""


@ajax_form_config(name='properties.html',
                  context=IGoogleMapLayer, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class GoogleLayerPropertiesEditForm(GoogleLayerMixinForm, MapLayerPropertiesEditForm):
    """Google layer properties edit form"""
