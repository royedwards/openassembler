###OpenAssembler Node python file###

'''
define
{
	name publishWindowsNT
	tags opsw
	input string Software "" ""
	input string Version "" ""
	input file BuildFolder "" ""
	output int result "" ""

}
'''
import os, sys,shutil
from OpenProject.getVaultPath import getVaultPath

class publishWindowsNT(getVaultPath):
   def publishWindowsNT_main(self, **connections):
	Software=connections["Software"]
	Version=connections["Version"]
	BuildFolder=connections["BuildFolder"]
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			vpath=self.getVaultPath_main(Path=":Software:"+str(Software)+"@"+str(Version))
			if os.path.isdir(vpath+"/bin/win"):
				if len(os.listdir(vpath+"/bin/win"))>0:
					return 0
				else:
					if os.path.isdir(BuildFolder):
						shutil.rmtree(vpath+"/bin/win")
						shutil.copytree(str(BuildFolder)+"/dist/",vpath+"/bin/win")
			return 1
		except:
			return 0	
	else:
		return 0