import os
import sqlite3
import shutil

def getLastRecordId():
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT * FROM students ORDER BY ID DESC LIMIT 1''')
	studentRecord = cursor.fetchone()
	#db.commit();
	db.close()
	if studentRecord is None:
		return -1
	else:
		return studentRecord[0]
	
def getUserNameCount(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT COUNT(*) FROM students where userName = ?''', (userName,))
	count = cursor.fetchone()
	db.close()
	return count[0]
	
def userExists(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT userName FROM students where userName = ?''', (userName,))
	exists = cursor.fetchall()
	db.close()
	if exists is None:
		return 0
	else:
		for i in range(0, len(exists)):
			tupl = exists[i]
			if tupl[0] == userName:
				return 1
	return 0
	
def getUserType(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT userType FROM students where userName = ?''', (userName,))
	userType = cursor.fetchone()
	db.close()
	if userType is None:
		return ""
	else:
		return userType[0]
	
	
def getSketchCount(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT sketchCount FROM students where userName = ?''', (userName,))
	sketchCount = cursor.fetchall()
	db.close()
	if sketchCount is None:
		return 0
	return sketchCount[0][0] 
	
def getUserPass(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT password FROM students where userName = ?''', (userName,))
	sketchCount = cursor.fetchall()
	db.close()
	if sketchCount is None:
		return 0
	return sketchCount[0][0] 

def getSavedSketchNames(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT sketchName FROM student_sketches where userName = ?''', (userName,))
	sketchNames = cursor.fetchall()
	db.close()
	arr = [None] * len(sketchNames)
	if sketchNames is None:
		return ''
	else:
		for i in range(0, len(sketchNames)):
			tupl = sketchNames[i]
			arr[i] = tupl[0]
	return arr
	
def sketchExist(userName,sketchName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT sketchName FROM student_sketches where userName = ?''', (userName,))
	sketchNames = cursor.fetchall()
	db.close()
	if sketchNames is None:
		return False
	else:
		for i in range(0,len(sketchNames)):
			tupl = sketchNames[i]
			if tupl[0] == sketchName:
				return True
	return False
	
def isUserLoggedin(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT loggedin FROM students where userName = ?''', (userName,))
	sketchCount = cursor.fetchall()
	db.close()
	if sketchCount is None:
		return 0
	return sketchCount[0][0]

def getAllLoggedinUsers():
	db = sqlite3.connect("database.db") 
	cursor = db.cursor()
	cursor.execute(''' SELECT userName FROM students where loggedin = 1''')
	studentRecord = cursor.fetchall()
	db.close()
	arr = [None] * len(studentRecord)
	if studentRecord is None:
		return False
	else:
		for i in range(0,len(studentRecord)):
			tupl = studentRecord[i]
			arr[i] = tupl[0]
			
	return arr
	
def getAllLoggedoutUsers():
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT userName FROM students where loggedin = 0''')
	studentRecord = cursor.fetchall()
	db.close()
	arr = [None] * len(studentRecord)
	if studentRecord is None:
		return False
	else:
		for i in range(0,len(studentRecord)):
			tupl = studentRecord[i]
			arr[i] = tupl[0]
			
	return arr

def getAllUsersNames():
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT userName FROM students''')
	studentRecord = cursor.fetchall()
	db.close()
	arr = [None] * len(studentRecord)
	if studentRecord is None:
		return False
	else:
		for i in range(0,len(studentRecord)):
			tupl = studentRecord[i]
			arr[i] = tupl[0]
			
	return arr
	
def getAllSavedSketches():
	db = sqlite3.connect("database.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT sketchName FROM student_sketches''')
	studentRecord = cursor.fetchall()
	db.close()
	arr = [None] * len(studentRecord)
	if studentRecord is None:
		return False
	else:
		for i in range(0,len(studentRecord)):
			tupl = studentRecord[i]
			arr[i] = tupl[0]
			
	return arr

	

def saveSketch(userName, data,fileName):
	userName = userName.lower();
	stuId = getLastRecordId() +1
	stuIdStr = str(stuId)
	sketchCount = str(getSketchCount(userName))
	sketchName = userName+"_"+sketchCount+".txt"
	
	sketchPath = "/home/pi/sketches/"+userName+"/"
	#sketchPath = userName+"/"
	sketchCount =0;
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor() 
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1 and not sketchExist(userName,sketchName):
		sketchCount = getSketchCount(userName) +1
		cursor.execute(''' INSERT INTO student_sketches(username, sketchName)
						VALUES (?,?)
						''', (userName,sketchName))
		cursor.execute(''' UPDATE students SET sketchCount = ? WHERE userName = ? ''', (sketchCount, userName))

	if not os.path.exists(sketchPath):
		print "user does not exists"
		os.makedirs(sketchPath)
	else:				
		f = open(sketchPath+sketchName, "w")
		f.write(data)
		f.close()

	db.commit()
	db.close()
	return sketchName
	

