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

from pyams_gis.interfaces.utility import IMapManager
from pyams_site.generations import check_required_utilities
from pyams_site.interfaces import ISiteGenerations
from pyams_utils.registry import utility_config

__docformat__ = 'restructuredtext'


REQUIRED_UTILITIES = (
    (IMapManager, '', None, 'Maps manager'),
)


@utility_config(name='PyAMS GIS', provides=ISiteGenerations)
class MapGenerationsChecker:
    """Maps generations checker"""

    order = 90
    generation = 1

    def evolve(self, site, current=None):
        """Check for required utilities"""
        check_required_utilities(site, REQUIRED_UTILITIES)
