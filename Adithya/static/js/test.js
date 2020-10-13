// d3.json('static/data/gasPriceState.json', function(data) {
//     console.log(data);
// });

// d3.json('static/data/statesData.geojson', function(data) {
//     console.log(data);
// });

// https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/counties.json

let statesFile = 'https://d3js.org/us-10m.v1.json'
let Alaska_Test = 'static/data/Alaska.json'

let statesData
let AlaskaData

let canvas = d3.select('#canvas')

let drawMap = () => {

    canvas.selectAll('path')
        .data(statesData)
        .enter()
        .append('path')
        .attr('d', d3.geoPath())
        .attr('class', 'states')
        .attr('fill', (statesDataItem) => {
            let id = statesDataItem['id']
            let state = AlaskaData.find((item) => {
                return item['id'] === id         //Parse through the gas price data and find the id that matches be sure to insert the id into the geojson
            })
        })
}


d3.json(statesFile).then(
    (data, error) => {
        if(error){
            console.log(error)
        }else{
            // statesData = data
            statesData = topojson.feature(data, data.objects.states).features
            console.log(statesData)
            

            d3.json(Alaska_Test).then(
                (data, error) => {
                    if(error){
                        console.log(error)
                    }
                    else{
                        AlaskaData = data
                        console.log('Alaska Data')
                        console.log(AlaskaData)
                        drawMap()
                    }
                }
            )
        }
    }
)
