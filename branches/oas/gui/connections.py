from PyQt4 import QtGui,QtCore
from oas.gui.menu import menuSetup

class drawConnections(QtGui.QGraphicsItem):
	def __init__(self,globalSettings):
		QtGui.QGraphicsItem.__init__(self)
		self.globalSettings=globalSettings
		self.name="__connections__not__to__recognize__"
		self.setZValue(0)
		self.lines=[]
		self.br=QtCore.QRectF(0, 0, 2000, 2000)

	def addConnection(self,outNode_name,inNode_name,variable):
		sceneItems=self.globalSettings['oas_scene'].items()
		for item in sceneItems:
			if item.name==inNode_name:
				inNode=item
			if item.name==outNode_name:
				outNode=item		
		out_ox=outNode.sizex-10
		out_oy=outNode.sizey-18
		keys=inNode.function.get_inputs().keys()
		keys.sort()
		for n in range (1,(len(inNode.function.get_inputs())+1)):
			if keys[n-1]==variable:
				in_ox=10
				in_oy=(n+1)*25-12
		self.lines.append([inNode,outNode,out_ox,out_oy,in_ox,in_oy,inNode_name,variable,outNode_name])

	def rename_node(self,old,new):
		newlines=[]
		for line in self.lines:
			if line[6]==old:
				newlines.append([line[0],line[1],line[2],line[3],line[4],line[5],new,line[7],line[8]])
			elif line[8]==old:
				newlines.append([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],new])
			else:
				newlines.append(line)
		self.lines=newlines

	def delConnection(self,inNode_name,variable):
		newlines=[]
		for line in self.lines:
			if line[6]==inNode_name and line[7]==variable:
				pass
			else:
				newlines.append(line)
		self.lines=newlines

	def delNode(self,noode_name):
		newlines=[]
		for line in self.lines:
			if line[6]==noode_name or line[8]==noode_name:
				pass
			else:
				newlines.append(line)
		self.lines=newlines

	def paint(self, painter, option, unused_widget):
                borderColor = QtGui.QColor(70,70,70)
                pen = QtGui.QPen()
                pen.setWidth(4)
                pen.setColor(borderColor)
                painter.setPen(pen)
                painter.setBrush(QtGui.QBrush(borderColor))     
                path=QtGui.QPainterPath()
		for line in self.lines:
			in_x=line[0].pos().x()+line[4]
			in_y=line[0].pos().y()+line[5]
			out_x=line[1].pos().x()+line[2]
			out_y=line[1].pos().y()+line[3]
			if (in_x-out_x)>0:
				fx=(in_x-out_x)/3*2+out_x
		                fy=out_y
		                sx=in_x-(in_x-out_x)/3*2
		                sy=in_y
		        else:
		                fx=-((in_x-out_x)/3*2)+out_x
		                fy=(out_y+in_y)/2
		                sx=in_x+(in_x-out_x)/3*2
		                sy=(out_y+in_y)/2
                        path.moveTo(out_x,out_y)
                        path.cubicTo(fx,fy,sx,sy,in_x,in_y)
                painter.strokePath(path,pen)

        def boundingRect(self):
		return QtCore.QRectF(self.br)

	def mousePressEvent(self,event):
		self.globalSettings['last_pos']=[self.mapToScene(event.pos()).x(),self.mapToScene(event.pos()).y()]
		eventpos=event.screenPos()
		if event.button()==2:
			mainmenu=QtGui.QMenu()
			menuSetup(self.globalSettings,mainmenu)
			mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
		QtGui.QGraphicsItem.mousePressEvent(self, event)



