###OpenAssembler Node python file###

'''
define
{
	name getUserList
	tags ocoo
	output multyUsers userlist "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getUserList(opdb_setup):
   def getUserList_main(self, **connections):

	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="userlist"
	    
	if oas_output=="userlist":
		try:
			ret=[]
			AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			path=AdminROOT+"/users/users.atr"
			fl=open(path,"r")
			readed=fl.read()
			fl.close()
			for line in readed.strip().split("\n"):
				ret.append({"username":line.split(" | ")[0].strip(), "name":line.split(" | ")[1].strip(), "email":line.split(" | ")[2].strip()})
			return ret
		except:
			return 0
			
	else:
		return 0
