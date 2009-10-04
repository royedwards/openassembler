###OpenAssembler Node python file###

'''
define
{
	name buildWindowsNT
	tags opsw
	input file Folder "" ""
	output int result "" ""

}
'''
import os, sys,shutil
if os.name=="nt":
    import win32api

class buildWindowsNT():
   def buildWindowsNT_main(self, **connections):
	Folder=connections["Folder"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			os.chdir(Folder)
			Folder=win32api.GetShortPathName(Folder)
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
		os.system("python "+str(folder+"\\"+setupfile))
		shutil.rmtree(folder+"\\build")

   def generate_setup(self,path,executeablename):
	content='''from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")

setup( options = {"py2exe": {"compressed": 1, "optimize": 2, "ascii": 1, "bundle_files": 1,"includes":"sip"}},
       zipfile = None,
       console = [{"script": \''''
	content+=str(executeablename)+"\'}])\n"
	fl=open(path+"\\setup_win_"+str(executeablename)+".py","w")
	fl.write(content)
	fl.close()
	self.runSetup(path, "setup_win_"+str(executeablename)+".py")


   def getExeces(self,path):
		fl = open(str(path)+"\\executeable.atr","r")
		rd=fl.read()
		fl.close()
		rd=rd.strip().lstrip()
		retlist=[]
		for lines in rd.split("\n"):
			retlist.append(str(lines.strip().lstrip()))
		return retlist

if __name__ == "__main__":
	print buildWindowsNT().buildWindowsNT_main(Folder=os.getenv('USERPROFILE')+"/tmp_opentools/OpenProjectBrowser_dev" ,oas_output="result")
 