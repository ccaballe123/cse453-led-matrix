#!/usr/bin/env python
import sys
import dbhandler as db
import constants as consts
import cgi
import random
import string



#cgi.test()

formData = cgi.FieldStorage()



formType = formData.getvalue('form-type')
userName = formData.getvalue('user-name')
password = formData.getvalue('password')
sessionVar = formType
loginSuccess = ""


#formType = "login"
#userName = "tmp"
html = consts.startHtml() + consts.clearSession();

def logUserIn():
	global html
	if db.userExists(userName) == 1 and db.getUserNameCount(userName) == 1 and db.getUserPass(userName) == password:
		#db.logUserIn(userName)
		sketches = db.getSavedSketchNames(userName)
		sessionVar = "login"
		html = html + consts.addSession("login") + consts.addSession("true") + consts.addSession(userName) + consts.addSession(str(len(sketches)))
			
		for i in range(0, len(sketches)):
			sessionVar = sketches[i]
			html = html + consts.addSession(sketches[i])
		html = html + consts.mainSite(userName) + consts.endHtml()
		print html
			
	else:	
		html = html + consts.wrongCreds(userName) + consts.endHtml()
		print html
			
def logAdminIn():
	print ""

 
def genPassword(numLetters):
	randomPass =''
	for x in range(numLetters):
		randomPass.join(random.choice(string.ascii_letters))
	
	return randomPass


if formType == 'login':
	#check for valid user name and pass by database
	if userName == 'tmp':
		html = html + consts.addSession("login") + consts.addSession("true") + consts.addSession(userName) + consts.addSession("0")+ consts.mainSite(userName) + consts.endHtml()
		print html
	#elif db.getUserType(userName) == 'admin':  #check if user is administrator  
	else:
		logUserIn()
			
			
		
	
	
if formType == 'register':
	#compute password based on username and add them to database
	randomPass = genPassword(3)
	if db.userExists(userName) == 1:
		html = html + consts.addSession("register") + consts.addSession("false") + consts.registerFailed(userName) + consts.endHtml()
		print html
	else:
		db.addUser(userName, randomPass)
		html = html + consts.addSession("register") + consts.addSession("true") + consts.addSession(randomPass) + consts.registerSuccess(userName) + consts.endHtml()
		print html
			

if formType == 'register-admin':
	passwordVerify = formData.getvalue('password-verify')
	if db.userExists(userName) == 1:
		html = html + consts.addSession("register-admin") + consts.addSession("false") + consts.registerFailed(userName) + consts.endHtml()
		print html
	else:
		if passwordVerify == password:
			db.addUser(userName, password)
			html = html + consts.addSession("register") + consts.addSession("true") + consts.registerFailed(userName) + consts.endHtml()
		else:
			html = html + consts.wrongCreds(userName) + consts.endHtml()
			print html
			
if formType == 'forgot-pass':
	print ""
		

def getUserName():
	return userName
	
def getFourmType():
	return formType

def getLoginSuccess():
	return loginSuccess
#def main():
	

#if __name__ == "__main__":
#	main()
