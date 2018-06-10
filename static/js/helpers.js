$(document).ready(function(){
	$('#delete_button').click(function() {
		$.ajax({
		    type: "DELETE",
		    url: $(this).data('url'),
		    success: function(data, text) {
				window.location.href = '/'; 
		    },
		    error: function(request, status, error) {
		    	alert(error);
		    }
		});
	});

	$("#search_button").on("click", function(e){
	    e.preventDefault();
	    var values = $('#search_form').serialize();
	    window.location.href = $('#search_form').attr('action') + '?q=' + values.split('=')[1];
	});
});
