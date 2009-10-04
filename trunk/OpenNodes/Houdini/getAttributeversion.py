###OpenAssembler Node python file###

'''
define
{
	name getAttributeversion
	tags hou
	input string Assetname "" ""
	output string version "" ""
}
'''

try:
	import hou
except:
	print "getAttributeversion will not work outside Houdini!!"

class getAttributeversion():
	def getAttributeversion_main(self, **connections):
		try:
			Assetname=connections["Assetname"]
		except:
			Assetname=""	

		try:
			ver=hou.node("/obj/ShotData").parm(Assetname).eval()
			return ver
		except:
			return 0

