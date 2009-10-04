###OpenAssembler Node python file###

'''
define
{
	name getAssetsInScene
	tags hou
	output houdiniObjects AssetObjects "[]" ""
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getAssetsInScene will not work outside Houdini!!"

class getAssetsInScene():
	def getAssetsInScene_main(self, **connections):
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="AssetObjects"	
		try:
			objs=hou.node("/obj").children()
			ret=[]
			for obj in objs:
				if obj.parm("dbPath")!=None:
					ret.append(obj)
			if oas_output=="AssetObjects":
				return ret
			elif oas_output=="nameList":
				ret2=[]
				for it in ret:
					ret2.append(it.name())
				return ret2
		except:
			return []

