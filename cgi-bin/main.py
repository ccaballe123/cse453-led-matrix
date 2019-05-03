import sys
import dbhandler as db

#db.saveSketch('random', 'data1', 'test1')
#db.saveSketch('random', 'data2', 'test2')
#db.saveSketch('random', 'data3', 'test3')
#db.saveSketch('Thomos', 'data4', 'test4')
#db.saveSketch('random2', 'data3', 'test3')
print db.addUser('Elvin','123')
db.saveSketch('Elvin', 'data1', 'test1')

