import sys
import dbhandler as db
import random
import string
import constants as consts


#db.saveSketch('random', 'data1', 'test1')
#db.saveSketch('random', 'data2', 'test2')
#db.saveSketch('random', 'data3', 'test3')
#db.saveSketch('Thomos', 'data4', 'test4')
#db.saveSketch('random2', 'data3', 'test3')
print db.addUser('Elvin','123')
db.saveSketch('Elvin', 'data1', 'test1')
db.saveSketch('Elvin', 'data2', 'test2')
db.saveSketch('Elvin', 'data3', 'test3')
db.saveSketch('Elvin', 'data4', 'test4')
db.saveSketch('Elvin', 'data5', 'test5')
#print db.userExists('Elvin')
#print db.getSketchCount('Elvin')
#print db.getUserNameCount('Elvin')

#sk = db.getSavedSketchNames('Elvin')

#print db.sketchExist('elvin','elvin_test2.txt')
#db.deleteSketch('elvin','elvin_test2.txt')
#print db.sketchExist('elvin','elvin_test2.txt')

print db.isUserLoggedin('elvin')
db.logUserIn('elvin')
print db.isUserLoggedin('elvin')


arr1 = db.getAllLoggedinUsers()
for i in range(0,len(arr1)):
	print arr1[i]

arr2 = db.getAllLoggedoutUsers()
for i in range(0,len(arr2)):
	print arr2[i]
	
arr3 = db.getAllUsersNames()
for i in range(0,len(arr3)):
	print arr3[i]

arr4 = db.getAllUsersNames()
for i in range(0,len(arr4)):
	print arr4[i]
	


db.logUserOut('elvin')
print db.isUserLoggedin('elvin')

#db.deleteUser('elvin')

def genPassword(numLetters):
	randomPass ="h" 
	for x in range(0, numLetters):
		randomPass.join(random.choice(string.ascii_lowercase))
	
	return randomPass

print genPassword(3)
