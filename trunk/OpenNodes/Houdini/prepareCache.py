###OpenAssembler Node python file###

'''
define
{
	name prepareCache
	tags hou
	input string nodeName "" ""
	input string Project "" ""
	input string Shot "" ""
	input string Comment "" ""
	input string parameterName "" ""
	input int firstFrame "" ""
	input int endFrame "" ""
	input int headAndTale "" ""
	output string realCacheFolder "" ""
}
'''

try:
	import hou
except:
	print "prepareCache will not work outside Houdini!!"

import os, sys
from OpenProject.getElementType import getElementType
from OpenEdit.sequenceFromShot import sequenceFromShot
from OpenProject.createElement import createElement
from OpenProject.createNewVersion import createNewVersion
from DigitalApes.reformatApesProjectName import reformatApesProjectName
from Houdini.createEmptyHDA import createEmptyHDA
from Houdini.publishAsset import publishAsset
from OpenProject.getLatestVersion import getLatestVersion

class prepareCache():
	def prepareCache_main(self, **connections):
		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""
		try:
			Project=str(connections["Project"])
		except:
			Project=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			nodeName=str(connections["nodeName"])
		except:
			nodeName=""
		try:
			parameterName=str(connections["parameterName"])
		except:
			parameterName=""
		try:
			firstFrame=int(connections["firstFrame"])
		except:
			firstFrame=""
		try:
			endFrame=int(connections["endFrame"])
		except:
			endFrame=""
		try:
			headAndTale=int(connections["headAndTale"])
		except:
			headAndTale=""

		sequence=getS(Project,Shot)

		if gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches")=="" or gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches")==0:
			return 0

		if gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName)=="" or gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName)==0:
			re=crE(":"+Project+":Movie:"+sequence+":"+Shot+":Caches","container",nodeName)

		if gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName)=="" or gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName)==0:
			re=crE(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName,"container",parameterName)

		if gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName+":Cache")=="" or gET(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName+":Cache")==0:
			re=crE(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName,"item","Cache")

		if glv(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName+":Cache")==0:
			versionwanabe="v001"
		else:
			versionwanabe="v"+str(int(str(glv(":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName+":Cache"))[1:])+1).zfill(3)
		apesproject=refo(Project)
		realPath="/W/Projects/"+apesproject+"/40_Cache/"+sequence+"/"+Shot+"/cg/"+nodeName+"/"+parameterName+"/"+versionwanabe

		if os.path.isdir(realPath):
			pass
		else:
			os.makedirs(realPath)

		hou.node("/obj/"+str(nodeName)).allowEditingOfContents()
		tmpname=crHDA("Cache",parameterName,":"+Project+":Movie:"+sequence+":"+Shot+":Caches:"+nodeName+":"+parameterName,"tmp_for_caching")

		node_a=hou.node("/obj/tmp_for_caching")
		node_b=node_a.createNode("geo","Cache")
		node_c=node_b.createNode("file","cache_to_load")
		hou.node("/obj/tmp_for_caching/Cache/file1").destroy()
		node_c.parm("file").set(realPath+"/$F4.bgeo")


		retA=pubA("/obj/tmp_for_caching",Comment)

		if str(retA)!=str(versionwanabe):
			return 0

		hou.node("/obj/tmp_for_caching").destroy()
		
		try:
			hou.node("/obj/"+nodeName).parm(parameterName+"_sopoutput").set(realPath+"/$F4.bgeo")
			hou.node("/obj/"+nodeName).parm(parameterName+"_f1").set(int(firstFrame)-int(headAndTale))
			hou.node("/obj/"+nodeName).parm(parameterName+"_f2").set(int(endFrame)+int(headAndTale))
			hou.node("/obj/"+nodeName).parm(parameterName+"_f3").set(1)
		except:
			return 0

		return realPath



def gET(Path):
	return getElementType().getElementType_main(Path=Path)

def getS(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)

def crE(Path,Type,Name):
	return createElement().createElement_main(Path=Path,Type=Type,Name=Name)

def crNV(Path,ReviewType,Comment):
	return createNewVersion().createNewVersion_main(Path=Path,ReviewType=ReviewType,Comment=Comment)

def refo(dbProjectName):
	return reformatApesProjectName().reformatApesProjectName_main(dbProjectName=dbProjectName)

def crHDA(Type,Name,dbPath,nameOverride):
	return createEmptyHDA().createEmptyHDA_main(Type=Type,Name=Name,dbPath=dbPath,nameOverride=nameOverride)

def pubA(assetPath,Comment):
	return publishAsset().publishAsset_main(assetPath=assetPath,Comment=Comment)

def glv(Path):
	return getLatestVersion().getLatestVersion_main(Path=Path)