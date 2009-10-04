###OpenAssembler Node python file###

'''
define
{
	name multiClicker
	tags qtmod
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class multiClicker():
	def multiClicker_main(self, **connections):
		try:
			for key in connections.keys():
				if key.split("_")[-1]=="Button":
					try:
						QtCore.QObject.connect(connections[key], QtCore.SIGNAL("clicked()"), connections[key.rsplit("_",1)[0]+"_Command"])
					except:
						pass
			return 1
		except:
			return 0