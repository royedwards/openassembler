###OpenAssembler Node python file###

'''
define
{
	name getDevelopmentCopy
	tags opsw
	input string Development "" ""
	input string Version "latest" ""
	input string Type "Software" ""
	output dbPath result "" ""

}
'''
import os, sys,shutil,errno
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getLatestVersion import getLatestVersion

class getDevelopmentCopy(opdb_setup,getElementType,getVaultPath,getLatestVersion):
   def getDevelopmentCopy_main(self, **connections):
	Development=connections["Development"]
	Version=connections["Version"]
	Type=connections["Type"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			if Type=="Software":
				dpath=devROOT+"/"+Development+"_dev"
				pref_path=":Software:"
			elif Type=="Nodes":
				dpath=devROOT+"/OpenNodes/"+Development+""
				pref_path=":OpenNodes:"
			else:
				return 0
			try:
				shutil.rmtree(dpath)
			except:
				pass
			if os.path.isdir(devROOT+"/OpenNodes/"):
				pass
			else:
				os.makedirs(devROOT+"/OpenNodes/")
			if os.path.isfile(devROOT+"/OpenNodes/__init__.py"):
				pass
			else:
				ini="__all__=[]"
				fl=open(devROOT+"/OpenNodes/__init__.py","w")
				fl.write(ini)
				fl.close()
			if self.getElementType_main(Path=pref_path+str(Development))==0:
				return 0
			vpath=self.getVaultPath_main(Path=pref_path+str(Development)+"@"+Version)
			if os.path.isdir(vpath):
				pass
			else:
				return 0
			self.copyfromVault(vpath,dpath,Type,Version,devROOT)

			self.createBaseversion(dpath,Version)

			return pref_path+str(Development)+"@"+Version
	else:
		return 0

   def createBaseversion(self,path, version):
		fl=open(path+"/baseVersion.atr","w")
		fl.write(str(version)+"\n")
		fl.close()

   def copyfromVault(self,VaultPath,DevPath,Type,Version,devROOT):
		shutil.copytree(VaultPath+"/dev/",DevPath)
		self.createBaseversion(DevPath, Version)

		prelist=self.getIncludesList(DevPath)
		for pr in prelist:
			if self.getElementType_main(Path=pr[1])!=0:
					if pr[1].find(":Software:")>0:
						tp="Software"
					else:
						tp="Nodes"
					if os.name=="nt":
						shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",DevPath+"/"+pr[0])
						verss=self.getLatestVersion_main(Path=pr[1])
						self.createBaseversion(DevPath+"/"+pr[0], verss)
					else:
						if tp=="Nodes":
							if os.path.isdir(devROOT+"/OpenNodes/"+pr[0]+"") or os.path.isdir(devROOT+"/"+pr[0]+"_dev"):
								pass
							else:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",devROOT+"/OpenNodes/"+pr[0]+"")
								verss=self.getLatestVersion_main(Path=pr[1])
								self.createBaseversion(devROOT+"/OpenNodes/"+pr[0]+"", verss)
							try:
								os.symlink(devROOT+"/OpenNodes/"+pr[0]+"",DevPath+"/"+pr[0])
							except:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",DevPath+"/"+pr[0])
								verss=self.getLatestVersion_main(Path=pr[1])
								self.createBaseversion(DevPath+"/"+pr[0], verss)
						elif tp=="Software":
							if os.path.isdir(devROOT+"/OpenNodes/"+pr[0]+"") or os.path.isdir(devROOT+"/"+pr[0]+"_dev"):
								pass
							else:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",devROOT+"/"+pr[0]+"_dev")
								verss=self.getLatestVersion_main(Path=pr[1])
								self.createBaseversion(devROOT+"/"+pr[0]+"_dev", verss)
							try:
								os.symlink(devROOT+"/"+pr[0]+"_dev",DevPath+"/"+pr[0])
							except:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",DevPath+"/"+pr[0])
								verss=self.getLatestVersion_main(Path=pr[1])
								self.createBaseversion(DevPath+"/"+pr[0], verss)
			else:
				return 0

   def getIncludesList(self,path):
		retlist=[]
		if os.path.isfile(path+"/includes.atr"):
			fl=open(path+"/includes.atr","r")
			readed=str(fl.read()).strip().lstrip()
			fl.close()
			if readed!="":
				lines=readed.split("\n")
				for line in lines:
					folding=str(line).split()[0]
					dentry=str(line).split()[1]
					retlist.append((folding,dentry))
		return retlist

if __name__ == "__main__":
	print getDevelopmentCopy().getDevelopmentCopy_main(Development="OpenProjectAdministrator",Version="v001",Type="Software",oas_output="result")
 