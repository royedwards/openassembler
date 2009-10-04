###OpenAssembler Node python file###

'''
define
{
	name buildPosixLinux
	tags opsw
	input file Folder "" ""
	output int result "" ""

}
'''
import os, sys,shutil

class buildPosixLinux():
   def buildPosixLinux_main(self, **connections):
	Folder=connections["Folder"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			os.chdir(Folder)
			ec=self.getExeces(Folder)

			for e in ec:
				self.generate_setup(Folder,e)
			return 1
		except:
			return 0	
	else:
		return 0

   def runSetup(self,folder, setupfile):
		os.chdir(folder)
		os.system("python "+str(folder+"/"+setupfile))

   def generate_setup(self,path,executeablename):
	content='''from cx_Freeze import setup, Executable
import sys

if len(sys.argv) == 1:
    sys.argv.append("build_exe")

setup( options = {"build_exe": {"compressed": 1, "optimize": 2,"includes":"sip"}}, executables = [Executable(\"'''
	content+=str(executeablename)+"\")])\n"
	fl=open(path+"/setup_lin_"+str(executeablename)+".py","w")
	fl.write(content)
	fl.close()
	self.runSetup(path, "setup_lin_"+str(executeablename)+".py")
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
	print buildPosixLinux().buildPosixLinux_main(Folder=os.getenv('USERPROFILE')+"/tmp_opentools/OpenProjectBrowser_dev" ,oas_output="result")
 