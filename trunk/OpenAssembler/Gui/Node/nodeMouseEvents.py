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

class nodeMouseEvents():
	def mousePressEvent(self, event):
		ax=event.pos().x()
		ay=event.pos().y()
		if event.button()==1:
			if (2<ax<16):
				if (self.sizey-40)<ay<(self.sizey-24):
					self.add_newAttribute(self.ID)

		if event.button()==2:
			result=""
			for ots in self.outs:
				if ots[0]<ax<ots[0]+ots[2] and ots[1]<ay<ots[1]+ots[3]:
					result=ots[4]
			for ots in self.ins:
				if ots[0]<ax<ots[0]+ots[2] and ots[1]<ay<ots[1]+ots[3]:
					result=ots[4]
			if result!="":
				eventpos=event.screenPos()
				mainmenu=QtGui.QMenu()
				mainmenu.setTitle("MainMenu")
				mainmenu.addAction("Kill Connection",lambda id=self.ID, result=result:self.delete_connection(id,result))
				mainmenu.addAction("Delete Attribute",lambda id=self.ID, result=result:self.remove_Attribute(id,result))
				mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
				return
			else:
				eventpos=event.screenPos()
				mainmenu=QtGui.QMenu()
				mainmenu.setTitle("MainMenu")
				mainmenu.addAction("Delete",lambda id=self.ID:self.do_oas_del_sel(id))
				mainmenu.addSeparator()
				mainmenu.addAction("Duplicate",lambda id=self.ID:self.do_oas_duplicate(id))
				mainmenu.addSeparator()
				mainmenu.addAction("Set as End-Node",lambda id=self.ID:self.do_oas_endnode(id))
				mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
				return
		self.setZValue(3)
		QtGui.QGraphicsItem.mousePressEvent(self, event)

	def mouseMoveEvent(self, event):
		ax=event.pos().x()
		ay=event.pos().y()
		if event.modifiers() & QtCore.Qt.ShiftModifier:
			self.tmp_pos(self.mapToScene(event.pos()).x(),self.mapToScene(event.pos()).y())
			result=""
			for ots in self.outs:
				if ots[0]<ax<ots[0]+ots[2] and ots[1]<ay<ots[1]+ots[3]:
					result=ots[4]
			if result!="":
				self.out_register=str(self.ID)+"."+str(result)
				self.tmp_connect(self.out_register)
				self.update()
				return
			self.update()
			return
		self.node_position()
		QtGui.QGraphicsItem.mouseMoveEvent(self, event)
		self.scene.update()

	def mouseDoubleClickEvent(self, event):
		self.attributeE(self.ID)
		QtGui.QGraphicsItem.mouseDoubleClickEvent(self, event)
		self.scene.update()

	def mouseReleaseEvent(self, event):
		self.del_tmp()
		try:
			self.setZValue(2)
			scenepos=self.mapToScene(event.pos())
			releaseitem=self.scene.itemAt(event.scenePos())
			itemlocalpos=releaseitem.mapFromScene(scenepos)
			ax=itemlocalpos.x()
			ay=itemlocalpos.y()
			result=releaseitem.define_ins(ax,ay)
			if result!="":
				self.in_register=str(releaseitem.backID())+"."+str(result)
				self.final_connect(self.out_register,self.in_register)
				self.scene.update()
				return
			self.out_register=""
			self.in_register=""
			QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
		except:
			QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
			self.out_register=""
			self.in_register=""