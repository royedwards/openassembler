###OpenAssembler Node python file###

'''
define
{
	name getVersionList
	tags opdb
	input dbPath Path "" ""
	output array2D Versions "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getVersionList(opdb_setup):
   def getVersionList_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="Versions"
	if oas_output=="Versions":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			Path=ProjectROOT+Path.replace(":","/")
			
			ret=[]
			if os.path.isfile(Path+"/versions.atr"):
				pf=open(Path+"/versions.atr","r")
				readed=pf.read()
				pf.close()
				readed=readed.strip().lstrip()
				if readed=="":
					pass
				else:
					lines=readed.split("\n")
					for line in lines:
						status=line.split()[1].strip("\"").lstrip("\"")
						other=line.split()[2].strip("\"").lstrip("\"")
						ver=line.split()[0].strip("\"").lstrip("\"")
						ret.append([line.split()[0],status,other])
			else:
				return 0
				#print "There is some problem in the getVersionList node, maybe the given Path is wrong..."
			return ret
		except:
			return 0
			
	else:
		return 0
