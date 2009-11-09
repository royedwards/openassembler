###OpenAssembler Node python file###

'''
define
{
	name getFileFromPath
	tags pymod
	input string input "" ""
	output string out "" ""
}
'''

import os,sys

class getFileFromPath():
	def getFileFromPath_main(self, **connections):
		input=str(connections["input"])
		try:
			a=os.path.split(input)[1]
			b=os.path.splitext(a)[0]
			return str(b)
		except:
			return 0