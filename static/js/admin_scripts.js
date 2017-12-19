function initMap(postcodes) {
    let cardiff = {lat: 51.481, lng: -3.180};
    let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: cardiff
    });

    getCoordinates(postcodes, function(webReturn){
      lngLat(map,webReturn);
    });
}

function getCoordinates(postcodes, callBack){
  let xhr = new XMLHttpRequest();
  let url = "https://api.postcodes.io/postcodes?filter=longitude,latitude";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-type", "application/json");
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          var json = JSON.parse(xhr.responseText);
          console.log(json)
          callBack(json);
      }
  };
  let postCodeData = JSON.stringify(postcodes);
  console.log(postCodeData);
  xhr.send(postCodeData);
}

function lngLat(map,webReturn) {
  let x = webReturn.result;
  for (var i=0; i<x.length;i++){
    let y = x[i].result;
    if (y != null){
        let marker = new google.maps.Marker({
          position: {lat:y.latitude, lng:y.longitude},
          map: map
        });
        marker.setMap(map);
    }
  }
}
