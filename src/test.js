
console.log("");
var formdata = new FormData();
formdata.append("Title", "Testtitle2");
formdata.append("Content", "TestContent2");
formdata.append("Img", "/C:/Users/parth/Pictures/1600328497491.jpg");

var requestOptions = {
  method: 'POST',
  body: formdata,
  redirect: 'follow'
};

fetch("http://localhost:8080/api/create/blog", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
