###OpenAssembler Node python file###

'''
define
{
	name delWidget
	tags qtmod
	input string name "name" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class delWidget():
	def delWidget_main(self, **connections):
		name=connections["name"]
		_cache=connections["_cache"]
		if _cache.has_key("oas_Widgets"):
			if _cache["oas_Widgets"].has_key(str(name)):
				try:
					_cache["oas_Widgets"][str(name)]["widgetItem"].close()
					del _cache["oas_Widgets"][str(name)]
				except:
					return 0
				return 1
			else:
				return 1
		else:
			return 1

