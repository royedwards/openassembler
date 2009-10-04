###OpenAssembler Node python file###

'''
define
{
	name getVersionComment
	tags opdb
	input dbPath Path "" ""
	input string Version "" ""
	output string comment "" ""

}
'''
import os, sys,time
from Setup import opdb_setup
from getCleanPath import getCleanPath
from OpenProject.getVaultPath import getVaultPath
class getVersionComment(opdb_setup,getCleanPath):
   def getVersionComment_main(self, **connections):

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
		oas_output="comment"

	if oas_output=="comment":
		try:

			ret=""
			vPath=getV(Path+"@"+Version)

			try:
				fl=open(vPath+"/submissioncomment.atr","r")
				readed=fl.read()
				fl.close()

				ret=readed.split("\n")[1].strip()

			except:
				pass

			return ret
		except:
			return 0
			
	else:
		return 0


def getV(Path):
	return getVaultPath().getVaultPath_main(Path=Path)