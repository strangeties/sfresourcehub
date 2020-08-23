"use strict";

var resource = {
  category: 'CLOTHING',
  org_name: 'Bay Area Women\'s & Children\'s Center',
  resource_name: 'clothing',
  resource_street: '318 Leavenworth St, San Francisco, CA 94102',
  resource_notes: 'For more than three decades, BAWCC has had one of the largest Free Clothing Closets for women and children in San Francisco.  In addition to giving out women and children\'s clothing, we give out smaller household items such as bedding, kitchen items, books, and even small pieces of furniture.',
  longitude: -122.41414,
  latitude: 37.784106,
};

function initMap() {
  var resourceLatLng = {lat: resource.latitude, lng: resource.longitude};
  var sfLatLng = {lat: 37.7749, lng: -122.4194 };
  var contentString = `<div class='resource_category'>--- ${resource.resource_name} ---</div>
                        <div class='resource_org_name'>${resource.org_name}</div>
                       <div class='resource_street'>${resource.resource_street}</div>
                       <div class='resource_notes'>${resource.resource_notes}</div>`;
  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });
  
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
  marker.addListener('click', function() {
    infowindow.open(map, marker);
  });
}
