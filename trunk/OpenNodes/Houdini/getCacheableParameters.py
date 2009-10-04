###OpenAssembler Node python file###

'''
define
{
	name getCacheableParameters
	tags hou
	input string nodeName "" ""
	output array1D nameList "[]" ""
}
'''

try:
	import hou
except:
	print "getCacheableParameters will not work outside Houdini!!"

class getCacheableParameters():
	def getCacheableParameters_main(self, **connections):
		try:
			nodeName=str(connections["nodeName"])
		except:
			nodeName=""
		try:
			finret=[]
			params=hou.node("/obj/"+nodeName).parmsInFolder(("Cache",))
			for ps in params:
				if ps.name().split("_")[-1]=="sopoutput":
					finret.append(str(ps.name().split("_sopoutput")[0]))

			return finret
		except:
			return []

