###OpenAssembler Node python file###

'''
define
{
	name createNewAsset
	tags amanage
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Name "" ""
	input string Type "" ""
	output string name "" ""

}
'''

from OpenProject.createElement import createElement

class createNewAsset():
	def createNewAsset_main(self, **connections):
		try:
			Project=connections["Project"]
		except:
			Project=""
		try:
			Sequence=connections["Sequence"]
		except:
			Sequence=""
		try:
			Shot=connections["Shot"]
		except:
			Shot=""
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

		if Name=="" or Type=="":
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

		if Type=="Items":

			if Project=="":
				return 0
			dbPath=":"+Project+":Assets:"+Type

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
			if Project=="":
				return 0
			dbPath=":"+Project+":Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Engine")

			if en==0:
				return 0
		elif Type=="CameraSetups":
			dbPath=":General:Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Camera")

			if en==0:
				return 0
		elif Type=="Misc":
			if Project=="" or Sequence=="" or Shot=="":
				return 0
			dbPath=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Misc")
			if en==0:
				return 0
		elif Type=="LightSetups":
			dbPath=":General:Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Lightrig")
			if en==0:
				return 0
		elif Type=="Passes":
			if Project=="" or Sequence=="" or Shot=="":
				return 0
			dbPath=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "Pass")
			if en==0:
				return 0
		elif Type=="RenderSetups":
			dbPath=":General:Assets:"+Type
			root=crE(dbPath,"container",name)
			if root==0:
				return 0

			en=crE(dbPath+":"+name,"item", "RenderSetup")
			if en==0:
				return 0
		else:
			return 0

		return name


def crE(Path,Type,Name):
	return createElement().createElement_main(Path=Path,Type=Type,Name=Name)

