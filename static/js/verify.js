var main = function() {

	var SHA256 =  new Hashes.SHA256;

	$('#fileInput').change(function() {
		var props = $(this).prop('files');
		var file = props[0];
		var reader = new FileReader();

		console.log(file);

		reader.onload = function() {
			
			var fileData = reader.result;
			var hash = SHA256.hex(fileData)			
			$('#hash-status').append("<p><b>File Hash: </b>" + hash + "</p>");
			$('#hash').val(hash);			
			console.log('SHA256: ' + SHA256.hex(hash));

			// Create a request variable and assign a new XMLHttpRequest object to it.
			var request = new XMLHttpRequest();

			// Open a new connection, using the GET request on the URL endpoint
			request.open('GET', 'http://127.0.0.1:5000/api/1.0/item/' + hash, true);

			request.onload = function () {
				
				var data = JSON.parse(this.response);
				console.log(data);

				if (request.status >= 200 && request.status < 400) {
					$("#items").append("<tr class=\"field\"><td>Title</td><td class=\"value\">" + data.item.title + "</td></tr>");
					$("#items").append("<tr class=\"field\"><td>Owner</td><td class=\"value\">" + data.item.owner + "</td></tr>");
					$("#items").append("<tr class=\"field\"><td>Description</td><td class=\"value\">" + data.item.description + "</td></tr>");	 
  					}  					 
  				else {
    				console.log('error');
 		 			}
				}

			// Send request
			request.send();				
			}

		reader.readAsBinaryString(file);
  
	});
}


$(document).ready(main);

