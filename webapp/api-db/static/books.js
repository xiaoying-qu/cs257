/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {
    var button = document.getElementById("peopleButton");
    button.onclick = showPeople;

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

function showPeople() {
    let url = getAPIBaseURL() + '/people/';

    // Send the request to the books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(people) {
        // Add the <option> elements to the <select> element
        peoplebody = '';
        for (var k = 0; k<people.length; k++) {
            var person = people[k];
            peoplebody += person.id + person.name + '\n';
        }
        var peoplelist = document.getElementById("peopleList")
        peoplelist.innerHTML = peoplebody;
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}
