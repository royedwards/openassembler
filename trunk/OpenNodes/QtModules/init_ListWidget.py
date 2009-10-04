###OpenAssembler Node python file###

'''
define
{
	name init_ListWidget
	tags qtmod
	input array1D Items "[]" ""
	input uiItem Entry "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class init_ListWidget():
	def init_ListWidget_main(self, **connections):
		Items=connections["Items"]
		Entry=connections["Entry"]
		if Entry=="":
			return 0
		else:
			Entry.clear()
			try:
				n=0
				for item in Items:
					QtGui.QListWidgetItem(Entry)
					Entry.item(n).setText(str(item))
					n+=1
			except:
				Entry.clear()

			return 1
