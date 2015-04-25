$(document).ready(function() {
	ymaps.ready(init);
	var myMap,
		myPlaceMark;

	function init() {
		var myMap = new ymaps.Map("map", {
			center: [55.9313, 37.516143],
			zoom: 12
		}, {
			balloonMaxWidth: 1500
		});

		var containers = [];
		for (i = 0; i < 15; i++) {
			myGeoObject = new ymaps.GeoObject({
				geometry: {
					type: 'Rectangle',
					coordinates: [
		                [55.93488, 37.51885],
		                [55.935, 37.519]
		            ], 
		        },
		            properties: {
		            	hintContent: 'Контейнер #7',
		
		            	balloonContentBody: [
		            	'<div class = "ball"> Улица Первомайская, дом 40 <br> Текущая заполненность: 30% <br> Прогнозируемая дата вывоза: 25.04.2015 </div>'].join(''),
		       
		            }
				}, {
					draggable: true,
			        // Цвет и прозрачность заливки.
			        fillColor: '#ffff0022',
			        // Цвет и прозрачность границ.
			        
			});
			containers.push(myGeoObject);
		}

		//важно
		myMap.events.add('click', function(e) {
			var coords = e.get('coords');
			var balloonWithFields = new ymaps.Balloon(myMap);
			balloonWithFields.options.setParent(myMap.options);
			balloonWithFields.open(coords, {
				contentHeader: 'Введите объём контейнера',
				contentBody: [
					'<form class = "coolForm"><input type = "text" size = "10%"></input> <input type = "submit" value = "Добавить"></input></form>'
				]
			})	
			ymaps.geocode(coords).then(function(res) {
				var realAdress = res.geoObjects.get(0);
				var realAdressText = realAdress.properties.get('name');
				var xCoord = coords[0];
				var yCoord = coords[1];
			})
		})


		myMap.geoObjects.add(myGeoObject);
		setUpControls (myMap, myGeoObject);
	}

	function setUpControls(map, GeoObject) {
		var btnSize = new ymaps.control.Button('Изменить размер');
		
		btnSize.options.set('maxWidth', 200);
		btnSize.events.add(['select', 'deselect'], function (e) {
			GeoObject.geometry.setCoordinates(e.get('type') == 'select' ? [
	            [55, 37.66],
	            [55.64, 37]
	        ] : [
	            [55.665, 53],
	            [55.64, 51]
	        ])
		})
		var addContainer = new ymaps.control.Button({
			data: {
				content: 'Добавить контейнер'
			},
			options: {
				maxWidth: 200
			}});

		map.controls.add(addContainer);
		map.controls.add(btnSize);
	};

})