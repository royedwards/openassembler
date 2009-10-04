###OpenAssembler Node python file###

'''
define
{
	name uninstallSoftware
	tags opsw
	input dbPath Path "" ""
	output int result "" ""

}
'''
import os, sys,shutil,platform
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getNameFromPath import getNameFromPath
from OpenProject.getVersionFromPath import getVersionFromPath
from OpenProject.getCleanPath import getCleanPath

class uninstallSoftware(getVaultPath,getNameFromPath,getVersionFromPath,getCleanPath):
   def uninstallSoftware_main(self, **connections):
	Path=connections["Path"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":

			name=self.getNameFromPath_main(Path=Path)
			to_path="/opt/OpenTools"
			if platform.system()=="Windows":
				to_path="C:/OpenTools"

			if os.path.isdir(to_path+"/bin/"+name):
				shutil.rmtree(to_path+"/bin/"+name)

			vpath=self.getVaultPath_main(Path=Path)
			exc=self.getExeces(vpath+"/dev")
			for ex in exc:
				if platform.system()=="Linux":
					try:
						os.remove("/usr/bin/"+ex)
					except:
						pass

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

			text=""
			for rrr in rew:
				if str(self.getCleanPath_main(Path=Path))==str(self.getCleanPath_main(Path=rrr)):
					pass
				else:
					text+=rrr+"\n"


			fl=open(to_path+"/installed.atr","w")
			fl.write(text)
			fl.close()


			return 1

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


if __name__ == "__main__":
	print uninstallSoftware().uninstallSoftware_main(Path=":Software:OpenTextEditor",oas_output="result")
 