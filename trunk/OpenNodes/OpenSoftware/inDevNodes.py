###OpenAssembler Node python file###

'''
define
{
	name inDevNodes
	tags opsw
	output array1D nodes "[]" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class inDevNodes(opdb_setup):
   def inDevNodes_main(self, **connections):
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="nodes"
	if oas_output=="nodes":
		try:

			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			inthedir=os.listdir(devROOT+"/OpenNodes/")
			ret=[]
			for itms in inthedir:
				if os.path.isdir(devROOT+"/OpenNodes/"+itms):
					ret.append(itms)
			return ret
		except:
			return 0
			
	else:
		return 0

if __name__ == "__main__":
	print inDevNodes().inDevNodes_main(oas_output="nodes")

