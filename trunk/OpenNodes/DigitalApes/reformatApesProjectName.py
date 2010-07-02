###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name reformatApesProjectName
	tags apes
	input string dbProjectName "" ""
	output string apesProjectName "" ""
}
'''
import os

class reformatApesProjectName:
   def reformatApesProjectName_main(self,**connections):
	dbProjectName=connections["dbProjectName"]
	if dbProjectName=="1_GP":
		return "01_GP"
	else:
		return dbProjectName