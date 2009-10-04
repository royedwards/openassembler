###OpenAssembler Node python file###

'''
define
{
	name set_TextEdit
	tags qtmod
	input string setPlainText "" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys

class set_TextEdit():
	def set_TextEdit_main(self, **connections):
		setPlainText=connections["setPlainText"]
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			Entry.setPlainText(str(setPlainText))
			return 1




