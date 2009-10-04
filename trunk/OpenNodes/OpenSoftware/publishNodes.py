###OpenAssembler Node python file###

'''
define
{
	name publishNodes
	tags opsw
	input string Nodes "" ""
	input string Comment "" ""
	output string version "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.createNewVersion import createNewVersion
from OpenProject.createElement import createElement

class publishNodes(opdb_setup,getElementType,createNewVersion,createElement):
   def publishNodes_main(self, **connections):
	Nodes=connections["Nodes"]
	Comment=connections["Comment"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="version"
	if oas_output=="version":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			type=self.getElementType_main(Path=":OpenNodes:"+str(Nodes))
			Nodes=str(Nodes)
			if type!="item":
				r=self.createElement_main(Path=":OpenNodes",Type="item",Name=str(Nodes))
				if r==0:
					return 0
			newversion=self.createNewVersion_main(Path=":OpenNodes:"+str(Nodes),ReviewType="Software",Comment=Comment)
			try:
				#os.makedirs(VaultROOT+"/OpenNodes/"+str(Nodes)+"/"+str(newversion)+"/dev")
				os.makedirs(VaultROOT+"/OpenNodes/"+str(Nodes)+"/"+str(newversion)+"/patch")
			except:
				return 0
			self.cleanFiles(str(devROOT+"/OpenNodes/"+str(Nodes)+""))
			self.checkImportantFiles(Nodes,devROOT)
			self.copyToVault(Nodes,devROOT,VaultROOT,newversion)
			self.createBaseversion(newversion,Nodes,devROOT)
			return newversion
		except:
			return 0	
	else:
		return 0
   def createBaseversion(self,newversion,Nodes,devROOT):
		fl=open(devROOT+"/OpenNodes/"+str(Nodes)+"/baseVersion.atr","w")
		fl.write(str(newversion)+"\n")
		fl.close()

   def copyToVault(self,Nodes,devROOT,VaultROOT,newversion):
		ignorelist=[]
		prelist=self.getIncludesList(Nodes,devROOT)
		for i in prelist:
			ignorelist.append(i[0])	
		shutil.copytree(str(devROOT+"/OpenNodes/"+Nodes+""),str(VaultROOT+"/OpenNodes/"+Nodes+"/"+newversion+"/dev/"))
		for f in ignorelist:
			shutil.rmtree(str(VaultROOT+"/OpenNodes/"+Nodes+"/"+newversion+"/dev/"+str(f)+"/"))


   def getIncludesList(self,Nodes,devROOT):
		retlist=[]
		if os.path.isfile(devROOT+"/OpenNodes/"+Nodes+"/includes.atr"):
			fl=open(devROOT+"/OpenNodes/"+Nodes+"/includes.atr","r")
			readed=str(fl.read()).strip().lstrip()
			fl.close()
			if readed!="":
				lines=readed.split("\n")
				for line in lines:
					folding=str(line).split()[0]
					dentry=str(line).split()[1]
					retlist.append((folding,dentry))
		return retlist

   def checkImportantFiles(self,Nodes,devROOT):

		if os.path.isfile(devROOT+"/OpenNodes/"+Nodes+"/includes.atr"):
			pass
		else:
			fl=open(devROOT+"/OpenNodes/"+Nodes+"/includes.atr","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/OpenNodes/"+Nodes+"/CHANGELOG"):
			pass
		else:
			fl=open(devROOT+"/OpenNodes/"+Nodes+"/CHANGELOG","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/OpenNodes/"+Nodes+"/README"):
			pass
		else:
			fl=open(devROOT+"/OpenNodes/"+Nodes+"/README","w")
			fl.write("")
			fl.close()

   def cleanFiles(self,folder):
		if os.path.isdir(folder):
			content=os.listdir(folder)
			for con in content:
				if os.path.isdir(folder+"/"+con):
					self.cleanFiles(folder+"/"+con)
				elif os.path.isfile(folder+"/"+con):
					if con[-4:]==".pyc" or con[-4:]==".pyo" or con=="baseVersion.atr":
						os.remove(folder+"/"+con)
					if con[:1]==".":
						os.remove(folder+"/"+con)

if __name__ == "__main__":
	print publishNodes().publishNodes_main(Nodes="OpenProject",oas_output="version")
 