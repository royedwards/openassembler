###OpenAssembler Node python file###

'''
define
{
	name setExecName
	tags opsw
	input string Software "" ""
	input string ExecName "" ""
	output string execName "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup


class setExecName(opdb_setup):
   def setExecName_main(self, **connections):
	Software=connections["Software"]
	ExecName=connections["ExecName"]

	devROOT=self.opdb_dev_settings(self.opdb_setup_read())
	sPath=devROOT+"/"+str(Software)+"_dev"
	if os.path.isdir(sPath):
		pass
	else:
		return 0
	try:
		fl=open(sPath+"/executeable.atr","w")
		fl.write(str(ExecName))
		fl.close()
		return ExecName
	except:
		return 0

 