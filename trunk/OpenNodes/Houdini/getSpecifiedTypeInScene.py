###OpenAssembler Node python file###

'''
define
{
	name getSpecifiedTypeInScene
	tags hou
	input string Type "" ""
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getSpecifiedTypeInScene will not work outside Houdini!!"

class getSpecifiedTypeInScene():
	def getSpecifiedTypeInScene_main(self, **connections):
		try:
			Type=connections["Type"]
		except:
			Type=""	
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
					cat=item.parm("dbType").eval()
					if cat==Type:
						ret2.append(item.name())
				return ret2
		except:
			return []

