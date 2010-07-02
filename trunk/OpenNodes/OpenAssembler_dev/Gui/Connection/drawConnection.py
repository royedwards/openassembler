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

class DrawConnection(QtGui.QGraphicsItem):
	def __init__(self,scene):
		QtGui.QGraphicsItem.__init__(self)
		self.lines=[]
		self.scene=scene
		self.setZValue(0)

	def addConnection(self,oitem,outpoint,iitem,inpoint,cID):
		self.lines.append([oitem,outpoint,iitem,inpoint,cID])
		self.update()

	def getConnectionID(self,ID,Connection):
		ret=[]
		for item in self.lines:
			if item[0].backID()==ID and item[1]==Connection:
				ret.append(item[4])
			elif item[2].backID()==ID and item[3]==Connection:
				ret.append(item[4])
			else:
				pass
		return ret

	def removeConnection(self,ID,Connection):
		ret=[]
		for item in self.lines:
			if item[0].backID()==ID and item[1]==Connection:
				item[0].unMarkConnection(Connection)
				item[2].unMarkConnection(item[3])
			elif item[2].backID()==ID and item[3]==Connection:
				item[2].unMarkConnection(Connection)
				item[0].unMarkConnection(item[1])
			else:
				ret.append(item)
		self.lines=ret
		self.update()

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
			incenter=cline[2].in_center(cline[3])
			if outcenter==[] or incenter==[]:
				return
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
