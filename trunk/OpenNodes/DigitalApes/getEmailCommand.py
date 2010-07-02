###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name getEmailCommand
	tags apes
	input string JobName "" ""
	output string command "" ""
}
'''
import os,sys

class getEmailCommand:
   def getEmailCommand_main(self,**connections):
	try:
		JobName=str(connections["JobName"])
	except:
		JobName=""
	return "python /W/Projects/projectDb/Softwares/OpenNodes/PyModules/emailSend.py robot@digitalapes.com render@digitalapes.com "+JobName+" 192.168.3.11\n"
