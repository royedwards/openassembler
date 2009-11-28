###OpenAssembler Node python file###

'''
define
{
	name isHoudiniRunning
	tags hou
	output any result "" ""

}
'''

class isHoudiniRunning():
	def isHoudiniRunning_main(self, **connections):
		try:
			import hou
			return 1
		except:
			return 0