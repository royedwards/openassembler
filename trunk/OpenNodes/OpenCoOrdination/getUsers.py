###OpenAssembler Node python file###

'''
define
{
	name getUsers
	tags ocoo
	output array1D users "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getUsers(opdb_setup):
   def getUsers_main(self, **connections):

	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="users"
	    
	if oas_output=="users":
		try:
			ret=[]
			AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			path=AdminROOT+"/users/users.atr"
			fl=open(path,"r")
			readed=fl.read()
			fl.close()
			for line in readed.strip().split("\n"):
				ret.append(line.split(" | ")[1].strip())
			return ret
		except:
			return 0
			
	else:
		return 0
