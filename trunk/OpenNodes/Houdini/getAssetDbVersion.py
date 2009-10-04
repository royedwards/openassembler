###OpenAssembler Node python file###

'''
define
{
	name getAssetDbVersion
	tags hou
	input string Name "" ""
	output string version "" ""

}
'''
try:
	import hou
except:
	print "getAssetDbVersion will not work outside Houdini!!"

class getAssetDbVersion():
	def getAssetDbVersion_main(self, **connections):

		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"		

		try:

			asset=hou.node("/obj/"+Name)
			if asset==None:
				return 0
			ver=asset.type().definition().version()
			return ver

		except:
			return 0
		