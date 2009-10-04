###OpenAssembler Node python file###

'''
define
{
	name accessWidget
	tags qtmod
	input string widgetName "widget_node_has_to_be_cache_on" ""
	input string callName "" ""
	output any reply "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class accessWidget():
	def accessWidget_main(self, **connections):
		_cache=connections["_cache"]
		widgetName=str(connections["widgetName"])
		callName=str(connections["callName"])
		passt={}
		for key in connections.keys():
			if key=="_cache" or key=="_do_cache" or key=="_frame" or key=="widgetName" or key=="oas_output":
				pass
			else:
				passt[key]=connections[key]
		if _cache.has_key("oas_Widgets"):
			if _cache["oas_Widgets"].has_key(str(widgetName)):
				accessPoint=_cache["oas_Widgets"][str(widgetName)]["accessPoint"]
				return accessPoint.access(**passt)
			else:
				return 0
		else:
			return 0

