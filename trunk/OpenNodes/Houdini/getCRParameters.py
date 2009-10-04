###OpenAssembler Node python file###

'''
define
{
	name getCRParameters
	tags hou
	input string Type "" ""
	input string nodeName "" ""
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getCRParameters will not work outside Houdini!!"

class getCRParameters():
	def getCRParameters_main(self, **connections):
		try:
			Type=connections["Type"]
		except:
			Type=""
		try:
			nodeName=connections["nodeName"]
		except:
			nodeName=""
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
				params=hou.node("/obj/"+nodeName).parmsInFolder(("Cache",))
				for ps in params:
					if ps.name().split("_")[-1]=="sopoutput":
						finret.append(str(ps.name().split("_sopoutput")[0]))

			elif Type=="Render":
				for node in ret2:
					try:
						if str(hou.node("/obj/"+node).parm("dbType").eval())=="RenderSetup":
							finret.append(node)
					except:
						pass
			else:
				pass

			return finret
		except:
			return []

