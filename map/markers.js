"use strict";

const sfLatLng = {lat: 37.7749, lng: -122.4194 };

var markers = []
var infoWindows = []

function initMap() {
    var map = new google.maps.Map(document.getElementById("map"),
                                  {
    center: sfLatLng,
    zoom: 13
    });
    
    for (var i = 0; i < resources.length; i++) {
        var resource = resources[i]
        var resourceLatLng = {lat: resource.lat, lng: resource.long};
        
        var contentString = `<div class='resource_category'>--- ${resource.resource_name} ---</div>
        <div class='resource_org_name'>${resource.org_name}</div>
        <div class='resource_street'>${resource.address}</div>
        <div class='resource_notes'>${resource.notes}</div>`;
        
        var infoWindow = new google.maps.InfoWindow({
        content: contentString
        });
        
        var marker = new google.maps.Marker({
        position: resourceLatLng,
        map: map,
        icon: "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png",
        title: resource.resource_name
        });
        
        google.maps.event.addListener(marker,'click', (function(marker,contentString,infowWindow){
            return function() {
                infowWindow.setContent(contentString);
                infowWindow.open(map,marker);
            };
        })(marker,contentString,infoWindow));
    }
}
