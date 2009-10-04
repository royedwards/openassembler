###OpenAssembler Node python file###

'''
define
{
	name addWidget
	tags qtmod
	input QtWidget Widget "" ""
	input string name "switche_cache_to_access_the_widget_later" ""
	input uiItem motherItem "" ""
	input uiItem layoutToPlace "" ""
	output string outName "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class addWidget():
	def addWidget_main(self, **connections):
		name=connections["name"]
		Widget=connections["Widget"]
		motherItem=connections["motherItem"]
		layoutToPlace=connections["layoutToPlace"]
		oas_output=connections["oas_output"]

		if Widget=="" or motherItem=="" or layoutToPlace=="":
			return 0

		item=QtGui.QWidget(motherItem)
		Widget.setupUi(item)
		layoutToPlace.addWidget(item)
		if str(connections["_do_cache"]) == "True":
			_cache=connections["_cache"]
			if _cache.has_key("oas_Widgets"):
				_cache["oas_Widgets"][str(name)]={"widgetItem":item,"accessPoint":Widget}
			else:
				_cache["oas_Widgets"]={str(name):{"widgetItem":item,"accessPoint":Widget}}

		if oas_output=="outName":
			return name
		else:
			return 1
