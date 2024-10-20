=================
PyAMS GIS package
=================

Introduction
------------

This package is composed of a set of utility functions, usable into any Pyramid application.
They are used to handle maps and layers in web applications.

    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()

    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp(hook_zca=True)
    >>> config = setUp(hook_zca=True)
    >>> config.registry.settings['zodbconn.uri'] = 'file://{dir}/Data.fs?blobstorage_dir={dir}/blobs'.format(
    ...     dir=temp_dir)

    >>> import transaction
    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from cornice import includeme as include_cornice
    >>> include_cornice(config)
    >>> from cornice_swagger import includeme as include_swagger
    >>> include_swagger(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_site import includeme as include_site
    >>> include_site(config)
    >>> from pyams_i18n import includeme as include_i18n
    >>> include_i18n(config)
    >>> from pyams_security import includeme as include_security
    >>> include_security(config)
    >>> from pyams_form import includeme as include_form
    >>> include_form(config)
    >>> from pyams_viewlet import includeme as include_viewlet
    >>> include_viewlet(config)
    >>> from pyams_table import includeme as include_table
    >>> include_table(config)
    >>> from pyams_gis import includeme as include_gis
    >>> include_gis(config)

    >>> from pyams_site.generations import upgrade_site
    >>> request = DummyRequest()
    >>> app = upgrade_site(request)
    Upgrading PyAMS timezone to generation 1...
    Upgrading PyAMS I18n to generation 1...
    Upgrading PyAMS security to generation 2...
    Upgrading PyAMS GIS to generation 1...

    >>> from pyams_utils.registry import set_local_registry
    >>> set_local_registry(app)


GIS transformations
-------------------

The first API provided by PyAMS_gis is related to coordinates transformations:

    >>> from pprint import pformat, pprint
    >>> from pyams_gis.transform import transform

Points can be provided in several formats:

    >>> pprint(transform((0.0, 90.0), 4326, 2154))
    {'point': {'latitude': 7342679.450303347, 'longitude': 11185002.041692967},
     'srid': 2154}

    >>> pprint(transform([0.0, 90.0], 4326, 2154))
    {'point': {'latitude': 7342679.450303347, 'longitude': 11185002.041692967},
     'srid': 2154}

    >>> pprint(transform({'longitude': 0.0, 'latitude': 90.0}, 4326, 2154))
    {'point': {'latitude': 7342679.450303347, 'longitude': 11185002.041692967},
     'srid': 2154}

    >>> pprint(transform({'longitude': 0.0, 'latitude': 90.0}, 4326, 4326))
    {'point': {'latitude': 90.0, 'longitude': 0.0},
     'srid': 4326}


GIS transform API
-----------------

This transformation API is available as a REST API:

    >>> from pyams_gis.api import transform_point

    >>> request = DummyRequest(path='/api/gis/rest/transform/point', method='POST',
    ...                        params={'point': {'longitude': 0.0, 'latitude': 90.0}, 'from_srid': 4326, 'to_srid': 2154})
    >>> pprint(transform_point(request))
    {'point': {'latitude': 7342679.450303347, 'longitude': 11185002.041692967},
     'srid': 2154,
     'status': 'success'}

    >>> from pyams_gis.api import transform_area
    >>> request = DummyRequest(path='/api/gis/rest/transform/area', method='POST',
    ...                        params={'area': {'x1': 0.0, 'y1': 90.0, 'x2': 0.1, 'y2': 90.1}, 'from_srid': 4326, 'to_srid': 2154})
    >>> pprint(transform_area(request))
    {'area': {'x1': 11185002.041692967,
              'x2': 11178532.325169353,
              'y1': 7342679.450303347,
              'y2': 7362624.658507054},
     'srid': 2154,
     'status': 'success'}


GIS schemas fields
------------------

PyAMS_gis provides several custom schema fields which can to used to handle points and rectangular areas:

    >>> from zope.interface import Interface, implementer
    >>> from zope.schema.fieldproperty import FieldProperty
    >>> from pyams_gis.schema import GeoPointField, GeoAreaField
    >>> from pyams_gis.point import GeoPoint
    >>> from pyams_gis.area import GeoArea

    >>> class ITestClass(Interface):
    ...     point = GeoPointField(title="Point")
    ...     area = GeoAreaField(title="Area")

    >>> @implementer(ITestClass)
    ... class TestClass:
    ...     point = FieldProperty(ITestClass['point'])
    ...     area = FieldProperty(ITestClass['area'])

    >>> test_instance = TestClass()

    >>> point = GeoPoint(longitude=0.0, latitude=90.0)
    >>> test_instance.point = point
    >>> bool(point)
    True
    >>> pprint(point.get_coordinates(projection=2154))
    (11185002.041692967, 7342679.450303347)
    >>> pprint(point.wgs_coordinates)
    (Decimal('0'), Decimal('90'))
    >>> pprint(point.to_json())
    {'crs': 4326.0, 'lat': 90.0, 'lon': 0.0}

    >>> area = GeoArea(x1=0.0, y1=90.0, x2=0.1, y2=90.1)
    >>> test_instance.area = area
    >>> bool(area)
    True
    >>> pprint(area.get_coordinates(projection=2154))
    ((11185002.041692967, 7342679.450303347),
     (11178532.325169353, 7362624.658507054))
    >>> pprint(area.wgs_coordinates)
    ((Decimal('0'), Decimal('90')),
     (Decimal('0.1000000000000000055511151231257827021181583404541015625'),
      Decimal('90.099999999999994315658113919198513031005859375')))
    >>> pprint(area.to_json())
    {'crs': 4326, 'x1': 0.0, 'x2': 0.1, 'y1': 90.0, 'y2': 90.1}


GIS maps configuration
----------------------

PyAMS_gis allows you to define a default map configuration:

    >>> from zope.schema.vocabulary import getVocabularyRegistry
    >>> from pyams_gis.interfaces.layer import PYAMS_GIS_LAYERS_VOCABULARY
    >>> from pyams_gis.layer import MapLayersVocabulary
    >>> from pyams_gis.configuration import MapConfiguration

    >>> getVocabularyRegistry().register(PYAMS_GIS_LAYERS_VOCABULARY, MapLayersVocabulary)
    >>> getVocabularyRegistry().get(app, PYAMS_GIS_LAYERS_VOCABULARY)
    <pyams_gis.layer.MapLayersVocabulary object at 0x...>

    >>> configuration = MapConfiguration()
    >>> pprint(configuration.get_configuration())
    {'adjust': 'auto',
     'attributionControl': True,
     'center': {'lat': 45, 'lon': 5.0},
     'crs': 'L.CRS.EPSG3857',
     'fullscreenControl': False,
     'keyboard': True,
     'layerControl': False,
     'scrollWheelZoom': False,
     'zoom': 11,
     'zoomControl': True}

Let's add a layer to this default configuration:

    >>> from pyams_utils.registry import get_utility
    >>> from pyams_gis.interfaces.utility import IMapManager
    >>> from pyams_gis.layer import WMSMapLayer

    >>> layer = WMSMapLayer()
    >>> layer.name = 'wms'
    >>> layer.title = {'en': 'WMS'}

    >>> manager = get_utility(IMapManager)
    >>> manager[layer.name] = layer

    >>> configuration.layers = ['wms']
    >>> pprint(configuration.get_configuration())
    {'adjust': 'auto',
     'attributionControl': True,
     'center': {'lat': 45, 'lon': 5.0},
     'crs': 'L.CRS.EPSG3857',
     'fullscreenControl': False,
     'keyboard': True,
     'layerControl': False,
     'layers': [{'factory': 'MyAMS.gis.factory.WMS',
                 'format': 'image/png',
                 'maxZoom': 18,
                 'name': 'wms',
                 'title': 'WMS',
                 'url': 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                 'version': '1.1.1'}],
     'scrollWheelZoom': False,
     'zoom': 11,
     'zoomControl': True}


GIS schema fields widgets
-------------------------

    >>> from zope.interface import alsoProvides
    >>> from zope.i18n.locales import Locale, LocaleIdentity
    >>> from pyams_layer.interfaces import IPyAMSLayer
    >>> from pyams_form.field import Fields
    >>> from pyams_form.form import EditForm

    >>> class TestEditForm(EditForm):
    ...     fields = Fields(ITestClass)

    >>> request = DummyRequest(locale=Locale(LocaleIdentity('en', None, None, None)))
    >>> alsoProvides(request, IPyAMSLayer)

    >>> form = TestEditForm(test_instance, request)
    >>> form.update()

    >>> point_widget = form.widgets['point']
    >>> print(point_widget.render())
    <div class="object-field"
         data-ams-modules='{"gis": "/--static--/pyams_gis/:version:.../js/pyams_gis.js"}'>
        <div class="position-absolute t-m3 t-md-3 r-3 r-md-5">
            <div class="d-flex flex-row flex-md-column mb-2">
                <div class="btn btn-light my-1"
                     data-toggle="modal"
                     href="#modal_dialog_form_widgets_point">
                    <i class="fa fa-fw fa-lg fa-map-marker hint opaque align-baseline"
                       data-placement="top" data-offset="0,10"
                       title="Select location from map"></i>
                </div>
                <div class="btn btn-light my-1"
                     data-ams-click-handler="MyAMS.gis.position.clear">
                    <i class="fa fa-fw fa-lg fa-trash hint opaque align-baseline"
                       data-placement="bottom" data-offset="0,10"
                       title="Clear selected position"></i>
                </div>
            </div>
            <div id="modal_dialog_form_widgets_point"
                 class="modal fade"
                 data-ams-events-handlers='{
                    "show.bs.modal": "MyAMS.gis.position.init",
                    "shown.bs.modal": "MyAMS.gis.modalShown"
                 }'>
                <div class="modal-dialog modal-max">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                                <i class="fa fa-fw fa-times-circle"></i>
                            </button>
                            <h3 class="modal-title">
                                <span class="title">Select marker position</span>
                            </h3>
                        </div>
                        <div class="ams-form">
                            <div class="modal-body">
                                <div class="map map-location"
                                     id="map_location_form_widgets_point"
                                     data-map-leaflet-fieldname="form.widgets.point"></div>
                                </div>
                                <footer>
                                    <button type="button" class="btn btn-primary close-widget"
                                            data-dismiss="modal"
                                            data-ams-click-event="marker.closed.position"
                                            data-ams-click-event-options='{"fieldname": "form.widgets.point"}'>
                                        OK
                                    </button>
                                </footer>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-group widget-group row">
                <label for="form-widgets-point-widgets-longitude"
                       class="col-form-label text-md-right control-label col-md-3 ">
                    Longitude
                </label>
            <div class="col-md-4">
                <div class="form-widget "><input type="text"
                   id="form-widgets-point-widgets-longitude"
                   name="form.widgets.point.widgets.longitude"
                   class="text-widget dotteddecimalfield-field"
                   readonly="readonly"
                   value="0" /></div>
            </div>
        </div>
        <div class="form-group widget-group row">
            <label for="form-widgets-point-widgets-latitude"
                   class="col-form-label text-md-right control-label col-md-3 ">
                Latitude
            </label>
            <div class="col-md-4">
                <div class="form-widget "><input type="text"
                   id="form-widgets-point-widgets-latitude"
                   name="form.widgets.point.widgets.latitude"
                   class="text-widget dotteddecimalfield-field"
                   readonly="readonly"
                   value="90" /></div>
            </div>
        </div>
        <div class="form-group widget-group row">
            <label for="form-widgets-point-widgets-projection"
                   class="col-form-label text-md-right control-label col-md-3 required">
                Projection system
            </label>
            <div class="col-md-4">
                <div class="form-widget "><select id="form-widgets-point-widgets-projection"
                        name="form.widgets.point.widgets.projection"
                        class="select-widget required choice-field"
                        size="1">
                        <option id="form-widgets-point-widgets-projection-0"
                                value="4326"
                                selected="selected">WGS84 (GPS)</option>
                        <option id="form-widgets-point-widgets-projection-1"
                                value="3857">WGS84 Web Mercator</option>
                        <option id="form-widgets-point-widgets-projection-2"
                                value="2154">Lambert 93 (Metropolitan France)</option>
                        <option id="form-widgets-point-widgets-projection-3"
                                value="27572">Extended Lambert II (Metropolitan France)</option>
                        <option id="form-widgets-point-widgets-projection-4"
                                value="4559">UTM Zone 20N (Martinique, Guadeloupe)</option>
                        <option id="form-widgets-point-widgets-projection-5"
                                value="2972">UTM Zone 22N (Guyane)</option>
                        <option id="form-widgets-point-widgets-projection-6"
                                value="4471">UTM Zone 38S (Mayotte)</option>
                        <option id="form-widgets-point-widgets-projection-7"
                                value="2975">UTM Zone 40S (La Réunion)</option>
                    </select>
                    <input name="form.widgets.point.widgets.projection-empty-marker" type="hidden" value="1" /></div>
            </div>
        </div>
        <input name="form.widgets.point-empty-marker" type="hidden" value="1" />
    </div>

    >>> area_widget = form.widgets['area']
    >>> print(area_widget.render())
    <div class="object-field"
         data-ams-modules='{"gis": "/--static--/pyams_gis/:version:.../js/pyams_gis.js"}'>
        <div class="position-absolute t-m3 t-md-3 r-3 r-md-5">
            <div class="d-flex flex-row flex-md-column mb-2">
                <div class="btn btn-light my-1"
                     data-toggle="modal"
                     href="#modal_dialog_form_widgets_area">
                    <i class="fa fa-fw fa-lg fa-map-marker hint opaque align-baseline"
                       data-placement="top" data-offset="0,10"
                       title="Select area from map"></i>
                </div>
                <div class="btn btn-light my-1"
                     data-ams-click-handler="MyAMS.gis.area.clear">
                    <i class="fa fa-fw fa-lg fa-trash hint opaque align-baseline"
                       data-placement="bottom" data-offset="0,10"
                       title="Clear selected position"></i>
                </div>
            </div>
            <div id="modal_dialog_form_widgets_area"
                 class="modal fade"
                 data-ams-events-handlers='{
                    "show.bs.modal": "MyAMS.gis.area.init",
                    "shown.bs.modal": "MyAMS.gis.area.setBounds"
                 }'>
                <div class="modal-dialog modal-max">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                                <i class="fa fa-fw fa-times-circle"></i>
                            </button>
                            <h3 class="modal-title">
                                <span class="title">Select map area</span>
                            </h3>
                        </div>
                        <div class="ams-form">
                            <div class="modal-body">
                                <div class="map map-location"
                                     id="map_area_form_widgets_area"
                                     data-map-leaflet-fieldname="form.widgets.area"></div>
                                </div>
                                <footer>
                                    <button type="button" class="btn btn-primary close-widget"
                                            data-dismiss="modal"
                                            data-ams-click-event="marker.closed.position"
                                            data-ams-click-event-options='{"fieldname": "form.widgets.area"}'>
                                        OK
                                    </button>
                                </footer>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-group widget-group row">
                <label for="form-widgets-area-widgets-x1"
                       class="col-form-label text-md-right control-label col-md-3 ">
                    West limit
                </label>
            <div class="col-md-4">
                <div class="form-widget "><input type="text"
                   id="form-widgets-area-widgets-x1"
                   name="form.widgets.area.widgets.x1"
                   class="text-widget dotteddecimalfield-field"
                   readonly="readonly"
                   value="0" /></div>
            </div>
        </div>
        <div class="form-group widget-group row">
            <label for="form-widgets-area-widgets-y1"
                   class="col-form-label text-md-right control-label col-md-3 ">
                South limit
            </label>
            <div class="col-md-4">
                <div class="form-widget "><input type="text"
                   id="form-widgets-area-widgets-y1"
                   name="form.widgets.area.widgets.y1"
                   class="text-widget dotteddecimalfield-field"
                   readonly="readonly"
                   value="90" /></div>
                </div>
            </div>
            <div class="form-group widget-group row">
                <label for="form-widgets-area-widgets-x2"
                       class="col-form-label text-md-right control-label col-md-3 ">
                    East limit
                </label>
                <div class="col-md-4">
                    <div class="form-widget "><input type="text"
                       id="form-widgets-area-widgets-x2"
                       name="form.widgets.area.widgets.x2"
                       class="text-widget dotteddecimalfield-field"
                       readonly="readonly"
                       value="0.100" /></div>
            </div>
        </div>
        <div class="form-group widget-group row">
            <label for="form-widgets-area-widgets-y2"
                   class="col-form-label text-md-right control-label col-md-3 ">
                North limit
            </label>
            <div class="col-md-4">
                <div class="form-widget "><input type="text"
                   id="form-widgets-area-widgets-y2"
                   name="form.widgets.area.widgets.y2"
                   class="text-widget dotteddecimalfield-field"
                   readonly="readonly"
                   value="90.100" /></div>
            </div>
        </div>
        <div class="form-group widget-group row">
            <label for="form-widgets-area-widgets-projection"
                   class="col-form-label text-md-right control-label col-md-3 required">
                Projection system
            </label>
            <div class="col-md-4">
                <div class="form-widget "><select id="form-widgets-area-widgets-projection"
                    name="form.widgets.area.widgets.projection"
                    class="select-widget required choice-field"
                    size="1">
                        <option id="form-widgets-area-widgets-projection-0"
                                value="4326"
                                selected="selected">WGS84 (GPS)</option>
                        <option id="form-widgets-area-widgets-projection-1"
                                value="3857">WGS84 Web Mercator</option>
                        <option id="form-widgets-area-widgets-projection-2"
                                value="2154">Lambert 93 (Metropolitan France)</option>
                        <option id="form-widgets-area-widgets-projection-3"
                                value="27572">Extended Lambert II (Metropolitan France)</option>
                        <option id="form-widgets-area-widgets-projection-4"
                                value="4559">UTM Zone 20N (Martinique, Guadeloupe)</option>
                        <option id="form-widgets-area-widgets-projection-5"
                                value="2972">UTM Zone 22N (Guyane)</option>
                        <option id="form-widgets-area-widgets-projection-6"
                                value="4471">UTM Zone 38S (Mayotte)</option>
                        <option id="form-widgets-area-widgets-projection-7"
                                value="2975">UTM Zone 40S (La Réunion)</option>
                    </select>
                    <input name="form.widgets.area.widgets.projection-empty-marker" type="hidden" value="1" /></div>
            </div>
        </div>
        <input name="form.widgets.area-empty-marker" type="hidden" value="1" />
    </div>


Tests cleanup:

    >>> tearDown()
