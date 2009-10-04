###OpenAssembler Node python file###

'''
define
{
	name startLocalRender
	tags hou
	input string ropPath "" ""
	output int result "" ""
}
'''

try:
	import hou
except:
	print "startLocalRender will not work outside Houdini!!"


class startLocalRender():
	def startLocalRender_main(self, **connections):
		try:
			ropPath=str(connections["ropPath"])
		except:
			ropPath=""

		try:
			hou.node(ropPath).render()
			return 1
		except:
			return 0
