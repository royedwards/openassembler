###OpenAssembler Node python file###

'''
define
{
	name getBuildBelongings
	tags hou
	input string NodeName "" ""
	output string belonging "" ""
}
'''

try:
	import hou
except:
	print "getBuildBelongings will not work outside Houdini!!"

class getBuildBelongings():
	def getBuildBelongings_main(self, **connections):
		try:
			NodeName=connections["NodeName"]
		except:
			NodeName=""	
		try:
			ret=hou.node("/obj/ShotData").parm(NodeName+"_BuildBelongings").eval()
			return ret
		except:
			return "111"

