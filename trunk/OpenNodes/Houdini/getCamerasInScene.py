###OpenAssembler Node python file###

'''
define
{
	name getCamerasInScene
	tags hou
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getCamerasInScene will not work outside Houdini!!"

class getCamerasInScene():
	def getCamerasInScene_main(self, **connections):
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="nameList"	
		try:
			objs=hou.node("/obj").children()
			ret=[]
			for obj in objs:
				if obj.parm("dbPath")!=None:
					ret.append(obj)

			if oas_output=="nameList":
				ret2=[]
				for item in ret:
					origcat=item.parm("dbType").eval()
					if origcat=="Camera":
						ret2.append(item.name())
				return ret2
		except:
			return []

