###OpenAssembler Node python file###

'''
define
{
	name getVersionListWithComments
	tags opdb
	input dbPath Path "" ""
	output array1D Versions "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup
from OpenProject.getVersionComment import getVersionComment

class getVersionListWithComments(opdb_setup):
   def getVersionListWithComments_main(self, **connections):
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
			pOld=Path
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
						ver=line.split()[0].strip("\"").lstrip("\"")
						cmnt=gvc(pOld,ver)
						retu=str(ver)+" ("+str(cmnt)+")"
						ret.append(retu)
			else:
				return 0
				#print "There is some problem in the getVersionList node, maybe the given Path is wrong..."
			return ret
		except:
			return 0
			
	else:
		return 0

def gvc(Path,Version):
	return getVersionComment().getVersionComment_main(Path=Path,Version=Version)