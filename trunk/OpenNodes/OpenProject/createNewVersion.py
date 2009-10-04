###OpenAssembler Node python file###

'''
define
{
	name createNewVersion
	tags opdb
	input dbPath Path "" ""
	input string ReviewType "" ""
	input string Comment "" ""
	output string version "" ""

}
'''

import os, sys,time
from Setup import opdb_setup
from getElementType import getElementType
from getLatestVersion import getLatestVersion

class createNewVersion(opdb_setup,getElementType,getLatestVersion):
   def createNewVersion_main(self, **connections):

	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		version=connections["version"]
	except:
		version=""
	try:
		ReviewType=connections["ReviewType"]
	except:
		ReviewType="unknown"
	try:
		Comment=connections["Comment"]
	except:
		Comment="empty"
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="version"
	if oas_output=="version":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			path_type=self.getElementType_main(Path=Path)
			newversion=""
			if path_type!="item":
				return 0

			try:
				latestversion=self.getLatestVersion_main(Path=Path)
			except:
				latestversion="v000"
			if str(latestversion)==str(0):
				latestversion="v000"
			
			newversion="v"+str(int(str(latestversion)[1:])+1).zfill(3)
			fl=open(ProjectROOT+"/"+Path.replace(":","/")+"/versions.atr","r")
			vfile=fl.read()
			fl.close()
			cuser=""
			if os.name=="nt":
				cuser=os.environ.get("USERNAME")
			else:	
				cuser=os.environ.get("USER")

			vfile=vfile.strip().lstrip()+"\n"+newversion+" \"\" \""+str(cuser)+"\"\n"

			fl=open(ProjectROOT+"/"+Path.replace(":","/")+"/versions.atr","w")
			fl.write(vfile)
			fl.close()

			os.makedirs(VaultROOT+str(Path.replace(":","/"))+"/"+str(newversion))

			if ReviewType=="unknown":
				pass
			else:
				aroot=""
				if Path.count(":")>1:
					project=Path.split(":")[1]
					aroot=AdminROOT+"/"+str(project)+"/Review/"+str(ReviewType)
					if os.path.isdir(aroot):
						pass
					else:
						os.makedirs(aroot)

					sp=aroot+"/newsubmissionspath.atr"
					if os.path.isfile(sp):
						fl=open(sp,"r")
						redd=fl.read()
						fl.close()
						reddlist=redd.strip().split("\n")
						chk=0
						for item in reddlist:
							if str(item).strip()==str(Path):
								chk=1
						if chk==1:
							pass
						else:
							redd=str(redd).strip()+"\n"+str(Path)+"\n"
							fl=open(sp,"w")
							fl.write(redd)
							fl.close()

					else:
						redd=str(Path)+"\n"
						fl=open(sp,"w")
						fl.write(redd)
						fl.close()

					ltime=time.strftime("%Y%m%d%H%M%S",time.gmtime())
					tet=str(Path)+"@"+str(newversion)+"\n"+str(Comment)

					tet=str(Path)+"@"+str(newversion)+" | "+str(cuser)+" | "+str(ltime) + "\n"+str(Comment)
					fl=open(VaultROOT+str(Path.replace(":","/"))+"/"+str(newversion)+"/submissioncomment.atr","w")
					fl.write(tet)
					fl.close()
					
				else:
					pass
			return newversion
		except:
			return 0
			
	else:
		return 0
		

if __name__ == "__main__":
	print createNewVersion().createNewVersion_main(Path=":sandbox:sanditem",oas_output="version")
 