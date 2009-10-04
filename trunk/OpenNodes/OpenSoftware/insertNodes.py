###OpenAssembler Node python file###

'''
define
{
	name insertNodes
	tags opsw
	input string Software "" ""
	input array1D nodeDevList "" "" 
	output int result "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup


class insertNodes(opdb_setup):
   def insertNodes_main(self, **connections):
	Software=connections["Software"]
	nodeDevList=connections["nodeDevList"]
	devROOT=self.opdb_dev_settings(self.opdb_setup_read())
	sPath=devROOT+"/"+str(Software)+"_dev"
	if os.path.isdir(sPath):
		pass
	else:
		return 0

	for item in nodeDevList:
		try:
			shutil.rmtree(str(sPath)+"/"+str(item))
		except:
			pass
		try:
			shutil.copytree(devROOT+"/OpenNodes/"+str(item),sPath+"/"+str(item))
		except:
			return 0

	return 1