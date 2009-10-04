###OpenAssembler Node python file###

'''
define
{
	name getPassBelongings
	tags hou
	input string NodeName "" ""
	output string belonging "" ""
}
'''

try:
	import hou
except:
	print "getPassBelongings will not work outside Houdini!!"

class getPassBelongings():
	def getPassBelongings_main(self, **connections):
		try:
			NodeName=connections["NodeName"]
		except:
			NodeName=""	
		try:
			ret=hou.node("/obj/ShotData").parm(NodeName+"_PassBelongings").eval()
			return ret
		except:
			return ""