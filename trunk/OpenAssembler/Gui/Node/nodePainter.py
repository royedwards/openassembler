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

class nodePainter():
	def paint(self, painter, option, unused_widget):
		font=QtGui.QFont("Sans",10)
		font.setBold(True)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		painter.setFont(font)
		if option.state & QtGui.QStyle.State_Selected:
			borderColor = QtGui.QColor(212,255,42)
		else:
			borderColor = QtGui.QColor(51,51,51)

		if option.state & QtGui.QStyle.State_MouseOver:
			fillColor = QtGui.QColor(204,204,204).dark(120)
		else:
			fillColor=QtGui.QColor(204,204,204)

		connectioncolor=QtGui.QColor(51,51,51)
		trianglecolor=QtGui.QColor(210,210,210)
		greencolor=QtGui.QColor(90,160,44)
		yellowcolor=QtGui.QColor(192,185,115)
		bluecolor=QtGui.QColor(90,44,160)

		pen = QtGui.QPen()
		pen.setWidthF(1)
		pen.setColor(borderColor)
		painter.setPen(pen)
		
		painter.setBrush(QtGui.QBrush(borderColor))
		painter.drawRoundedRect(QtCore.QRect(40,0,self.sizex-80,60),10,10)

		pen.setColor(QtGui.QColor(125,125,125))
		painter.setPen(pen)
		painter.drawText(40,0,self.sizex-80,20,0x0084,self.nodeUpperLabel)

		font.setBold(False)
		painter.setFont(font)

		pen.setColor(connectioncolor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(connectioncolor))

		iz=[]
		for key in self.Input.keys():
			iz.append(key)

		oz=[]
		for key in self.Output.keys():
			oz.append(key)

		iz.sort()
		oz.sort()

		n=1
		while n<=len(iz):
			if self.connected_ins.count(iz[n-1])>0:
						pen.setColor(greencolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(greencolor))
			if str(self.Input[iz[n-1]]["value"])[:1]==">" or str(self.Input[iz[n-1]]["value"])[:1]=="$":
						pen.setColor(yellowcolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(yellowcolor))	
			if str(self.Input[iz[n-1]]["value"])[:1]=="=":
						pen.setColor(bluecolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(bluecolor))				
			self.ins.append([0,n*40,30,30,iz[n-1]])
			painter.drawRoundedRect(QtCore.QRect(0,n*40,50,30),5,5)
			pen.setColor(connectioncolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(connectioncolor))
			n+=1
		n=1
		while n<=len(oz):
			if self.connected_outs.count(oz[n-1])>0:
						pen.setColor(greencolor)
						painter.setPen(pen)
						painter.setBrush(QtGui.QBrush(greencolor))
			self.outs.append([self.sizex-30,n*40,30,30,oz[n-1]])
			painter.drawRoundedRect(QtCore.QRect(self.sizex-30,n*40,30,30),5,5)
			pen.setColor(connectioncolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(connectioncolor))
			n+=1

		pen.setColor(trianglecolor)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(trianglecolor))

		n=1
		while n<=len(iz):
			typ=self.Input[iz[n-1]]["variable_type"]
			icolor=self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			painter.drawPolygon(QtCore.QPoint(9,n*40+7),QtCore.QPoint(9,n*40+23),QtCore.QPoint(15,n*40+15))
			n+=1
		n=1
		while n<=len(oz):
			typ=self.Output[oz[n-1]]["variable_type"]
			icolor=self.getArrtibuteColor(typ)
			pen.setColor(icolor)
			painter.setPen(pen)
			painter.setBrush(QtGui.QBrush(icolor))
			painter.drawPolygon(QtCore.QPoint(self.sizex-13,n*40+7),QtCore.QPoint(self.sizex-13,n*40+23),QtCore.QPoint(self.sizex-7,n*40+15))
			n+=1

		pen.setColor(QtGui.QColor(0,0,0))
		pen.setWidth(2)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(fillColor))
		painter.drawRoundedRect(QtCore.QRect(20,20,self.sizex-40,self.sizey-30),10,10)

		n=1
		while n<=len(iz):
			painter.drawText(25,n*40,self.sizex/2,30,0x0081,iz[n-1])
			n+=1
		n=1
		while n<=len(oz):
			painter.drawText(self.sizex/2,n*40,self.sizex/2-25,30,0x0082,oz[n-1])
			n+=1

		trianglecolor=QtGui.QColor(210,210,210)
		orangecolor=QtGui.QColor(160,130,44)

		pen.setColor(orangecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		painter.setBrush(QtGui.QBrush(orangecolor))

		painter.drawEllipse(2,self.sizey-40,16,16)

		font.setBold(True)
		painter.setFont(font)
		pen.setColor(trianglecolor)
		pen.setWidth(2)
		painter.setPen(pen)

		painter.drawText(2,self.sizey-40,16,16,0x0084,"+")