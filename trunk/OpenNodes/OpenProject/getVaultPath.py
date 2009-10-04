###OpenAssembler Node python file###

'''
define
{
	name getVaultPath
	tags opdb
	input dbPath Path "" ""
	output file result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from getLiveVersion import getLiveVersion
from getLatestVersion import getLatestVersion
from getVersionList import getVersionList

class getVaultPath(opdb_setup,getElementType,getVersionList,getLiveVersion,getLatestVersion):
   def getVaultPath_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			path_type=self.getElementType_main(Path=Path)			
			if path_type=="item" or path_type=="version":
				pass
			else:
				return 0

			ret=""
			if Path.find("@")>0:
				vlist=self.getVersionList_main(Path=Path.split("@")[0])
				if vlist==0:
					return 0
				if Path.split("@")[1][:1]=="v":
					for vs in vlist:
						if vs[0]==Path.split("@")[1]:
							ret = str(VaultROOT+Path.replace(":","/").replace("@","/"))
							if os.path.isdir(ret):
								pass
							else:
								ret=""
				elif Path.split("@")[1]=="live":
					livev=self.getLiveVersion_main(Path=Path.split("@")[0])
					ret = VaultROOT+Path.split("@")[0].replace(":","/")+"/"+livev
					if os.path.isdir(ret):
						pass
					else:
						ret=""
				elif Path.split("@")[1]=="latest":
					lv=self.getLatestVersion_main(Path=Path.split("@")[0])
					ret = VaultROOT+Path.split("@")[0].replace(":","/")+"/"+lv
					if os.path.isdir(ret):
						pass
					else:
						ret=""
			else:
				livev=self.getLiveVersion_main(Path=Path)
				ret = VaultROOT+Path.replace(":","/")+"/"+livev
				if os.path.isdir(ret):
					pass
				else:
					ret=""				


			if ret=="":
				return 0
			return ret
		except:
			return 0
	else:
		return 0

if __name__ == "__main__":
	print getVaultPath().getVaultPath_main(Path=":sandbox:sanditem",oas_output="result")
