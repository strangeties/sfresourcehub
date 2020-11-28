"use strict";

const tenderloinLatLng = { lat:37.7847, lng:-122.4145 };

var markers = [];
var infoWindows = [];

function initMap() {
  var map = new google.maps.Map(document.getElementById("map"), {
    center: tenderloinLatLng,
    zoom: 16,
  });

  var tables_by_category = {};

  for (var i = 0; i < resources_from_database.length; i++) {
    var resource = resources_from_database[i];
    var resourceLatLng = { lat: parseFloat(resource.lat), lng: parseFloat(resource.long) };
    var category_index = categories.indexOf(resource.category);
    var category =
      category_index == -1 ? "Unknown Category" : category_names[category_index];

    var commonContentString = `
        <div class='resource_name'>${resource.resource_name}</div>
        <div class='resource_notes'>offered by <div class="bold" style="display:inline;">${resource.org_name}</div></div>
        <br>
        <div class='resource_street'>opening hours:${resource.hrs}</div>
        <div class='resource_street'>${resource.address}</div>`;
 
    var infoWindowContentString = `
        <div class="info-window darken-on-hover">
        <a href="#card${resource.id}" style="text-decoration:none;">${commonContentString}</a>
        </div>`;

    var listingContentString = `
        ${commonContentString}
        <div class='resource_street'><a href='${resource.link}'>${resource.link}</a></div>
        <div class='resource_street'>${resource.phone}</div>
        <br>
        <div class='resource_street' style='height:auto;'>${resource.notes}</div>
        <br>
        <div class="align-div-to-bottom" style="width:100%;">
           <div class="shadow m-2">
           <a class="btn btn-resource-listing bold darken-on-hover" style="width:100%;"
             href="#map"
             role="button">View On Map</a>
           </div>
        </div>`;

    var infoWindow = new google.maps.InfoWindow({
      content: infoWindowContentString,
    });

    var marker = new google.maps.Marker({
      position: resourceLatLng,
      map: map,
      icon: category_index == -1 ? default_icon : icons[category_index],
      title: resource.resource_name,
    });

    markers.push(marker);
    infoWindows.push(infoWindow);

    if (!(category in tables_by_category)) {
      tables_by_category[category] = '';
    }
    tables_by_category[category] = `
        ${tables_by_category[category]}
        <div class="card col-auto shadow p-3 m-2 bg-white"
         style="height:100%;"
         id="card${resource.id}" >
         <div>${listingContentString}</div>
        </div>`;
  }

  // Specifies info window and marker behavior.
  for (var i = 0; i < markers.length; i++) {
    var marker = markers[i];
    google.maps.event.addListener(
      marker,
      "click",
      (function (marker, i) {
        return function () {
          // Closes every other info window.
          for (var j = 0; j < markers.length; j++) {
            if (i === j) {
              continue;
            }
            infoWindows[j].close();
            markers[j].open = false;
          }
          // Adjusts window of interest.
          if (marker.open) {
            infoWindows[i].close();
            marker.open = false;
          } else {
            infoWindows[i].open(map, marker);
            marker.open = true;
          }
        };
      })(marker, i)
    );
  }

  // Adds listings.
  var tableRef = document.getElementById("resource_listings");
  for (category in tables_by_category) {
    var div = document.createElement('div');
    div.style.width = '100%';
    div.className = "row m-4";
    
    var title_div = document.createElement('div');
    title_div.style = 'width:100%';
    title_div.style['font-size'] = 'x-large';
    title_div.style.color = '#00AECB';
    title_div.className = 'row m-1';
    title_div.innerHTML = category;

    var listings_div = document.createElement('div')
    listings_div.className = 'row m-2';
    listings_div.innerHTML = tables_by_category[category]

    div.appendChild(title_div);
    div.appendChild(listings_div);
    tableRef.appendChild(div);
  }
}
