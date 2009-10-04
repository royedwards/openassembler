# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui
import Gui.Node.drawNode as DN

import sys

class mainmenu():
	def mousePressEvent(self,event):
		self.lastpos(event.scenePos().x(),event.scenePos().y())
		if event.button()==2:
			nodesincats=self.getavailableNodeList()
			eventpos=event.screenPos()
			mainmenu=QtGui.QMenu()
			mainmenu.setTitle("MainMenu")
			filemenu=QtGui.QMenu(mainmenu)
			filemenu.setTitle("File")
			editmenu=QtGui.QMenu(mainmenu)
			editmenu.setTitle("Other")
			executemenu=QtGui.QMenu(mainmenu)
			executemenu.setTitle("Execute")
			
			for key in nodesincats.keys():
				submenu=QtGui.QMenu(mainmenu)
				submenu.setTitle(key)
				list_sorted=nodesincats[key]
				list_sorted.sort()
				for item in list_sorted:
					submenu.addAction(item,lambda item=item:self.addNode(item))
				mainmenu.addMenu(submenu)

			filemenu.addAction("New",self.new_file)
			filemenu.addSeparator()
			filemenu.addAction("Open",self.open_file)
			#filemenu.addAction("Import",self.import_file)
			filemenu.addSeparator()
			filemenu.addAction("Save",self.save_file)
			filemenu.addAction("Save As",self.save_fileAs)
			filemenu.addSeparator()
			filemenu.addAction("Generate",self.do_generate)
			filemenu.addSeparator()
			filemenu.addAction("Exit", self.do_exit)

			editmenu.addAction("Delete Selected",self.do_oas_del_sel)
			editmenu.addSeparator()
			editmenu.addAction("Duplicate Selected",self.do_oas_duplicate)
			editmenu.addSeparator()
			editmenu.addAction("Run!!!",self.do_run)
			#editmenu.addAction("Duplicate with connections",self.do_oas_duplicate_wc)

			#executemenu.addAction("Preview",self.do_oas_preview)
			#executemenu.addAction("Run!!!",self.do_oas_run)

			mainmenu.addSeparator()
			mainmenu.addMenu(filemenu)
			mainmenu.addMenu(editmenu)
			#mainmenu.addMenu(executemenu)

			mainmenu.exec_(QtCore.QPoint(eventpos.x(),eventpos.y()))
		QtGui.QGraphicsItem.mousePressEvent(self, event)

	def do_oas_del_sel(self):
		selected=self.scene.selectedItems()
		if selected==[]:
			return
		for item in selected:
			self.delete_node(item.backID())

	def do_oas_duplicate(self):
		selected=self.scene.selectedItems()
		if selected==[]:
			return
		for item in selected:
			self.duplicateNode(item.backID())

	def do_exit(self):
		sys.exit()