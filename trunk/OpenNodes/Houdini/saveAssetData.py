###OpenAssembler Node python file###

'''
define
{
	name saveAssetData
	tags hou
	input string assetName "" ""
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input functionCall noShotDataDialog "" ""
	input string Comment "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "saveAssetData will not work outside Houdini!!"

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
from AssetManager.createNewAsset import createNewAsset

class saveAssetData():
	def saveAssetData_main(self, **connections):
		try:
			assetName=str(connections["assetName"])
		except:
			assetName=""
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

		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""

		ch=0
		for node in hou.node("/obj").children():
			if node.name()=="ShotData":
				ch=1

		if ch==0:
			noShotDataDialog()
			return 0

		path="/obj/ShotData"

		shotROOTdbPath=":"+Project+":Movie:"+Sequence+":"+Shot

		if geT(shotROOTdbPath)=="" or geT(shotROOTdbPath)==0:
			return 0

		assetType=hou.node("/obj/"+assetName).parm("dbType").eval()

		#--------------------------------publish---------------------------------------------

		if assetType=="Pass" or assetType=="Misc":
			if hou.node("/obj/"+assetName).matchesCurrentDefinition()==False:
				dbPath_gb=hou.node("/obj/"+assetName).parm("dbPath").eval()
				if assetType=="Misc":
					af=geT(dbPath_gb)
					if str(af)=="" or str(af)=="0":
						crNEWA(Project,Sequence,Shot,assetName,"Misc")

				if assetType=="Pass":
					af=geT(dbPath_gb)
					if str(af)=="" or str(af)=="0":
						crNEWA(Project,Sequence,Shot,assetName,"Passes")

					retget=geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Renders:"+assetName)
					if str(retget)=="" or str(retget)=="0":
						try:
							rerere=crE(":"+Project+":Movie:"+Sequence+":"+Shot+":Renders","item",assetName)
							if rerere==0:
								print "There was some problem during the creation of the pass folder!!!"
						except:
							print "There was some problem during the creation of the pass folder --2-- !!!"

				pre=pubA("/obj/"+str(assetName),Comment)
				if pre==0:
					print "-----There was some error during the publish on this node:"+assetName

		#----------------------------------preferences save--------------------------------------------

		savepath=shotROOTdbPath+":Attributes:"+assetName
		if geT(savepath)=="" or geT(savepath)==0:
			crE(shotROOTdbPath+":Attributes","item",assetName)
			
		version=crNV(shotROOTdbPath+":Attributes:"+assetName,"Animation",Comment)
		if version==0:
			return 0
		vpath=getVP(shotROOTdbPath+":Attributes:"+assetName+"@"+version)
		try:
			hou.node("/obj/ShotData").parm(assetName).set(version)
		except:
			attr=hou.StringParmTemplate(assetName,assetName,1,(version,))
			hou.node(path).addSpareParmTuple(attr,("Setupversions",))
		for pm in hou.node("/obj/"+assetName).parms():
			pname=pm.name()
			if pname=="dbPath" or pname=="dbType":
				pass
			else:
				pyvar=pm.asCode()
				fl=open(vpath+"/"+pname+".py","w")
				fl.write(pyvar)
				fl.close()
		try:
			hou.node(path).parmsInFolder(("Setupversions",))
		except:
			hou.node(path).addSpareParmFolder("Setupversions")
		try:
			hou.node(path).parmsInFolder(("PassBelongings",))
		except:
			hou.node(path).addSpareParmFolder("PassBelongings")
		try:
			hou.node(path).parmsInFolder(("BuildBelongings",))
		except:
			hou.node(path).addSpareParmFolder("BuildBelongings")

		try:
			hou.node(path).parm(assetName+"_PassBelongings").eval()
		except:
			attr=hou.StringParmTemplate(assetName+"_PassBelongings",assetName,1,("",))
			hou.node(path).addSpareParmTuple(attr,("PassBelongings",))		
		try:
			hou.node(path).parm(assetName+"_BuildBelongings").eval()
		except:
			attr=hou.StringParmTemplate(assetName+"_BuildBelongings",assetName,1,("111",))
			hou.node(path).addSpareParmTuple(attr,("BuildBelongings",))

		return 1
	

def crNEWA(Project,Sequence,Shot,Name,Type):
	return createNewAsset().createNewAsset_main(Project=Project,Sequence=Sequence,Shot=Shot,Name=Name,Type=Type)
	
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