###OpenAssembler Node python file###

'''
define
{
	name setLiveVersion
	tags opdb
	input dbPath Path "" ""
	input string Version "" ""
	output string result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from getVersionList import getVersionList

class setLiveVersion(opdb_setup,getElementType,getVersionList):
   def setLiveVersion_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Version=connections["Version"]
	except:
		Version=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			path_type=self.getElementType_main(Path=Path)
			if path_type!="item":
				return 0
			vlist=self.getVersionList_main(Path=Path)
			if vlist==0:
				return 0
			ret=""
			duplicity={}
			for vline in vlist:
				if duplicity.has_key(str(vline[0])):
					pass
				else:
					duplicity[str(vline[0])]=""
					if str(vline[1])=="live":
						if str(vline[0])==str(Version):
							ret+= vline[0]+" \"live\" "+"\""+vline[2]+"\"\n"
						else:
							ret+= vline[0]+" \"\" "+"\""+vline[2]+"\"\n"
					else:
						if str(vline[0])==str(Version):
							ret+= vline[0]+" \"live\" "+"\""+vline[2]+"\"\n"
						else:
							ret+= vline[0]+" \"\" "+"\""+vline[2]+"\"\n"
			if ret=="":
				return 0
			fl=open(ProjectROOT+"/"+Path.replace(":","/")+"/versions.atr","w")
			fl.write(ret)
			fl.close()
			return Version
		except:
			return 0
	else:
		return 0

if __name__ == "__main__":
	setLiveVersion().setLiveVersion_main(Path=":sandbox:sanditem",Version="v004",oas_output="result")
