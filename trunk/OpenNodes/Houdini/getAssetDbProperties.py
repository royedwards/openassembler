###OpenAssembler Node python file###

'''
define
{
	name getAssetDbProperties
	tags hou
	input string assetName "" ""
	output string dbPath "" ""
	output string dbType "" ""
	output string dbName "" ""
}
'''

try:
	import hou
except:
	print "getAssetDbProperties will not work outside Houdini!!"

class getAssetDbProperties():
	def getAssetDbProperties_main(self, **connections):
		try:
			assetName=connections["assetName"]
		except:
			assetName=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="dbPath"	

		if oas_output=="dbPath":
			try:
				return hou.node("/obj/"+str(assetName)).parm("dbPath").eval()
			except:
				return 0
		if oas_output=="dbType":
			try:
				return hou.node("/obj/"+str(assetName)).parm("dbType").eval()
			except:
				return 0
		if oas_output=="dbName":
			try:
				path=hou.node("/obj/"+str(assetName)).parm("dbPath").eval()
				return path.rsplit(":",1)[1]
			except:
				return 0