"use strict";

var resource = {
  category: 'FOOD',
  org_name: 'Bay Area Rescue Mission',
  resource_name: 'dinner',
  resource_street: '',
  resource_notes: '',
  longitude: -122.41414,
  latitude: 37.784106,
};

function initMap() {
  var resourceLatLng = {lat: resource.latitude, lng: resource.longitude};
  var sfLatLng = {lat: 37.7749, lng: -122.4194 };
  var myLatLng = {lat: -25.363, lng: 131.044 };
  var toLatLng = {lat: 43.6532, lng: -79.3832 };

//  var map = new google.maps.Map(document.getElementById('map'), {
//    center: {lat: -122.4194, lng: 37.7749 },
//    zoom: 4,
//  });
  
   var map = new google.maps.Map(document.getElementById("map"),
                                    {
                                        center: sfLatLng,
                                        zoom: 13
                                    });
  var marker = new google.maps.Marker({
    position: resourceLatLng,
    map: map,
    icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
    title: resource.resource_name
  });
}
