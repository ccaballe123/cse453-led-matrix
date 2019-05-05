import sys
import dbhandler as db
import constants as consts
import cgi
import random
import string


#db.saveSketch('random', 'data1', 'test1')
#db.saveSketch('random', 'data2', 'test2')
#db.saveSketch('random', 'data3', 'test3')
#db.saveSketch('Thomos', 'data4', 'test4')
#db.saveSketch('random2', 'data3', 'test3')
#print db.addUser('elwin','123')
db.saveSketch('elwin', 'data1', 'test1')
db.saveSketch('elwin', 'data2', 'test2')
db.saveSketch('elwin', 'data3', 'test3')
db.saveSketch('elwin', 'data4', 'test4')
db.saveSketch('elwin', 'data5', 'test5')
print db.userExists('elvin')
#print db.getSketchCount('elwin')
#print db.getUserNameCount('elwin')


def genPassword(numLetters):
	randomPass =''
	for x in range(0,numLetters):
		randomPass +=  random.choice(string.ascii_letters)
	#print randomPass.lower()
	return randomPass.lower()

genPassword(3)
print
print ''.join(random.choice(string.ascii_letters))
