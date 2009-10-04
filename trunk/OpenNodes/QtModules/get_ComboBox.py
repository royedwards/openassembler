###OpenAssembler Node python file###

'''
define
{
	name get_ComboBox
	tags qtmod
	input uiItem Entry "" ""
	output string currentText "" ""
	output int currentIndex "" ""
	output int count "" ""
	output array1D Items "" ""
}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class get_ComboBox():
	def get_ComboBox_main(self, **connections):
		Entry=connections["Entry"]
		try: 
			oas_output=connections["oas_output"]
		except:
			oas_output="currentText"
		if Entry=="":
			return 0
		else:
			if oas_output=="currentText":
				return str(Entry.currentText())

			elif oas_output=="currentIndex":
				return int(Entry.currentIndex())

			elif oas_output=="count":
				return int(Entry.count())

			elif oas_output=="Items":
				ret=[]
				for n in range(0,int(Entry.count())):
					ret.append(str(Entry.itemText(n)))
				return ret
