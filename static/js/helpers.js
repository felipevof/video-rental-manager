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
});
