###OpenAssembler Node python file###

'''
define
{
	name getVersionFromPath
	tags opdb
	input dbPath Path "" ""
	output string result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from getLatestVersion import getLatestVersion
from getLiveVersion import getLiveVersion
from getCleanPath import getCleanPath

class getVersionFromPath(opdb_setup,getElementType,getLatestVersion,getLiveVersion,getCleanPath):
   def getVersionFromPath_main(self, **connections):
	try:
		Path=str(connections["Path"])
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
			path_type=self.getElementType_main(Path=Path)
			if path_type==0:
				return 0
			ret=""
			if str(Path).find("@")>0:
				ret=str(str(Path).split("@")[1])
				if ret=="live":
					ret=self.getLiveVersion_main(Path=self.getCleanPath_main(Path=Path))
				elif ret=="latest":
					ret=self.getLatestVersion_main(Path=self.getCleanPath_main(Path=Path))
			else:
				ret=0
			if ret=="":
				return 0
			return ret
	else:
		return 0

if __name__ == "__main__":
	print getVersionFromPath().getVersionFromPath_main(Path=":sandbox:sanditem@v027",oas_output="result")
