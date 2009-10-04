###OpenAssembler Node python file###

'''
define
{
	name getElementType
	tags opdb
	input dbPath Path "" ""
	output string ElementType "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getElementType(opdb_setup):
   def getElementType_main(self, **connections):

	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="ElementType"

	if oas_output=="ElementType":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			ret=""
			if Path.find(".")>0:
				Path=ProjectROOT+Path.replace(":","/").replace(".","/")+".atr"
				if os.path.isfile(Path):
					ret="attribute"
			elif Path.find("@")>0:
					if Path.split("@")[1][:1]=="v" or Path.split("@")[1]=="live" or Path.split("@")[1]=="latest":
						ret="version"
			else:
				Path=ProjectROOT+Path.replace(":","/")
				if os.path.isdir(Path):
					if os.path.isfile(Path+"/projects.atr"):
						ret="projectRoot"
					elif os.path.isfile(Path+"/elements.atr"):
						ret="container"
					elif os.path.isfile(Path+"/versions.atr"):
						ret="item"

						
					else:
						pass
			return ret
		except:
			return 0
			
	else:
		return 0
