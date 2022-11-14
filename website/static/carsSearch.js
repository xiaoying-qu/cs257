// CS257 end-to-end assignment
// written by Xiaoying QU and Yiming Xia
// 11.9.2022

window.onload = initialize;

function initialize() {
    var button = document.getElementById("searchButton");
    button.onclick = showCars;

}

// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function showCars() {
    let searchString = document.getElementById("searchString").value;
    let url = getAPIBaseURL() + '/search/' + searchString;

    // Send the request to the books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(cars) {
        // Add the <option> elements to the <select> element
        carlist = '';
        for (var k = 0; k<cars.length; k++) {
            var car = cars[k];
            carlist += car.model + '     ' + car.make + '     ' + car.co2 + '<br>';
        }
        var carlist_by_make = document.getElementById("carlist_by_make")
        carlist_by_make.innerHTML = carlist;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}
