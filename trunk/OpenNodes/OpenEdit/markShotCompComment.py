###OpenAssembler Node python file###

'''
define
{
	name markShotCompComment
	tags oped
	input dbPath dbPath "" ""
	input string lineToChange "" ""
	input string toThisValue "" ""
	output int result "" ""
}
'''
import os, sys, platform
from getEdit import getEdit
from Setup import opdb_setup
from OpenProject.getAttribute import getAttribute
from OpenProject.setAttribute import setAttribute

class markShotCompComment(getAttribute,setAttribute):
   def markShotCompComment_main(self, **connections):
	try:
	    dbPath=str(connections["dbPath"])
	except:
	    dbPath=""
	try:
	    lineToChange=str(connections["lineToChange"])
	except:
	    lineToChange=""
	try:
	    toThisValue=str(connections["toThisValue"])
	except:
	    toThisValue=""


	try:
		ai=self.getAttribute_main(Path=dbPath,oas_output="value")
		newline=""
		if toThisValue=="no":
			newline=lineToChange.replace("yes","no")
		else:
			newline=lineToChange.replace("no","yes")
		bi=ai.replace(lineToChange,newline)
		self.setAttribute_main(Path=dbPath,Value=bi)
		return 1
	except:
		return 0
			
