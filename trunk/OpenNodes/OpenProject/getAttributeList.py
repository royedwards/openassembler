###OpenAssembler Node python file###

'''
define
{
	name getAttributeList
	tags opdb
	input dbPath Path "" ""
	output array1D AttributeList "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getAttributeList(opdb_setup):
   def getAttributeList_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="AttributeList"

	if oas_output=="AttributeList":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			Path=ProjectROOT+Path.replace(":","/")
			
			ret=[]
			if os.path.isdir(Path):
				listed=os.listdir(Path)
				for item in listed:
					if os.path.isfile(str(Path+"/"+item)):
						if os.path.splitext(str(Path+item))[1][1:][:3]=="atr":
							if (str(item)!="elements.atr") and (str(item)!="versions.atr") and (str(item)!="projects.atr"):
								ret.append(str(item.split(".")[0]))

			return ret
		except:
			return 0
			
	else:
		return 0
