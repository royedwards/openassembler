from PyQt4 import QtGui,QtCore
from oas.gui.mouse import mouse

class drawNode(QtGui.QGraphicsItem,mouse):
	def __init__(self,function,globalSettings):
		QtGui.QGraphicsItem.__init__(self)
		self.globalSettings=globalSettings
		self.function=function
		self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable | QtGui.QGraphicsItem.ItemIsMovable | QtGui.QGraphicsItem.ItemIsFocusable)
		self.setAcceptsHoverEvents(True)
		self.setZValue(1)
		self.sizex=175
		self.name=self.function.nodename
		self.size_adjust()

	def size_adjust(self):
		self.sizey=(len(self.function.get_inputs())+1)*25+33
		if self.sizey<100:
			self.sizey=100

	def paint(self, painter, option, unused_widget):
		font=QtGui.QFont("Sans",10)
		font.setBold(True)
		font.setStyleStrategy(QtGui.QFont.ForceOutline)
		painter.setFont(font)
		pen = QtGui.QPen()
		pen.setWidthF(2)
		painter.setPen(pen)
		#mouse events
		if option.state & QtGui.QStyle.State_Selected:
			borderColor = QtGui.QColor(220,220,220)
		else:
			borderColor = QtGui.QColor(50,50,50)

		if option.state & QtGui.QStyle.State_MouseOver:
			fillColor = QtGui.QColor(204,204,204).dark(150)
		else:
			fillColor=QtGui.QColor(204,204,204)
		if self.function.error==True:
			fillColor=QtGui.QColor(200,50,50)
		pen.setColor(borderColor)
		painter.setPen(pen)
		#main shape
		painter.setBrush(QtGui.QBrush(borderColor))
		if self.function.nodetype=="network":
			painter.drawRect(0,0,self.sizex,60)
		else:
			painter.drawRoundedRect(QtCore.QRect(0,0,self.sizex,60),10,10)
		if self.globalSettings['current_level'].exitnode==self.function.nodename:
			painter.setBrush(QtGui.QBrush(QtGui.QColor(204,04,04)))
			painter.drawEllipse(self.sizex-20,3,15,15)
		painter.setBrush(QtGui.QBrush(fillColor))
		painter.drawRect(0,20,self.sizex,self.sizey-30)
		#header text
		pen.setColor(QtGui.QColor(125,125,125))
		painter.setPen(pen)
		if len(self.function.nodename)>15:
			name_to_display=self.function.nodename[:14]+"..."
		else:
			name_to_display=self.function.nodename
		painter.drawText(20,0,self.sizex-40,20,0x0084,name_to_display)
		#connections
		keys=self.function.get_inputs().keys()
		keys.sort()
		for n in range (1,(len(self.function.get_inputs())+1)):
			if self.function.get_inputs()[keys[n-1]]["route_to_parent"]==True:
				pen.setColor(QtGui.QColor(204,04,04))
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(QtGui.QColor(204,04,04)))
				painter.drawRect(2,5+n*25,20,15)
			else:
				pen.setColor(borderColor)
				painter.setPen(pen)
				painter.setBrush(QtGui.QBrush(borderColor))
				painter.drawRect(2,5+n*25,20,15)
		pen.setColor(QtGui.QColor(125,125,125))
		painter.setPen(pen)
		painter.setBrush(QtGui.QBrush(borderColor))	
		for n in range(0,len(keys)):
			if (len(str(keys[n]))>16):
				param_to_disp=str(keys[n][:14]+"...")
			else:
				param_to_disp=str(keys[n])
			painter.drawText(25,5+(n+1)*25,self.sizex-5,15,0x0081,param_to_disp)
		#plus
		pen.setColor(borderColor)
		painter.setPen(pen)
		painter.setBrush(QtGui.QBrush(borderColor))
		if self.function.extendable_connections!=False:
			painter.drawRect(2,self.sizey-27,20,15)
		#out
		painter.drawRect(self.sizex-20,self.sizey-27,20,15)		
		#plus text
		if self.function.extendable_connections!=False:
			pen.setColor(QtGui.QColor(125,125,125))
			painter.setPen(pen)
			painter.drawText(0,self.sizey-25,20,15,0x0084,"+")

	def boundingRect(self):
		return QtCore.QRectF(0, 0, self.sizex, self.sizey)

	def sceneSpaceRect(self):
		return self.mapToScene(QtCore.QRectF(0, 0, self.sizex, self.sizey))

	def define_ins(self,x,y):
		keys=self.function.get_inputs().keys()
		keys.sort()
		result=""
		for n in range (1,(len(self.function.get_inputs())+1)):
			if (2<x<20) and (5+n*25<y<5+n*25+15):		
				result=keys[n-1]
		return result


