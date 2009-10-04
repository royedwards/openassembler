###OpenAssembler Node python file###

'''
define
{
	name getCacheableAssetsInScene
	tags hou
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getCacheableAssetsInScene will not work outside Houdini!!"

class getCacheableAssetsInScene():
	def getCacheableAssetsInScene_main(self, **connections):
		try:
			objs=hou.node("/obj").children()
			ret=[]
			for obj in objs:
				if obj.parm("dbPath")!=None:
					ret.append(obj)

			ret2=[]
			for it in ret:
				ret2.append(it.name())

			finret=[]

			for node in ret2:
				try:
					tmp=hou.node("/obj/"+node).parmsInFolder(("Cache",))
					finret.append(node)
				except:
					pass
			return finret
		except:
			return []

