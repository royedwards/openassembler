###OpenAssembler Node python file###

'''
define
{
	name saveShotDescription
	tags hou
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input functionCall noShotDataDialog "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "saveShotDescription will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from OpenEdit.sequenceFromShot import sequenceFromShot
from OpenProject.getAttribute import getAttribute
from OpenProject.setAttribute import setAttribute
from OpenProject.getVersionList import getVersionList
from OpenProject.getVaultPath import getVaultPath
from OpenEdit.getFramerange import getFramerange
from Houdini.getAssetsInScene import getAssetsInScene
from Houdini.actualShot import actualShot
from AssetManager.createAssetDb import createAssetDb
from Houdini.publishAsset import publishAsset
from OpenProject.createElement import createElement
from OpenProject.createNewVersion import createNewVersion
from OpenProject.getLatestVersion import getLatestVersion

class saveShotDescription():
	def saveShotDescription_main(self, **connections):
		try:
			Project=str(connections["Project"])
		except:
			Project=""
		try:
			Sequence=str(connections["Sequence"])
		except:
			Sequence=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			noShotDataDialog=connections["noShotDataDialog"]
		except:
			noShotDataDialog=""


		ch=0
		for node in hou.node("/obj").children():
			if node.name()=="ShotData":
				ch=1

		if ch==0:
			noShotDataDialog()
			return 0

		in_scene_assets=gAss()


		notLoadedLines=hou.node("/obj/ShotData").parmsInFolder(("NotLoadedAssets",))

		path="/obj/ShotData"

		shotROOTdbPath=":"+Project+":Movie:"+Sequence+":"+Shot

		if geT(shotROOTdbPath)=="" or geT(shotROOTdbPath)==0:
			return 0

		shotdesc=""
		for ass in in_scene_assets:
			ass_name=ass
			tmp=hou.node("/obj/"+ass).parm("dbPath").eval()
			ass_dbname=tmp.rsplit(":",1)[1]
			ass_type=hou.node("/obj/"+ass).parm("dbType").eval()
			ass_version=hou.node("/obj/"+ass).type().definition().version()
			try:
				ass_par_version=hou.node(path).parm(ass).eval()
			except:
				ass_par_version=glv(shotROOTdbPath+":Attributes:"+ass)
			try:
				ass_pazz=hou.node(path).parm(ass+"_PassBelongings").eval()
			except:
				ass_pazz=""
			try:
				ass_bui=hou.node(path).parm(ass+"_BuildBelongings").eval()
			except:
				ass_bui="111"
			shotdesc+=str(ass_name)+" | "+str(ass_type)+" | "+str(ass_dbname)+" | "+str(ass_version)+" | "+str(ass_par_version)+" | "+str(ass_pazz)+" | "+str(ass_bui) +"\n"

		for nll in notLoadedLines:
			st=nll.eval()
			shotdesc+=st+"\n"

		setA(shotROOTdbPath+".shotsetup",shotdesc)

		return 1
		
def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def getSeq(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)

def getA(Path):
	return getAttribute().getAttribute_main(Path=Path)

def setA(Path,Value):
	return setAttribute().setAttribute_main(Path=Path, Value=Value)

def getVL(Path):
	return getVersionList().getVersionList_main(Path=Path)

def getVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)

def getFR(Project,Shot):
	return getFramerange().getFramerange_main(Project=Project,Shot=Shot)

def gAss():
	return getAssetsInScene().getAssetsInScene_main(oas_output="nameList")

def aShot(output):
	return actualShot().actualShot_main(oas_output=output)

def cADb(dbPath,Name,Type):
	return createAssetDb().createAssetDb_main(dbPath=dbPath,Name=Name,Type=Type)

def pubA(assetPath,Comment):
	return publishAsset().publishAsset_main(assetPath=assetPath,Comment=Comment)

def crE(Path,Type,Name):
	return createElement().createElement_main(Path=Path,Type=Type,Name=Name)

def crNV(Path,ReviewType,Comment):
	return createNewVersion().createNewVersion_main(Path=Path,ReviewType=ReviewType,Comment=Comment)

def glv(path):
	return getLatestVersion().getLatestVersion_main(Path=path)