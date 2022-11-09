/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 */

window.onload = initialize;

function initialize() {
    loadAuthorsSelector();

    let element = document.getElementById('author_selector');
    if (element) {
        element.onchange = onAuthorsSelectionChanged;
    }
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

function loadAuthorsSelector() {
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
        let selectorBody = '';
        for (let k = 0; k < people.length; k++) {
            let people = people[k];
            selectorBody += people['id'] + people['name'] + ', ' + people['age'];
        }

        let selector = document.getElementById('people_table');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}
