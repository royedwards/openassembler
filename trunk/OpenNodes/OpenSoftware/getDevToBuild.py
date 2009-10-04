###OpenAssembler Node python file###

'''
define
{
	name getDevToBuild
	tags opsw
	input string Development "" ""
	input string Version "latest" ""
	input file Tmp "" ""
	output int result "" ""

}
'''
import os, sys,shutil,errno
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getLatestVersion import getLatestVersion

class getDevToBuild(opdb_setup,getElementType,getVaultPath,getLatestVersion):
   def getDevToBuild_main(self, **connections):
	Development=connections["Development"]
	Version=connections["Version"]
	Tmp=connections["Tmp"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			devROOT=self.opdb_dev_settings(self.opdb_setup_read())
			dpath=Tmp+"/"+Development+"_dev"
			pref_path=":Software:"

			if os.path.isdir(dpath):
				return 0
			if self.getElementType_main(Path=pref_path+str(Development))==0:
				return 0
			vpath=self.getVaultPath_main(Path=pref_path+str(Development)+"@"+Version)
			if os.path.isdir(vpath):
				pass
			else:
				return 0
			self.copyfromVault(vpath,dpath,Version,Tmp)

			self.createBaseversion(dpath,Version)

			return 1
		except:
			return 0	
	else:
		return 0

   def createBaseversion(self,path, version):
		fl=open(path+"/baseVersion.atr","w")
		fl.write(str(version)+"\n")
		fl.close()

   def copyfromVault(self,VaultPath,DevPath,Version,Tmp):
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
						verss=self.getLatestVersion_main(pr[1])
						self.createBaseversion(DevPath+"/"+pr[0], verss)
					else:
						if tp=="Nodes":
							if os.path.isdir(Tmp+"/"+pr[0]+"_ndev") or os.path.isdir(Tmp+"/"+pr[0]+"_dev"):
								pass
							else:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",Tmp+"/OpenNodes/"+pr[0]+"")
								verss=self.getLatestVersion_main(pr[1])
								self.createBaseversion(Tmp+"/OpenNodes/"+pr[0]+"_ndev", verss)
							try:
								os.symlink(Tmp+"/"+pr[0]+"_ndev",DevPath+"/"+pr[0])
							except:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",DevPath+"/"+pr[0])
								verss=self.getLatestVersion_main(pr[1])
								self.createBaseversion(DevPath+"/"+pr[0], verss)
						elif tp=="Software":
							if os.path.isdir(Tmp+"/OpenNodes/"+pr[0]+"") or os.path.isdir(Tmp+"/"+pr[0]+"_dev"):
								pass
							else:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",Tmp+"/"+pr[0]+"_dev")
								verss=self.getLatestVersion_main(pr[1])
								self.createBaseversion(Tmp+"/"+pr[0]+"_dev", verss)
							try:
								os.symlink(Tmp+"/"+pr[0]+"_dev",DevPath+"/"+pr[0])
							except:
								shutil.copytree(self.getVaultPath_main(Path=pr[1]+"@latest")+"/dev/",DevPath+"/"+pr[0])
								verss=self.getLatestVersion_main(pr[1])
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
	print getDevToBuild().getDevToBuild_main(Development="OpenProjectAdministrator",Version="v001",Type="Software",oas_output="result")
 