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

from zope.container.folder import Folder
from zope.interface import implementer
from zope.schema.fieldproperty import FieldProperty
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from pyams_gis.interfaces.configuration import IMapConfigurationTarget
from pyams_gis.interfaces.layer import PYAMS_GIS_LAYERS_VOCABULARY
from pyams_gis.interfaces.utility import IMapManager
from pyams_i18n.interfaces import II18n
from pyams_utils.factory import factory_config
from pyams_utils.registry import get_utility
from pyams_utils.request import check_request
from pyams_utils.vocabulary import vocabulary_config

__docformat__ = 'restructuredtext'


@factory_config(IMapManager)
@implementer(IMapConfigurationTarget)
class MapManager(Folder):
    """Map manager utility"""
    
    show_home_menu = FieldProperty(IMapManager['show_home_menu'])


@vocabulary_config(name=PYAMS_GIS_LAYERS_VOCABULARY)
class MapLayersVocabulary(SimpleVocabulary):
    """Map manager layers vocabulary"""

    def __init__(self, context):
        request = check_request()
        manager = get_utility(IMapManager)
        super().__init__([
            SimpleTerm(layer.__name__,
                       title=II18n(layer).query_attribute('title', request=request))
            for layer in manager.values()
        ])
