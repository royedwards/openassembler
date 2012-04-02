import sys
from PyQt4 import QtCore, QtGui
from oas.gui.node import drawNode
from oas.gui.functions import gui_functions

class keyHandler(gui_functions):
	def keyPressEvent(self,event):
		if str(event.text())=="+":
			self.globalSettings['oas_view'].scale(1.25,1.25)
		elif event.key()==16777223 or event.key()==16777219:
			selected=self.globalSettings['oas_scene'].selectedItems()
			for item in selected:
				self.globalSettings['current_level'].del_node(node=item.name)
				self.globalSettings['connection_visualizer'].delNode(item.name)
				self.globalSettings['oas_scene'].removeItem(item)
				self.globalSettings['oas_scene'].update()
		elif str(event.text())=="-":
			self.globalSettings['oas_view'].scale(0.8,0.8)
		elif str(event.text())=="h":
			self.globalSettings['oas_view'].resetTransform()
		elif str(event.text())=="a":
			all=self.globalSettings['oas_scene'].items()
			selection=[]
			for item in all:
				if item.name!="__connections__not__to__recognize__":
					selection.append(item)
			if selection==[]:
				return
			fx=[]
			fy=[]
			sx=[]
			sy=[]
			for item in selection:
				bb=item.boundingRect()
				fx.append(item.mapToScene(bb).value(0).x())
				fy.append(item.mapToScene(bb).value(0).y())
				sx.append(item.mapToScene(bb).value(2).x())
				sy.append(item.mapToScene(bb).value(2).y())
			minx=min(fx)
			wid=max(sx)-minx
			miny=min(fy)
			hei=max(sy)-miny
			self.globalSettings['oas_view'].fitInView(QtCore.QRectF(minx,miny,wid,hei),QtCore.Qt.KeepAspectRatio)
		elif str(event.text())=="f":
			selection=self.globalSettings['oas_scene'].selectedItems()
			if selection==[]:
				return
			fx=[]
			fy=[]
			sx=[]
			sy=[]
			for item in selection:
				bb=item.boundingRect()
				fx.append(item.mapToScene(bb).value(0).x())
				fy.append(item.mapToScene(bb).value(0).y())
				sx.append(item.mapToScene(bb).value(2).x())
				sy.append(item.mapToScene(bb).value(2).y())
			minx=min(fx)
			wid=max(sx)-minx
			miny=min(fy)
			hei=max(sy)-miny
			self.globalSettings['oas_view'].fitInView(QtCore.QRectF(minx,miny,wid,hei),QtCore.Qt.KeepAspectRatio)
			self.globalSettings['oas_view'].scale(0.5,0.5)
		elif str(event.text())=="g":
			if self.globalSettings['oas_view'].dragMode()==1:
				self.globalSettings['oas_view'].setDragMode(QtGui.QGraphicsView.RubberBandDrag)
			elif self.globalSettings['oas_view'].dragMode()==2:
				self.globalSettings['oas_view'].setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
		elif str(event.text())==" ":
			if self.splitter.sizes()[1]==0:
				self.splitter.setSizes([700,200])
			else:
				self.splitter.setSizes([1,0])
		elif str(event.text())=="r":
			result=self.globalSettings['rootLevel'].run(start_node=self.globalSettings['rootLevel'].exitnode)
			self.globalSettings['statusbar'].showMessage("Execution result: "+str(result))
			for it in self.globalSettings['oas_scene'].items():	
				it.update()
		elif str(event.text())=="u":
			if self.globalSettings['current_level'].parent!=None:
				self.globalSettings['current_level']=self.globalSettings['current_level'].parent
				self.buildGUILevel()
		elif str(event.text())=="i":
			selected=self.globalSettings['oas_scene'].selectedItems()
			if len(selected)==1 and selected[0].function.nodetype=="network":
				self.globalSettings['current_level']=selected[0].function
				self.buildGUILevel()
		elif str(event.text())=="s":
			stats=self.globalSettings['current_level'].node_statistics()
			self.globalSettings['window'].statistics.setText(str(stats))
	

