###OpenAssembler Node python file###

'''
define
{
	name updateAssetInScene
	tags hou
	input string Name "" ""
	input string newVersion "" ""
	output string version "" ""

}
'''
try:
	import hou
except:
	print "updateAssetInScene will not work outside Houdini!!"

from loadHDA import loadHDA
from OpenProject.getElementType import getElementType

class updateAssetInScene():
	def updateAssetInScene_main(self, **connections):

		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			newVersion=str(connections["newVersion"])
		except:
			newVersion=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="result"		

		try:

			asset=hou.node("/obj/"+Name)
			dbType=asset.parm("dbType").eval()
			dbPath=asset.parm("dbPath").eval()
			visib=asset.isObjectDisplayed()
			if str(geT(dbPath+":"+dbType+"@"+newVersion))!="version":
				return 0

			if asset==None:
				return 0
			parameters=[]
			for ps in asset.parms():
				parameters.append(ps.asCode())

			asset.destroy()

			dbName=dbPath.rsplit(":",1)[1]

			LHD(dbName,dbType,newVersion,dbPath,Name)

			newasset=hou.node("/obj/"+Name)

			for code in parameters:
				try:
					exec(code)
				except:
					print "Some Parameter was missing found!"

			newasset.setDisplayFlag(visib)
			try:
				newasset.matchCurrentDefinition()
			except:
				pass

			return newVersion

		except:
			return 0
		

def LHD(Name,Type,Version,dbPath,nameOverride):
	return loadHDA().loadHDA_main(Name=Name,Type=Type,Version=Version,dbPath=dbPath,nameOverride=nameOverride)

def geT(Path):
	return getElementType().getElementType_main(Path=Path)
