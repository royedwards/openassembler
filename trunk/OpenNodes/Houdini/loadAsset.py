###OpenAssembler Node python file###

'''
define
{
	name loadAsset
	tags hou
	input string Assetname "" ""
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Type "" ""
	output any result "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "loadAsset will not work outside Houdini!!"

from Houdini.loadHDA import loadHDA

class loadAsset():
	def loadAsset_main(self, **connections):
		try:
			Assetname=str(connections["Assetname"])
		except:
			Assetname=""
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
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="list"		

		path="/obj/ShotData"

		if Type=="Items":
			dbPath=":"+Project+":Assets:"+Type+":"+Assetname
			ret=LHD(Assetname,"Model","latest",dbPath,Assetname+"_Model")
			hou.node("/obj/"+Assetname+"_Model").setDisplayFlag(False)
			hou.node("/obj/"+Assetname+"_Model").matchCurrentDefinition()
			LHD(Assetname,"Setup","latest",dbPath,Assetname+"_Setup")
			hou.node("/obj/"+Assetname+"_Setup").setDisplayFlag(False)
			hou.node("/obj/"+Assetname+"_Setup").matchCurrentDefinition()
			for item in hou.node("/obj/"+Assetname+"_Model").parmsInFolder(("Materials",)):
				try:
					item.set("/obj/"+Assetname+"_Material/"+str(item.name().split("_shop")[0])+"/out")
				except:
					pass
			try:
				ret2=LHD(Assetname,"Deform","latest",dbPath,Assetname+"_Deform")
				hou.node("/obj/"+Assetname+"_Deform").matchCurrentDefinition()
				hou.node("/obj/"+Assetname+"_Deform").setDisplayFlag(False)
			except:
				pass
			LHD(Assetname,"Material","latest",dbPath,Assetname+"_Material")
			hou.node("/obj/"+Assetname+"_Material").matchCurrentDefinition()
			hou.node("/obj/"+Assetname+"_Material").setDisplayFlag(False)

		elif  Type=="Engines":
			dbPath=":"+Project+":Assets:"+Type+":"+Assetname
			LHD(Assetname,"Engine","latest",dbPath,Assetname+"_Engine")
			hou.node("/obj/"+Assetname+"_Engine").matchCurrentDefinition()

		elif  Type=="LightSetups":
			dbPath=":General:Assets:"+Type+":"+Assetname
			LHD(Assetname,"Lightrig","latest",dbPath,Assetname+"_Light")
			hou.node("/obj/"+Assetname+"_Light").matchCurrentDefinition()

		elif  Type=="CameraSetups":
			dbPath=":General:Assets:"+Type+":"+Assetname
			LHD(Assetname,"Camera","latest",dbPath,Assetname+"_Camera")
			hou.node("/obj/"+Assetname+"_Camera").matchCurrentDefinition()

		elif  Type=="RenderSetups":
			dbPath=":General:Assets:"+Type+":"+Assetname
			LHD(Assetname,"RenderSetup","latest",dbPath,Assetname+"_RenderSetup")
			hou.node("/obj/"+Assetname+"_RenderSetup").matchCurrentDefinition()

		elif Type=="Passes" or Type=="Misc":
			retpath=""
			RT=""
			if Type=="Passes":
				RT="Pass"
			elif Type=="Misc":
				RT="Misc"

			if Assetname.split(" ")[1].strip()=="(General)":
				retpath=":General:Assets:"+Type+":"+Assetname.split(" ")[0].strip()
			elif Assetname.split(" ")[1].strip()=="(Show)":
				retpath=":"+Project+":Movie:Assets:"+Type+":"+Assetname.split(" ")[0].strip()
			elif Assetname.split(" ")[1].strip()=="(Sequence)":
				retpath=":"+Project+":Movie:"+Sequence+":Assets:"+Type+":"+Assetname.split(" ")[0].strip()
			elif Assetname.split(" ")[1].strip()=="(Shot)":
				retpath=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type+":"+Assetname.split(" ")[0].strip()

			LHD(Assetname.split(" ")[0].strip(),RT,"latest",retpath,Assetname.split(" ")[0].strip()+"_"+RT)
			try:
				hou.node("/obj/"+Assetname.split(" ")[0].strip()+"_"+RT).matchCurrentDefinition()
			except:
				pass

		elif Type=="Caches":
			Aspl=Assetname.split(" >>> ")
			dbPath=":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+str(Aspl[0])+":"+str(Aspl[1])
			LHD(str(Aspl[1]),"Cache","latest",dbPath,str(Aspl[0])+"_"+str(Aspl[1])+"_Cache")
			try:
				hou.node("/obj/"+str(Aspl[0])+"_"+str(Aspl[1])+"_Cache").matchCurrentDefinition()
			except:
				pass

		elif Type=="Shaders":
			dbPath=":General:Assets:"+Type+":"+Assetname
			LHD(Assetname,"Shader","latest",dbPath,Assetname+"_Shader")
			hou.node("/obj/"+Assetname+"_Shader").matchCurrentDefinition()


		try:
			attr=hou.StringParmTemplate(Assetname,Assetname,1,("",))
			hou.node(path).addSpareParmTuple(attr,("Setupversions",))	
		except:
			pass

		try:
			attr=hou.StringParmTemplate(Assetname+"_PassBelongings",Assetname,1,("",))
			hou.node(path).addSpareParmTuple(attr,("PassBelongings",))		
		except:
			pass

		try:
			attr=hou.StringParmTemplate(Assetname+"_BuildBelongings",Assetname,1,("",))
			hou.node(path).addSpareParmTuple(attr,("BuildBelongings",))
		except:
			pass
		return 1


def LHD(Name,Type,Version,dbPath,nameOverride):
	return loadHDA().loadHDA_main(Name=Name,Type=Type,Version=Version,dbPath=dbPath,nameOverride=nameOverride)