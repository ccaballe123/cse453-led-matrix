
import string
import sys



def mainSite(userName):
	return """<script type="text/javascript">  login('%s'); </script>""" % userName
		 		
def forgotPass(userName):
	return """
					Redirecting...
					<script type="text/javascript"> saveUserInfo('123',3,'file1','file2','file3');</script>
					<script type="text/javascript">  login('%s'); </script>
		 		""" % userName

def registerSuccess(userName):	 		
	return """LED Matrix Register
			  Redirecting...
			<script type="text/javascript">  registerSuccess('%s'); </script> """ % userName
		 		
		 		
def registerFailed(userName):
	return """<script type="text/javascript">  registerFailed('%s'); </script>	""" % userName


def wrongCreds():	 		
	return """<p>This is awkward seems you ennterd the wrong username or password please try again.</p>
		 		<p>if you wish to login but not save your work you may login using username 'tmp' and no password.</p>
		 		<button onclick="window.location.href = '../led-matrix/index.html';">Try again</button>
					
					<script type="text/javascript"> 
						function goback() {
							window.location.href = '../led-matrix/matrix.html'; 
					`	}
						
						</script>"""
def addSession(sessionVar):
	return """<script type="text/javascript"> saveSessionVariable('%s');</script>""" % sessionVar
def clearSession():
	return """<script type="text/javascript"> sessionStorage.clear();</script>"""
	
def startHtml():
	return """Content-type: text/html\n\n 
		 	<!DOCTYPE html> 
		 	<html lang="en">
		 		<head>
		 			<title>LED Matrix</title> 
		 			LED Matrix
		 			<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
					<meta content="utf-8" http-equiv="encoding">
		 			<script type="text/javascript" src="../led-matrix/src/login.js"></script>
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js" ></script>
					<script type="text/javascript" charset="utf-8" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
		 		</head>
		 		<body >"""
	
def endHtml():
	return """</body></html>"""
