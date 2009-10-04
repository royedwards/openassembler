###OpenAssembler Node python file###

'''
define
{
	name setPassBelongings
	tags hou
	input string NodeName "" ""
	input string Value "" ""
	output string belonging "" ""
}
'''

try:
	import hou
except:
	print "setPassBelongings will not work outside Houdini!!"

class setPassBelongings():
	def setPassBelongings_main(self, **connections):
		try:
			NodeName=connections["NodeName"]
		except:
			NodeName=""	
		try:
			Value=connections["Value"]
		except:
			Value=""	
		try:
			hou.node("/obj/ShotData").parm(NodeName+"_PassBelongings").set(Value)
			return 1
		except:
			return 0