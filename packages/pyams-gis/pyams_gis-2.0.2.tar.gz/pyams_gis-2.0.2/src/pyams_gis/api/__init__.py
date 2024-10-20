# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

from cornice import Service
from cornice.validators import colander_validator
from pyramid.httpexceptions import HTTPOk
from pyramid.testing import DummyRequest

from pyams_gis.api.schema import GeoAreaTransformRequest, GeoAreaTransformResponse, GeoPointTransformRequest, \
    GeoPointTransformResponse
from pyams_gis.interfaces import REST_AREA_TRANSFORM_ROUTE, REST_POINT_TRANSFORM_ROUTE
from pyams_gis.transform import have_gdal, transform
from pyams_security.interfaces.base import USE_INTERNAL_API_PERMISSION
from pyams_security.rest import check_cors_origin, set_cors_headers
from pyams_utils.rest import rest_responses

__docformat__ = 'restructuredtext'


#
# Point transform service
#

point_transform_service = Service(name=REST_POINT_TRANSFORM_ROUTE,
                                  pyramid_route=REST_POINT_TRANSFORM_ROUTE,
                                  description="PyAMS GIS point transformation service")


@point_transform_service.options(validators=(check_cors_origin, set_cors_headers))
def point_transform_options(request):
    """Point transformation options endpoint"""
    return ''


point_transform_responses = rest_responses.copy()
point_transform_responses[HTTPOk.code] = GeoPointTransformResponse(
    description="Point transformation response")


@point_transform_service.post(schema=GeoPointTransformRequest,
                              validators=(check_cors_origin, colander_validator, set_cors_headers),
                              response_schemas=point_transform_responses,
                              permission=USE_INTERNAL_API_PERMISSION,
                              require_csrf=False)
def transform_point(request):
    """Point transformation request handler"""
    params = request.params if isinstance(request, DummyRequest) else request.validated.get('body')
    result = {
        'status': 'success'
    }
    result.update(transform(**params))
    return result


#
# Area transform service
#

area_transform_service = Service(name=REST_AREA_TRANSFORM_ROUTE,
                                 pyramid_route=REST_AREA_TRANSFORM_ROUTE,
                                 description="PyAMS GIS area transformation service")


@area_transform_service.options(validators=(check_cors_origin, set_cors_headers))
def area_transform_options(request):
    """Area transformation options endpoint"""
    return ''


area_transform_responses = rest_responses.copy()
area_transform_responses[HTTPOk.code] = GeoAreaTransformResponse(
    description="Area transformation response")


@area_transform_service.post(schema=GeoAreaTransformRequest,
                             validators=(check_cors_origin, colander_validator, set_cors_headers),
                             response_schemas=area_transform_responses,
                             permission=USE_INTERNAL_API_PERMISSION,
                             require_csrf=False)
def transform_area(request):
    """Area transformation request handler"""
    params = request.params if isinstance(request, DummyRequest) else request.validated.get('body')
    result = {
        'status': 'success'
    }
    area = params.get('area')
    from_srid = params.get('from_srid')
    to_srid = params.get('to_srid')
    if (not have_gdal) or (from_srid == to_srid):
        result.update({
            'area': {
                'x1': float(area['x1']),
                'y1': float(area['y1']),
                'x2': float(area['x2']),
                'y2': float(area['y2'])
            },
            'srid': to_srid
        })
        return result
    point1 = transform((area['x1'], area['y1']), from_srid, to_srid)
    point2 = transform((area['x2'], area['y2']), from_srid, to_srid)
    result.update({
        'area': {
            'x1': point1['point']['longitude'],
            'y1': point1['point']['latitude'],
            'x2': point2['point']['longitude'],
            'y2': point2['point']['latitude']
        },
        'srid': to_srid
    })
    return result
