###OpenAssembler Node python file###

'''
define
{
	name renderModelTurntable
	tags hou
	input string Name "" ""
	input dbPath dbPath "" ""
	input string Version "latest" ""
	output string hipFile "" ""

}
'''
import os,sys

try:
	import hou
except:
	print "renderModelTurntable will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from Houdini.loadHDA import loadHDA
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getVersionFromPath import getVersionFromPath

class renderModelTurntable():
	def renderModelTurntable_main(self, **connections):
		try:
			dbPath=connections["dbPath"]
		except:
			dbPath=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			Version=str(connections["Version"])
		except:
			Version=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="hipFile"		

		if str(geT(dbPath))=="" or str(geT(dbPath))=="0":
			return 0

		vers=getVerFrompath(str(dbPath)+":Model@"+str(Version))
		vPath=gVP(str(dbPath)+":Model@"+str(vers))

		if str(vPath)=="0" or vPath=="":
			return 0

		if os.path.isdir(vPath+'/hipFile'):
			pass
		else:
			os.makedirs(vPath+'/hipFile')
		if os.path.isdir(vPath+'/render'):
			pass
		else:
			os.makedirs(vPath+'/render')
		if os.path.isdir(vPath+'/mov'):
			pass
		else:
			os.makedirs(vPath+'/mov')

		hou.hipFile.clear()

		ret1=LHD(Name,"Model",Version,dbPath,"Turntable_Model")
		par=hou.node("/obj/Turntable_Model").parm("ry")
		hou.setFrame(1)
		par.setKeyframe(hou.Keyframe(0))
		hou.setFrame(101)
		par.setKeyframe(hou.Keyframe(720))
		hou.setFrame(1)

		coll=""
		for item in hou.node("/obj/Turntable_Model").children():
			coll+=str(item.path())+" "

		mat_pars=hou.node("/obj/Turntable_Model").parmsInFolder(("Materials",))

		for pa in mat_pars:
			try:
				pa.set("/obj/Turntable_Shader/turntableShop/out")
			except:
				pass
		
		ret2=LHD("LookdevLightRig","Lightrig","latest",":General:Assets:LightSetups:LookdevLightRig","Turntable_Lightrig")
		hou.node("/obj/"+"Turntable_Lightrig").parm("models").set(coll)
		ret3=LHD("modelTurntable","RenderSetup","latest",":General:Assets:RenderSetups:modelTurntable","Turntable_RenderSetup")

		rsobj=hou.node("/obj/Turntable_RenderSetup")
		rsobj.parm("tt_picture").set(vPath+'/render/'+Name+".$F4.exr")
		rsobj.parm("tt_comment").set(Name+"_"+vers)

		ret4=LHD("autoscaleCamera","Camera","latest",":General:Assets:CameraSetups:autoscaleCamera","Turntable_LookdevCamera")
		hou.node("/obj/"+"Turntable_LookdevCamera").parm("models").set(coll)
		ret5=LHD("ModelTurntableShader","Shader","latest",":General:Assets:Shaders:ModelTurntableShader","Turntable_Shader")	


		hou.hipFile.save(vPath+'/hipFile/turntable.hip')

		hou.exit()


def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def LHD(Name,Type,Version,dbPath,nameOverride):
	return loadHDA().loadHDA_main(Name=Name,Type=Type,Version=Version,dbPath=dbPath,nameOverride=nameOverride)

def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)

def getVerFrompath(Path):
	return getVersionFromPath().getVersionFromPath_main(Path=Path)