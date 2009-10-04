###OpenAssembler Node python file###

'''
define
{
	name inDevelopment
	tags opsw
	output array1D softwares "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class inDevelopment(opdb_setup):
   def inDevelopment_main(self, **connections):
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="softwares"

	if oas_output=="softwares":
		try:

			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			inthedir=os.listdir(devROOT)
			ret=[]
			for itms in inthedir:
				if os.path.isdir(devROOT+"/"+itms):
					if itms[-4:]=="_dev":
						ret.append(itms[:-4])
			return ret
		except:
			return 0
			
	else:
		return 0

if __name__ == "__main__":
	print inDevelopment().inDevelopment_main(oas_output="softwares")

