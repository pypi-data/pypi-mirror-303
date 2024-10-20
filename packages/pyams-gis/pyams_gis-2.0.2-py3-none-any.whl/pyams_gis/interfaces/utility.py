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

"""PyAMS_gis.interfaces.utility module

This module defines base maps manager interfaces.
"""

from zope.annotation.interfaces import IAttributeAnnotatable
from zope.container.constraints import contains
from zope.container.interfaces import IContainer
from zope.interface import Interface
from zope.schema import Bool

from pyams_gis.interfaces.layer import IMapLayer

__docformat__ = 'restructuredtext'

from pyams_gis import _


class IMapManagerInfo(Interface):
    """Map manager information interface"""

    show_home_menu = Bool(title=_("Access menu from home"),
                          description=_("If 'yes', a menu will be displayed to get access to "
                                        "maps manager from site admin home page"),
                          required=True,
                          default=False)
    
    
class IMapManager(IMapManagerInfo, IContainer, IAttributeAnnotatable):
    """Map manager interface"""

    contains(IMapLayer)
