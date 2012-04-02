#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
from oas.core.loader import nodeCataloge
from oas.core.level import levelBase
ROOTPATH=os.path.realpath(os.path.dirname(sys.argv[0]))

from PyQt4 import QtGui,QtCore,uic
from oas.gui.keys import keyHandler
from oas.gui.menu import menuSetup
from oas.gui.mouse import mouse
from oas.gui.connections import drawConnections

class OASWindow(QtGui.QMainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)
	self.mainw=uic.loadUi(ROOTPATH+"/oas/gui/design/oas_main.ui",self)
  
class GUI_main(OASWindow,keyHandler,menuSetup,drawConnections):
	def __init__(self):
		OASWindow.__init__(self)
		brush=QtGui.QBrush(QtCore.Qt.BrushStyle(2))
		brush.setColor(QtGui.QColor(150,150,150))
		self.globalSettings={"last_pos":[1000,1000],"tmp_pos":[0,0],"tmp_connection_from":"","tmp_connection_to_node":"","tmp_connection_to_input":""}
		self.oas_graphic_view.setBackgroundBrush(brush)
		self.globalSettings['nodeCatalog']=nodeCataloge().buildCataloge()
		self.globalSettings['filename']=""
		self.globalSettings['oas_scene']=QtGui.QGraphicsScene()
		self.oas_graphic_view.setScene(self.globalSettings['oas_scene'])
		self.oas_graphic_view.centerOn(QtCore.QPointF(1000,1000))
		self.globalSettings['oas_view']=self.oas_graphic_view
		self.globalSettings['rootLevel']=levelBase(None)
		self.globalSettings['current_level']=self.globalSettings['rootLevel']
		self.splitter.setSizes([1,0])
		self.splitter_2.setSizes([1,0])
		self.globalSettings['statusbar']=self.statusBar()
		self.globalSettings['window']=self
		self.globalSettings['widgets']=[]
		self.globalSettings['attribute_content']={}

		menubar = self.menuBar()
		menuSetup(self.globalSettings,menubar)

		item=drawConnections(self.globalSettings)
		self.globalSettings['oas_scene'].addItem(item)
		self.globalSettings['connection_visualizer']=item

class init_no_gui:
	def start(self):
		self.globalSettings={"gui":False,"node_levels":{"root":[]},"current_level":"root"}
		self.globalSettings['nodeCatalog']=nodeCataloge().buildCataloge()
		print str(self.globalSettings['nodeCatalog']["oas_plus"].function)

def main():
		if len(sys.argv)>1 and sys.argv[1]=="no-gui":
			app=init_no_gui()
			app.start()
		else:	
			app = QtGui.QApplication(sys.argv)
			gui=GUI_main()
			gui.show()
			app.exec_()

if __name__ == "__main__":
	main()



