###OpenAssembler Node python file###

'''
define
{
	name set_Visibility
	tags qtmod
	input uiItem Entry "" ""
	output int show "" ""
	output int hide "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class set_Visibility():
	def set_Visibility_main(self, **connections):
		Entry=connections["Entry"]
		try: 
		    oas_output=connections["oas_output"]
		except:
		    oas_output="hide"
		if Entry=="":
			return 0
		else:
			if oas_output=="hide":
				Entry.hide()
				return 1
			elif oas_output=="show":
				Entry.show()
				return 1
		return 0
