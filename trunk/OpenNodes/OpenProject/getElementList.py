###OpenAssembler Node python file###

'''
define
{
	name getElementList
	tags opdb
	input dbPath Path "" ""
	output array1D Elements "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup
from getProjects import getProjects

class getElementList(opdb_setup,getProjects):
   def getElementList_main(self, **connections):
	
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="Elements"

	if oas_output=="Elements":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			if Path==":":
				ret=self.getProjects_main()
			else:
				Path=ProjectROOT+Path.replace(":","/")
				if os.path.isfile(Path+"/elements.atr"):
					pf=open(Path+"/elements.atr","r")
					readed=pf.read()
					pf.close()
					readed=readed.strip().lstrip()
					ret=readed.split()
				else:
					pass
					#print "There is some problem in the getElementList node, maybe the given Path is wrong..."
			
			return ret
		except:
			return 0
			
	else:
		return 0
