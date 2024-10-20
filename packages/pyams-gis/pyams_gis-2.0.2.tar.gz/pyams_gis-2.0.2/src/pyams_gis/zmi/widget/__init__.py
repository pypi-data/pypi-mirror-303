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

from zope.interface import Interface

from pyams_gis.zmi.interfaces import IMapHeaderViewletManager
from pyams_layer.interfaces import IFormLayer
from pyams_viewlet.manager import WeightOrderedViewletManager, viewletmanager_config


@viewletmanager_config(name='pyams_gis.map.header',
                       layer=IFormLayer, view=Interface,
                       provides=IMapHeaderViewletManager)
class MapHeaderViewletManager(WeightOrderedViewletManager):
    """Map header viewlet manager"""
