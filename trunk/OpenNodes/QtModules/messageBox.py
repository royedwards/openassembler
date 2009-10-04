###OpenAssembler Node python file###

'''
define
{
	name messageBox
	tags qtmod
	input any returnValue "" ""
	input string setTitle "MessageBox" ""
	input string if_Zero "" ""
	input string if_NonZero "" ""
	output any _returnValue "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class messageBox():
	def messageBox_main(self, **connections):
		returnValue=connections["returnValue"]
		if_Zero=str(connections["if_Zero"])
		if_NonZero=str(connections["if_NonZero"])
		setTitle=str(connections["setTitle"])
		try:
			if returnValue==0:
				if str(if_Zero).strip()!="":
					QtGui.QMessageBox.information(QtGui.QMessageBox(),setTitle,str(if_Zero))
			else:
				if str(if_NonZero)!="":
					a=QtGui.QMessageBox.information(QtGui.QMessageBox(),setTitle,str(if_NonZero))
			return returnValue
		except:
			return returnValue



