###OpenAssembler Node python file###

'''
define
{
	name init_LineEntry
	tags qtmod
	input string setText "" ""
	input uiItem Entry "" ""
	input functionCall returnPressed "" ""
	input functionCall editingFinished "" ""
	input functionCall cursorPositionChanged "" ""
	input functionCall selectionChanged "" ""
	input functionCall textChanged "" ""
	input functionCall textEdited "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_LineEntry():
	def init_LineEntry_main(self, **connections):
		setText=connections["setText"]
		Entry=connections["Entry"]
		returnPressed=connections["returnPressed"]
		editingFinished=connections["editingFinished"]
		cursorPositionChanged=connections["cursorPositionChanged"]
		selectionChanged=connections["selectionChanged"]
		textChanged=connections["textChanged"]
		textEdited=connections["textEdited"]
		if Entry=="":
			return 0
		else:
			Entry.setText(setText)
			if returnPressed!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("returnPressed()"), returnPressed)
			if editingFinished!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("editingFinished()"), editingFinished)
			if cursorPositionChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("cursorPositionChanged()"), cursorPositionChanged)
			if selectionChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("selectionChanged()"), selectionChanged)
			if textChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("textChanged()"), textChanged)
			if textEdited!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("textEdited()"), textEdited)
			return 1

