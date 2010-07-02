###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name getTextureFolder
	tags apes
	input string Project "" ""
	input string Asset "" ""
	input string Texture "" ""
	input string Version "" ""
	output Path texturepath "" ""
}
'''
import os,sys
from DigitalApes.reformatApesProjectName import reformatApesProjectName

class getTextureFolder:
   def getTextureFolder_main(self,**connections):
	try:
		Project=str(connections["Project"])
	except:
		Project=""
	try:
		Asset=str(connections["Asset"])
	except:
		Asset=""
	try:
		Texture=str(connections["Texture"])
	except:
		Texture=""
	try:
		Version=str(connections["Version"])
	except:
		Version=""

	try:
		safeProject=reformat(Project)
		if os.name=="nt":
			texturepath="W:/Projects/"+safeProject+"/22_Textures/"+Asset+"/"+Texture+"/"+Version
		else:
			texturepath="/W/Projects/"+safeProject+"/22_Textures/"+Asset+"/"+Texture+"/"+Version
		if os.path.isdir(texturepath):
			pass
		else:
			os.makedirs(texturepath)
		return texturepath
	except:
		return 0

def reformat(dbProjectName):
	return reformatApesProjectName().reformatApesProjectName_main(dbProjectName=dbProjectName)