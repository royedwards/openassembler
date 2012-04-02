import sys
from PyQt4 import QtCore, QtGui
from oas.gui.node import drawNode
from oas.core.level import levelBase
from oas.core.functions import core_functions
from oas.gui.functions import gui_functions
from oas.core.level import levelBase

class menuSetup(core_functions,gui_functions):
	def __init__(self,globalSettings,mainmenu):
		self.globalSettings=globalSettings
		filemenu=QtGui.QMenu(mainmenu)
		filemenu.setTitle("File")
		filemenu.addAction("New",self.new_scene)
		filemenu.addSeparator()
		filemenu.addAction("Open",self.open_file)
		filemenu.addSeparator()
		filemenu.addAction("Save",self.save_file)
		filemenu.addAction("Save As",self.save_fileAs)
		filemenu.addSeparator()
		filemenu.addAction("Exit", self.do_exit)
		nodemenu=QtGui.QMenu(mainmenu)
		nodemenu.setTitle("Nodes")

		menuCategories={}
		for key in self.globalSettings['nodeCatalog'].keys():
			currentCategory=str(self.globalSettings['nodeCatalog'][key].function.__module__).split(".")[-1]
			if menuCategories.has_key(currentCategory):
				menuCategories[currentCategory].append(key)
			else:
				menuCategories[currentCategory]=[key]
		for key in menuCategories.keys():
			submenu=QtGui.QMenu(nodemenu)
			submenu.setTitle(key)
			for item in menuCategories[key]:
				submenu.addAction(item, lambda item=item: self.addNode(item))
			nodemenu.addMenu(submenu)
		nodemenu.addAction("newNodeLevel",self.addNodeLevel)
		mainmenu.addMenu(nodemenu)
		mainmenu.addMenu(filemenu)
		mainmenu.addAction("Execute!",self.execute)

        def do_exit(self):
                sys.exit()

	def execute(self):
		result=self.globalSettings['rootLevel'].run(start_node=self.globalSettings['rootLevel'].exitnode)
		self.globalSettings['statusbar'].showMessage("Execution result: "+str(result))
		for it in self.globalSettings['oas_scene'].items():	
			it.update()
		return result

	def empty(self):
		pass

	def addNodeLevel(self):
		node=levelBase(self.globalSettings['current_level'])
		self.add(node)

	def addNode(self,node_to_add):
		node=self.globalSettings['nodeCatalog'][node_to_add]
		self.add(node)

	def add(self,node):
		created_node=self.globalSettings['current_level'].add_node(node=node)
		created_node.position=[self.globalSettings['last_pos'][0],self.globalSettings['last_pos'][1]]
		item=drawNode(created_node,self.globalSettings)
		effect=QtGui.QGraphicsDropShadowEffect()
		effect.setBlurRadius(30)
		effect.setOffset(5)
		item.setGraphicsEffect(effect)
		item.setPos(self.globalSettings['last_pos'][0],self.globalSettings['last_pos'][1])
		self.globalSettings['oas_scene'].addItem(item)

	def save_file(self):
		currentfile=self.globalSettings['filename']
		if currentfile=="":
			currentfile = QtGui.QFileDialog.getSaveFileName(self.globalSettings['window'],'Save OpenAssebler Network!','untitled.oas')	
			if currentfile=="":
				return
		self.save_object(self.globalSettings['rootLevel'],str(currentfile))
		self.globalSettings['filename']=str(currentfile)

	def save_fileAs(self):
		currentfile = QtGui.QFileDialog.getSaveFileName(self.globalSettings['window'],'Save OpenAssebler Network!','untitled.oas')	
		if currentfile=="":
			return
		self.save_object(self.globalSettings['rootLevel'],str(currentfile))
		self.globalSettings['filename']=str(currentfile)

	def open_file(self):
		currentfile = QtGui.QFileDialog.getOpenFileName(self.globalSettings['window'], 'Open OpenAssembler Nerwork!','')
		if currentfile=="":
			return
		self.globalSettings['rootLevel']=self.load_object(str(currentfile))
		self.globalSettings['current_level']=self.globalSettings['rootLevel']
		self.globalSettings['filename']=str(currentfile)
		self.buildGUILevel()

	def new_scene(self):
		self.globalSettings['filename']=""
		self.globalSettings['rootLevel']=levelBase(None)
		self.globalSettings['current_level']=self.globalSettings['rootLevel']
		self.buildGUILevel()

