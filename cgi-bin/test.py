#!/usr/bin/env python
import sys
import dbhandler as db
import login 
import constants as consts



#db.submitSketch("test", "TESTlksajf;lksajdf;lkajsdf;lkajsfd;lksajdf;lakjsdf")
db.readyToSend("test5");
db.addUser("elwin","user","")


data = db.getReadySketchData(3)

print data

print db.getSavedSketchData("elwin", "elwin_11.txt")