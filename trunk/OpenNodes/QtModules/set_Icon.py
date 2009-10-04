###OpenAssembler Node python file###

'''
define
{
	name set_Icon
	tags qtmod
	input file File "" ""
	input file iconFolder "" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class set_Icon():
	def set_Icon_main(self, **connections):
		File=str(connections["File"])
		iconFolder=str(connections["iconFolder"])
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap(str(iconFolder+File)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			Entry.setIcon(icon)
			return 1
