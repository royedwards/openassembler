###OpenAssembler Node python file###

'''
define
{
	name insertOBJ
	tags hou
	input string geofile "" ""
	input string comment "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "insertOBJ will not work outside Houdini!!"

class insertOBJ():
	def insertOBJ_main(self, **connections):
		try:
			geofile=connections["geofile"]
		except:
			geofile=""
		try:
			comment=connections["comment"]
		except:
			comment=""

		if os.path.isfile(geofile):
			pass
		else:
			return 0

		gn=hou.node("/obj").createNode("geo","tmp_geo")
		pth=gn.path()
		gf=hou.node(pth+"/file1")
		gf.parm("file").set(geofile)
		gf.setComment(comment)
		gf.setHardLocked(1)
		gr=gf.createOutputNode("group")
		gr.parm("destroyname").set("*")
		at=gr.createOutputNode("attribpromote")
		at.setDisplayFlag(1)
		at.setRenderFlag(1)
		at.parm("inname").set("N")
		at.parm("outclass").set(3)

		return 1