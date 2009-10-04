###OpenAssembler Node python file###

'''
define
{
	name set_LineEntry
	tags qtmod
	input string setText "" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys

class set_LineEntry():
	def set_LineEntry_main(self, **connections):
		setText=connections["setText"]
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			Entry.setText(str(setText))
			return 1




