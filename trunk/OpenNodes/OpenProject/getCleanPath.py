###OpenAssembler Node python file###

'''
define
{
	name getCleanPath
	tags opdb
	input dbPath Path "" ""
	output dbPath result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
class getCleanPath(opdb_setup,getElementType):
   def getCleanPath_main(self, **connections):
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
			if path_type==0:
				return 0
			ret=""
			if str(Path).find("@")>0:
				ret=str(str(Path).split("@")[0])
			else:
				ret=str(Path)
			if ret[-1:]==":":
				if ret!=":":
					ret=ret[:-1]
			if ret=="":
				return 0
			return ret
		except:
			return 0
	else:
		return 0

if __name__ == "__main__":
	print getCleanPath().getCleanPath_main(Path=":",oas_output="result")
