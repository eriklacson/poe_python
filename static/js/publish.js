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
			$('#hash-status').append("<p><b>File Hash: </b>" + hash + "/p");
			$('#hash').val(hash);			
			console.log('SHA256: ' + SHA256.hex(data));				

			}

		reader.readAsBinaryString(file);			
	});

	var fileDisplayArea = document.getElementById('fileDisplayArea');
		
	$('form').submit(function (event) {


		// Create a request variable and assign a new XMLHttpRequest object to it.
		var request = new XMLHttpRequest();

		// Serialize form data
		var data = $(this).serializeArray();
		console.log(data)

		//prevent default form action		
 		event.preventDefault();

 		//extract has value
 		var hash = data[0].value;

 		//create json object for item data
 		var jsonInfo = {item:{}};

 		//extract form data and store in json
 		jsonInfo.item.title = data[1].value;
 		jsonInfo.item.owner = data[2].value;
 		jsonInfo.item.description = data[3].value;

 		//convert dict to json
  		var output =  JSON.stringify(jsonInfo);

  		// Send post request
		request.send(output);

  		$('#result_display').text(output);
  
	});

}


$(document).ready(main);



	// Open a new connection, using the GET request on the URL endpoint
	request.open('GET', '/api/1.0/publish/' + key, true);

	// Send post request
	request.send(output);