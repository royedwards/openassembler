###OpenAssembler Node python file###

'''
define
{
	name filterAssets
	tags hou
	input houdiniObjects in_Objects "" ""
	output houdiniObjects out_Objects "" ""
}
'''

try:
	import hou
except:
	print "filterAssets will not work outside Houdini!!"

class filterAssets():
	def filterAssets_main(self, **connections):
		try:
			ret=[]
			for obj in in_Objects:
				if obj.parm("dbPath")!=None:
					ret.append(obj)
		except:
			return []

