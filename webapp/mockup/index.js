


window.onload = initialize()

function initialize(){
    loadMakeSelector();

    let 
}

function getAPIBaseURL(){
    let baseURL = window.location.protocol
                    +'//'+window.location.hostname
                    +'//'+window.location.port
                    +'/api';
    return baseURL;
}

function loadMakeSelector(){
    let url = getAPIBaseURL + '/makes';

    fetch(url,{method:'get'})

    .then((response) => response.json())

    .then(function(makes) {
        let selectorBody = '';
        for (let k =0;k<makes.length;k++){
            let make = makes[k]
            selectorBody += '<option values="' + makes['id'] + '">'
                                + makes[make] + '</option>\n';

        }
        let selector = document.getElementById('make_selector');
        if (selector){
            selector.innerHTML = selectorBody;
        }
    })

    .catch(function(error){
        console.log(error);
    });

}
