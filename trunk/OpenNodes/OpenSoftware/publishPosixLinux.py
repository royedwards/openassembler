###OpenAssembler Node python file###

'''
define
{
	name publishPosixLinux
	tags opsw
	input string Software "" ""
	input string Version "" ""
	input file BuildFolder "" ""
	output int result "0" ""

}
'''
import os, sys,shutil
from OpenProject.getVaultPath import getVaultPath

class publishPosixLinux(getVaultPath):
   def publishPosixLinux_main(self, **connections):
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
			if os.path.isdir(vpath+"/bin/linux"):
				if len(os.listdir(vpath+"/bin/linux"))>0:
					return 0
				else:
					if os.path.isdir(BuildFolder):
						shutil.rmtree(vpath+"/bin/linux")
						shutil.copytree(str(BuildFolder)+"/build/exe.linux-i686-2.5/",vpath+"/bin/linux")
			return 1
		except:
			return 0	
	else:
		return 0