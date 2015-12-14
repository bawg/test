	$(document).ready(function(){
		$(document).on("click","#getdata-button", function() {
		//test Confirmed
		alert('hello6');
		//$( this ).after( "<p>Another paragraph!</p>" );
		//$('#showdata').html("hello");
			$.getJSON('http://www.laviedevin.com/Test.php',function(data) {
				//noresponse
				alert('hello5');
				$('#showdata').html("item1="+data.item1+" item2="+data.item2+" item3="+data.item3+"");
			});
		});
	});
