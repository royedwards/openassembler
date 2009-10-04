###OpenAssembler Node python file###

'''
define
{
	name deleteElement
	tags opdb
	input dbPath Path "" ""
	input string Description "" ""
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

class deleteElement(opdb_setup,getElementType,getProjects,getElementList,checkLogPath):
   def deleteElement_main(self, **connections):

	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Description=connections["Description"]
	except:
		Description=""
	try:
		User=connections["User"]
	except:
		User="USER"
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
			self.ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			type=self.getElementType_main(Path=Path)
			self.timerec=strftime("%Y%b%d_%H%M%S", localtime())
			cuser=""
			if os.name=="nt":
				cuser=os.environ.get("USERNAME")
			else:	
				cuser=os.environ.get("USER")


			if (int(Path.count(":")) > int(1)) or (int(Path.count(".")) > int(0)):
				if type=="item" or type=="container":
					pr=Path.split(":")[1]
					if int(self.checkLogPath_main(logSystemPath=self.AdminROOT+"/"+pr+"/delete_list.atr",Path=Path))==int(1):
						pass
					else:
						fl=open(self.AdminROOT+"/"+pr+"/delete_list.atr","r")
						rea=fl.read()
						fl.close()
															
						tolog=rea.strip().lstrip()+"\n"+str(Path)+"   "+cuser+"   "+str(self.timerec)+"   "+Description+"\n"
						
						fl=open(self.AdminROOT+"/"+pr+"/delete_list.atr","w")
						fl.write(tolog)
						fl.close()	
			
					pre=self.getElementList_main(self.rollback_path(Path))
						
					saved=""
					for p in pre:
						if p==Path[Path.rfind(":"):][1:]:
							pass
						else:
							saved+="\n"+p
					pf=open(self.ProjectROOT+"/"+self.rollback_path(Path).replace(":","/")+"/elements.atr","w")
					pf.write(saved)
					pf.close()
			
					
				elif type=="attribute":
					fn=Path.split(".")[0]
					ex=Path.split(".")[1]
					os.remove(ProjectROOT+"/"+fn.replace(":","/")+".atr")
			
			else:
				pass
						
			return 1
		except:
			return 0
			
	else:
		return 0


   def rollback_path(self,Path):
   	pth=str(Path)
   	if pth.find(".")>0:
   		retPath=pth.rsplit(".",1)[0]
   	elif pth.find("@")>0:
   		retPath=pth.rsplit("@",1)[0]
   	else:
   		retPath=pth.rsplit(":",1)[0]
		
   	return retPath
	 
