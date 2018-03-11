
// Employee functions


function employeePopup(properties) {
    return `<table>
                <tr>
                    <th scope="row">Name</th>
                        <td>${properties.degree} ${properties.name} ${properties.surname}&nbsp;</td></tr>
                    <th scope="row">Email</th>
                        <td> ${properties.email}&nbsp;</td></tr>
                    <th scope="row">Phone</th>
                    <td> ${properties.phone}&nbsp;</td></tr>
                    <th scope="row">URL</th>
                    <td> <a href=${properties.url}>${properties.url}&nbsp;</a></td></tr>
                </tr>\
           </table>`
}

function pop_employees(feature, layer) {
    layer.on({
        mouseout: function(e) {
            for (i in e.target._eventParents) {
                e.target._eventParents[i].resetStyle(e.target);
            }
        },
        mouseover: highlightFeature,
    });
    popupContent = employeePopup(feature.properties);
    layer.bindPopup(popupContent, {maxHeight: 400});
}

var femaleIcon = L.icon({
    iconUrl: "../markers/female_icon.png",
    iconSize: [20.0, 20.0]
})

var maleIcon = L.icon({
    iconUrl: "{% static 'markers/male_icon.png' %}",
    iconSize: [20.0, 20.0]
})

function set_marker(feature, latlng) {
    switch (feature.properties.sex) {
        case 'M':
            return L.marker(latlng, {'icon': maleIcon})
            break;
        case 'F':
            return L.marker(latlng, {'icon': femaleIcon})
            break
    }
};

// Rooms functions


function roomPopup(properties) {
    return `<table>
            <tr>
                <th scope="row">Name</th>
                    <td>${properties.name}&nbsp;</td></tr>
                <th scope="row">Symbol</th>
                    <td> ${properties.symbol} &nbsp;</td></tr>
            </tr>\
            </table>`
}

function pop_rooms(feature, layer) {
layer.on({
    mouseout: function(e) {
        for (i in e.target._eventParents) {
            e.target._eventParents[i].resetStyle(e.target);
        }
    },
    mouseover: highlightFeature,
});
popupContent = roomPopup(feature.properties);
layer.bindPopup(popupContent, {maxHeight: 400});
};

function style_rooms(feature) {
    return {
        pane: 'pane_rooms',
        opacity: 1,
        color: 'rgba(0,0,0,1.0)',
        lineCap: 'butt',
        lineJoin: 'miter',
        weight: 1.0,
        fill: true,
        fillOpacity: 1,
        fillColor: feature.properties.color
    };
}


function addOverlay(data, name, opts) {
    var overlay = L.geoJSON(data, opts)

}


// Baselayer functions

function style_baselayer() {
    return {
        pane: 'pane_baselayer',
        opacity: 1,
        color: 'rgba(80,80,80,1.0)',
        lineCap: 'square',
        lineJoin: 'bevel',
        weight: 1.0,
        fillOpacity: 1,
    }
};