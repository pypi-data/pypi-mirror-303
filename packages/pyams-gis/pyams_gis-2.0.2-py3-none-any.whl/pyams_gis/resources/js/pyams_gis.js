/* global MyAMS */

'use strict';


if (window.$ === undefined) {
	window.$ = MyAMS.$;
}


const GIS = {

	L: null,

	API_ENDPOINT: '/api/gis/rest',
	WGS_SRID: 4326,

	_layersControlAddItem: function(obj) {
		const
			group = $('<div></div>').addClass('inline-group'),
			label = $('<label></label>').addClass(obj.overlay ? "checkbox" : "radio"),
			span = $('<i></i>'),
			checked = this._map.hasLayer(obj.layer);
		let input, name;
		if (obj.overlay) {
			input = document.createElement('input');
			input.type = 'checkbox';
			input.className = 'leaflet-control-layers-selector';
			input.defaultChecked = checked;
		} else {
			input = this._createRadioElement('leaflet-base-layers', checked);
		}
		input.layerId = L.stamp(obj.layer);
		$(input).addClass(obj.overlay ? "checkbox" : "radio");
		GIS.L.DomEvent.on(input, 'click', this._onInputClick, this);
		name = $('<span></span>').text(` ${obj.name}`);
		label.append(input);
		label.append(span);
		label.append(name);
		group.append(label);
		const container = obj.overlay ? this._overlaysList : this._baseLayersList;
		$(container).append(group);
		return group;
	},

	/**
	 * Main Leaflet map initialization
	 */
	init: (context, options, callback) => {
		return new Promise((resolve, reject) => {
			MyAMS.ajax.check([
				window.L
			], [
				`/--static--/pyams_gis/js/leaflet-1.9.4${MyAMS.env.extext}.js`
			]).then((first_load) => {
				const required = [];
				if (first_load) {
					GIS.L = window.L;
					GIS.L.Control.Layers.prototype._addItem = GIS._layersControlAddItem;
					required.push(MyAMS.core.getScript(
						`/--static--/pyams_gis/js/leaflet-gesture-handling${MyAMS.env.extext}.js`));
					required.push(MyAMS.core.getScript(
						`/--static--/pyams_gis/js/Control.FullScreen${MyAMS.env.extext}.js`));
					required.push(MyAMS.core.getCSS(`/--static--/pyams_gis/css/leaflet-1.9.4${MyAMS.env.extext}.css`,
						'leaflet'));
					required.push(MyAMS.core.getCSS(`/--static--/pyams_gis/css/leaflet-gesture-handling${MyAMS.env.extext}.css`,
						'leaflet-gesture-handling'));
					required.push(MyAMS.core.getCSS(`/--static--/pyams_gis/css/Control.FullScreen${MyAMS.env.extext}.css`,
						'leaflet-fullscreen'));
				}
				$.when.apply($, required).then(() => {

					const createMap = (map, config) => {
						return new Promise((resolveMap, rejectMap) => {
							const data = map.data();
							let settings = {
								preferCanvas: data.mapLeafletPreferCanvas || false,
								attributionControl: data.mapLeafletAttributionControl === undefined ?
									config.attributionControl :
									data.mapLeafletAttributionControl,
								zoomControl: data.mapLeafletZoomControl === undefined ?
									config.zoomControl :
									data.mapLeafletZoomControl,
								fullscreenControl: data.mapLeafletFullscreen === undefined ?
									config.fullscreenControl && {
										pseudoFullscreen: true
									} || null :
									data.mapLeafletFullscreen,
								crs: data.mapLeafletCrs || MyAMS.core.getObject(config.crs) || GIS.L.CRS.EPSG3857,
								center: data.mapLeafletCenter || config.center,
								zoom: data.mapLeafletZoom || config.zoom,
								gestureHandling: data.mapLeafletWheelZoom === undefined ?
									!config.scrollWheelZoom :
									data.mapLeafletWheelZoom,
								keyboard: data.mapLeafletKeyboard === undefined ?
									config.keyboard && !L.Browser.mobile :
									data.amsLeafletKeyboard
							};
							settings = $.extend({}, settings, options);
							map.trigger('map.init', [map, settings, config]);
							const
								leafmap = L.map(map.attr('id'), settings),
								layersConfig = [],
								layersControl = {};
							if (config.layers) {
								for (let idx = 0; idx < config.layers.length; idx++) {
									const layerConfig = config.layers[idx];
									map.trigger('map.layer.init', [map, layerConfig]);
									layersConfig.push(GIS.getLayer(map, leafmap, layerConfig));
								}
							} else {
								layersConfig.push(L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
									name: 'osm',
									title: 'OpenStreetMap',
									maxZoom: 19,
									attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
								}));
							}
							$.when.apply($, layersConfig).then((...layers) => {
								for (let idx = 0; idx < layers.length; idx++) {
									layers[idx].addTo(leafmap);
									if (config.layers) {
										layersControl[config.layers[idx].title] = layers[idx];
									}
								}
								if (config.zoomControl && (data.mapLeafletHideZoomControl !== true)) {
									L.control.scale().addTo(leafmap);
								}
								if (config.layerControl) {
									L.control.layers({}, layersControl).addTo(leafmap);
								}
								if (config.center) {
									leafmap.setView(new L.LatLng(config.center.lat, config.center.lon),
										config.zoom || 13);
								} else if (config.bounds) {
									leafmap.fitBounds(config.bounds);
								}
								map.data('leafmap', leafmap);
								map.data('leafmap.config', config);
								map.data('leafmap.layers', layers.reduce((res, layer) => ({
									...res,
									[layer.options.name]: layer
								}), {}));
								map.trigger('map.finishing', [map, leafmap, config]);
								if (callback) {
									callback(leafmap, config);
								}
								map.trigger('map.finished', [map, leafmap, config]);
								resolveMap(leafmap);
							});
						});
					}

					const maps = $.map(context, (elt) => {
						return new Promise((resolveConfig, rejectConfig) => {
							const
								map = $(elt),
								data = map.data(),
								config = data.mapConfiguration;
							if (config) {
								createMap(map, config).then((leafmap) => {
									resolveConfig({
										'leafmap': leafmap,
										'config': config
									});
								});
							} else {
								MyAMS.ajax.post(data.mapConfigurationUrl || 'get-map-configuration.json', {}).then((config) => {
									createMap(map, config).then((leafmap) => {
										resolveConfig({
											'leafmap': leafmap,
											'config': config
										});
									});
								});
							}
						});
					});
					$.when.apply($, maps).then((result) => {
						resolve(result);
					});
				});
			});
		});
	},

	/**
	 * Invalidate map size after modal shown event
	 */
	modalShown: (event) => {
		const
			map = $('.map', event.currentTarget),
			leafmap = map.data('leafmap');
		if (leafmap) {
			leafmap.invalidateSize();
		}
	},

	/**
	 * Create new layer by calling matching factory
	 */
	getLayer: (map, leafmap, layer) => {
		return new Promise((resolve, reject) => {
			const factory = MyAMS.core.getObject(layer.factory);
			if (factory !== undefined) {
				delete layer.factory;
				const deferred = [];
				if (layer.dependsOn) {
					for (const name in layer.dependsOn) {
						if (!layer.dependsOn.hasOwnProperty(name)) {
							continue;
						}
						if (MyAMS.core.getObject(name) === undefined) {
							deferred.push(MyAMS.core.getScript(layer.dependsOn[name]));
						}
					}
					delete layer.dependsOn;
				}
				$.when.apply($, deferred).then(() => {
					resolve(factory(map, leafmap, layer));
				});
			}
		});
	},

	/**
	 * Map layers factories
	 */
	factory: {

		GeoJSON: (map, leafmap, layer) => {
			const url = layer.url;
			delete layer.url;
			const result = L.geoJSON(null, layer);
			map.on('map.finished', (evt, map, leafmap, config) => {
				$.get(url, (data) => {
					result.addData(data.geometry, {
						style: layer.style
					});
					if (config.fitLayer === layer.name) {
						leafmap.fitBounds(result.getBounds());
					}
				});
			});
			return result;
		},

		TileLayer: (map, leafmap, layer) => {
			const url = layer.url;
			delete layer.url;
			return L.tileLayer(url, layer);
		},

		WMS: (map, leafmap, layer) => {
			const url = layer.url;
			delete layer.url;
			return L.tileLayer.wms(url, layer);
		},

		Geoportal: {
			WMS: (map, leafmap, layer) => {
				MyAMS.core.getCSS(`/--static--/pyams_gis/css/GpPluginLeaflet${MyAMS.env.extext}.css`, 'geoportal');
				return L.geoportalLayer.WMS(layer);
			}
		},

		ESRI: {
			Feature: (map, leafmap, layer) => {
				return L.esri.featureLayer(layer);
			}
		},

		Google: (map, leafmap, layer) => {
			const apiKey = layer.apiKey;
			delete layer.apiKey;
			if (MyAMS.core.getObject('window.google.maps') === undefined) {
				const script = MyAMS.core.getScript(`https://maps.googleapis.com/maps/api/js?key=${apiKey}`);
				$.when.apply($, [script]);
			}
			return L.gridLayer.googleMutant(layer);
		}
	},

	/**
	 * PyAMS_gis REST API caller
	 */
	call: (method, params) => {
		return new Promise((resolve, reject) => {
			MyAMS.require('ajax').then(() => {
				MyAMS.ajax.post(`${window.location.origin}${GIS.API_ENDPOINT}/${method}`, params, {
					contentType: 'application/json; charset=utf-8'
				}).then(resolve, reject);
			});
		});
	},

	/**
	 * Init markers layer
	 */
	markers: {

		init: (maps, callback) => {

			return new Promise((resolve, reject) => {

				MyAMS.ajax.check([
					L.MarkerClusterGroup
				], [
					`/--static--/pyams_gis/js/leaflet.markercluster${MyAMS.env.extext}.js`
				]).then((firstLoad) => {

					const deferred = [];
					if (firstLoad) {
						deferred.push(MyAMS.core.getCSS(`/--static--/pyams_gis/css/MarkerCluster${MyAMS.env.extext}.css`,
							'leaflet-markercluster'));
					}

					$.when.apply($, deferred).then(() => {
						maps.each((idx, elt) => {

							const
								map = $(elt),
								data = map.data(),
								leafmap = map.data('leafmap'),
								config = map.data('leafmap.config'),
								markers = data.mapMarkers;

							let markerIcon,
								activeIcon;

							// show tooltip
							function hoverMarker(evt) {
								this.setIcon(activeIcon);
								this.openPopup();
								const marker = $(`[id="marker-${this.options.markerId}"]`);
								if (marker.exists()) {
									marker.addClass(marker.data('ams-active-class') || 'active');
									if (evt.scroll !== false) {
										MyAMS.ajax.check(
											$.scrollTo,
											`${MyAMS.baseURL}ext/jquery-scrollto-2.1.2${MyAMS.env.extext}.js`,
											() => {
												marker.parents('.markers-target').scrollTo(marker);
											}
										);
									}
								}
							}

							// hide tooltip
							function leaveMarker(evt) {
								this.closePopup();
								this.setIcon(markerIcon);
								const marker = $(`[id="marker-${this.options.markerId}"]`);
								if (marker.exists()) {
									marker.removeClass(marker.data('ams-active-class') || 'active');
								}
							}

							// click marker
							function clickMarker(e) {
								window.location.href = this.options.clickURL;
							}

							if (markers) {
								// create custom icon
								markerIcon = L.icon({
									iconUrl: markers.icon.url,
									iconSize: markers.icon.size,
									iconAnchor: markers.icon.anchor
								});
								const activeIconSize = [
									markers.icon.size[0] * 1.25,
									markers.icon.size[1] * 1.25
								];
								activeIcon = L.icon({
									iconUrl: markers.icon.url,
									iconSize: activeIconSize,
									iconAnchor: [
										activeIconSize[0] / 2,
										activeIconSize[1] - 1
									]
								});
								// customize cluster icon
								let markersClusterCustom;
								if (data.mapMarkersClusters === false) {
									markersClusterCustom = L.featureGroup();
								} else {
									markersClusterCustom = L.markerClusterGroup({
										iconCreateFunction: (cluster) => {
											return L.divIcon({
												html: cluster.getChildCount(),
												className: markers.clusterClass || 'map-cluster',
												iconSize: null
											});
										}
									});
								}

								// object to save markers
								const icons = {};

								// create markers
								for (let idx = 0; idx < markers.markers.length; idx++) {
									const
										markerConfig = markers.markers[idx],
										latLng = new L.LatLng(markerConfig.point.y, markerConfig.point.x),
										marker = new L.Marker(latLng, {
											icon: markerIcon,
											clickURL: markerConfig.href,
											markerId: markerConfig.id,
											alt: markerConfig.id
										}),
										popup = new L.popup({
											offset: new L.Point(0, -markers.icon.size[1]),
											closeButton: false,
											autoPan: true
										});
									marker.addEventListener('mouseover', hoverMarker);
									marker.addEventListener('mouseout', leaveMarker);
									if (markerConfig.href) {
										marker.addEventListener('click', clickMarker);
									}
									icons[markerConfig.id] = marker;
									// bind tooltip with title content
									let label;
									if (markerConfig.img) {
										label = '<div>' +
											`<div class="marker__label p-2">${markerConfig.label}</div>` +
											`  <div class="text-center">` +
											`    <img src="${markerConfig.img.src}" width="${markerConfig.img.w}" height="${markerConfig.img.h}" alt="" />` +
											`  </div>` +
											`</div>`;
									} else {
										label = markerConfig.label;
									}
									if (label) {
										let className = markers.tooltipClass || 'map-tooltip';
										if (markerConfig.img) {
											className += ' p-0';
										}
										marker.bindPopup(label, {
											direction: 'top',
											offset: [0, -markerIcon.options.iconSize[1]],
											opacity: 1,
											className: className,
											closeButton: false,
											autoPan: true
										});
										marker.addEventListener('mouseover', hoverMarker);
										marker.addEventListener('mouseout', leaveMarker);
									}
									markersClusterCustom.addLayer(marker);
								}
								leafmap.addLayer(markersClusterCustom);
								map.data('markers', icons);
								if (config.adjust === 'auto') {
									leafmap.fitBounds(markersClusterCustom.getBounds());
									if (markers.markers.length === 1) {
										leafmap.setZoom(config.zoom);
									}
								}
							}
						});
					});
				});
			});
		}
	},

	/**
	 * Single position marker management
	 */
	position: {

		init: (evt)=> {
			/* Position marker initialization */
			const map = $('.map', $(evt.currentTarget));
			if (map.data('leafmap') === undefined) {
				map.css('height', $(window).height() - 250);
				GIS.init(map, {}).then(({leafmap, config}) => {
					const
						data = map.data(),
						icon = L.icon({
							iconUrl: '/--static--/pyams_gis/img/marker-icon.png',
							iconSize: [25, 41],
							iconAnchor: [12, 39]
						}),
						fieldname = data.mapLeafletFieldname,
						longitude = $(`input[name="${fieldname}.widgets.longitude"]`),
						latitude = $(`input[name="${fieldname}.widgets.latitude"]`),
						marker = L.marker();
					marker.setIcon(icon);
					if (longitude.val() && latitude.val()) {
						const
							projection = $(`select[name="${fieldname}.widgets.projection"]`),
							params = {
								point: {
									longitude: parseFloat(longitude.val()),
									latitude: parseFloat(latitude.val())
								},
								from_srid: projection.val() || GIS.WGS_SRID,
								to_srid: GIS.WGS_SRID
							};
						GIS.call('transform/point', params).then((result) => {
							if (result.status === 'success') {
								const point = result.point;
								marker.setLatLng({
									lon: point.longitude,
									lat: point.latitude
								});
								marker.addTo(leafmap);
								leafmap.setView(marker.getLatLng(), config.zoom || 13);
							}
						});
					} else {
						const bounds = config.bounds;
						if (bounds) {
							marker.setLatLng([
								(bounds[0].lat + bounds[1].lat) / 2,
								(bounds[0].lon + bounds[1].lon) / 2
							]);
						} else {
							marker.setLatLng([-90, 0]);
						}
						marker.addTo(leafmap);
						leafmap.setView(marker.getLatLng(), config.zoom || 8);
					}
					map.data('marker', marker);
					leafmap.on('click', GIS.position.onClick);
				});
			}
		},

		onClick: (event) => {
			const
				map = event.target.getContainer(),
				data = $(map).data(),
				marker = data.marker,
				latlng = event.latlng;
			marker.setLatLng(latlng);
			const
				fieldname = data.mapLeafletFieldname,
				projection = $(`select[name="${fieldname}.widgets.projection"]`),
				params = {
					point: {
						longitude: latlng.lng,
						latitude: latlng.lat
					},
					from_srid: GIS.WGS_SRID,
					to_srid: projection.val()
				};
			GIS.call('transform/point', params).then((result) => {
				if (result.status === 'success') {
					const point = result.point;
					$(`input[name="${fieldname}.widgets.longitude"]`).val(point.longitude);
					$(`input[name="${fieldname}.widgets.latitude"]`).val(point.latitude);
					$(map).trigger('marker.changed', [map, point]);
				}
			});
		},

		/**
		 * Store previous value before projection change
		 */
		beforeProjectionChange: (event) => {
			const select = $(event.currentTarget);
			select.data('ams-old-value', select.val());
		},

		/**
		 * Refresh coordinates on projection change
		 */
		changedProjection: (event)=> {
			const
				select = $(event.currentTarget),
				map = $('.map', select.parents('fieldset:first')),
				fieldname = map.data('map-leaflet-fieldname'),
				longitude = $(`input[name="${fieldname}.widgets.longitude"]`),
				latitude = $(`input[name="${fieldname}.widgets.latitude"]`),
				oldValue = select.data('ams-old-value'),
				newValue = select.val();
			if (oldValue !== newValue) {
				if (longitude.val() && latitude.val()) {
					const params = {
						point: {
							longitude: parseFloat(longitude.val()),
							latitude: parseFloat(latitude.val())
						},
						from_srid: oldValue,
						to_srid: newValue
					};
					GIS.call('transform/point', params).then((result) => {
						if (result.status === 'success') {
							const point = result.point;
							longitude.val(point.longitude);
							latitude.val(point.latitude);
						}
					});
				}
			}
		},

		clear: (event)=> {
			// Clear fieldset
			const fieldset = $(event.currentTarget).parents('fieldset:first');
			$('input', fieldset).val(null);
			// reset map position and zoom level
			const
				map = $('.map', fieldset),
				marker = map.data('marker');
			if (marker) {
				marker.setLatLng([-90, 0]);
				const
					leafmap = map.data('leafmap'),
					config = map.data('leafmap.config');
				if (config.bounds) {
					leafmap.fitBounds(config.bounds);
				} else {
					const map_data = map.data();
					leafmap.setView(map_data.mapLeafletCenter || config.center,
									config.zoom || 13);
				}
			}
			map.trigger('marker.cleared.position', [map]);
		},

		moveMarkerTo: function(map, position, srid) {
			// Update fields
			const fieldname = map.data('map-leaflet-fieldname');
			$(`input[name="${fieldname}.widgets.longitude"]`).val(position.lon);
			$(`input[name="${fieldname}.widgets.latitude"]`).val(position.lat);
			// Get map coordinates
			const params = {
				point: {
					longitude: position.lon,
					latitude: position.lat
				},
				from_srid: srid,
				to_srid: 4326
			};
			const marker = map.data('marker');
			if (marker) {
				GIS.call('transform/point', params).then((result) => {
					if (result.status === 'success') {
						const point = result.result.point;
						marker.setLatLng({
							lon: point.longitude,
							lat: point.latitude
						});
						map.data('leafmap').setView(position);
					}
				});
			}
		}
	},


	/**
	 * Single rectangular area management
	 */
	area: {

		init: (evt) => {
			const map = $('.map', $(evt.currentTarget));
			if (map.data('leafmap') === undefined) {
				map.css('height', $(window).height() - 250);
				GIS.init(map, {}).then(({leafmap, config}) => {
					L.Draw = L.Draw || {};
					L.Edit = L.Edit || {};
					MyAMS.ajax.check([
						L.Draw, L.Draw.Event, L.Map.TouchExtend, L.Edit.SimpleShape
					], [
						`/--static--/pyams_gis/js/Draw/Leaflet.draw${MyAMS.env.extext}.js`,
						`/--static--/pyams_gis/js/Draw/Leaflet.Draw.Event${MyAMS.env.extext}.js`,
						`/--static--/pyams_gis/js/Draw/ext/TouchEvents${MyAMS.env.extext}.js`,
						`/--static--/pyams_gis/js/Draw/edit/handler/Edit.SimpleShape${MyAMS.env.extext}.js`
					]).then(() => {
						MyAMS.ajax.check(
							L.Edit.Rectangle,
							`/--static--/pyams_gis/js/Draw/edit/handler/Edit.Rectangle${MyAMS.env.extext}.js`
						).then(() => {

							const initRectangle = (p1, p2) => {
								const group = new L.FeatureGroup();
								rectangle = L.rectangle([p1, p2]);
								group.addLayer(rectangle);
								leafmap.addLayer(group);
								rectangle.editing.enable();
								map.data('area', rectangle);
								leafmap.on(L.Draw.Event.EDITMOVE, GIS.area.changedArea);
								leafmap.on(L.Draw.Event.EDITRESIZE, GIS.area.changedArea);
								leafmap.on(L.Draw.Event.EDITVERTEX, GIS.area.changedArea);
								// setTimeout(() => {
								// 	leafmap.fitBounds(rectangle.getBounds());
								// }, 50);
							}

							const
								data = map.data(),
								fieldname = data.mapLeafletFieldname,
								x1 = $(`input[name="${fieldname}.widgets.x1"]`),
								y1 = $(`input[name="${fieldname}.widgets.y1"]`),
								x2 = $(`input[name="${fieldname}.widgets.x2"]`),
								y2 = $(`input[name="${fieldname}.widgets.y2"]`);
							let p1,
								p2,
								rectangle;
							if (x1.val() && y1.val() && x2.val() && y2.val()) {
								const
									projection = $(`select[name="${fieldname}.widgets.projection"]`),
									params = {
										area: {
											x1: parseFloat(x1.val()),
											y1: parseFloat(y1.val()),
											x2: parseFloat(x2.val()),
											y2: parseFloat(y2.val())
										},
										from_srid: projection.val() || GIS.WGS_SRID,
										to_srid: GIS.WGS_SRID
									};
								GIS.call('transform/area', params).then((result) => {
									if (result.status === 'success') {
										const area = result.area;
										p1 = L.latLng({lon: area.x1, lat: area.y1});
										p2 = L.latLng({lon: area.x2, lat: area.y2});
										initRectangle(p1, p2);
									}
								});
							} else {
								const config = map.data('leafmap.config');
								if (config.bounds) {
									p1 = L.latLng(config.bounds[0]);
									p2 = L.latLng(config.bounds[1]);
								} else {
									p1 = L.latLng({lon: -168, lat: -56.37});
									p2 = L.latLng({lon: 191.25, lat: 83.72});
								}
								initRectangle(p1, p2);
							}
						});
					});
				});
			}
		},

		setBounds: (event) => {
			const
				map = $('.map', event.currentTarget),
				leafmap = map.data('leafmap'),
				rectangle = map.data('area');
			if (leafmap) {
				leafmap.invalidateSize();
				leafmap.fitBounds(rectangle.getBounds());
			}
		},

		last_event: null,

		changedArea: (event)=> {
			GIS.area.last_event = event;
			setTimeout(() => {
				if (event === GIS.area.last_event) {
					const
						map = event.target.getContainer(),
						data = $(map).data(),
						area = data.area.getBounds(),
						fieldname = data.mapLeafletFieldname,
						projection = $(`select[name="${fieldname}.widgets.projection"]`).val(),
						params = {
							area: {
								x1: area.getWest(),
								y1: area.getSouth(),
								x2: area.getEast(),
								y2: area.getNorth()
							},
							from_srid: GIS.WGS_SRID,
							to_srid: projection
						};
					GIS.call('transform/area', params).then((result) => {
						if (result.status === 'success') {
							const area = result.area;
							$(`input[name="${fieldname}.widgets.x1"]`).val(area.x1);
							$(`input[name="${fieldname}.widgets.y1"]`).val(area.y1);
							$(`input[name="${fieldname}.widgets.x2"]`).val(area.x2);
							$(`input[name="${fieldname}.widgets.y2"]`).val(area.y2);
						}
					});
				}
			}, 100);
		},

		/**
		 * Store previous value before projection change
		 */
		beforeProjectionChange: (event) => {
			const select = $(event.currentTarget);
			select.data('ams-old-value', select.val());
		},

		changedProjection: (event)=> {
			const
				select = $(event.currentTarget),
				map = $('.map', select.parents('fieldset:first')),
				fieldname = map.data('map-leaflet-fieldname'),
				x1 = $(`input[name="${fieldname}.widgets.x1"]`),
				y1 = $(`input[name="${fieldname}.widgets.y1"]`),
				x2 = $(`input[name="${fieldname}.widgets.x2"]`),
				y2 = $(`input[name="${fieldname}.widgets.y2"]`),
				oldValue = select.data('ams-old-value'),
				newValue = select.val();
			if (oldValue !== newValue) {
				if (x1.val() && y1.val() && x2.val() && y2.val()) {
					const params = {
						area: {
							x1: parseFloat(x1.val()),
							y1: parseFloat(y1.val()),
							x2: parseFloat(x2.val()),
							y2: parseFloat(y2.val())
						},
						from_srid: oldValue,
						to_srid: newValue
					};
					GIS.call('transform/area', params).then((result) => {
						if (result.status === 'success') {
							const area = result.area;
							x1.val(area.x1);
							y1.val(area.y1);
							x2.val(area.x2);
							y2.val(area.y2);
						}
					});
				}
			}
		},

		clear: (event)=> {
			// Clear fieldset
			const fieldset = $(event.currentTarget).parents('fieldset:first');
			$('input', fieldset).val(null);
			const map = $('.map', fieldset);
			map.trigger('marker.cleared.area', [map]);
		}
	}
};


if (window.MyAMS) {
	MyAMS.config.modules.push('gis');
	MyAMS.gis = GIS;
	console.debug("MyAMS: GIS module loaded...");
}
