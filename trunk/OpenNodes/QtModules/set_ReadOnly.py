###OpenAssembler Node python file###

'''
define
{
	name set_ReadOnly
	tags qtmod
	input boolean Status "True" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class set_ReadOnly():
	def set_ReadOnly_main(self, **connections):
		Status=str(connections["Status"])
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			Entry.setReadOnly(Status)
			return 1
