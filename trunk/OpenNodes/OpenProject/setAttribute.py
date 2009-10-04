###OpenAssembler Node python file###

'''
define
{
	name setAttribute
	tags opdb
	input dbPath Path "" ""
	input any Value "" ""
	output int result "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class setAttribute(opdb_setup):
   def setAttribute_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Value=connections["Value"]
	except:
		Value=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			
			Path=ProjectROOT+Path.replace(":","/").replace(".","/")+".atr"
			pf=open(Path,"w")
			pf.write(Value)
			pf.close()
			return 1
		except:
			return 0
			
	else:
		return 0
		
