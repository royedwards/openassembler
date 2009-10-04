###OpenAssembler Node python file###

'''
define
{
	name testPosixLinux
	tags opsw
	input file Folder "" ""
	output int result "" ""

}
'''
import os, sys,shutil

class testPosixLinux():
   def testPosixLinux_main(self, **connections):
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
				self.runSetup(Folder,e)
			return 1
		except:
			return 0	
	else:
		return 0
   def runSetup(self,folder, file):
		os.chdir(folder)
		os.system(str(folder+"/build/exe.linux-i686-2.5/"+file))

   def getExeces(self,path):
		fl = open(str(path)+"/executeable.atr","r")
		rd=fl.read()
		fl.close()
		rd=rd.strip().lstrip()
		retlist=[]
		for lines in rd.split("\n"):
			retlist.append(str(lines.strip().lstrip()))
		return retlist