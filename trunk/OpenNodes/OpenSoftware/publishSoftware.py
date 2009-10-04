###OpenAssembler Node python file###

'''
define
{
	name publishSoftware
	tags opsw
	input string Software "" ""
	input string Comment "" ""
	output string version "" ""

}
'''
import os, sys,shutil
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.createNewVersion import createNewVersion
from OpenProject.createElement import createElement

class publishSoftware(opdb_setup,getElementType,createNewVersion,createElement):
   def publishSoftware_main(self, **connections):
	Software=connections["Software"]
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
			type=self.getElementType_main(Path=":Software:"+str(Software))
			Software=str(Software)
			if type!="item":
				r=self.createElement_main(Path=":Software",Type="item",Name=str(Software))
				if r==0:
					return 0
			newversion=self.createNewVersion_main(Path=":Software:"+str(Software),ReviewType="Software",Comment=Comment)
			try:
				os.makedirs(VaultROOT+"/Software/"+str(Software)+"/"+str(newversion)+"/bin/linux")
				os.makedirs(VaultROOT+"/Software/"+str(Software)+"/"+str(newversion)+"/bin/osx")
				os.makedirs(VaultROOT+"/Software/"+str(Software)+"/"+str(newversion)+"/bin/win")
				#os.makedirs(VaultROOT+"/Software/"+str(Software)+"/"+str(newversion)+"/dev")
				os.makedirs(VaultROOT+"/Software/"+str(Software)+"/"+str(newversion)+"/patch")
			except:
				return 0

			self.cleanFiles(str(devROOT+"/"+str(Software)+"_dev"))

			self.checkImportantFiles(Software,devROOT)

			self.copyToVault(Software,devROOT,VaultROOT,newversion)

			self.createBaseversion(newversion,Software,devROOT)

			return newversion
		except:
			return 0	
	else:
		return 0
   def createBaseversion(self,newversion,Software,devROOT):
		fl=open(devROOT+"/"+str(Software)+"_dev/baseVersion.atr","w")
		fl.write(str(newversion)+"\n")
		fl.close()

   def copyToVault(self,Software,devROOT,VaultROOT,newversion):
		ignorelist=[]
		prelist=self.getIncludesList(Software,devROOT)
		for i in prelist:
			ignorelist.append(i[0])	
		shutil.copytree(str(devROOT+"/"+Software+"_dev"),str(VaultROOT+"/Software/"+Software+"/"+newversion+"/dev/"))
		for f in ignorelist:
			shutil.rmtree(str(VaultROOT+"/Software/"+Software+"/"+newversion+"/dev/"+str(f)+"/"))


   def getIncludesList(self,Software,devROOT):
		retlist=[]
		if os.path.isfile(devROOT+"/"+Software+"_dev/includes.atr"):
			fl=open(devROOT+"/"+Software+"_dev/includes.atr","r")
			readed=str(fl.read()).strip().lstrip()
			fl.close()
			if readed!="":
				lines=readed.split("\n")
				for line in lines:
					folding=str(line).split()[0]
					dentry=str(line).split()[1]
					retlist.append((folding,dentry))
		return retlist

   def checkImportantFiles(self,Software,devROOT):
		if os.path.isdir(devROOT+"/"+Software+"_dev/Icons"):
			pass
		else:
			os.makedirs(devROOT+"/"+Software+"_dev/Icons")

		if os.path.isfile(devROOT+"/"+Software+"_dev/includes.atr"):
			pass
		else:
			fl=open(devROOT+"/"+Software+"_dev/includes.atr","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/"+Software+"_dev/CHANGELOG"):
			pass
		else:
			fl=open(devROOT+"/"+Software+"_dev/CHANGELOG","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/"+Software+"_dev/README"):
			pass
		else:
			fl=open(devROOT+"/"+Software+"_dev/README","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/"+Software+"_dev/INSTALL"):
			pass
		else:
			fl=open(devROOT+"/"+Software+"_dev/INSTALL","w")
			fl.write("")
			fl.close()

		if os.path.isfile(devROOT+"/"+Software+"_dev/executeable.atr"):
			pass
		else:
			fl=open(devROOT+"/"+Software+"_dev/executeable.atr","w")
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
	print publishSoftware().publishSoftware_main(Software="OpenProjectAdministrator",oas_output="version")
 