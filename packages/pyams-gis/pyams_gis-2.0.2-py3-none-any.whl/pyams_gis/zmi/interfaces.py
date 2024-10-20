# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_gis.zmi.interfaces module

This module defines interfaces used for PyAMS_gis management interface.
"""

from zope.interface import Interface

from pyams_skin.interfaces.view import IModalAddForm
from pyams_table.interfaces import ITable
from pyams_viewlet.interfaces import IViewletManager
from pyams_zmi.interfaces.viewlet import INavigationMenuItem

__docformat__ = 'restructuredtext'


class IMapManagerMenu(INavigationMenuItem):
    """Maps manager menu interface"""


class IMapManagerLayersTable(ITable):
    """Maps manager layers table marker interface"""


class IMapManagerLayersView(Interface):
    """Maps manager layers view interface"""


class IMapHeaderViewletManager(IViewletManager):
    """Map header viewlet manager marker interface"""


class IMapLayerAddForm(IModalAddForm):
    """Map layer add form marker interface"""
