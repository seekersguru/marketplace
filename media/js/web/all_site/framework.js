$(document).ready(
	function(){
		// Remove error message on click of input 
		$("input").click(function(){
			$(this).parent().removeClass("has-error");
		});
			
		$( ".form_button" ).click(
				function() {
					
					var form = $("#"+$(this)[0].id.split("_")[0]);
					var url=form.attr("action");
					var postData=form.serialize();
					postData=postData+"&web_site=1";
					
					
					
					//Making ajax request
					$.ajax({
						type: "post",
						url: url,
						data: postData,
						contentType: "application/x-www-form-urlencoded",
						success: function(responseData, textStatus, jqXHR) {
							
							if (responseData["result"]=="error"){
								$("#success_div").hide();
								$("#error_div").hide();
								$("#error_div").html(responseData["message"]);
								// Scroll to top to show the position
								window.scrollTo(0, 0);
								$("#error_div").slideDown();
								$.each(responseData["error_fields"],function(i,v){
									$('[name="'+v+'"]').parent().addClass("has-error");
								})
								
							}
							else if (responseData["result"]=="success"){
								if (responseData["json"]["redirect_to"]){
									location.href=responseData["json"]["redirect_to"];
								}else{
									$("#success_div").hide();
									$("#error_div").hide();
									$("#success_div").html(responseData["message"]);
									$("#success_div").slideDown();
								}
							}							
						},
						error: function(jqXHR, textStatus, errorThrown) {
							alert(errorThrown);
						}
					});
					//Complete ajax request					
				}
		)
	
	}
);
