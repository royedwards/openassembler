###OpenAssembler Node python file###

'''
define
{
	name getAttribute
	tags opdb
	input dbPath Path "" ""
	output string value "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getAttribute(opdb_setup):
   def getAttribute_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="value"

	if oas_output=="value":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			Path=ProjectROOT+Path.replace(":","/").replace(".","/")+".atr"
			pf=open(Path,"r")
			readed=pf.read()
			pf.close()
			return readed.strip()
		except:
			return 0
			
	else:
		return 0
