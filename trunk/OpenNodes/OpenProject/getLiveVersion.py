###OpenAssembler Node python file###

'''
define
{
	name getLiveVersion
	tags opdb
	input dbPath Path "" ""
	output string version "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from getVersionList import getVersionList
from getCleanPath import getCleanPath

class getLiveVersion(opdb_setup,getElementType,getVersionList,getCleanPath):
   def getLiveVersion_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="version"
	if oas_output=="version":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			Path=self.getCleanPath_main(Path=Path)
			path_type=self.getElementType_main(Path=Path)
			if path_type!="item":
				return 0
			vlist=self.getVersionList_main(Path=Path)
			if vlist==0:
				return 0
			ret=""
			for vline in vlist:
				if vline[1]=="live":
					ret= vline[0]
			if ret=="":
				return 0
			return ret
		except:
			return 0
			
	else:
		return 0
		

if __name__ == "__main__":
	print getLiveVersion().getLiveVersion_main(Path=":sandbox:sanditem",oas_output="version")
 