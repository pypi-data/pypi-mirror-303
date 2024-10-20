#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS GIS.include module

This module is used for Pyramid integration
"""

import re

from pyams_gis.interfaces import MANAGE_MAPS_PERMISSION, REST_AREA_TRANSFORM_PATH, REST_AREA_TRANSFORM_ROUTE, \
    REST_AREA_TRANSFORM_ROUTE_SETTING, REST_POINT_TRANSFORM_PATH, REST_POINT_TRANSFORM_ROUTE, \
    REST_POINT_TRANSFORM_ROUTE_SETTING
from pyams_security.interfaces.names import SYSTEM_ADMIN_ROLE

__docformat__ = 'restructuredtext'

from pyams_gis import _


def include_package(config):
    """Pyramid package include"""

    # add translations
    config.add_translation_dirs('pyams_gis:locales')

    # register permissions
    config.register_permission({
        'id': MANAGE_MAPS_PERMISSION,
        'title': _("Manage GIS maps")
    })

    # upgrade system manager role
    config.upgrade_role(SYSTEM_ADMIN_ROLE,
                        permissions={MANAGE_MAPS_PERMISSION})

    # register REST transform API routes
    config.add_route(REST_POINT_TRANSFORM_ROUTE,
                     config.registry.settings.get(REST_POINT_TRANSFORM_ROUTE_SETTING,
                                                  REST_POINT_TRANSFORM_PATH))
    config.add_route(REST_AREA_TRANSFORM_ROUTE,
                     config.registry.settings.get(REST_AREA_TRANSFORM_ROUTE_SETTING,
                                                  REST_AREA_TRANSFORM_PATH))

    try:
        import pyams_zmi  # pylint: disable=import-outside-toplevel,unused-import
    except ImportError:
        config.scan(ignore=[re.compile(r'pyams_gis\..*\.zmi\.?.*').search])
    else:
        config.scan()
