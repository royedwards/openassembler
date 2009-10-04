###OpenAssembler Node python file###

'''
define
{
	name createShot
	tags oped
	input string Project "" ""
	input string Sequence "" ""
	input string ShotName "" ""
	output int result "" ""

}
'''
import os, sys
from OpenProject.getElementType import getElementType
from OpenProject.createElement import createElement
from OpenProject.getVaultPath import getVaultPath
from OpenProject.setAttribute import setAttribute

class createShot(getElementType,createElement,getVaultPath,setAttribute):
   def createShot_main(self, **connections):
	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Sequence=connections["Sequence"]
	except:
	    Sequence=""
	try:
	    ShotName=connections["ShotName"]
	except:
	    ShotName=""

	if ShotName=="" or Project=="" or Sequence=="":
		return 0

	if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName)=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName)==0:
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence),Type="container",Name=str(ShotName))
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName,Type="container",Name="Assets")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName,Type="container",Name="Attributes")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName,Type="container",Name="Caches")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName,Type="container",Name="Renders")

		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName+":Assets",Type="container",Name="RenderSetups")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName+":Assets",Type="container",Name="LightSetups")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName+":Assets",Type="container",Name="Passes")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName+":Assets",Type="container",Name="Misc")


	self.setAttribute_main(Path=":"+str(Project)+":Movie:"+str(Sequence)+":"+ShotName+".framerange",Value="100,200")

	return 1	
		
