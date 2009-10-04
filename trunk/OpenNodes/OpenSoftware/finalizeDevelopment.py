###OpenAssembler Node python file###

'''
define
{
	name finalizeDevelopment
	tags opsw
	input string Software "" ""
	input string execName "" ""
	input file inputOas "" ""
	input file inputUI "" ""
	output int result "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup


class finalizeDevelopment(opdb_setup):
   def finalizeDevelopment_main(self, **connections):
	Software=str(connections["Software"])
	execName=str(connections["execName"])
	inputOas=str(connections["inputOas"])
	inputUI=str(connections["inputUI"])

	devROOT=self.opdb_dev_settings(self.opdb_setup_read())
	sPath=devROOT+"/"+str(Software)+"_dev"

	if Software=="" or execName=="" or inputOas=="" :
		return 0

	if os.name=="nt":
		os.system("C:/OpenTools/bin/OpenAssembler/oas_finalizer "+str(inputOas) +" "+str(Software)+" "+sPath+"/"+str(execName))
	else:
		os.system("/opt/OpenTools/bin/OpenAssembler/oas_finalizer "+str(inputOas) +" "+str(Software)+" "+sPath+"/"+str(execName))
		os.system("chmod 755 "+sPath+"/"+str(execName))

	if inputUI=="":
		pass
	else:
		if inputUI==str(sPath+"/ui/main.ui"):
			pass
		else:
			try:
				shutil.copy(inputUI,str(sPath+"/ui/main.ui"))
			except:
				return 0

	return 1

	