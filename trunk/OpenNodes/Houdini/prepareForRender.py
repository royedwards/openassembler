###OpenAssembler Node python file###

'''
define
{
	name prepareForRender
	tags hou
	input string Project "" ""
	input string Shot "" ""
	input string Pass "" ""
	input string RenderVersion "" ""
	input string RenderSetup "" ""
	input int FirstFrame "100" ""
	input int Endframe "200" ""
	input int Increment "1" ""
	output string hipFile "" ""

}
'''
import os,sys

try:
	import hou
except:
	print "prepareForRender will not work outside Houdini!!"

from Houdini.buildShot import buildShot
from OpenEdit.sequenceFromShot import sequenceFromShot
from AssetManager.saveShotDescriptionTo import saveShotDescriptionTo
from DigitalApes.getRenderFolder import getRenderFolder

class prepareForRender():
	def prepareForRender_main(self, **connections):
		try:
			Project=str(connections["Project"])
		except:
			Project=""
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
			RenderSetup=str(connections["RenderSetup"])
		except:
			RenderSetup=""
		try:
			FirstFrame=int(connections["FirstFrame"])
		except:
			FirstFrame=""
		try:
			Endframe=int(connections["Endframe"])
		except:
			Endframe=""
		try:
			Increment=int(connections["Increment"])
		except:
			Increment=""

		try:
			hou.hipFile.clear()

			bShot(Project,Shot)

			hou.node("/obj/"+Pass).setDisplayFlag(True)

			hou.node("/obj/"+RenderSetup).parm("framerange1").set(FirstFrame)
			hou.node("/obj/"+RenderSetup).parm("framerange2").set(Endframe)
			hou.node("/obj/"+RenderSetup).parm("framerange3").set(Increment)

			seq=sFS(Project,Shot)

			ssd(Project,seq,Shot,Pass,RenderVersion)

			picturepath=grf(Project,seq,Shot,Pass,RenderVersion)

			hou.node("/obj/"+RenderSetup).parm("picture_out").set(picturepath+"/seq/"+Shot+"_"+Pass+"_"+RenderVersion+".$F4.exr")


			for child in hou.node("/obj").children():
				try:
					child.allowEditingOfContents()
				except:
					pass

			hou.hipFile.save(picturepath+"/hipFile/"+Pass+".hip")

			return picturepath+"/hipFile/"+Pass+".hip"

		except:
			return 0


def bShot(Project,Shot):
	return buildShot().buildShot_main(Type="render",Project=Project,Shot=Shot)

def sFS(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)

def ssd(Project,Sequence,Shot,Pass,Version):
	return saveShotDescriptionTo().saveShotDescriptionTo_main(Project=Project,Sequence=Sequence,Shot=Shot,Pass=Pass,Version=Version)

def grf(Project,Sequence,Shot,Pass,RenderVersion):
	return getRenderFolder().getRenderFolder_main(Project=Project,Sequence=Sequence,Shot=Shot,Pass=Pass,RenderVersion=RenderVersion)