var mapOptions;
var map;
var markers = [];

function initialize() {
    mapOptions = {
        zoom: 6,
        center: new google.maps.LatLng(35.4500, -112.0667)
    };
    map = new google.maps.Map(document.getElementById('tour-map'), mapOptions);

    $.getJSON('/get_tour_dates', function(data) {
        $.each(data, function(key, val) {
            markMap(val.fields);
        });
    });
}

function markMap(data){
    var position = new google.maps.LatLng(data.coords_y, data.coords_x);
    var marker = new google.maps.Marker({
        position: position,
        map: map,
        visible: true,
        draggable: false
    });
    markers.push(marker);

}

google.maps.event.addDomListener(window, 'load', initialize);