###OpenAssembler Node python file###

'''
define
{
	name integrityChecker
	tags opdb
	input dbPath Path "" ""
	output int result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from  getElementType import getElementType
from getProjects import getProjects
from createElement import createElement
from time import time, localtime, strftime
from getElementList import getElementList
from getVersionList import getVersionList
from checkLogPath import checkLogPath
from writeIntegrityPanic import writeIntegrityPanic
from createProject import createProject

class integrityChecker(opdb_setup,getElementType,getProjects,createElement,getElementList,getVersionList,checkLogPath,writeIntegrityPanic,createProject):

   def create_log(self,Path,logdescription):
	logfile=""
	if self.getElementType_main(Path=Path)=="projectRoot":
		logfile=self.AdminROOT+"/common/integrity_logs/"+str(self.timerec)+".log"
	elif self.getElementType_main(Path=Path)!="":
		pr=Path.split(":")[1]
		logfile=self.AdminROOT+"/"+pr+"/integrity_logs/"+str(self.timerec)+".log"
	else:
		pass
		
	if logfile!="":
		if os.path.isfile(logfile):
			fl=open(logfile,"r")
			rea=fl.read()
			fl.close()
			
			tolog=rea.strip().lstrip()+"\n"+str(Path)+"   "+logdescription+"\n"
			
			fl=open(logfile,"w")
			fl.write(tolog)
			fl.close()
		else:
			tolog=str(Path)+"   "+logdescription+"\n"
			
			fl=open(logfile,"w")
			fl.write(tolog)
			fl.close()			

   def checker_loop(self,Path):
	print Path
	path_type=self.getElementType_main(Path=Path)
	if path_type=="projectRoot":
		pre=self.getProjects_main()
		p_c=os.listdir(self.ProjectROOT+Path.replace(":","/"))
		p_d=[]
		for p_ in p_c:
			if os.path.isdir(self.ProjectROOT+Path.replace(":","/")+str(p_)):
				p_d.append(p_)
		
		filestodelete=[]
		for pp in p_c:
			if os.path.isfile(self.ProjectROOT+"/"+str(pp)):
				if pp=="elements.atr" or pp=="versions.atr":
					filestodelete.append(pp)
					
		if len(filestodelete) > 0:
			for flss in filestodelete:
				os.remove(self.ProjectROOT+"/"+flss)
				self.create_log(Path,"Project root was cleaned from failing .atr files.")
		
		duplchk={}
		for i in pre:
			duplchk[i]=pre.count(i)
		ccc=0
		for i in duplchk.keys():
			if int(duplchk[i]) > 1:
				ccc=1
			else:
				pass
		if ccc==1:
			ret_solve=""
			for elem in duplchk.keys():
				ret_solve+=elem+"\n"
			#-------------------------here we solve the duplicated entries problem
			fi=open(self.ProjectROOT+"/projects.atr","w")
			fi.write(ret_solve)
			fi.close()
			pre=self.getProjects_main()
			self.create_log(Path,"There was duplicated entries in the elementdescription file, so I recreated them.")
				
		
		for prr in pre:
			#------------- solving the case of the registrad folder without a type definition file
			if os.path.isdir(self.ProjectROOT+"/"+prr):
				if self.getElementType_main(Path=Path+prr)=="":
					ff=open(self.ProjectROOT+"/"+prr+"/elements.atr","w")
					ff.write("")
					ff.close()
					self.create_log(Path,"This was a registred empty folder: "+str(":"+prr)+" now it is a container.")
				else: 
					pass
		
		if set(pre) == set(p_d):
			pass
				
		else:
			p_mr=list(set(pre).difference(set(p_d))) #tobb a bejegyzes mint kene
			p_md=list(set(p_d).difference(set(pre))) #tobb a konyvtar mint kene

			if len(p_md) > 0:
				for di in p_md:
					if self.getElementType_main(Path=Path+di)=="":
						
						if len(os.listdir(self.ProjectROOT+"/"+di)) < 1:
							#-----------------------we solved the empty folder case..........
							os.rmdir(self.ProjectROOT+"/"+di)
							self.create_log(Path,"Empty folder was deleted: "+str(":"+di))
						else:	
							#-------------------------------------------here we solve the problem when we found a directory without any element entry and we do not even know its type
							self.writeIntegrityPanic_main(Path=Path,Problem=di,Description="I can not categorize this folder: "+di+" at the end of the path, please take care about it.")
							self.create_log(Path,"User action is needed for: "+str(":"+di))
						
					elif self.getElementType_main(Path=Path+di)=="item" or self.getElementType_main(Path=Path+di)=="container":
						
						#---------------------------------herer we solve the case with the folders which are for delete

						if int(self.checkLogPath_main(logSystemPath=self.AdminROOT+"/common/project_delete_list.atr",Path=Path+str(di)))==int(1):
							pass
						else:

							fl=open(self.AdminROOT+"/common/project_delete_list.atr","r")
							rea=fl.read()
							fl.close()
							
							tolog=rea.strip().lstrip()+"\n"+str(Path+di)+"   integrityCheck   "+str(self.timerec)+"   integrityCheck automatically placed this item to the delelte list.\n"
					
							fl=open(self.AdminROOT+"/common/project_delete_list.atr","w")
							fl.write(tolog)
							fl.close()	
							self.create_log(Path,"Delete request was placed for: "+str(":"+di))
			
			if len(p_mr) > 0:
				for el in p_mr:
					#--------------------here we solve the problem when there is more items in a project.art file, and we create containers for it.
					#os.makedirs(self.ProjectROOT+Path.replace(":","/")+str(el))
					#pf=open(self.ProjectROOT+str(Path.replace(":","/"))+"/"+str(el)+"/elements.atr","w")
					#pf.write("")
					#pf.close()
					self.createProject_main(str(el))
					self.create_log(Path,"Project: "+str(el)+" created.")
		
	
		for em in pre:
			self.checker_loop(":"+em)
		
		#ve=self.getVersionList_main(Path)
		#if len(ve)>0:
		#	for v in self.getVersionList_main(Path):
		#		self.checker_loop(Path+"@"+v[0])
	
	elif path_type=="container" or path_type=="item":
		pre=self.getElementList_main(Path=Path)
		p_c=os.listdir(self.ProjectROOT+Path.replace(":","/"))
		p_d=[]
		for p_ in p_c:
			if os.path.isdir(self.ProjectROOT+Path.replace(":","/")+"/"+str(p_)):
				p_d.append(p_)
		duplchk={}
		for i in pre:
			duplchk[i]=pre.count(i)
		ccc=0
		
		for i in duplchk.keys():
			if int(duplchk[i]) > 1:
				ccc=1
			else:
				pass
		if ccc==1:
			ret_solve=""
			for elem in duplchk.keys():
				ret_solve+=elem+"\n"
			#-------------------------here we solve the duplicated entries problem
			fi=open(self.ProjectROOT+Path.replace(":","/")+"/elements.atr","w")
			fi.write(ret_solve)
			fi.close()
			pre=self.getProjects_main()
			self.create_log(Path,"There was duplicated entries in the elementdescription file, so I recreated them.")
			
		for prr in pre:
			#------------- solving the case of the registred folder without a type definition file
			if os.path.isdir(self.ProjectROOT+Path.replace(":","/")+"/"+prr):
				if self.getElementType_main(Path=Path+":"+prr)=="":
					ff=open(self.ProjectROOT+Path.replace(":","/")+"/"+prr+"/elements.atr","w")
					ff.write("")
					ff.close()
					self.create_log(Path,"This was a registred empty folder: "+str(Path+":"+prr)+" now it is a container.")
				else: 
					pass
		
		if set(pre) == set(p_d):
			pass
		
		else:
			p_mr=list(set(pre).difference(set(p_d))) #tobb a bejegyzes mint kene
			p_md=list(set(p_d).difference(set(pre))) #tobb a konyvtar mint kene
			if len(p_md) > 0:
				for di in p_md:
					
					if self.getElementType_main(Path=Path+":"+di)=="":
						if len(os.listdir(self.ProjectROOT+Path.replace(":","/")+"/"+di)) < 1:
							#-----------------------we solved the empty folder case..........
							os.rmdir(self.ProjectROOT+Path.replace(":","/")+"/"+di)
							self.create_log(Path,"Empty folder was deleted: "+str(Path+":"+di))
						else:	
							#-------------------------------------------here we solve the problem when we found a directory without any element entry and we do not even know its type
							self.writeIntegrityPanic_main(Path=Path,Problem=di,Description=("I can not categorize this folder: "+di+" at the end of the path, please take care about it."))
							self.create_log(Path,"User action is needed for: "+str(Path+":"+di))
						
					elif self.getElementType_main(Path=Path+":"+di)=="item" or self.getElementType_main(Path=Path+":"+di)=="container":
						
						#---------------------------------herer we solve the case with the folders which are for delete

						if int(self.checkLogPath_main(logSystemPath=self.AdminROOT+"/"+self.getp(Path)+"/delete_list.atr",Path=Path+":"+str(di)))==int(1):
							pass
						else:

							fl=open(self.AdminROOT+"/"+self.getp(Path)+"/delete_list.atr","r")
							rea=fl.read()
							fl.close()
							
							tolog=rea.strip().lstrip()+"\n"+str(Path+":"+di)+"   integrityCheck   "+str(self.timerec)+"   integrityCheck automatically placed this item to the delelte list.\n"
					
							fl=open(self.AdminROOT+"/"+self.getp(Path)+"/delete_list.atr","w")
							fl.write(tolog)
							fl.close()	
							self.create_log(Path,"Delete request was placed for: "+str(Path+":"+di))
			
			if len(p_mr) > 0:
				for el in p_mr:
					#--------------------here we solve the problem when there is more items in a element.art file, and we create containers for it.
					os.makedirs(self.ProjectROOT+Path.replace(":","/")+"/"+str(el))
					pf=open(self.ProjectROOT+str(Path.replace(":","/"))+"/"+str(el)+"/elements.atr","w")
					pf.write("")
					pf.close()
					self.create_log(Path,"Container: "+str(el)+" created.")
		
	
		if path_type=="item":
			vers=self.getVersionList_main(Path=Path)
			if len(vers) > 0:
				for ww in vers:
					vw=ww[0]
					if os.path.isdir(self.VaultROOT+"/"+Path.replace(":","/")+"/"+vw):
						pass
					else:
						os.makedirs(self.VaultROOT+"/"+Path.replace(":","/")+"/"+vw)
						self.create_log(Path,"Version folder was created in the vaults: @"+str(vw))
			else:
				if os.path.isdir(self.VaultROOT+"/"+Path.replace(":","/")):
					pass
				else:
					os.makedirs(self.VaultROOT+"/"+Path.replace(":","/"))
					self.create_log(Path,"Item folder was created in the Vault.")
		for em in pre:
			self.checker_loop(Path+":"+em)
		
		#ve=self.getVersionList_main(Path)
		#if len(ve)>0:
		#	for v in self.getVersionList_main(Path):
		#		self.checker_loop(Path+"@"+v[0])
			
	elif path_type=="version":
		pass
		
		
	elif path_type=="attribute":
		pass
			
   def getp(self,path):
	return path.split(":")[1]	
	
   def integrityChecker_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		self.getElementType_main(Path=Path)
		try:
			
			self.ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			self.VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			
			self.timerec=strftime("%Y%b%d_%H%M%S", localtime())


			self.checker_loop(Path)

			return 1
		except:
			return 0
			
	else:
		return 0


if __name__ == "__main__":
	integrityChecker().integrityChecker_main(Path=":",oas_output="result")
 
