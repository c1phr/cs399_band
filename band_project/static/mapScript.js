var mapOptions;
var map;

function initialize() {
    mapOptions = {
        zoom: 8,
        center: new google.maps.LatLng(35.1848, -111.66178)
    };

    map = new google.maps.Map(document.getElementById('tour-map'), mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);