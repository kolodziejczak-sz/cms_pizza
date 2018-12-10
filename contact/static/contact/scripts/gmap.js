(function() {
  const map = new google.maps.Map(document.getElementById('gmap'), {
    center: latlng,
    zoom: 8
  });
  new google.maps.Marker({ position: latlng, map });
})()