def getAllSavedSkethData(userName):
	userName = userName.lower()
	sketchNames = getSavedSketchNames(userName);
	
	sketchData = [None] * len(sketchNames)
	for i in range(0, len(sketchNames)):
		sketchPath = "/home/pi/sketches/"+userName+"/"+sketchNames[i]

		if not os.path.exists(sketchPath):
			print "User does not hava a folder in this path"
			#os.makedirs(sketchPath)
		else:
			f = open(sketchPath, "r")
			sketchData[i] = f.readline()
			print sketchData[i]
	
	f.close()
	return 
	


def addUser(userName, userType, password):
	userName = userName.lower();
	stuId = getLastRecordId() +1
	sketchPath = "/home/pi/sketches/"+userName+"/"
	#sketchPath = userName+"/"
	thisUserNameCount = getUserNameCount(userName)
	success = -1
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor() 
	try:
		cursor.execute(''' INSERT INTO students(id,username,userType,password,sketchCount,loggedin)
						VALUES (?,?,?,?,0,0)
						''', (stuId,userName,userType,password))
		db.commit()
		if not os.path.exists(sketchPath):
			os.makedirs(sketchPath)
		
		success = 0
	except db.IntegrityError:
		success = -1
	#finally:
		#cursor.close()
		#db.close()


	
	cursor.close()
	db.close()
		
	return success
	
def deleteSketch(userName, sketchName):
	userName = userName.lower();
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	
	#sketchPath = "/home/elwin/sketches/"+userName+"/"
	sketchPath = userName+"/"+sketchName
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1 and sketchExist(userName,sketchName):
		sketchCount = getSketchCount(userName) - 1
		cursor.execute(''' DELETE FROM student_sketches WHERE sketchName = ?''', (sketchName,))
		cursor.execute(''' UPDATE students SET sketchCount = ? WHERE userName = ? ''', (sketchCount, userName))
		db.commit()
		db.close()
	
	try:
		os.remove(sketchPath)
	except OSError as e:  ## if failed, report it back  ##
		print ("Error: %s - %s." % (e.filename, e.strerror))
		

def deleteUser(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	
	#sketchPath = "/home/elwin/sketches/"+userName+"/"
	sketchPath = userName+"/"
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1:
		cursor.execute(''' DELETE FROM student_sketches WHERE userName = ?''', (userName,))
		cursor.execute(''' DELETE FROM students WHERE userName = ? ''', (userName,))
		db.commit()
		db.close()
	
	try:
		shutil.rmtree(sketchPath)
	except OSError as e:  ## if failed, report it back  ##
		print ("Error: %s - %s." % (e.filename, e.strerror))
		

def logUserIn(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1 :
		cursor.execute(''' UPDATE students SET loggedin = 1 WHERE userName = ? ''', (userName,))
		db.commit()
		db.close()
		
def logUserOut(userName):
	userName = userName.lower();
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1 :
		cursor.execute(''' UPDATE students SET loggedin = 0 WHERE userName = ? ''', (userName,))
		db.commit()
		db.close()




def submitSketch(userName, sketchData):
	userName = userName.lower()
	success = -1
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor() 
	try:
		cursor.execute(''' INSERT INTO submitted_sketches(userName, sketchData)
						VALUES (?,?)
						''', (userName,sketchData))
		db.commit()
		
		success = 0
	except db.IntegrityError:
		success = -1
	#finally:
		#cursor.close()
		#db.close()

	
	cursor.close()
	db.close()
		
	return success


def readyToSend(sketchData):

	f = open("dbIdx.txt", "r")
	dbIdx = int(f.readline())
	f.close()
		
	
	db = sqlite3.connect("database.db")


	cursor = db.cursor() 
	try:
		cursor.execute(''' UPDATE ready_for_display SET sketchData = ?  WHERE id = ? 
						''', (sketchData,dbIdx))
		db.commit()
		
		success = 0
	except db.IntegrityError:
		success = -1
	#finally:
		#cursor.close()
		#db.close()



	if dbIdx == 9:
		dbIdx =0
	else:
		dbIdx += 1

	f = open("dbIdx.txt", "w")
	f.write(str(dbIdx));
	f.close()
	
	cursor.close()
	db.close()
		
	return success


def getReadySketchData(sketchId):
	db = sqlite3.connect("database.db") 
	cursor = db.cursor()
	cursor.execute(''' SELECT sketchData FROM ready_for_display where id = ?''', (sketchId,))
	sketchData = cursor.fetchone()
	db.close()
	if sketchData is None:
		return ""
	return sketchData[0]

def getSavedSketchData(userName, fileName):
	sketchPath = "/home/pi/sketches/"+userName+"/"+fileName
	f = open (sketchPath, "r")
	return f.readline()
