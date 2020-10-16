/* <html>
<head>
	<title>My first chart using FusionCharts Suite XT</title>
	<script type="text/javascript" src="https://cdn.fusioncharts.com/fusioncharts/latest/fusioncharts.js"></script>
	<script type="text/javascript" src="https://cdn.fusioncharts.com/fusioncharts/latest/themes/fusioncharts.theme.fusion.js"></script>
	<script type="text/javascript"> */

		FusionCharts.ready(function(){
			var chartObj = new FusionCharts({
    type: 'multilevelpie',
    renderAt: 'chart-container',

    width: '900',
    height: '600',
    dataFormat: 'json',
    dataSource: {
        "chart": {
            "caption": "Crude Oil Production Breakup | Thousand Barrels",
            "subcaption": "JUL-2020",
            "showPlotBorder": "1",
            "piefillalpha": "60",
            "basefontsize": "15",
            "baseFont":"outCnvBaseFont" ,
            // "Helvetica Neue,Arial",
            "pieborderthickness": "3",
            "hoverfillcolor": "#CCCCCC",
            "piebordercolor": "#FFFFFF",
            "hoverfillcolor": "#CCCCCC",
            "numberprefix": "$",
            "plottooltext": "$label, $$valueK, $percentValue",
            //Theme
            "theme": "fusion",
            "innerRadius": "30"
        },
        "category": [{
            "label": "US{br}Crude{br}Oil{br}Production",
            "color": "#ffffff",
            "value": "340496",
            "category": [{
                "label": "PADD1",
                "color": "#f8bd19",
                "value": "2030",
                "tooltext": "PADD1, $$valueK, $percentValue",
                "category": [
                {
                    "label": "VA,PA,NY,FL",
                    "color": "#f8bd19",
                    "value": "1508"
                },
              ]
            }, {
                "label": "PADD2",
                "color": "#33ccff",
                "value": "53172",
                "tooltext": "PADD2, $$valueK, $percentValue",
                "category": [
                
                {
                    "label": "North Dakota",
                    "color": "#33ccff",
                    "value": "31900"
                },
                {
                    "label": "KS,OH,SD,TE,IL,IA",
                    "color": "#33ccff",
                    "value": "6456"
                },
                {
                    "label": "OK",
                    "color": "#33ccff",
                    "value": "14936"
                },
               
              ]
            }, {
                "label": "PADD3",
                "color": "#ffcccc",
                "value": "233556",
                "tooltext": "PADD3, $$valueKBarrels, $percentValue",
                "category": [
                
                {
                    "label": "Louisiana",
                    "color": "#2ca02c",
                    "value": "3139"
                },
                {
                    "label": "New Mexico",
                    "color": "#2ca02c",
                    "value": "30613"
                },
                {
                    "label": "AR,AL",
                    "color": "#2ca02c",
                    "value": "664"
                }, 
                {
                    "label": "Texas",
                    "color": "#2ca02c",
                    "value": "146773"
                },
                
                {
                    "label": "Mississippi",
                    "color": "#2ca02c",
                    "value": "1258"
                },
                {
                    "label": "Federal{br}Offshore{br}(PADD3)",
                    "color": "#2ca02c",
                    "value": "51108"
                },

              ]
            }, {
                "label": "PADD4",
                "color": "#ccff66",
                "value": "25558",
                "category": [
                {
                    "label": "Montana",
                    "color": "#ccff66",
                    "value": "1648"
                },{
                    "label": "Colorado",
                    "color": "#ccff66",
                    "value": "13955"},
                {
                    "label": "Utah",
                    "color": "#ccff66",
                    "value": "2607"
                },
                {
                    "label": "Wyoming",
                    "color": "#ccff66",
                    "value": "7348"
                },
                
              ]
            },
            {
                "label": "PADD5",
                "color": "#d62728",
                "value": "26181",
                "category": [{
                    "label": "Alaska",
                    "color": "#d62728",
                    "value": "13767"
                }, {
                    "label": "Arizona",
                    "color": "#d62728",
                    "value": "1"
                }, {
                    "label": "California",
                    "color": "#d62728",
                    "value": "12014"
                },
                // {
                //     "label": "Nevada",
                //     "color": "#FF9900",
                //     "value": "15"
                // },
                // {
                //     "label": "Federal Offshore(PADD 5)",
                //     "color": "#FF9900",
                //     "value": "383",
                //     "basefontsize":"25"
                // },
                
              ]
            }]
        }]
    }
}
);

			chartObj.render();
		});
// 	</script>
// 	</head>
// 	<body>
// 		<div id="chart-container">FusionCharts XT will load here!</div>
// 	</body>
// </html>