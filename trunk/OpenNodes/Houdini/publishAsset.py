###OpenAssembler Node python file###

'''
define
{
	name publishAsset
	tags hou
	input string assetPath "" ""
	input string Comment "" ""
	output string version "" ""
}
'''
import os,sys
try:
	import hou
except:
	print "publishAsset will not work outside Houdini!!"

from OpenProject.createNewVersion import createNewVersion
from OpenProject.getElementType import getElementType
from OpenProject.getVaultPath import getVaultPath

class publishAsset():
	def publishAsset_main(self, **connections):
		try:
			assetPath=connections["assetPath"]
		except:
			assetPath=""
		try:
			Comment=connections["Comment"]
		except:
			Comment=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"	
		try:
			asset=hou.node(assetPath)
			dbPath=str(asset.parm("dbPath").eval())
			dbType=str(asset.parm("dbType").eval())
			if geT(dbPath+":"+dbType)!="item":
				return 0

			newversion=str(crV(dbPath+":"+dbType,dbType,Comment))
			if newversion==0 or newversion=="":
				return 0
		
			vPath=gVP(dbPath+":"+dbType+"@"+newversion)

			try:
				otlpath=str(asset.type().definition().libraryFilePath())
				if otlpath!="Embedded":
					hou.hda.uninstallFile(otlpath)
				asset.type().definition().setVersion(newversion)
				asset.type().definition().updateFromNode(asset)
				asset.type().definition().copyToHDAFile(vPath+"/"+dbType+".otl",dbPath.rsplit(":",1)[1]+"_"+dbType+"_"+newversion,dbPath.rsplit(":",1)[1]+"_"+dbType+"_"+newversion)
				otlpath=str(asset.type().definition().libraryFilePath())
				if otlpath!="Embedded":
					hou.hda.uninstallFile(otlpath)
				asset.type().definition().setVersion(newversion)
				asset.type().definition().updateFromNode(asset)
				asset.matchCurrentDefinition()

			except:
				return 0

			return newversion
		except:
			return 0

def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def crV(Path,ReviewType,Comment):
	return createNewVersion().createNewVersion_main(Path=Path,ReviewType=ReviewType,Comment=Comment)

def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)