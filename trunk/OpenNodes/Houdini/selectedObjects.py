###OpenAssembler Node python file###

'''
define
{
	name selectedObjects
	tags hou
	output houdiniObjects Objects "" ""

}
'''

try:
	import hou
except:
	print "selectedObjects will not work outside Houdini!!"

class selectedObjects():
	def selectedObjects_main(self, **connections):
		
		try:
			return hou.selectedNodes()
		except:
			return ()

