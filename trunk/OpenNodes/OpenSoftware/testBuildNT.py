###OpenAssembler Node python file###

'''
define
{
	name testBuildNT
	tags opsw
	input file Folder "" ""
	output int result "" ""

}
'''
import os, sys,shutil
if os.name=="nt":
    import win32api

class testBuildNT():
   def testBuildNT_main(self, **connections):
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
				self.runSetup(Folder,e)
			return 1
		except:
			return 0	
	else:
		return 0

   def runSetup(self,folder, file):
		os.chdir(folder)
		os.system(str(folder+"\dist\\"+file+".exe"))
		shutil.rmtree(folder+"\\build")

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
	print testBuildNT().testBuildNT_main(Folder=os.getenv('USERPROFILE')+"/tmp_opentools/OpenProjectBrowser_dev" ,oas_output="result")
 