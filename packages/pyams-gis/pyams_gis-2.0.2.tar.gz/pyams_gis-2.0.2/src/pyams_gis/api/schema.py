# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

from colander import MappingSchema, Decimal, Integer, SchemaNode, String

__docformat__ = 'restructuredtext'

from pyams_utils.rest import BaseResponseSchema


class Coordinate(MappingSchema):
    """Coordinate field"""
    latitude = SchemaNode(Decimal(),
                          description="Latitude")
    longitude = SchemaNode(Decimal(),
                           description="Longitude")
    
    
class SRID(Integer):
    """Spatial reference system identifier"""
    
    
class GeoPoint(MappingSchema):
    """Geographic point schema"""
    
    
class Area(MappingSchema):
    """Geographic rectangular area schema"""
    x1 = SchemaNode(Decimal(),
                    description="Upper-left point longitude coordinate")
    y1 = SchemaNode(Decimal(),
                    description="Upper-left point latitude coordinate")
    x2 = SchemaNode(Decimal(),
                    description="Lower-right point longitude coordinate")
    y2 = SchemaNode(Decimal(),
                    description="Lower-right point latitude coordinate")


class GeoPointTransformInfo(MappingSchema):
    """Geographic point transformation schema"""
    point = Coordinate(description="Point coordinates")
    from_srid = SchemaNode(SRID(),
                           description="Source SRID")
    to_srid = SchemaNode(SRID(),
                         description="Target SRID")
    
    
class GeoPointTransformRequest(MappingSchema):
    """Geographic point transformation request"""
    body = GeoPointTransformInfo(description="Point transformation request")
    
    
class GeoPointTransformResult(BaseResponseSchema):
    """Geographic point transformation result"""
    point = Coordinate()
    srid = SchemaNode(SRID(),
                      description="Coordinates SRID")
    
    
class GeoPointTransformResponse(MappingSchema):
    """Geographic point transformation response"""
    body = GeoPointTransformResult()
    
    
class GeoAreaTransformInfo(MappingSchema):
    """Geographic area transformation schema"""
    area = Area(description="Area coordinates")
    from_srid = SchemaNode(SRID(),
                           description="Source SRID")
    to_srid = SchemaNode(SRID(),
                         description="Target SRID")


class GeoAreaTransformRequest(MappingSchema):
    """Geographic area transformation request"""
    body = GeoAreaTransformInfo(description="Area transformation request")
    
    
class GeoAreaTransformResult(BaseResponseSchema):
    """Geographic area transformation result"""
    area = Area()
    srid = SchemaNode(SRID(),
                      description="Coordinates SRID")
    
    
class GeoAreaTransformResponse(MappingSchema):
    """Geographic area transformation response"""
    body = GeoAreaTransformResult()
