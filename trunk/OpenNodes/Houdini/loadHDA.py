###OpenAssembler Node python file###

'''
define
{
	name loadHDA
	tags hou
	input string Type "" ""
	input string Name "" ""
	input dbPath dbPath "" ""
	input string nameOverride "" ""
	input string Version "latest" ""
	output any version "" ""

}
'''
import os,sys
try:
	import hou
except:
	print "loadHDA will not work outside Houdini!!"

from OpenProject.getElementType import getElementType
from OpenProject.getVersionList import getVersionList
from Houdini.createEmptyHDA import createEmptyHDA
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getVersionFromPath import getVersionFromPath

class loadHDA():
	def loadHDA_main(self, **connections):
		try:
			nameOverride=str(connections["nameOverride"])
		except:
			nameOverride=""
		try:
			dbPath=connections["dbPath"]
		except:
			dbPath=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			Version=str(connections["Version"])
		except:
			Version=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="version"		

		if str(geT(dbPath))=="" or str(geT(dbPath))=="0":
			return 0


		vl=gVList(dbPath+":"+Type)
		vlist=[]
		for v in vl:
			vlist.append(v[0])

		if vlist==[]:
			crHDA(Name,dbPath,Type,nameOverride)
		elif vlist==0:
			return 0

		if Version=="v000" and vlist!=[]:
			Version="v001"

		vers=getVerFrompath(str(dbPath)+":"+str(Type)+"@"+str(Version))
		chk=0

		for v in vlist:
			if str(v)==str(vers):
				chk=1

		if chk==0:
			return 0
		else:
			vPath=gVP(str(dbPath)+":"+str(Type)+"@"+str(Version))
			
			if vPath==0:
				return 0
			file_to_load=vPath+"/"+Type+".otl"
			if os.path.isfile(file_to_load):
				array=[]
				try:
					array=hou.hda.definitionsInFile("Embedded")
				except:
					pass
				cs=0
				for itts in array:
					if itts.nodeTypeName()==Name+"_"+Type+"_"+vers:
						cs=1
				if cs!=1:
					hou.hda.installFile(file_to_load)
				if nameOverride=="":
					asset=hou.node("/obj").createNode(Name+"_"+Type+"_"+vers,Name)
				else:
					asset=hou.node("/obj").createNode(Name+"_"+Type+"_"+vers,nameOverride)
				asset.allowEditingOfContents()
				otlpath=str(asset.type().definition().libraryFilePath())
				if cs!=1:
					hou.hda.uninstallFile(otlpath)
				asset.type().definition().setVersion(vers)
				asset.type().definition().updateFromNode(asset)
				return vers
			else:
				return 0
		

def geT(Path):
	return getElementType().getElementType_main(Path=Path)

def gVList(Path):
	return getVersionList().getVersionList_main(Path=Path)

def crHDA(Name,Path,Type,nameOverride):
	return createEmptyHDA().createEmptyHDA_main(Name=Name,dbPath=Path,Type=Type,nameOverride=nameOverride)

def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)

def getVerFrompath(Path):
	return getVersionFromPath().getVersionFromPath_main(Path=Path)
