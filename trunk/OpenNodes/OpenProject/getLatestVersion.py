###OpenAssembler Node python file###

'''
define
{
	name getLatestVersion
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

class getLatestVersion(opdb_setup,getElementType,getVersionList,getCleanPath):
   def getLatestVersion_main(self, **connections):
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
			vformax=[]
			for vline in vlist:
				vformax.append(int(str(vline[0])[1:]))

			return "v"+str(max(vformax)).zfill(3)
		except:
			return 0
			
	else:
		return 0
		

if __name__ == "__main__":
	print getLatestVersion().getLatestVersion_main(Path=":sandbox:sanditem@v003",oas_output="version")
 