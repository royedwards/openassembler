###OpenAssembler Node python file###

'''
define
{
	name get_DateEdit
	tags qtmod
	input uiItem Entry "" ""
	output string date "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class get_DateEdit():
	def get_DateEdit_main(self, **connections):
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			return str(str(Entry.date().year())+"."+str(Entry.date().month())+"."+str(Entry.date().day()))

