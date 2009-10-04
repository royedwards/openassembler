###OpenAssembler Node python file###

'''
define
{
	name getMultiLevelsInScene
	tags hou
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getMultiLevelsInScene will not work outside Houdini!!"

class getMultiLevelsInScene():
	def getMultiLevelsInScene_main(self, **connections):
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
					origpath=item.parm("dbPath").eval()
					cat=origpath.rsplit(":",2)[1]
					if cat=="RenderSetups" or cat=="Passes" or cat=="LightSetups" or cat=="Misc":
						ret2.append(item.name())
				return ret2
		except:
			return []

