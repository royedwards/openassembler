###OpenAssembler Node python file###

'''
define
{
	name saveShotAttributes
	tags hou
	input array1D saveAttributesOnThisAssets "[]" ""
	input array1D publishThisAssets "[]" ""
	input string Comment "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "saveShotAttributes will not work outside Houdini!!"

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

class saveShotAttributes():
	def saveShotAttributes_main(self, **connections):
		try:
			saveAttributesOnThisAssets=connections["saveAttributesOnThisAssets"]
		except:
			saveAttributesOnThisAssets=[]
		try:
			publishThisAssets=connections["publishThisAssets"]
		except:
			publishThisAssets=[]
		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""

		ch=0
		for node in hou.node("/obj").children():
			if node.name()=="ShotData":
				ch=1

		if ch==0:
			return 0

		in_scene_assets=gAss()

		notLoadedLines=hou.node("/obj/ShotData").parmsInFolder(("NotLoadedAssets",))

		project=aShot("Project")
		sequence=aShot("Sequence")
		shot=aShot("Shot")

		path="/obj/ShotData"

		shotROOTdbPath=":"+project+":Movie:"+sequence+":"+shot

		if geT(shotROOTdbPath)=="" or geT(shotROOTdbPath)==0:
			return 0


		for itm in publishThisAssets:
			item=hou.node("/obj/"+str(itm))
			origpath=item.parm("dbPath").eval()
			if origpath.find(shotROOTdbPath)<0:
				item.parm("dbPath").lock(False)
				cat=origpath.rsplit(":",2)[1]
				assname=origpath.rsplit(":",2)[2]

				item.type().definition().removeParmTuple("dbPath")

				newpath=shotROOTdbPath+":Assets:"+cat+":"+assname

				pp=hou.StringParmTemplate("dbPath","dbPath",1,(newpath,))
				item.type().definition().addParmTuple(pp,("projectDB",))
				
				item.parm("dbPath").lock(True)
				otype=item.parm("dbType").eval()
				if geT(newpath)=="" or geT(newpath)==0:
					cre=cADb(shotROOTdbPath+":Assets:"+cat,assname,cat)

			finalpath=item.parm("dbPath").eval()
			finaltype=item.parm("dbType").eval()

			pre=pubA("/obj/"+str(itm),Comment)

		for i in publishThisAssets:
			chk=0
			for a in saveAttributesOnThisAssets:
				if i==a:
					chk=1
			if chk==0:
				saveAttributesOnThisAssets.append(i)

		for item in saveAttributesOnThisAssets:
			savepath=shotROOTdbPath+":Attributes:"+item
			if geT(savepath)=="" or geT(savepath)==0:
				crE(shotROOTdbPath+":Attributes","item",item)
			
			version=crNV(shotROOTdbPath+":Attributes:"+item,"unknown",Comment)
			if version==0:
				return 0
			vpath=getVP(shotROOTdbPath+":Attributes:"+item+"@"+version)
			try:
				hou.node("/obj/ShotData").parm(item).set(version)
			except:
				attr=hou.StringParmTemplate(item,item,1,(version,))
				hou.node(path).addSpareParmTuple(attr,("Setupversions",))
			for pm in hou.node("/obj/"+item).parms():
				pname=pm.name()
				if pname=="dbPath" or pname=="dbType":
					pass
				else:
					pyvar=pm.asCode()
					fl=open(vpath+"/"+pname+".py","w")
					fl.write(pyvar)
					fl.close()

		shotdesc=""
		for ass in in_scene_assets:
			ass_name=ass
			ass_type=hou.node("/obj/"+ass).parm("dbType").eval()
			if ass_type=="Pass":
				retget=geT(":"+project+":Movie:"+sequence+":"+shot+":Renders:"+ass_name)
				if str(retget)=="" or str(retget)=="0":
					try:
						rerere=crE(":"+project+":Movie:"+sequence+":"+shot+":Renders","item",ass_name)
						if rerere==0:
							print "There was some problem during the creation of the pass folder!!!"
					except:
						print "There was some problem during the creation of the pass folder --2-- !!!"

			tmp=hou.node("/obj/"+ass).parm("dbPath").eval()
			ass_dbname=tmp.rsplit(":",1)[1]
			ass_version=hou.node("/obj/"+ass).type().definition().version()
			ass_par_version=glv(shotROOTdbPath+":Attributes:"+ass)
			shotdesc+=str(ass_name)+" | "+str(ass_type)+" | "+str(ass_dbname)+" | "+str(ass_version)+" | "+str(ass_par_version)+"\n"

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