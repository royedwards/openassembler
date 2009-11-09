###OpenAssembler Node python file###

'''
define
{
	name loadAssetAttributes
	tags hou
	input string AssetName "" ""
	input string Project "" ""
	input dbPath Shot "" ""
	input string Version "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "loadAssetAttributes will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from OpenEdit.sequenceFromShot import sequenceFromShot
from OpenProject.getVaultPath import getVaultPath

class loadAssetAttributes():
	def loadAssetAttributes_main(self, **connections):
		try:
			Version=str(connections["Version"])
		except:
			Version=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			AssetName=str(connections["AssetName"])
		except:
			AssetName=""
		try:
			Project=connections["Project"]
		except:
			Project=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"		

		Sequence=getSeq(Project,Shot)

		if str(geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Attributes:"+AssetName+"@"+Version))=="" or str(geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Attributes:"+AssetName+"@"+Version))=="0":
			return 0

		vpath=getVP(":"+Project+":Movie:"+Sequence+":"+Shot+":Attributes:"+AssetName+"@"+Version)
		dir_content=os.listdir(vpath)
		try:
			hou.node("/obj/ShotData").parm(AssetName).set(Version)
		except:
			attr=hou.StringParmTemplate(AssetName,AssetName,1,(Version,))
			hou.node("/obj/ShotData").addSpareParmTuple(attr,("Setupversions",))
		for desc_files in dir_content:
			prcont=""
			if os.path.isfile(str(vpath+"/"+desc_files))==True:
				if os.path.splitext(desc_files)[1][1:][:2]=="py":
					prfile=open(str(vpath+"/"+desc_files),"r")
					prcont=prfile.read()
					prfile.close()
			if prcont!="":
				try:
					try:
						hou.node("/obj/"+AssetName).parm(os.path.splitext(desc_files)[0]).deleteAllKeyframes()
					except:
						print "KeyDeletion failed!!!"
					exec(prcont)
					try:
						locals().pop("hou_node")
					except:
						print "hou_locale deletion problem"

					if len(locals()["hou_parm"].keyframes())>0:
						for kf in locals()["hou_parm"].keyframes():
							kf.interpretAccelAsRatio(False)
							locals()["hou_parm"].setKeyframe(kf)
						hou.setFrame(locals()["hou_parm"].keyframes()[0].frame())
						exec(prcont)
						try:
							locals().pop("hou_node")
						except:
							print "hou_locale deletion problem"

				except:
					print "There was some error while loading the attributes back!", desc_files,AssetName

		return 1
		
def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def getSeq(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)

def getVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)
