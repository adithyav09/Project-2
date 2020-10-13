
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

// var Prices = d3.select("#Price");
// var Brand = d3.select("Brand");
// var Zip_Code = d3.select("Zipcode")

const dataSource = {
  chart: {
    caption: "Different countries Gross Export/IMPORT DATA ",
    subcaption: "Jul-2020",
    nodelabelposition: "outside",
    showlegend: 0,
    theme: "fusion",
    mode: "post",
    linkcolorbydominance: "1",
    animation: "0"
  },
  nodes: [
    {
      label: "India"
    },
    {
      label: "USA"
    },
    {
      label: "CHINA"
    },
    {
      label: "UAE"
    },
    {
      label: "JAPAN"
    },
    {
      label: "SOUTH KOREA"
    },
    {
      label: "CANADA"
    },
    {
      label: "UK"
    },
    {
      label: "SAUDI ARABIA"
    }

  ],
  links: [
    {
      from: "INDIA",
      to: "USA",
      value: 3486
    },
    {
      from: "USA",
      to: "INDIA",
      value: 10710
    },
    {
      from: "USA",
      to: "China",
      value: 26395
    },
    {
      from: "CHINA",
      to: "USA",
      value: 4
    },
    {
      from: "USA",
      to: "UAE",
      value: 771
    },
    {
      from: "UAE",
      to: "USA",
      value: 907
    },
    {
      from: "CANADA",
      to: "USA",
      value: 123425
    },
    {
      from: "USA",
      to: "CANADA",
      value: 27720
    },
    {
      from: "USA",
      to: "UK",
      value: 12142
    },
    {
      from: "UK",
      to: "USA",
      value: 2598
    },
    {
      from: "USA",
      to: "SAUDI ARABIA",
      value: 16
    },
    {
      from: "SAUDI ARABIA",
      to: "USA",
      value: 22271
    },
    {
      from: "USA",
      to: "JAPAN",
      value: 20556
    },
    {
      from: "JAPAN",
      to: "USA",
      value: 673
    },
    {
      from: "USA",
      to: "SOUTH KOREA",
      value: 12686
    },
    {
      from: "SOUTH KOREA",
      to: "USA",
      value: 3427
    },
    
  ]
};

FusionCharts.ready(function() {
  var myChart = new FusionCharts({
    type: "chord",
    renderAt: "chart-container",
    width: "100%",
    height: "100%",
    dataFormat: "json",
    dataSource
  }).render();
});
