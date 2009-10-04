###OpenAssembler Node python file###

'''
define
{
	name init_ComboBox
	tags qtmod
	input array1D Items "[]" ""
	input uiItem Entry "" ""
	input string defaultItem "" ""
	input functionCall currentIndexChanged "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_ComboBox():
	def init_ComboBox_main(self, **connections):
		Items=connections["Items"]
		Entry=connections["Entry"]
		defaultItem=connections["defaultItem"]
		currentIndexChanged=connections["currentIndexChanged"]
		if Entry=="":
			return 0
		else:
			Entry.clear()
			try:
				index=0
				for n in range (0,len(Items)):
					Entry.addItem(QtCore.QString())
					Entry.setItemText(n,str(Items[n]))
					if defaultItem==str(Items[n]):
						index=n

				Entry.setCurrentIndex(index)

			except:
				Entry.clear()
			if currentIndexChanged!="":
				QtCore.QObject.connect(Entry, QtCore.SIGNAL("currentIndexChanged(QString)"), currentIndexChanged)
			return 1
