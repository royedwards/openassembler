###OpenAssembler Node python file###

'''
define
{
	name init_TextEdit
	tags qtmod
	input string setPlainText "" ""
	input uiItem Entry "" ""
	input functionCall cursorPositionChanged "" ""
	input functionCall selectionChanged "" ""
	input functionCall textChanged "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_TextEdit():
	def init_TextEdit_main(self, **connections):
		setPlainText=connections["setPlainText"]
		Entry=connections["Entry"]
		cursorPositionChanged=connections["cursorPositionChanged"]
		selectionChanged=connections["selectionChanged"]
		textChanged=connections["textChanged"]
		if Entry=="":
			return 0
		else:
			Entry.setPlainText(setPlainText)
			if cursorPositionChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("cursorPositionChanged()"), cursorPositionChanged)
			if selectionChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("selectionChanged()"), selectionChanged)
			if textChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("textChanged()"), textChanged)
			return 1

