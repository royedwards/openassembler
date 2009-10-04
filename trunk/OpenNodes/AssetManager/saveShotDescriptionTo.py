###OpenAssembler Node python file###

'''
define
{
	name saveShotDescriptionTo
	tags amanage
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Pass "" ""
	input string Version "" ""
	output int result "" ""

}
'''

import os, sys, shutil

from OpenProject.getVaultPath import getVaultPath
from OpenProject.getAttribute import getAttribute

class saveShotDescriptionTo():
	def saveShotDescriptionTo_main(self, **connections):
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
			Pass=str(connections["Pass"])
		except:
			Pass=""
		try:
			Version=str(connections["Version"])
		except:
			Version=""
		try:

			origfilecontent=getA(":"+Project+":Movie:"+Sequence+":"+Shot+".shotsetup")

			vp=gVP(":"+Project+":Movie:"+Sequence+":"+Shot+":Renders:"+Pass+"@"+Version)

			fl=open(str(vp)+"/shotsetup.atr","w")
			fl.write(origfilecontent)
			fl.close()

			return 1
		except:
			return 0


def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)

def getA(Path):
	return getAttribute().getAttribute_main(Path=Path)