#!/usr/bin/env python
import sys
import dbhandler as db
import cgi
import random
import string



#cgi.test()

formData = cgi.FieldStorage()



formType = formData.getvalue('form-type')
userName = formData.getvalue('user-name')
password = formData.getvalue('password')
submit = formData.getvalue('submit')


#formType = "login"
#userName = "tmp"

 
def genPassword(numLetters):
	randomPass =''
	for x in range(numLetters):
		randomPass.join(random.choice(string.ascii_letters))
	
	return randomPass


if formType == 'login':
	#check for valid user name and pass by database
	if userName == 'tmp':
		 print """Content-type: text/html\n\n 
		 	<!DOCTYPE html> 
		 	<html lang="en">
		 		<head>
		 			<title>LED Matrix</title> 
		 			LED Matrix Login
		 			<script type="text/javascript" charset="utf-8"> window.location.href = '../led-matrix/matrix.html'; </script>
		 		</head>
		 		"""

		
	
	
#if formType == 'register':
	#compute password based on username and add thmem to database	


#def main():
	

#if __name__ == "__main__":
#	main()
