###OpenAssembler Node python file###

'''
define
{
	name deleteProject
	tags opdb
	input string Project "" ""
	input string User "" ""
	output int result "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup
from getElementType import getElementType
from getProjects import getProjects
from getElementList import getElementList
from time import time, localtime, strftime
from checkLogPath import checkLogPath

class deleteProject(opdb_setup,getElementType,getProjects,getElementList,checkLogPath):
   def deleteProject_main(self, **connections):

	try:
		Project=connections["Project"]
	except:
		Project=""
	try:
		User=connections["User"]
	except:
		User=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"


	if oas_output=="result":
		try:
			self.ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			type=self.getElementType_main(Project)
			self.timerec=strftime("%Y%b%d_%H%M%S", localtime())
			cuser=""
			if os.name=="nt":
				cuser=os.environ.get("USERNAME")
			else:	
				cuser=os.environ.get("USER")

			if Project!="":
					pr=Project
					if int(self.checkLogPath_main(logSystemPath=self.AdminROOT+"/common/project_delete_list.atr",Path=":"+Project))==int(1):
						pass
					else:
						fl=open(self.AdminROOT+"/common/project_delete_list.atr","r")
						rea=fl.read()
						fl.close()
															
						tolog=rea.strip().lstrip()+"\n"+str(":"+Project)+"   "+cuser+"   "+str(self.timerec)+"   "+"Do not delete project, just in case you know what are you doing!!!!!!!"+"\n"
						
						fl=open(self.AdminROOT+"/common/project_delete_list.atr","w")
						fl.write(tolog)
						fl.close()	
			
					pre=self.getProjects_main()
					saved=""
					for p in pre:
						if p==Project:
							pass
						else:
							saved+="\n"+p
					pf=open(self.ProjectROOT+"/projects.atr","w")
					pf.write(saved)
					pf.close()
			
			
			else:
				pass
						
			return 1
		except:
			return 0
			
	else:
		return 0

	