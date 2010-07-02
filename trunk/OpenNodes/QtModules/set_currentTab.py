###OpenAssembler Node python file###

'''
define
{
	name set_currentTab
	tags qtmod
	input uiItem tabWidget "" ""
	input uiItem tab "" ""
	output int result "" ""

}
'''

import os, sys
from PyQt4 import QtCore, QtGui

class set_currentTab():
	def set_currentTab_main(self, **connections):
		tabWidget=connections["tabWidget"]
		tab=connections["tab"]

		try:
			tabWidget.setCurrentIndex(tabWidget.indexOf(tab))
		except:
			return 0
		return 1
