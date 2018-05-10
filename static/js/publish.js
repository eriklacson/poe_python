var main = function() {

	var SHA256 =  new Hashes.SHA256;


	$('#fileInput').change(function() {
		var props = $(this).prop('files');
		console.log("Hello World");			
	});

	var fileDisplayArea = document.getElementById('fileDisplayArea');
		
	$('form').submit(function (event) {

		var data = $(this).serializeArray();
		console.log(data)		
 		event.preventDefault();

 		var hash = data[0].value;
 		var jsonInfo = {item:{}};
 		jsonInfo.item.title = data[1].value;
 		jsonInfo.item.owner = data[2].value;
 		jsonInfo.item.description = data[3].value;
  		var output =  JSON.stringify(jsonInfo);
  		$('#result_display').text(output);
  
	});

}


$(document).ready(main);
