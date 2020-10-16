
//ZIP API JS

var ZipData = null;

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "https://www.zipcodeapi.com/rest/" + zipapi + "/info.json/" + userzipinput + "/degrees");


xhr.send(ZipData);
console.log(ZipData);


----------------------------------------------

//Collect API JS
var CoordsData = null;

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});
//change to location to variables from zip

xhr.open("GET", "https://api.collectapi.com/gasPrice/fromCoordinates?lng=28.979530&lat=41.015137");
xhr.setRequestHeader("content-type", "application/json");
xhr.setRequestHeader("authorization", "apikey 60NpjP2khNX0u5YCngWVa8:3q7xw9Ij4XoszUMayKd6lk");

xhr.send(data);