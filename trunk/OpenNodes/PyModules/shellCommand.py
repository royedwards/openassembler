###OpenAssembler Node python file###

'''
define
{
	name shellCommand
	tags pymod
	input string command "" ""
	output any result "" ""

}
'''

import sys,os

class shellCommand():
	def shellCommand_main(self, **connections):

		try:
			command=connections["command"]
		except:
			command=""

		return os.system(command)