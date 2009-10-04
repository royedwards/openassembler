###OpenAssembler Node python file###

'''
define
{
	name inputDialog
	tags qtmod
	input string setTitle "QuestionBox" ""
	input string Question "" ""
	output string Answer "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class inputDialog():
	def inputDialog_main(self, **connections):
		Question=str(connections["Question"])
		setTitle=str(connections["setTitle"])
		try:
			rep=QtGui.QInputDialog.getText(QtGui.QDialog(),setTitle,Question)
			if rep[1]==False:
				return ""
			else:
				return str(rep[0])
			return rep
		except:
			return 0