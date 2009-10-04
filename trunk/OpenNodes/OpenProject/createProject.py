###OpenAssembler Node python file###

'''
define
{
	name createProject
	tags opdb
	input string name "" ""
	output int result "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class createProject(opdb_setup):
   def createProject_main(self, **connections):

	try:
		name=connections["name"]
	except:
		name=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			
			pf=open(ProjectROOT+"/projects.atr","r")
			readed=pf.read()
			pf.close()
			
			pf=open(ProjectROOT+"/projects.atr","w")
			readed=readed.strip().lstrip()+"\n"+str(name)
			pf.write(readed)
			pf.close()
			
			os.makedirs(ProjectROOT+"/"+str(name))
			os.makedirs(VaultROOT+"/"+str(name))
			os.makedirs(AdminROOT+"/"+str(name))
			os.makedirs(AdminROOT+"/"+str(name)+"/integrity_logs")

			pf=open(AdminROOT+"/"+str(name)+"/delete_list.atr","w")
			pf.write("")
			pf.close()			

			pf=open(AdminROOT+"/"+str(name)+"/integrity_panic.atr","w")
			pf.write("")
			pf.close()
						
			pf=open(ProjectROOT+"/"+str(name)+"/elements.atr","w")
			pf.write("")
			pf.close()
						
			return 1
		except:
			return 0
			
	else:
		return 0
		
