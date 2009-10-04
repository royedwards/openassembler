###OpenAssembler Node python file###

'''
define
{
	name setBuildBelongings
	tags hou
	input string NodeName "" ""
	input string Value "" ""
	output string belonging "" ""
}
'''

try:
	import hou
except:
	print "setBuildBelongings will not work outside Houdini!!"

class setBuildBelongings():
	def setBuildBelongings_main(self, **connections):
		try:
			NodeName=connections["NodeName"]
		except:
			NodeName=""	
		try:
			Value=connections["Value"]
		except:
			Value=""	
		try:
			hou.node("/obj/ShotData").parm(NodeName+"_BuildBelongings").set(Value)
			return 1
		except:
			return 0