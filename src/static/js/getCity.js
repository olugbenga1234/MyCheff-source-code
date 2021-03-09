let geocode = {
    reverseGeocode: function (latitude, longitude) {

        var apikey = '802d4ef7800045bf97f56f1387096a10';
        // var latitude = '51.0';
        //var longitude = '7.0';

        var api_url = 'https://api.opencagedata.com/geocode/v1/json'

        var request_url = api_url
            + '?'
            + 'key=' + apikey
            + '&q=' + encodeURIComponent(latitude + ',' + longitude)
            + '&pretty=1'
            + '&no_annotations=1';

        // see full list of required and optional parameters:
        // https://opencagedata.com/api#forward

        var request = new XMLHttpRequest();
        request.open('GET', request_url, true);

        //set longitude and latitude value to app
        //console.log(longitude)
        //console.log(latitude)
        //document.getElementById('cheff_coord').value = latitude + ',' + longitude
        //document.getElementById('latitude').value = latitude;

        request.onload = function () {
            // see full list of possible response codes:
            // https://opencagedata.com/api#codes

            if (request.status === 200) {
                // Success!
                var data = JSON.parse(request.responseText);
                //alert(data.results[0].formatted); // print the location
                //document.getElementById('location').value = data.results[0].formatted; //full address
                document.getElementById('city').value = data.results[0].components.city; //only city
                //document.getElementById('usercity').value = data.results[0].components.city; //only city

            } else if (request.status <= 500) {
                // We reached our target server, but it returned an error

                console.log("unable to geocode! Response code: " + request.status);
                var data = JSON.parse(request.responseText);
                console.log('error msg: ' + data.status.message);
            } else {
                console.log("server error");
            }
        };

        request.onerror = function () {
            // There was a connection error of some sort
            console.log("unable to connect to server");
        };

        request.send();  // make the request

    },
    getLocation: function () {
        function success(data) {
            geocode.reverseGeocode(data.coords.latitude, data.coords.longitude);
        }

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(success, console.error);
        }
        else {
            console.error
        }
    }
};

geocode.getLocation();

