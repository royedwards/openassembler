###OpenAssembler Node python file###

'''
define
{
	name getExecName
	tags opsw
	input string Software "" ""
	output string execName "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup


class getExecName(opdb_setup):
   def getExecName_main(self, **connections):
	Software=connections["Software"]
	devROOT=self.opdb_dev_settings(self.opdb_setup_read())
	sPath=devROOT+"/"+str(Software)+"_dev"
	if os.path.isdir(sPath):
		pass
	else:
		return 0

	if os.path.isfile(sPath+"/executeable.atr"):
		fl=open(sPath+"/executeable.atr","r")
		ree=fl.read()
		fl.close()
		ree=ree.strip().split("\n")
		ret=ree[0].strip()
		return ret
	else:
		fl=open(sPath+"/executeable.atr","w")
		fl.write("")
		fl.close()
		return ""

 