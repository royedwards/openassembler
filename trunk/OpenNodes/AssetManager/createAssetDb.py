###OpenAssembler Node python file###

'''
define
{
	name createAssetDb
	tags amanage
	input dbPath dbPath "" ""
	input string Name "" ""
	input string Type "" ""
	output string name "" ""

}
'''

from OpenProject.getElementType import getElementType
from OpenProject.createElement import createElement
from OpenProject.getElementList import getElementList

class createAssetDb():
	def createAssetDb_main(self, **connections):
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
			oas_output=connections["oas_output"]
		except:
			oas_output="result"		

		if oas_output=="result":

			if Name=="" or dbPath=="":
				return 0

		char_list="1234567890_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

		name=""
		for st in Name:
			ss=""
			if char_list.find(st)>-1:
				ss=st
			name+=ss

		if name=="":
			return 0

		if str(getT(dbPath))=="" or str(getT(dbPath))=="0":
			return 0

		if Type=="Items":

			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			tx=crE(dbPath+":"+name,"container", "Texture")
			md=crE(dbPath+":"+name,"item", "Model")
			ma=crE(dbPath+":"+name,"item", "Material")
			se=crE(dbPath+":"+name,"item", "Setup")
			de=crE(dbPath+":"+name,"item", "Deform")


			if tx*md*ma*se==0:
				return 0

		elif Type=="Engines":

			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Engine")

			if en==0:
				return 0
		elif Type=="CameraSetups":

			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Camera")

			if en==0:
				return 0
		elif Type=="Misc":
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Misc")
			if en==0:
				return 0
		elif Type=="LightSetups":
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Lightrig")
			if en==0:
				return 0
		elif Type=="Passes":
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Pass")
			if en==0:
				return 0
		elif Type=="RenderSetups":
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "RenderSetup")
			if en==0:
				return 0
		else:
			return 0

		return name


def getT(Path):
	return getElementType().getElementType_main(Path=Path)

def crE(Path,Type,Name):
	return createElement().createElement_main(Path=Path,Type=Type,Name=Name)

def getEL(Path):
	return getElementList().getElementList_main(Path=Path)

