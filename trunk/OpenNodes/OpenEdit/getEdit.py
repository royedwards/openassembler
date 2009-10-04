###OpenAssembler Node python file###

'''
define
{
	name getEdit
	tags oped
	input string Project "" ""
	input string Version "" ""
	output multyEdit edit "" ""

}
'''
import os, sys, platform
from OpenProject.getVaultPath import getVaultPath

class getEdit(getVaultPath):
   def getEdit_main(self, **connections):

	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Version=connections["Version"]
	except:
	    Version="live"
	try: 
	    oas_output=connection["oas_output"]
	except:
	    oas_output="edit"
	
	if oas_output=="edit":
		try:
			ret=[]
			Path=str(self.getVaultPath_main(Path=":"+str(Project)+":Story:Edit@"+str(Version)))
			if Path=="" or Path==0:
				return 0
			Path+="/edit.atr"
			pf=open(Path,"r")
			readed=pf.read()
			pf.close()
			readed=readed.strip()
			for lines in readed.split("\n"):
				sh_order=str(lines.split(" | ")[0].strip().lstrip())
				sh_name=str(lines.split(" | ")[1].strip().lstrip())
				sh_state=str(lines.split(" | ")[2].strip().lstrip())
				sh_track=str(lines.split(" | ")[3].strip().lstrip())
				sh_in=str(lines.split(" | ")[4].strip().lstrip())
				sh_out=str(lines.split(" | ")[5].strip().lstrip())
				sh_start=str(lines.split(" | ")[6].strip().lstrip())
				sh_end=str(lines.split(" | ")[7].strip().lstrip())
				ret.append([sh_order, {"name":sh_name, "state":sh_state, "track":sh_track, "inpoint":sh_in, "outpoint":sh_out,"startframe": sh_start,"endframe": sh_end}])
			return ret
		except:
			return 0
			
	else:
		return 0
