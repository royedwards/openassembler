###OpenAssembler Node python file###

'''
define
{
	name buildShot
	tags hou
	input string Type "" ""
	input string Project "" ""
	input string Shot "" ""
	input Path shotOverride "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "buildShot will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from Houdini.loadHDA import loadHDA
from OpenEdit.sequenceFromShot import sequenceFromShot
from OpenProject.getAttribute import getAttribute
from OpenProject.setAttribute import setAttribute
from OpenProject.getVersionList import getVersionList
from OpenProject.getVaultPath import getVaultPath
from OpenEdit.getFramerange import getFramerange
from OpenProject.getLatestVersion import getLatestVersion


class buildShot():
	def buildShot_main(self, **connections):
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			Project=connections["Project"]
		except:
			Project=""
		try:
			shotOverride=str(connections["shotOverride"])
		except:
			shotOverride=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"		


		try:
			Sequence=getSeq(Project,Shot)

			if str(geT(":"+Project+":Movie:"+Sequence+":"+Shot))=="" or str(geT(":"+Project+":Movie:"+Sequence+":"+Shot))=="0":
				return 0

			hou.hipFile.clear()

			hou.node("/obj").createNode("null","ShotData")
			path="/obj/ShotData"
			hou.node(path).addSpareParmFolder("projectDB")
			hou.node(path).addSpareParmFolder("NotLoadedAssets")
			hou.node(path).addSpareParmFolder("Setupversions")
			hou.node(path).addSpareParmFolder("PassBelongings")
			hou.node(path).addSpareParmFolder("BuildBelongings")

			pp=hou.StringParmTemplate("dbProject","dbProject",1,(Project,))
			hou.node(path).addSpareParmTuple(pp,("projectDB",))
			hou.node(path).parm("dbProject").lock(True)
			pt=hou.StringParmTemplate("dbShot","dbShot",1,(Shot,))
			hou.node(path).addSpareParmTuple(pt,("projectDB",))
			hou.node(path).parm("dbShot").lock(True)
			pt=hou.StringParmTemplate("dbShotType","dbShotType",1,(Type,))
			hou.node(path).addSpareParmTuple(pt,("projectDB",))
			hou.node(path).parm("dbShotType").lock(True)
			hou.node(path).setDisplayFlag(False)
			fps=getA(":"+Project+".fps")

			hou.setFps(int(fps))

			framerange=getFR(Project,Shot)

			hou.hscript("tset `"+str(int(framerange[0])-1)+"/$FPS` `"+str(framerange[1])+"/$FPS`")

			hou.setFrame(int(framerange[0]))

			attribute=""
			if shotOverride!="":
				if os.path.isfile(shotOverride):
					fl=open(shotOverride,"r")
					attribute=fl.read()
					fl.close()
			else:
				attribute=getA(":"+Project+":Movie:"+Sequence+":"+Shot+".shotsetup")
				if attribute=="" or attribute==0:
					attribute=getA(":"+Project+":Movie:"+Sequence+".shotsetup")
			
			if attribute=="":
				return 0

			parsed=[]
			for line in attribute.split("\n"):
				linearray=[]
				for entry in line.split("|"):
					linearray.append(entry.strip())
				parsed.append(linearray)

			passes=[]
			for item in parsed:
				if item[1]=="Pass":
					passes.append(item[0])
			allpass=""
			for psa in passes:
				allpass+=psa+","

			try:
				if allpass[-1:]==",":
					allpass=allpass[:-1]
			except:
				pass

			allbuild="111"

			for item in parsed:
				try:
					psez= item[5]
				except:
					psez= allpass

				try:
					blls=item[6]
				except:
					blls= allbuild

				if item[1] == "Model":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Model",item[3],":"+Project+":Assets:Items:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				if item[1] == "Deform":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Deform",item[3],":"+Project+":Assets:Items:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Setup":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Setup",item[3],":"+Project+":Assets:Items:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Material":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Material",item[3],":"+Project+":Assets:Items:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()	
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Engine":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Engine",item[3],":"+Project+":Assets:Engines:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Camera":
					LHD(item[2],"Camera",item[3],":General:Assets:CameraSetups:"+item[2],item[0])
					hou.node("/obj/"+item[0]).matchCurrentDefinition()

				elif item[1] == "Misc":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Misc",item[3],":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:Misc:"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Pass":
					if loadORnot(Type,psez,blls)==1:
						LHD(item[2],"Pass",item[3],":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:Passes:"+item[2],item[0])
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Lightrig":
					if loadORnot(Type,psez,blls)==1:
						obj=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:LightSetups:"+item[2]+":Lightrig"
						shotlevel=getVL(obj)
						if shotlevel==[] or shotlevel==0:
							obj2=":"+Project+":Movie:"+Sequence+":Assets:LightSetups:"+item[2]+":Lightrig"
							seqlevel=getVL(obj2)
							if seqlevel==[] or seqlevel==0:
								obj3=":"+Project+":Movie:Assets:LightSetups:"+item[2]+":Lightrig"
								showlevel=getVL(obj3)
								if showlevel==[] or showlevel==0:
									obj4=":General:Assets:LightSetups:"+item[2]+":Lightrig"
									globallevel=getVL(obj4)
									if globallevel==[] or globallevel==0:
										pt=hou.StringParmTemplate(item[0],item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
										hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))
										hou.node(path).parm(item[0]).lock(True)
									else:
										LHD(item[2],"Lightrig",item[3],":General:Assets:LightSetups:"+item[2],item[0])
										hou.node("/obj/"+item[0]).setDisplayFlag(False)
										hou.node("/obj/"+item[0]).matchCurrentDefinition()
								else:
										LHD(item[2],"Lightrig",item[3],":"+Project+":Movie:Assets:LightSetups:"+item[2],item[0])
										hou.node("/obj/"+item[0]).setDisplayFlag(False)
										hou.node("/obj/"+item[0]).matchCurrentDefinition()
							else:
								LHD(item[2],"Lightrig",item[3],":"+Project+":Movie:"+Sequence+":Assets:LightSetups:"+item[2],item[0])
								hou.node("/obj/"+item[0]).setDisplayFlag(False)
								hou.node("/obj/"+item[0]).matchCurrentDefinition()
						else:
							LHD(item[2],"Lightrig",item[3],":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:LightSetups:"+item[2],item[0])
							hou.node("/obj/"+item[0]).setDisplayFlag(False)
							hou.node("/obj/"+item[0]).matchCurrentDefinition()
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))
					
				elif item[1] == "RenderSetup":
					if loadORnot(Type,psez,blls)==1:
						obj=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:RenderSetups:"+item[2]+":RenderSetup"
						shotlevel=getVL(obj)
						if shotlevel==[] or shotlevel==0:
							obj2=":"+Project+":Movie:"+Sequence+":Assets:RenderSetups:"+item[2]+":RenderSetup"
							seqlevel=getVL(obj2)
							if seqlevel==[] or seqlevel==0:
								obj3=":"+Project+":Movie:Assets:RenderSetups:"+item[2]+":RenderSetup"
								showlevel=getVL(obj3)
								if showlevel==[] or showlevel==0:
									obj4=":General:Assets:RenderSetups:"+item[2]+":RenderSetup"
									globallevel=getVL(obj4)
									if globallevel==[] or globallevel==0:
										pt=hou.StringParmTemplate(item[0],item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
										hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))
										hou.node(path).parm(item[0]).lock(True)
									else:
										LHD(item[2],"RenderSetup",item[3],":General:Assets:RenderSetups:"+item[2],item[0])
										hou.node("/obj/"+item[0]).matchCurrentDefinition()
								else:
										LHD(item[2],"RenderSetup",item[3],":"+Project+":Movie:Assets:RenderSetups:"+item[2],item[0])
										hou.node("/obj/"+item[0]).matchCurrentDefinition()
							else:
								LHD(item[2],"RenderSetup",item[3],":"+Project+":Movie:"+Sequence+":Assets:RenderSetups:"+item[2],item[0])
								hou.node("/obj/"+item[0]).matchCurrentDefinition()
						else:
							LHD(item[2],"RenderSetup",item[3],":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:RenderSetups:"+item[2],item[0])
							hou.node("/obj/"+item[0]).matchCurrentDefinition()
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				elif item[1] == "Cache":
					if loadORnot(Type,psez,blls)==1:
						or_nodename=item[0].rsplit("_",2)[0]
						LHD(item[2],"Cache" ,item[3],":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+or_nodename+":"+item[2],item[0])
						hou.node("/obj/"+item[0]).matchCurrentDefinition()
						hou.node("/obj/"+item[0]).setDisplayFlag(False)
					else:
						pt=hou.StringParmTemplate(item[0]+"_nL",item[0],1,(item[0]+"|"+item[1]+"|"+item[2]+"|"+item[3]+"|"+item[4]+"|"+item[5]+"|"+item[6],))
						hou.node(path).addSpareParmTuple(pt,("NotLoadedAssets",))

				if loadORnot(Type,psez,blls)==1 or item[1] == "Camera":
					prcont=""
					lv=glv(":"+Project+":Movie:"+Sequence+":"+Shot+":Attributes:"+item[0])
					if lv==0 or lv=="":
						pass
					else:
						vpath=getVP(":"+Project+":Movie:"+Sequence+":"+Shot+":Attributes:"+item[0]+"@"+item[4])
						dir_content=os.listdir(vpath)
						attr=hou.StringParmTemplate(item[0],item[0],1,(item[4],))
						hou.node(path).addSpareParmTuple(attr,("Setupversions",))
						for desc_files in dir_content:
							if os.path.isfile(str(vpath+"/"+desc_files))==True:
								if os.path.splitext(desc_files)[1][1:][:2]=="py":
									prfile=open(str(vpath+"/"+desc_files),"r")
									prcont=prfile.read()
									prfile.close()
							if prcont!="":
								try:
									exec(prcont)
									try:
										locals().pop("hou_node")
									except:
										print "hou_locale deletion problem"
								except:
									print "There was some error while loading the attributes back!", desc_files,item[0]


					attr=hou.StringParmTemplate(item[0]+"_PassBelongings",item[0],1,(psez,))
					hou.node(path).addSpareParmTuple(attr,("PassBelongings",))		

					attr=hou.StringParmTemplate(item[0]+"_BuildBelongings",item[0],1,(blls,))
					hou.node(path).addSpareParmTuple(attr,("BuildBelongings",))	
			return 1
		except:
			return 0

def loadORnot(buildType,passbelonging,buildbelonging):
	if buildType.find(":")>-1:
		bT=buildType.split(":")[1]
	else:
		bT=buildType
	list=[]
	for item in passbelonging.split(","):
		if item.strip()=="":
			pass
		else:
			list.append(item)
	if buildbelonging[0]=="1":
		list.append("Main")
	if buildbelonging[1]=="1":
		list.append("Effect")
	if buildbelonging[2]=="1":
		list.append("Environment")
	ch=0
	for it in list:
		if str(it)==str(bT):
			ch=1
	if str(bT)=="Full":
		ch=1
	return ch

def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def LHD(Name,Type,Version,dbPath,nameOverride):
	return loadHDA().loadHDA_main(Name=Name,Type=Type,Version=Version,dbPath=dbPath,nameOverride=nameOverride)

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

def glv(path):
	return getLatestVersion().getLatestVersion_main(Path=path)
