###OpenAssembler Node python file###

'''
define
{
	name init_DateEdit
	tags qtmod
	input string setDate "" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_DateEdit():
	def init_DateEdit_main(self, **connections):
		setDate=connections["setDate"]
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			try:
				qd=QtCore.QDate()
				qd.setDate(int(setDate.split(".")[0]),int(setDate.split(".")[1]),int(setDate.split(".")[2]))
				Entry.setDate(qd)
			except:
				pass
			return 1

