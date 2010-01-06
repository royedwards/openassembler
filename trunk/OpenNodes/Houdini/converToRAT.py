###OpenAssembler Node python file###

'''
define
{
	name converToRAT
	tags hou
	input string originalfile "" ""
	input string convertedfile "" ""
	output string outfile "" ""

}
'''
import os,sys

from OpenEdit.sequenceFromShot import sequenceFromShot

class converToRAT():
	def converToRAT_main(self, **connections):
		try:
			originalfile=str(connections["originalfile"])
		except:
			originalfile=""
		try:
			convertedfile=str(connections["convertedfile"])
		except:
			convertedfile=""
		try:

			os.system("iconvert -t RAT "+originalfile+" "+convertedfile+" compression none")
			if os.path.isfile(convertedfile):
				return convertedfile
			else:
				return 0

		except:
			return 0 
