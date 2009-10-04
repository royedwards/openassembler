###OpenAssembler Node python file###

'''
define
{
	name questionBox
	tags qtmod
	input string setTitle "QuestionBox" ""
	input string Question "" ""
	output string Answer "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class questionBox():
	def questionBox_main(self, **connections):
		Question=str(connections["Question"])
		setTitle=str(connections["setTitle"])
		try:
			rep=QtGui.QMessageBox.question(QtGui.QMessageBox(),setTitle,str(Question),"Ok", "Cancel")
			return rep
		except:
			return returnValue



