###OpenAssembler Node python file###

'''
define
{
	name devBaseVersion
	tags opsw
	input string Software "" ""
	output string version "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class devBaseVersion(opdb_setup):
   def devBaseVersion_main(self, **connections):
	Software=connections["Software"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="version"
	if oas_output=="version":
		try:
			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			if os.path.isfile(str(devROOT+"/"+Software+"_dev/baseVersion.atr")):
				fl=open(str(devROOT+"/"+Software+"_dev/baseVersion.atr"),"r")
				ret=fl.read()
				fl.close()
			elif os.path.isfile(str(devROOT+"/OpenNodes/"+Software+"/baseVersion.atr")):
				fl=open(str(devROOT+"/OpenNodes/"+Software+"/baseVersion.atr"),"r")
				ret=fl.read()
				fl.close()
			if ret!="":
				ret=ret.strip().lstrip()
			return ret
		except:
			return 0
			
	else:
		return 0

if __name__ == "__main__":
	print devBaseVersion().devBaseVersion_main(Software="OpenAssembler",oas_output="version")

