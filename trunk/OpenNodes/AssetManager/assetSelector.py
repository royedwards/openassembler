###OpenAssembler Node python file###

'''
define
{
	name assetSelector
	tags amanage
	input any ALL "" ""
	input any Model "" ""
	input any Setup "" ""
	input any Cache "" ""
	input any Material "" ""
	input any Light "" ""
	input any Pass "" ""
	input any RenderSetup "" ""
	input any Engine "" ""
	input any Camera "" ""
	input any _refresh "" ""
	output int result "" ""

}
'''
import os, sys
from PyQt4 import QtCore, QtGui

class assetSelector():
	def assetSelector_main(self, **connections):
		self.cch=connections["_cache"]
		self.ref=connections["_refresh"]

		QtCore.QObject.connect(connections["ALL"], QtCore.SIGNAL("clicked()"), self.all_sel)
		QtCore.QObject.connect(connections["Model"], QtCore.SIGNAL("clicked()"), self.model_sel)


	def all_sel(self):
		self.cch["filterAssets"]="all"
		self.ref()
			
	def model_sel(self):
		print "Moddddddddddddddddddddddddddddddddddddddddddddd"
		self.cch["filterAssets"]="Model"
		self.ref()