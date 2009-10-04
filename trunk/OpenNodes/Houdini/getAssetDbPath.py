###OpenAssembler Node python file###

'''
define
{
	name getAssetDbPath
	tags hou
	input string Name "" ""
	output dbPath dbPath "" ""

}
'''
try:
	import hou
except:
	print "getAssetDbPath will not work outside Houdini!!"

class getAssetDbPath():
	def getAssetDbPath_main(self, **connections):

		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="dbPath"		

		try:

			asset=hou.node("/obj/"+Name)
			if asset==None:
				return 0
			dbp=asset.parm("dbPath").eval()
			dbtyp=asset.parm("dbType").eval()
			
			return dbp+":"+dbtyp

		except:
			return 0
		