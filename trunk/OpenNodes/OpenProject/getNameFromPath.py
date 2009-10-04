###OpenAssembler Node python file###

'''
define
{
	name getNameFromPath
	tags opdb
	input dbPath Path "" ""
	output string result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from getCleanPath import getCleanPath
class getNameFromPath(opdb_setup,getElementType,getCleanPath):
   def getNameFromPath_main(self, **connections):
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
			path_type=self.getElementType_main(Path=Path)
			if path_type=="" or path_type==0:
				return 0
			ret=""
			cp=self.getCleanPath_main(Path=Path)
			if cp==":":
				ret=cp
			else:
				ret=cp.split(":")[-1]
			if ret=="":
				return 0
			return ret
		except:
			return 0
	else:
		return 0

if __name__ == "__main__":
	print getNameFromPath().getNameFromPath_main(Path=":",oas_output="result")
