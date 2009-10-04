###OpenAssembler Node python file###

'''
define
{
	name init_Button
	tags qtmod
	input uiItem Entry "" ""
	input functionCall clicked "" ""
	input functionCall pressed "" ""
	input functionCall released "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_Button():
	def init_Button_main(self, **connections):
		Entry=connections["Entry"]
		clicked=connections["clicked"]
		pressed=connections["pressed"]
		released=connections["released"]
		if Entry=="":
			return 0
		else:
			if clicked!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("clicked()"), clicked)
			if pressed!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("pressed()"), pressed)
			if released!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("released()"), released)
			return 1
