###OpenAssembler Node python file###

'''
define
{
	name delDevelopmentCopy
	tags opsw
	input string Development "" ""
	input string Type "Software" ""
	output dbPath result "" ""

}
'''
import os, sys,shutil,errno
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getLatestVersion import getLatestVersion

class delDevelopmentCopy(opdb_setup,getElementType,getVaultPath,getLatestVersion):
   def delDevelopmentCopy_main(self, **connections):
	Development=str(connections["Development"])
	Type=connections["Type"]

	devROOT=self.opdb_dev_settings(self.opdb_setup_read())
	p=""
	if Type=="Software":
		dpath=devROOT+"/"+Development+"_dev"
		p=":Software:"+str(Development)
	elif Type=="Nodes":
		dpath=devROOT+"/OpenNodes/"+Development+""
		p=":OpenNodes:"+str(Development)
	else:
		return 0
	try:
		shutil.rmtree(dpath)
		return p
	except:
		return 0
