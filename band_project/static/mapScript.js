var mapOptions;
var map;
var markers = [];

function initialize() {
    // Map settings, default zoom and center point
    mapOptions = {
        zoom: 6,
        center: new google.maps.LatLng(35.4500, -112.0667)
    };
    // Create the map object
    map = new google.maps.Map(document.getElementById('tour-map'), mapOptions);

    // Grab the coordinates of all the tour dates from the database
    $.getJSON('/get_tour_dates', function(data) {
        $.each(data, function(key, val) {
            markMap(val.fields);
        });
    });
}

function markMap(data){
    // Create a new Google Maps LatLng object so that we can make a marker there (format is latitude, longitude)
    var position = new google.maps.LatLng(data.coords_y, data.coords_x);
    // Create a new Google Maps Marker object
    var marker = new google.maps.Marker({
        position: position,
        map: map,
        visible: true,
        draggable: false
    });
    // In case we ever want to get to the marker again, throw it in an array
    markers.push(marker);

}

// Listen for the document to be ready, and then initialize the map
google.maps.event.addDomListener(window, 'load', initialize);