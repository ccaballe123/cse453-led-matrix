

function login(){
	window.location.href = 'matrix.html';
			$.ajax({
			 	type: "POST",
			      	url: "/cgi-bin/login.py",
				data: {param: dataString},
			     context: document.body
			});	
}
