###OpenAssembler Node python file###
'''
define
{
	name GYAR_compAssistantTabUpdater
	tags gyar
	input string tabWidget "" ""
	input any first "" ""
	input any secound "" ""
	output any result "" ""
}
'''
import os,sys
from PyQt4 import QtCore, QtGui

class GYAR_compAssistantTabUpdater:
   def GYAR_compAssistantTabUpdater_main(self,**connections):
	try:
		self.tabWidget=connections["tabWidget"]
	except:
		self.tabWidget=""
	try:
		self.first=connections["first"]
	except:
		self.first=""
	try:
		self.secound=connections["secound"]
	except:
		self.secound=""


	QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged (int)"),lambda t=self.tabWidget:chi(t=self.tabWidget, f=self.first, s=self.secound))

	return 1

def chi(t,f,s):
	if t.currentIndex()==0:
		f()
	else:
		s()