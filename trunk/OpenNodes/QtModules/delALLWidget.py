###OpenAssembler Node python file###

'''
define
{
	name delALLWidget
	tags qtmod
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class delALLWidget():
	def delALLWidget_main(self, **connections):
		_cache=connections["_cache"]
		if _cache.has_key("oas_Widgets"):

			for key in _cache["oas_Widgets"].keys():
				try:
					_cache["oas_Widgets"][str(key)]["widgetItem"].close()
					del _cache["oas_Widgets"][str(key)]
				except:
					return 0
			return 1
		else:
			return 1

