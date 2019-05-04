var currentUserName = "";
var sessionCookieCount =0;
sessionStorage.setItem("sessionCookieCount", String(sessionCookieCount));


//called from /var/www/cgi-bin/ directory
function login(userName){
	//sessionStorage.setItem("uname",userName);
	window.location.href = '../led-matrix/matrix.html';
			/*$.ajax({
			 	type: "GET",
			      	url: "/cgi-bin/login.py",
				data: {param: dataString},
			     context: document.body
			});	*/
}

function logout(userName){
	console.log(userName);
	//window.location.href = 'index.html';
	$.ajax({
      type:'get',
      url:"/cgi-bin/test.py",
      cache:false,
      //data:<if any arguments>,
      //async:asynchronous,
      //dataType:json, //if you want json
      success: function(data) {
        
        console.log(data);
      },
      error: function(request, status, error) {
        console.log(request);
        console.log(staus);
        console.log(error);
      }
   });
	
}

function saveUserInfo(password,sketchCount,...restArgs){
	sessionStorage.setItem("sketchCount",sketchCount);
	sessionStorage.setItem("saved-sketches",JSON.stringify(restArgs));
}

function saveSessionVariable(sessionVar){
	
	
	console.log("sessionCookieCnt " +sessionStorage.getItem("sessionCookieCount"))
	
	var sessionCnt = Number(sessionStorage.getItem("sessionCookieCount"));
	sessionStorage.setItem("session"+String(sessionCnt), String(sessionVar));
	console.log("cnt before "+sessionCnt);
	sessionCnt++;
	console.log("cnt after "+sessionCnt);
	sessionStorage.setItem("sessionCookieCount", String(sessionCnt));
	
	console.log("sessionCookieCnt " +sessionStorage.getItem("sessionCookieCount"));
	
	console.log("");
	console.log("");
	
}

