###OpenAssembler Node python file###

'''
define
{
	name getTextDialog
	tags qtmod
	input string setTitle "getTextDialog" ""
	input string Label "" ""
	output string text "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class getTextDialog():
	def getTextDialog_main(self, **connections):
		Label=str(connections["Label"])
		setTitle=str(connections["setTitle"])
		try:
			text, ok =QtGui.QInputDialog.getText(QtGui.QDialog(),setTitle,Label)
			if ok:
				return text
			else:
				return ""
		except:
			return 0



