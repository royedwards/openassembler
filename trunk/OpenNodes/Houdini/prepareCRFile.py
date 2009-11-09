###OpenAssembler Node python file###

'''
define
{
	name prepareCRFile
	tags hou
	input string Project "" ""
	input string Shot "" ""
	input string Type "" ""
	input string Node_Pass "" ""
	input string Param_Setup "" ""
	input any FirstFrame "100" ""
	input any Endframe "200" ""
	input any Increment "1" ""
	input any Head_n_Tail "5" ""
	input string Comment "" ""
	input file pathOverride "" ""
	output array1D name_hipFile "" ""

}
'''
import os,sys

try:
	import hou
except:
	print "prepareForRender will not work outside Houdini!!"

from Houdini.buildShot import buildShot
from OpenEdit.sequenceFromShot import sequenceFromShot
from AssetManager.saveShotDescriptionTo import saveShotDescriptionTo
from DigitalApes.getRenderFolder import getRenderFolder

from OpenProject.createElement import createElement
from OpenProject.getElementType import getElementType
from OpenProject.createNewVersion import createNewVersion
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getAttribute import getAttribute
from Houdini.createEmptyHDA import createEmptyHDA
from Houdini.publishAsset import publishAsset
from OpenProject.getLatestVersion import getLatestVersion


