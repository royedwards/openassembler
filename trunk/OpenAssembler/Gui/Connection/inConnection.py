#! /usr/bin/env python

# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui
from Gui.Menu_Shortcut.mainMenu import mainmenu

class DrawConnection(QtGui.QGraphicsItem,mainmenu):
	def __init__(self,collectedInput):
		QtGui.QGraphicsItem.__init__(self)
		self.lines=[]
		self.mouse_poz=[0,0]
		self.lastpos=collectedInput["lastPosition"]
		self.scene=collectedInput["oas_scene"]
		self.addNode=collectedInput["addNode"]
		self.save_file=collectedInput["save_file"]
		self.save_fileAs=collectedInput["save_fileAs"]
		self.new_file=collectedInput["new_file"]
		self.open_file=collectedInput["open_file"]
		self.import_file=collectedInput["import_file"]
		self.delete_node=collectedInput["delete_node"]
		self.duplicateNode=collectedInput["duplicateNode"]
		self.do_run=collectedInput["do_run"]
		self.cleanE=collectedInput["cleanE"]
		self.do_generate=collectedInput["do_generate"]
		self.getavailableNodeList=collectedInput["getavailableNodeList"]
		self.setZValue(0)

	def addConnection(self,oitem,outpoint):
		self.lines=[[oitem,outpoint]]
		self.update()
		self.scene.update()

	def mousePos(self,x,y):
		self.mouse_poz=[x,y]

	def delLine(self):
		self.lines=[]

	def boundingRect(self):
		sr=self.scene.sceneRect()
		return sr.united(QtCore.QRectF(-4000,-4000,4000,4000))

	def paint(self, painter, option, unused_widget):
		borderColor = QtGui.QColor(70,70,70)
		pen = QtGui.QPen()
		pen.setWidth(4)
		pen.setColor(borderColor)
		painter.setPen(pen)
		painter.setBrush(QtGui.QBrush(borderColor))	
		path=QtGui.QPainterPath()
		for cline in self.lines:
			outcenter=cline[0].out_center(cline[1])
			incenter=QtCore.QPointF(self.mouse_poz[0],self.mouse_poz[1])
			path.moveTo(outcenter.x(),outcenter.y())
			if (incenter.x()-outcenter.x())>0:
				fx=(incenter.x()-outcenter.x())/3*2+outcenter.x()
				fy=outcenter.y()
				sx=incenter.x()-(incenter.x()-outcenter.x())/3*2
				sy=incenter.y()
			else:
				fx=-((incenter.x()-outcenter.x())/3*2)+outcenter.x()
				fy=(outcenter.y()+incenter.y())/2
				sx=incenter.x()+(incenter.x()-outcenter.x())/3*2
				sy=(outcenter.y()+incenter.y())/2
			path.cubicTo(fx,fy,sx,sy,incenter.x(),incenter.y())
		painter.strokePath(path,pen)

	def backID(self):
		return "connection"
