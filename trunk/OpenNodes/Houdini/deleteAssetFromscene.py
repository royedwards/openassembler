###OpenAssembler Node python file###

'''
define
{
	name deleteAssetFromscene
	tags hou
	input string Name "" ""
	output int result "" ""

}
'''
try:
	import hou
except:
	print "getAssetDbVersion will not work outside Houdini!!"

class deleteAssetFromscene():
	def deleteAssetFromscene_main(self, **connections):

		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="result"		

		try:

			asset=hou.node("/obj/"+Name)
			if asset==None:
				return 0
			asset.destroy()
			return 1

		except:
			return 0
		