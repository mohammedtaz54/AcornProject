function initMap(postcodes) {
    var cardiff = {lat: 51.481, lng: -3.180};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: cardiff
    });

    getCoordinates(postcodes, function(siteData){
      longLat(map,siteData);
    });
}

function getCoordinates(postcodes, cb){
  var xhr = new XMLHttpRequest();
  var url = "https://api.postcodes.io/postcodes?filter=longitude,latitude";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onload = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          var json = JSON.parse(xhr.responseText);
          cb(json);
      }
  };
  var data = JSON.stringify(postcodes);
  console.log(data);
  xhr.send(data);
}

function longLat(map,webRtrn) {
  var x = webRtrn.result
  for (var i=0; i<x.length;i++){
    var y = x[i].result;
    var marker = new google.maps.Marker({
      position: {lat:y.latitude, lng:y.longitude},
      map: map
    });
    marker.setMap(map);
  }
}
