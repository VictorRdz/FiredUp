function registroEmpresaAutocomplete() {
    autocomplete = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} */(document.getElementById('empresa-pais-signup')),
        {types: ["geocode"]});
    autocomplete.addListener('place_changed', fillInAddress);
}

function registroVacanteAutocomplete() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -33.8688, lng: 151.2195},
        zoom: 16
    });
    autocomplete = new google.maps.places.Autocomplete(
        /** @type {!HTMLInputElement} */(document.getElementById('vacante-autocomplete')),
        {types: ["address"]});

    autocomplete.addListener('place_changed', fillInAddress);
   

}

function fillInAddress() {
    // Get the place details from the autocomplete object.
    var place = autocomplete.getPlace();
    document.getElementById('maps-name').value = place.name;
    document.getElementById('maps-address').value = place.formatted_address;
    document.getElementById('maps-lat').value = place.geometry.location.lat();
    document.getElementById('maps-lng').value = place.geometry.location.lng();
}
