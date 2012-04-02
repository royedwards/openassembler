from PyQt4 import QtCore, QtGui,uic
import os,sys
from oas.gui.variable_editor import variable_editor
ROOTPATH=os.path.realpath(os.path.dirname(sys.argv[0]))

class mouse(variable_editor):
	def mousePressEvent(self, event):
		ax=event.pos().x()
		ay=event.pos().y()
		if event.button()==1:
			if (2<ax<20) and ((self.sizey-27)<ay<(self.sizey-7)):
				if self.function.extendable_connections!=False:
					addinput(globalSettings=self.globalSettings,node=self)
		if event.button()==2:
			result=""
			keys=self.function.get_inputs().keys()
			keys.sort()
			for n in range (1,(len(self.function.get_inputs())+1)):
				if (2<ax<20) and (5+n*25<ay<5+n*25+15):
					result=keys[n-1]
			if result!="":
				eventpos=event.screenPos()
				mainmenu=QtGui.QMenu()
				mainmenu.setTitle(result)
				mainmenu.addAction("Kill Connection",lambda result=result:self.kill_connection(result))
				mainmenu.addSeparator()
				mainmenu.addAction("de/Route to parent",lambda result=result:self.route_to_parent(result))
				mainmenu.addSeparator()
				mainmenu.addAction("Delete input: "+str(result),lambda result=result:self.empty(result))
				mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
				return
			else:
				eventpos=event.screenPos()
				mainmenu=QtGui.QMenu()
				mainmenu.setTitle(self.name)
				mainmenu.addAction("Delete: "+self.name,self.delNode)
				mainmenu.addSeparator()
				mainmenu.addAction("Set as Exit-Node",self.exitnode)
				mainmenu.addSeparator()
				mainmenu.addSeparator()
				mainmenu.addAction("Execute!",self.run_this)
				mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
				return
		self.setZValue(3)

	def mouseMoveEvent(self, event):
		ax=event.pos().x()
		ay=event.pos().y()
		eventpos=event.screenPos()
		if event.modifiers() & QtCore.Qt.ShiftModifier:
			self.globalSettings['tmp_pos']=[self.mapToScene(event.pos()).x(),self.mapToScene(event.pos()).y()]
			if (self.sizex-20<ax<self.sizex-2) and ((self.sizey-27)<ay<(self.sizey-7)):
				self.globalSettings['tmp_connection_from']=self.name
				return
			return
		QtGui.QGraphicsItem.mouseMoveEvent(self, event)
		for item in self.globalSettings['oas_scene'].selectedItems():
			if item.name!="__connections__not__to__recognize__":
				posx=item.sceneSpaceRect().value(0).x()
				posy=item.sceneSpaceRect().value(0).y()
				item.function.position=[posx,posy]
		self.globalSettings['connection_visualizer'].br=self.globalSettings['oas_scene'].itemsBoundingRect()

	def mouseDoubleClickEvent(self, event):
		self.globalSettings['attribute_content']=self
		self.loadAttributes(self.globalSettings)
		QtGui.QGraphicsItem.mouseDoubleClickEvent(self, event)

	def mouseReleaseEvent(self, event):
		#self.del_tmp()
		if self.globalSettings['tmp_connection_from']!="":
			try:
				self.setZValue(2)
				scenepos=self.mapToScene(event.pos())
				releaseitem=self.globalSettings['oas_scene'].itemAt(event.scenePos())
				itemlocalpos=releaseitem.mapFromScene(scenepos)
				ax=itemlocalpos.x()
				ay=itemlocalpos.y()
				result=releaseitem.define_ins(ax,ay)
				if result!="":
					self.globalSettings['tmp_connection_to_node']=str(releaseitem.function.nodename)
					self.globalSettings['tmp_connection_to_input']=str(result)
					ret=self.globalSettings['current_level'].add_connection(outnode=self.globalSettings['tmp_connection_from'],innode=self.globalSettings['tmp_connection_to_node'],variable=self.globalSettings['tmp_connection_to_input'])
					if ret==True:
						try:
							self.globalSettings['connection_visualizer'].delConnection(self.globalSettings['tmp_connection_to_node'],self.globalSettings['tmp_connection_to_input'])
						except:
							pass
						self.globalSettings['connection_visualizer'].addConnection(self.name,self.globalSettings['tmp_connection_to_node'],self.globalSettings['tmp_connection_to_input'])
					self.globalSettings['tmp_connection_to_node']=""
					self.globalSettings['tmp_connection_to_input']=""
					self.globalSettings['tmp_connection_from']=""
					return
				self.globalSettings['tmp_connection_to_node']=""
				self.globalSettings['tmp_connection_to_input']=""
				self.globalSettings['tmp_connection_from']=""
				QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
			except:
				QtGui.QGraphicsItem.mouseReleaseEvent(self, event)
				self.globalSettings['tmp_connection_to_node']=""
				self.globalSettings['tmp_connection_to_input']=""
				self.globalSettings['tmp_connection_from']=""
		else:
			self.globalSettings['tmp_connection_to_node']=""
			self.globalSettings['tmp_connection_to_input']=""
			self.globalSettings['tmp_connection_from']=""	
			QtGui.QGraphicsItem.mouseReleaseEvent(self, event)

	def empty(self,name):
		pass

	def route_to_parent(self,connection):
		if self.function.get_inputs()[connection]["route_to_parent"]==False:
			self.globalSettings['current_level'].set_route_to_parent(node=self.name,variable=connection,value=True)
		else:
			self.globalSettings['current_level'].set_route_to_parent(node=self.name,variable=connection,value=False)

	def run_this(self):
		result=self.globalSettings['current_level'].run(start_node=self.name)
		self.globalSettings['statusbar'].showMessage("Execution result: "+str(result))
		for it in self.globalSettings['oas_scene'].items():	
			it.update()

	def exitnode(self):
		self.globalSettings['current_level'].exitnode=self.name

	def kill_connection(self,connection):
		self.globalSettings['current_level'].del_connection(node=self.name,variable=connection)
		self.globalSettings['connection_visualizer'].delConnection(self.name,connection)

	def delNode(self):
		self.globalSettings['current_level'].del_node(node=self.name)
		self.globalSettings['connection_visualizer'].delNode(self.name)
		self.globalSettings['oas_scene'].removeItem(self)

class addinput(QtGui.QDialog):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags(),globalSettings=None,node=None):
        QtGui.QDialog.__init__(self, parent, f)
	self.globalSettings=globalSettings
	self.node=node
	self.window=uic.loadUi(ROOTPATH+"/oas/gui/design/new_input.ui",self)
	QtCore.QObject.connect(self.window.toolButton, QtCore.SIGNAL("clicked()"), self.add_input)
	self.show()

    def add_input(self):
	name=str(self.window.nameEdit.text())
	if self.window.checkBox_text.checkState()==2:
		default=str(self.window.def_edit.text())
	else:
		default=float(self.window.doubleSpinBox.value())
	ret=self.node.function.add_input(name=name,default_value=default)
	if ret==True:
		self.node.size_adjust()
		self.node.update()
		self.window.close()



