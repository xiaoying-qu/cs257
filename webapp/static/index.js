// CS257 end-to-end assignment
// written by Xiaoying QU and Yiming Xia
// 11.9.2022

window.onload = initialize;

function initialize() {
    var sortButton = document.getElementById("fuel_consumption");
    var searchButton = document.getElementById()
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

