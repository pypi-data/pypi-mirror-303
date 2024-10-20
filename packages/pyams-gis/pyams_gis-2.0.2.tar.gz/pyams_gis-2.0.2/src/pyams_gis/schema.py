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

from zope.interface import implementer
from zope.schema import Object
from zope.schema.interfaces import IObject

from pyams_gis.interfaces import IGeoArea, IGeoPoint, IGeoPointZ

__docformat__ = 'restructuredtext'


class IGeoPointField(IObject):
    """GeoPoint schema field interface"""


@implementer(IGeoPointField)
class GeoPointField(Object):
    """GeoPoint field class"""

    def __init__(self, **kwargs):
        if 'schema' in kwargs:
            del kwargs['schema']
        super(GeoPointField, self).__init__(IGeoPoint, **kwargs)


class IGeoPointZField(IObject):
    """GeoPointZ schema field interface"""


@implementer(IGeoPointZField)
class GeoPointZField(Object):
    """GeoPointZ field class"""

    def __init__(self, **kwargs):
        if 'schema' in kwargs:
            del kwargs['schema']
        super(GeoPointZField, self).__init__(IGeoPointZ, **kwargs)


class IGeoAreaField(IObject):
    """GeoArea schema field interface"""


@implementer(IGeoAreaField)
class GeoAreaField(Object):
    """GeoArea field class"""

    def __init__(self, **kwargs):
        if 'schema' in kwargs:
            del kwargs['schema']
        super(GeoAreaField, self).__init__(IGeoArea, **kwargs)
