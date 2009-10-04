# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui

class keyHandler:
	def keyPressEvent(self,event):
		if str(event.text())=="+":
			self.oas_graphicsView.scale(1.25,1.25)
		elif event.key()==16777223:
			selected=self.oas_scene.selectedItems()
			if selected==[]:
				return
			for item in selected:
				self.delete_node(item.backID())
		elif str(event.text())=="-":
			self.oas_graphicsView.scale(0.8,0.8)
		elif str(event.text())=="h":
			self.oas_graphicsView.resetTransform()
		elif str(event.text())=="a":
			all=self.oas_scene.items()
			selection=[]
			for item in all:
				if str(item.backID())!="connection":
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
			self.oas_graphicsView.fitInView(QtCore.QRectF(minx,miny,wid,hei),QtCore.Qt.KeepAspectRatio)
		elif str(event.text())=="f":
			selection=self.oas_scene.selectedItems()
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
			self.oas_graphicsView.fitInView(QtCore.QRectF(minx,miny,wid,hei),QtCore.Qt.KeepAspectRatio)
			self.oas_graphicsView.scale(0.5,0.5)
		elif str(event.text())=="g":
			if self.oas_graphicsView.dragMode()==1:
				self.oas_graphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
			elif self.oas_graphicsView.dragMode()==2:
				self.oas_graphicsView.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
		elif str(event.text())==" ":
			if self.oas_splitter.sizes()[1]==0 and self.oas_splitter02.sizes()[0]==0 and self.oas_splitter02.sizes()[2]==0:
				self.oas_splitter02.setSizes([1,1,1])
				self.oas_splitter.setSizes([700,300])
			else:
				self.oas_splitter02.setSizes([0,1,0])
				self.oas_splitter.setSizes([1,0])
		elif str(event.text())=="r":
			self.do_run()

		elif str(event.text())=="u":
			self.reloadMCat()