class prepareCRFile():
	def prepareCRFile_main(self, **connections):
		try:
			Project=str(connections["Project"])
		except:
			Project=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			Node_Pass=str(connections["Node_Pass"])
		except:
			Node_Pass=""
		try:
			Param_Setup=str(connections["Param_Setup"])
		except:
			Param_Setup=""
		try:
			FirstFrame=int(connections["FirstFrame"])
		except:
			FirstFrame=100
		try:
			Endframe=int(connections["Endframe"])
		except:
			Endframe=200
		try:
			Increment=int(connections["Increment"])
		except:
			Increment=1
		try:
			Head_n_Tail=int(connections["Head_n_Tail"])
		except:
			Head_n_Tail=5
		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			pathOverride=str(connections["pathOverride"])
		except:
			pathOverride=""

		try:

			Sequence=sFS(Project,Shot)

			# construct the dbPath

			if Type=="Render":
				dbPath=":"+Project+":Movie:"+Sequence+":"+Shot+":Renders:"+Node_Pass
				if geT(dbPath)==0 or geT(dbPath)=="":
					crE(":"+Project+":Movie:"+Sequence+":"+shot+":Renders","item",Node_Pass)

			elif Type=="Cache":
				dbPath=":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup+":Cache"

				if geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches")=="" or geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches")==0:
					return ["No Cache folder...","","",""]

				if geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass)=="" or geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass)==0:
					re=crE(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches","container",Node_Pass)

				if geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup)=="" or geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup)==0:
					re=crE(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass,"container",Param_Setup)

				if geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup+":Cache")=="" or geT(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup+":Cache")==0:
					re=crE(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup,"item","Cache")

				tmpname=crHDA("Cache",Param_Setup,":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+Node_Pass+":"+Param_Setup,"tmp_for_caching")

				if glv(dbPath)==0:
					versionwanabe="v001"
				else:
					versionwanabe="v"+str(int(str(glv(dbPath))[1:])+1).zfill(3)

				picturepath=grf(Project,Sequence,Shot,Node_Pass,versionwanabe,Type,Param_Setup,Node_Pass)

				fullpath=picturepath+"/$F4.bgeo"
			
				node_a=hou.node("/obj/tmp_for_caching")
				node_b=node_a.createNode("geo","Cache")
				node_c=node_b.createNode("file","cache_to_load")
				hou.node("/obj/tmp_for_caching/Cache/file1").destroy()
				node_c.parm("file").set(fullpath)

				newversion=pubA("/obj/tmp_for_caching",Comment)

				if str(newversion)=="0":
					return ["Prooblem with the cachenodepublishing...","","",""]

				hou.node("/obj/tmp_for_caching").destroy()

			else:
				return ["Unknown category...","","",""]

			# create a new version
			if Type=="Render":
				newversion=crNV(dbPath,"Render",Comment)
				if newversion==0:
					return ["Can not create new version...",dbPath,"",""]

			# Save The Shot description file

			try:

				if pathOverride=="":
					origfilecontent=getA(":"+Project+":Movie:"+Sequence+":"+Shot+".shotsetup")
				else:
					if os.path.isfile(pathOverride):
						fx=open(pathOverride,"r")
						origfilecontent=fx.read()
						fx.close()
					else:
						origfilecontent=getA(":"+Project+":Movie:"+Sequence+":"+Shot+".shotsetup")

				vp=gVP(dbPath+"@"+newversion)

				fl=open(str(vp)+"/shotsetup.atr","w")
				fl.write(origfilecontent)
				fl.close()					

			except:
				["Shotdescription can not be saved...","","",""]

			# make the render-folder and get the path

			picturepath=grf(Project,Sequence,Shot,Node_Pass,newversion,Type,Param_Setup,Node_Pass)

			fullpath=""

			if Type=="Render":
				fullpath=picturepath+"/seq/"+Shot+"_"+Node_Pass+"_"+newversion+".$F4.exr"
			elif Type=="Cache":
				fullpath=picturepath+"/$F4.bgeo"
			else:
				pass

			# build the scene

			hou.hipFile.clear()
		
			if Type=="Cache":
				if os.path.isfile(str(vp)+"/shotsetup.atr"):
					bShot(Project,Shot,"Full",str(vp)+"/shotsetup.atr")
				else:
					bShot(Project,Shot,"Full","")
			else:
				cucc="Pass:"+str(Node_Pass)
				if os.path.isfile(str(vp)+"/shotsetup.atr"):
					bShot(Project,Shot,cucc,str(vp)+"/shotsetup.atr")
				else:
					bShot(Project,Shot,cucc,"")

			# make all node allowediting

			for child in hou.node("/obj").children():
				try:
					child.allowEditingOfContents()
				except:
					pass

			# record the rendernode_picturepath/bgeopath and set the framerange parameters

			if Type=="Render":
				resstring=getA(":"+Project+".resolution").strip()
				res=resstring.split("x")
				newx=int(res[0])*1.2
				newy=int(res[1])*1.2
				campath=hou.node("/obj/"+Param_Setup).parm("camera").eval()
				if hou.node("/obj/"+Param_Setup).parm("override_camerares").eval()==0:
					hou.node(campath).parm("winsizex").set(1.2)
					hou.node(campath).parm("winsizey").set(1.2)
					hou.node(campath).parm("resx").set(newx)
					hou.node(campath).parm("resy").set(newy)

				hou.node("/obj/"+Param_Setup).parm("picture_out").set(fullpath)
				hou.node("/obj/"+Node_Pass).setDisplayFlag(True)
				hou.node("/obj/"+Param_Setup).parm("framerange1").set(int(FirstFrame)-int(Head_n_Tail))
				hou.node("/obj/"+Param_Setup).parm("framerange2").set(int(Endframe)+int(Head_n_Tail))
				hou.node("/obj/"+Param_Setup).parm("framerange3").set(int(Increment))
			elif Type=="Cache":
				hou.node("/obj/"+Node_Pass).parm(Param_Setup+"_sopoutput").set(fullpath)
				hou.node("/obj/"+Node_Pass).parm(Param_Setup+"_f1").set(int(FirstFrame)-int(Head_n_Tail))
				hou.node("/obj/"+Node_Pass).parm(Param_Setup+"_f2").set(int(Endframe)+int(Head_n_Tail))
				hou.node("/obj/"+Node_Pass).parm(Param_Setup+"_f3").set(1)
			else:
				pass

			# save the hipfile

			rrunner="/cg/tools/cgru/houdini/houdini10/hrender_af.py $*\n"
			if Type=="Render":			
				frr=open(picturepath+"/hipFile/render.sh","w")
			else:
				frr=open(picturepath+"/render.sh","w")
			frr.write(rrunner)
			frr.close()
			try:
				if Type=="Render":
					os.system("chmod 755 "+picturepath+"/hipFile/render.sh")
				elif Type=="Cache":
					os.system("chmod 755 "+picturepath+"/render.sh")
			except:
				pass

			if Type=="Render":
				renderednode="/obj/"+Param_Setup+"/Sequence/out"
				hou.hipFile.save(picturepath+"/hipFile/"+Node_Pass+".hip")
				return [Shot+"_"+Node_Pass+"_"+newversion+"_render",picturepath+"/hipFile/"+Node_Pass+".hip",renderednode,picturepath+"/hipFile"]
			elif Type=="Cache":
				renderednode="/obj/"+Node_Pass+"/cacher_toHide/"+Param_Setup
				hou.hipFile.save(picturepath+"/"+Node_Pass+"_"+Param_Setup+".hip")
				return [Shot+"_"+Node_Pass+"_"+Param_Setup+"_"+newversion+"_cache",picturepath+"/"+Node_Pass+"_"+Param_Setup+".hip",renderednode,picturepath]

		except:
			return ["Unknown error...","","",""]

def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def bShot(Project,Shot,Type,shotOverride):
	return buildShot().buildShot_main(Type=Type,Project=Project,Shot=Shot,shotOverride=shotOverride)

def sFS(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)

def ssd(Project,Sequence,Shot,Pass,Version):
	return saveShotDescriptionTo().saveShotDescriptionTo_main(Project=Project,Sequence=Sequence,Shot=Shot,Pass=Pass,Version=Version)

def grf(Project,Sequence,Shot,Pass,RenderVersion,Type,CacheParameter,CacheNode):
	return getRenderFolder().getRenderFolder_main(Project=Project,Sequence=Sequence,Shot=Shot,Pass=Pass,RenderVersion=RenderVersion,Type=Type,CacheParameter=CacheParameter,CacheNode=CacheNode)

def crE(Path,Type,Name):
	return createElement().createElement_main(Path=Path,Type=Type,Name=Name)

def crNV(Path,ReviewType,Comment):
	return createNewVersion().createNewVersion_main(Path=Path,ReviewType=ReviewType,Comment=Comment)

def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)

def getA(Path):
	return getAttribute().getAttribute_main(Path=Path)

def crHDA(Type,Name,dbPath,nameOverride):
	return createEmptyHDA().createEmptyHDA_main(Type=Type,Name=Name,dbPath=dbPath,nameOverride=nameOverride)

def pubA(assetPath,Comment):
	return publishAsset().publishAsset_main(assetPath=assetPath,Comment=Comment)

def glv(Path):
	return getLatestVersion().getLatestVersion_main(Path=Path)