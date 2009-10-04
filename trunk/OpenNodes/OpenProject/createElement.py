###OpenAssembler Node python file###

'''
define
{
	name createElement
	tags opdb
	input dbPath Path "" ""
	input string Type "container" ""
	input string Name "" ""
	output int result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from getElementType import getElementType
from createProject import createProject
from getElementList import getElementList

class createElement(opdb_setup,getElementType,createProject,getElementList):
   def createElement_main(self, **connections):

	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Type=connections["Type"]
	except:
		Type=""
	try:
		Name=connections["Name"]
	except:
		Name=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			path_type=self.getElementType_main(Path=Path)
			existing_elements=self.getElementList_main(Path=Path)
			for le in existing_elements:
				if str(le) == str(Name):
					return 0
			if path_type=="projectRoot":
				return 0
				
			if Type == "attribute":
				if path_type=="attribute" or path_type=="version":
					print "This is not allowed to create an attribute on an attribute."
					return 0
				else:
					if os.path.isdir(ProjectROOT+str(Path.replace(":","/"))):
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/"+str(Name)+".atr","w")
						pf.write("")
						pf.close()
					else:
						print "The path is wrong in the createElement call."
						return 0
						
			elif Type == "container":
				if path_type=="attribute" or path_type=="item" or path_type=="version":
					print "This is not allowed to create this element in this type of element."
					return 0
				elif path_type=="container":
					if os.path.isdir(ProjectROOT+str(Path.replace(":","/"))):
						os.makedirs(ProjectROOT+str(Path.replace(":","/"))+"/"+str(Name))
						os.makedirs(VaultROOT+str(Path.replace(":","/"))+"/"+str(Name))
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/"+str(Name)+"/elements.atr","w")
						pf.write("")
						pf.close()

						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/elements.atr","r")
						re=pf.read()
						pf.close()
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/elements.atr","w")
						re=re.lstrip().strip()+"\n"+str(Name)
						pf.write(str(re))
						pf.close()
					else:
						print "The path is wrong in the createElement call."
						return 0
				elif path_type=="projectRoot":
					self.createProject_main(name=Name)
				
			elif Type == "item":
				if path_type=="attribute" or path_type=="item" or path_type=="version":
					print "This is not allowed to create this element in this type of element."
					return 0
				else:
					if os.path.isdir(ProjectROOT+str(Path.replace(":","/"))):
						os.makedirs(ProjectROOT+str(Path.replace(":","/"))+"/"+str(Name))
						os.makedirs(VaultROOT+str(Path.replace(":","/"))+"/"+str(Name))
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/"+str(Name)+"/versions.atr","w")
						pf.write("")
						pf.close()
						
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/elements.atr","r")
						re=pf.read()
						pf.close()
						pf=open(ProjectROOT+str(Path.replace(":","/"))+"/elements.atr","w")
						re=re.lstrip().strip()+"\n"+str(Name)
						pf.write(str(re))
						pf.close()
					else:
						print "The path is wrong in the createElement call."
						return 0
		
			return 1
		except:
			return 0
			
	else:
		return 0
		
