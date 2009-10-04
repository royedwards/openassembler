###OpenAssembler Node python file###

'''
define
{
	name get_ListWidget
	tags qtmod
	input uiItem Entry "" ""
	output array1D selectedItems "[]" ""
	output string currentItem "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class get_ListWidget():
	def get_ListWidget_main(self, **connections):
		Entry=connections["Entry"]
		try: 
			oas_output=connections["oas_output"]
		except:
			oas_output="selectedItems"
		if Entry=="":
			return 0
		else:
			if oas_output=="selectedItems":
				ret=[]
				for item in Entry.selectedItems():
					ret.append(str(item.text()))
				return ret
			if oas_output=="currentItem":
				try:
					ci=Entry.currentItem()
					return str(ci.text())
				except:
					return ""