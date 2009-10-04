###OpenAssembler Node python file###

'''
define
{
	name loadHDASets
	tags hou
	input string Type "" ""
	input string Name "" ""
	input dbPath dbPath "" ""
	input string nameOverride "" ""
	input string Version "latest" ""
	output any version "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "loadHDASets will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from Houdini.loadHDA import loadHDA

class loadHDASets():
	def loadHDASets_main(self, **connections):
		try:
			nameOverride=str(connections["nameOverride"])
		except:
			nameOverride=""
		try:
			dbPath=connections["dbPath"]
		except:
			dbPath=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			Version=str(connections["Version"])
		except:
			Version=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"		

		if str(geT(dbPath))=="" or str(geT(dbPath))=="0":
			return 0


		if Type=="Model":
			return LHD(Name,Type,Version,dbPath,nameOverride)
		elif Type=="Engine":
			return LHD(Name,Type,Version,dbPath,nameOverride)
			#hou.node("/obj/"+nameOverride).setDisplayFlag(False)
			#hou.node("/obj/"+nameOverride).setDisplayFlag(True)
		elif Type=="Setup":
			ret=LHD(Name,"Model","latest",dbPath,Name+"_Model")
			try:
				ret2=LHD(Name,"Deform","latest",dbPath,Name+"_Deform")
			except:
				pass
			return LHD(Name,Type,Version,dbPath,Name+"_Setup")
		elif Type=="Material":
			hou.hipFile.clear()
			ret1=LHD(Name,"Model","latest",dbPath,Name+"_Model")
			par=hou.node("/obj/"+Name+"_Model").parm("ry")
			coll=""
			for item in hou.node("/obj/"+Name+"_Model").children():
				coll+=str(item.path())+" "

			for item in hou.node("/obj/"+Name+"_Model").parmsInFolder(("Materials",)):
				try:
					item.set("/obj/"+Name+"_Material/"+str(item.name().split("_shop")[0])+"/out")
				except:
					pass
			hou.setFrame(1)
			par.setKeyframe(hou.Keyframe(0))
			hou.setFrame(101)
			par.setKeyframe(hou.Keyframe(360))
			hou.setFrame(1)
			ret2=LHD("LookdevLightRig","Lightrig","latest",":General:Assets:LightSetups:LookdevLightRig","Lookdev_Lightrig")
			hou.node("/obj/"+"Lookdev_Lightrig").parm("models").set(coll)
			ret3=LHD("LookdevLightRig","RenderSetup","latest",":General:Assets:LightSetups:LookdevLightRig","Lookdev_RenderSetup")
			ret4=LHD("autoscaleCamera","Camera","latest",":General:Assets:CameraSetups:autoscaleCamera","Lookdev_LookdevCamera")
			hou.node("/obj/"+"Lookdev_LookdevCamera").parm("models").set(coll)
			return LHD(Name,Type,Version,dbPath,Name+"_Material")			
		elif Type=="everything":
			ret=LHD(Name,"Model","latest",dbPath,Name+"_Model")
			hou.node("/obj/"+Name+"_Model").setDisplayFlag(False)
			hou.node("/obj/"+Name+"_Model").matchCurrentDefinition()
			LHD(Name,"Setup","latest",dbPath,Name+"_Setup")
			hou.node("/obj/"+Name+"_Setup").setDisplayFlag(False)
			hou.node("/obj/"+Name+"_Setup").matchCurrentDefinition()
			for item in hou.node("/obj/"+Name+"_Model").parmsInFolder(("Materials",)):
				try:
					item.set("/obj/"+Name+"_Material/"+str(item.name().split("_shop")[0])+"/out")
				except:
					pass
			try:
				ret2=LHD(Name,"Deform","latest",dbPath,Name+"_Deform")
				hou.node("/obj/"+Name+"_Deform").matchCurrentDefinition()
				hou.node("/obj/"+Name+"_Deform").setDisplayFlag(False)
			except:
				pass

			LHD(Name,"Material","latest",dbPath,Name+"_Material")
			hou.node("/obj/"+Name+"_Material").matchCurrentDefinition()
			hou.node("/obj/"+Name+"_Material").setDisplayFlag(False)
			return "latest"


def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def LHD(Name,Type,Version,dbPath,nameOverride):
	return loadHDA().loadHDA_main(Name=Name,Type=Type,Version=Version,dbPath=dbPath,nameOverride=nameOverride)