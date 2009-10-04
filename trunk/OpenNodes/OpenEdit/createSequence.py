###OpenAssembler Node python file###

'''
define
{
	name createSequence
	tags oped
	input string Project "" ""
	input string SequenceName "" ""
	output int result "" ""

}
'''
import os, sys
from OpenProject.getElementType import getElementType
from OpenProject.createElement import createElement
from OpenProject.getVaultPath import getVaultPath

class createSequence(getElementType,createElement,getVaultPath):
   def createSequence_main(self, **connections):
	try:
		Project=connections["Project"]
	except:
		Project=""
	try:
		SequenceName=connections["SequenceName"]
	except:
		SequenceName=""

	if SequenceName=="" or Project=="":
		return 0

	if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(SequenceName))=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(SequenceName))==0:
		self.createElement_main(Path=":"+str(Project)+":Movie",Type="container",Name=str(SequenceName))
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName),Type="container",Name="Assets")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName),Type="container",Name="Attributes")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName)+":Assets",Type="container",Name="RenderSetups")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName)+":Assets",Type="container",Name="LightSetups")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName)+":Assets",Type="container",Name="Passes")
		self.createElement_main(Path=":"+str(Project)+":Movie:"+str(SequenceName)+":Assets",Type="container",Name="Misc")
	return 1			

		
