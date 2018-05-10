var main = function() {

	$("#btn-publish").click(function handleFormSubmit() {

		var assetHash = $("#hash").val();
		var assetOwner = $("#hash").val();
		var assetTitle = $("#hash").val();
		var assetValue = $("#hash").val();

		// Stop the form from submitting since we’re handling that with AJAX.
  		event.preventDefault();
  
  		// TODO: Call our function to get the form data.
  		const data = {};

  		var output = JSON.stringify(data, null, "  ");

  		// Use `JSON.stringify()` to make the output valid, human-readable JSON.
  		$('#results__display').text("hello");
  
	});

}


  const handleFormSubmit = event => {
  

};

$(document).ready(main);