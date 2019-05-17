#!/usr/bin/env python
import sys
import dbhandler as db
import login 
import constants as consts
import cgi
import random
import string
import cgitb


cgitb.enable()

#cgi.test()

formData = cgi.FieldStorage()

formType = formData.getvalue('type')
userName = formData.getvalue('user')
matrixState = formData.getvalue('matrixState')
fileName = formData.getvalue('file')

#html = consts.startHtml()

print "Content-type: text/html\n\n"
#print "inside python "
#print formType
#print userName
#print fileName
#print matrixState


if formType == "saveSketch":
    if db.userExists(userName) == 1:
        print db.saveSketch(userName,matrixState,fileName)

if formType == "submitSketch":
    if db.userExists(userName) == 1:
        db.submitSketch(userName, matrixState)

if formType == "loadSketch":
    if db.userExists(userName) == 1:
        print db.getSavedSketchData(userName, fileName)


