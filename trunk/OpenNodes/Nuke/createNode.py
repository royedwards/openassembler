###OpenAssembler Node python file###

'''
define
{
	name createNode
	tags nuke
	input string Type "" ""
	input string nameOverride "" ""
	output string name "" ""

}
'''
try:
	import nuke
except:
	print "createNode will not work outside of Nuke!!!"

class createNode():
	def createNode_main(self, **connections):
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			nameOverride=str(connections["nameOverride"])
		except:
			nameOverride=""
		try:
			node=nuke.createNode(Type)
			node.setName(nameOverride)
			backname=node.name()
			return backname
		except:
			return 0
