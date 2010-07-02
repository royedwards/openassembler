###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name iconPath
	tags msc
	output file IconPath "" ""
}
'''
import os

class iconPath:
   def iconPath_main(self,**connections):
	iconPath=""
	if os.name=="nt":
		iconPath="C:/OpenTools/Icons/"
	elif os.name=="posix":
		iconPath="/Volumes/projects/assetManager/projectDb/GYAR_Pipeline/Icons"
	return iconPath