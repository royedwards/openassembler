###OpenAssembler Node python file###

'''
define
{
	name installSoftware
	tags opsw
	input dbPath Path "" ""
	output dbPath result "" ""

}
'''
import os, sys,shutil,platform
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getNameFromPath import getNameFromPath
from OpenProject.getVersionFromPath import getVersionFromPath
from OpenProject.getCleanPath import getCleanPath

class installSoftware(getVaultPath,getNameFromPath,getVersionFromPath,getCleanPath):
   def installSoftware_main(self, **connections):
	Path=connections["Path"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
			if Path.find("@")>-1:
				vpath=self.getVaultPath_main(Path=Path)
			else:
				Path=Path+"@live"
				vpath=self.getVaultPath_main(Path=Path)
			name=self.getNameFromPath_main(Path=Path)
			to_path="/opt/OpenTools"
			if os.name!="nt":
				from_path=vpath+"/dev"
			else:
				from_path=vpath+"/dev"
				to_path="C:/OpenTools"
			lddf=os.listdir(from_path)
			if len(lddf)<1:
				return 0
			if os.path.isdir(to_path+"/bin/"+name):
				shutil.rmtree(to_path+"/bin/"+name)
			try:
				shutil.copytree(from_path,to_path+"/bin/"+name)
			except:
				return 0
			vicon=os.listdir(to_path+"/bin/"+name+"/Icons")
			for vi in vicon:
				try:
					os.remove(to_path+"/Icons/"+vi)
				except:
					pass
				try:
					shutil.copy(to_path+"/bin/"+name+"/Icons/"+vi,to_path+"/Icons")
				except:
					pass
			exc=self.getExeces(vpath+"/dev")
			ics=self.getIncludes(vpath+"/dev")

			for incc in ics:
				shutil.copytree(str(self.getVaultPath_main(Path=":OpenNodes:"+str(incc)+"@live"))+"/dev",to_path+"/bin/"+name+"/"+str(incc))
			for ex in exc:
				if platform.system()=="Linux":
					try:
						os.remove("/usr/bin/"+ex)
					except:
						pass
					os.symlink(to_path+"/bin/"+name+"/"+ex,"/usr/bin/"+ex)
					us=os.environ.get('USER')
					os.system('chown -R '+str(us)+':users '+to_path+"/bin/"+name)
					os.system('chmod -R 755 '+to_path+"/bin/"+name)
					os.system('chmod -R 755 '+to_path+"/Icons")
					os.system('chmod -R 755 '+to_path+"/Icons")
					os.system('chmod -R 755 '+to_path+"/OpenNodes")
					os.system('chmod -R 755 '+"/usr/bin/"+ex)
			if os.path.isfile(to_path+"/installed.atr"):
				pass
			else:
				fl=open(to_path+"/installed.atr","w")
				fl.write("")
				fl.close()
			fl=open(to_path+"/installed.atr","r")
			r=fl.read()
			fl.close()

			r=r.strip().lstrip()
			rs=r.split("\n")
			rew=[]
			for ls in rs:
				tmp=ls.strip().lstrip()
				if tmp!="":
					rew.append(str(tmp))
			chk=0
			text=""
			for rrr in rew:
				if str(self.getCleanPath_main(Path=Path))==str(self.getCleanPath_main(Path=rrr)):
					text+=str(self.getCleanPath_main(Path=Path)+"@"+self.getVersionFromPath_main(Path=Path))+"\n"
					chk=1
				else:
					text+=rrr+"\n"
			if chk==0:
				text+=str(self.getCleanPath_main(Path=Path)+"@"+self.getVersionFromPath_main(Path=Path))+"\n"
			fl=open(to_path+"/installed.atr","w")
			fl.write(text)
			fl.close()

			return str(self.getCleanPath_main(Path=Path)+"@"+self.getVersionFromPath_main(Path=Path))
	else:
		return 0

   def getExeces(self,path):
		fl = open(str(path)+"/executeable.atr","r")
		rd=fl.read()
		fl.close()
		rd=rd.strip().lstrip()
		retlist=[]
		for lines in rd.split("\n"):
			retlist.append(str(lines.strip().lstrip()))
		return retlist

   def getIncludes(self,path):
		fl = open(str(path)+"/includes.atr","r")
		rd=fl.read()
		fl.close()
		rd=rd.strip().lstrip()
		retlist=[]
		for lines in rd.split("\n"):
			vale=str(lines.strip().split(" ")[0])
			if vale!="":
				retlist.append(vale)
		return retlist

if __name__ == "__main__":
	print installSoftware().installSoftware_main(Path=":Software:OpenTextEditor",oas_output="result")
 
