# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui

class assistantFunctions:
	def connect_tmp(self,outpoint):
		ots=outpoint.split(".")
		for item in self.oas_scene.items():
			if item.backID()==ots[0]:
				oitem=item
		self.inC.addConnection(oitem,ots[1])
		self.oas_scene.update()

	def pos_tmp(self,x,y):
		self.inC.mousePos(x,y)
		self.oas_scene.update()

	def del_tmp(self):
		self.inC.delLine()
		self.oas_scene.update()

	def lastPosition(self,x,y):
		self.last_point=QtCore.QPointF(x,y)

	def solveConnectionBug(self):
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

	def getavailableNodeList(self):
		return self.oas_menucats(mode="silent")

