# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

from zope.interface import Interface

from pyams_form.ajax import ajax_form_config
from pyams_form.field import Fields
from pyams_gis.interfaces import MANAGE_MAPS_PERMISSION
from pyams_gis.interfaces.utility import IMapManager, IMapManagerInfo
from pyams_gis.zmi.interfaces import IMapManagerMenu
from pyams_layer.interfaces import IPyAMSLayer
from pyams_utils.adapter import adapter_config
from pyams_viewlet.viewlet import viewlet_config
from pyams_zmi.form import AdminEditForm
from pyams_zmi.interfaces import IAdminLayer, IObjectLabel
from pyams_zmi.zmi.viewlet.menu import NavigationMenuItem

__docformat__ = 'restructuredtext'

from pyams_gis import _


@adapter_config(required=(IMapManager, IAdminLayer, Interface),
                provides=IObjectLabel)
def map_manager_label(context, request, view):
    """Maps manager label getter"""
    return request.localizer.translate(_("Maps manager"))


@viewlet_config(name='map-manager-properties.menu',
                context=IMapManager, layer=IAdminLayer,
                manager=IMapManagerMenu, weight=20,
                permission=MANAGE_MAPS_PERMISSION)
class MapManagerPropertiesMenu(NavigationMenuItem):
    """Map manager properties menu"""
    
    label = _("Properties")
    href = '#map-manager-properties.html'
    
    
@ajax_form_config(name='map-manager-properties.html',
                  context=IMapManager, layer=IPyAMSLayer,
                  permission=MANAGE_MAPS_PERMISSION)
class  MapManagerPropertiesEditForm(AdminEditForm):
    """Maps manager properties edit form"""
    
    title = _("Map manager properties")
    legend = _("Management interface")
    
    fields = Fields(IMapManagerInfo)
    