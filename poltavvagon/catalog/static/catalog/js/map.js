

function initMap() {
  // The location of Uluru
  const uluru = { lat: 49.598549196819036, lng: 34.47971274551836 };
  // The map, centered at Uluru
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 15,
    center: uluru,
  });
  // The marker, positioned at Uluru
  const marker = new google.maps.Marker({
    position: uluru,
    map: map,
  });
}

// 49.598549196819036, 34.47971274551836