###OpenAssembler Node python file###

'''
define
{
	name setShotCompComment
	tags oped
	input string Project "" ""
	input string Shot "" ""
	output array1D framerange "" ""
}
'''
import os, sys, platform
from getEdit import getEdit
from Setup import opdb_setup
from OpenProject.getAttribute import getAttribute
from OpenEdit.sequenceFromShot import sequenceFromShot

class setShotCompComment(getAttribute):
   def setShotCompComment_main(self, **connections):
	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Shot=connections["Shot"]
	except:
	    Shot=""
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="framerange"

	try:
		seq=sfs(Project,Shot)
		if seq==0 or seq=="":
			return [0,0]
		
		fr=self.getAttribute_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(Shot)+".framerange")
		if fr==0 or fr=="":
			return [0,0]
		ret=fr.strip().split(",")
		return ret
	except:
		return [0,0]
			
def sfs(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project, Shot=Shot)