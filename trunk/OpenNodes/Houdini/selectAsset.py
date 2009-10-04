###OpenAssembler Node python file###

'''
define
{
	name selectAsset
	tags hou
	input string Name "" ""
	output int result "" ""

}
'''
try:
	import hou
except:
	print "selectAsset will not work outside Houdini!!"


class selectAsset():
	def selectAsset_main(self, **connections):

		try:
			Name=str(connections["Name"])
		except:
			Name=""
	
		try:

			for item in hou.node("/obj").children():
				item.setSelected(False)

			asset=hou.node("/obj/"+Name)
			asset.setSelected(True)
			
			return 1

		except:
			return 0

