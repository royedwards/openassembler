###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name getRenderFolder
	tags apes
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Pass "" ""
	input string RenderVersion "" ""
	input string Type "Render" ""
	input string CacheParameter "" ""
	input string CacheNode "" ""
	output Path renderPath "" ""
}
'''
import os,sys
from DigitalApes.reformatApesProjectName import reformatApesProjectName

class getRenderFolder:
   def getRenderFolder_main(self,**connections):
	try:
		Project=str(connections["Project"])
	except:
		Project=""
	try:
		Sequence=str(connections["Sequence"])
	except:
		Sequence=""
	try:
		Shot=str(connections["Shot"])
	except:
		Shot=""
	try:
		Pass=str(connections["Pass"])
	except:
		Pass=""
	try:
		RenderVersion=str(connections["RenderVersion"])
	except:
		RenderVersion=""
	try:
		Type=str(connections["Type"])
	except:
		Type="Render"
	try:
		CacheParameter=str(connections["CacheParameter"])
	except:
		CacheParameter=""
	try:
		CacheNode=str(connections["CacheNode"])
	except:
		CacheNode=""


	try:
		safeProject=reformat(Project)
		if Type=="Render":
			if Sequence=="Animatics":
				picturepath="/W/Projects/"+safeProject+"/60_PreRenders/Animatics/Houdini/"+Sequence+"/"+Shot+"/"+Pass+"/"+RenderVersion
			elif Sequence=="Lookdev":
				picturepath="/W/Projects/"+safeProject+"/60_PreRenders/Animatics/Houdini/"+Sequence+"/"+Shot+"/"+Pass+"/"+RenderVersion
			else:
				picturepath="/W/Projects/"+safeProject+"/80_RenderLayers/"+Shot+"/CG/li/"+Pass+"/"+RenderVersion
		elif Type=="Cache":
			picturepath="/W/Projects/"+safeProject+"/40_Cache/"+Sequence+"/"+Shot+"/cg/"+CacheNode+"/"+CacheParameter+"/"+RenderVersion
		else:
			return 0

		if os.path.isdir(picturepath):
			pass
		else:
			os.makedirs(picturepath)
			if Type=="Render":
				os.makedirs(picturepath+"/hipFile/SHD")
				os.makedirs(picturepath+"/hipFile/PC")
				os.makedirs(picturepath+"/seq")
		return picturepath
	except:
		return 0

def reformat(dbProjectName):
	return reformatApesProjectName().reformatApesProjectName_main(dbProjectName=dbProjectName)