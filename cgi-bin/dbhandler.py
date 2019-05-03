import os
import sqlite3

def getLastRecordId():
	db = sqlite3.connect("test.db") 
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
	db = sqlite3.connect("test.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT COUNT(*) FROM students where userName = ?''', (userName,))
	count = cursor.fetchone()
	db.close()
	return count[0]
	
def userExists(userName):
	db = sqlite3.connect("test.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT id FROM students where userName = ?''', (userName,))
	exists = cursor.fetchall()
	db.close()
	if len(exists) ==0:
		return 0
	return 1
	
def getSketchCount(userName):
	db = sqlite3.connect("test.db") 
	cursor = db.cursor();
	cursor.execute(''' SELECT sketchCount FROM students where userName = ?''', (userName,))
	sketchCount = cursor.fetchone()
	db.close()
	return sketchCount[0]


def saveSketch(userName, data, fileName):
	userName = userName.lower();
	stuId = getLastRecordId() +1
	stuIdStr = str(stuId)
	sketchName = userName+"_"+fileName+".txt"
	
	#sketchPath = "/home/elwin/sketches/"+userName+"/"
	sketchPath = userName+"/"
	
	
		
	
	db = sqlite3.connect("test.db")
	cursor = db.cursor() 
	
	if userExists(userName) == 1 and getUserNameCount(userName) == 1:
		cursor.execute(''' INSERT INTO students-sketches(userName, sketchName)
						VALUES (?,?)
						''', (userName,sketchName))

	if not os.path.exists(sketchPath):
		os.makedirs(sketchPath)
		cursor.execute(''' INSERT INTO students(id,userName,sketchName,sketchCount)
						VALUES (?,?,?,0)
						''', (stuId,userName,sketchName))
	else:
		sketchCount = getSketchCount(userName) +1
	
		cursor.execute(''' UPDATE students SET sketchCount = ? WHERE userName = ? ''', (userName,sketchCount))
						
		f = open(sketchPath+sketchName, "w")
		f.write(data)
		f.close()

	db.commit()
	db.close()
	
	
	


def addUser(userName, password):
	userName = userName.lower();
	stuId = getLastRecordId() +1
	#sketchPath = "/home/elwin/sketches/"+userName+"/"
	sketchPath = userName+"/"
	thisUserNameCount = getUserNameCount(userName)
	success = -1
	
	db = sqlite3.connect("test.db")
	cursor = db.cursor() 
	try:
		cursor.execute(''' INSERT INTO students(id,userName,sketchName,sketchCount)
						VALUES (?,?,NULL,0)
						''', (stuId,userName))
		db.commit()
		if not os.path.exists(sketchPath):
			os.makedirs(sketchPath)
		
		success = 0
	except MySQLdb.IntegrityError:
		success = -1
	finally:
		cursor.close()
		db.close()
		
	return success
	
	

	


	
