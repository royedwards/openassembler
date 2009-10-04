###OpenAssembler Node python file###

'''
define
{
	name getProjects
	tags opdb
	output array1D Projects "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getProjects(opdb_setup):
   def getProjects_main(self, **connections):
	try:
		Projects=connections["Projects"]
	except:
		Projects=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="Projects"
	if oas_output=="Projects":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			projects=[]
			
			if os.path.isfile(ProjectROOT+"/projects.atr"):
				pf=open(ProjectROOT+"/projects.atr","r")
				readed=pf.read()
				pf.close()
				readed=readed.strip().lstrip()
				projects=readed.split()
			else:
				print "There is some problem with the projects.atr file in your ProjectROOT..."
				
			return projects
		except:
			return 0
			
	else:
		return 0
