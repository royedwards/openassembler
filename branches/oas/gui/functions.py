from oas.gui.node import drawNode
from PyQt4 import QtCore, QtGui

class gui_functions:
	def buildGUILevel(self):
		for item in self.globalSettings['oas_scene'].items():
			if item.name!="__connections__not__to__recognize__":
				self.globalSettings['connection_visualizer'].delNode(item.name)
				self.globalSettings['oas_scene'].removeItem(item)
		for key in self.globalSettings['current_level'].nodelist.keys():
			item=drawNode(self.globalSettings['current_level'].nodelist[key],self.globalSettings)
			effect=QtGui.QGraphicsDropShadowEffect()
			effect.setBlurRadius(30)
			effect.setOffset(5)
			item.setGraphicsEffect(effect)
			item.setPos(self.globalSettings['current_level'].nodelist[key].position[0],self.globalSettings['current_level'].nodelist[key].position[1])
			self.globalSettings['oas_scene'].addItem(item)
		for key in self.globalSettings['current_level'].nodelist.keys():
			for ins in self.globalSettings['current_level'].nodelist[key].get_inputs().keys():
				if self.globalSettings['current_level'].nodelist[key].get_inputs()[ins]["route_to_parent"]!=True:
					if self.globalSettings['current_level'].nodelist[key].get_inputs()[ins]["connection"]!="":
						self.globalSettings['connection_visualizer'].addConnection(self.globalSettings['current_level'].nodelist[key].get_inputs()[ins]["connection"],self.globalSettings['current_level'].nodelist[key].nodename,ins)
		self.globalSettings['connection_visualizer'].br=self.globalSettings['oas_scene'].itemsBoundingRect()	

