###OpenAssembler Node python file###

'''
define
{
	name getCRNodes
	tags hou
	input string Type "" ""
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getCRNodes will not work outside Houdini!!"

class getCRNodes():
	def getCRNodes_main(self, **connections):
		try:
			Type=connections["Type"]
		except:
			Type=""
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

			if Type=="Cache":
				for node in ret2:
					try:
						tmp=hou.node("/obj/"+node).parmsInFolder(("Cache",))
						finret.append(node)
					except:
						pass

			elif Type=="Render":
				for node in ret2:
					try:
						if str(hou.node("/obj/"+node).parm("dbType").eval())=="Pass":
							finret.append(node)
					except:
						pass
			else:
				pass

			return finret
		except:
			return []

