var main = function() {

	$("#key").text(key);

	// Create a request variable and assign a new XMLHttpRequest object to it.
	var request = new XMLHttpRequest();

	// Open a new connection, using the GET request on the URL endpoint
	request.open('GET', 'http://127.0.0.1:5000/api/1.0/item/' + key, true);

	request.onload = function () {
  	// Begin accessing JSON data here

  	var data = JSON.parse(this.response);

  	if (request.status >= 200 && request.status < 400) {

  			$("#asset").append("<tr class=\"field\"><td>Title</td><td class=\"value\">" + data.item.title + "</td></tr>");
  			$("#asset").append("<tr class=\"field\"><td>Owner</td><td class=\"value\">" + data.item.owner + "</td></tr>");
  			$("#asset").append("<tr class=\"field\"><td>Description</td><td class=\"value\">" + data.item.description + "</td></tr>");	 
  		} 
  	else {
    	console.log('error');
 		 }
  
	}

	// Send request
	request.send();
}

$(document).ready(main);