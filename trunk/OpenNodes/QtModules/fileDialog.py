###OpenAssembler Node python file###

'''
define
{
	name fileDialog
	tags qtmod
	input string Title "FileDialog" ""
	input string Filter "ALL (*.*)"
	input file defaultFolder "" ""
	output file getDirectory "" "" 
	output file getOpenName "" "" 
	output array1D getOpenNames "" "" 
	output file getSaveName "" "" 

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class fileDialog():
	def fileDialog_main(self, **connections):
		Title=str(connections["Title"])
		Filter=str(connections["Filter"])
		defaultFolder=str(connections["defaultFolder"])
		try: 
		    oas_output=connections["oas_output"]
		except:
		    oas_output="getDirectory"
		if oas_output=="getDirectory":
			return str(QtGui.QFileDialog.getExistingDirectory(QtGui.QFileDialog(),Title,defaultFolder))
		elif oas_output=="getOpenName":
			return str(QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),Title,defaultFolder,QtGui.QFileDialog().tr(Filter)))
		elif oas_output=="getOpenNames":
			files=QtGui.QFileDialog.getOpenFileNames(QtGui.QFileDialog(),Title,defaultFolder,QtGui.QFileDialog().tr(Filter))
			ret=[]
			for items in files:
				ret.append(str(items))
			return ret
		elif oas_output=="getSaveName":
			return str(QtGui.QFileDialog.getSaveFileName(QtGui.QFileDialog(),Title,"",QtGui.QFileDialog().tr(Filter)))