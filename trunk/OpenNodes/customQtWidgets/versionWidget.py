###OpenAssembler Node python file###

'''
define
{
	name versionWidget
	tags qtwidg
	input file iconPath "" ""
	input functionCall onClickEvent "" ""
	output QtWidget initCall "" ""

}
'''

from PyQt4 import QtCore, QtGui
from OpenProject.getComments import getComments
from OpenProject.getVersionList import getVersionList


class versionWidget(object):
    def versionWidget_main(self,**connections):
	self.iconPath=connections["iconPath"]
	self.onClickEvent=connections["onClickEvent"]
	self.selected=""
	return self
 
    def setupUi(self, oas_versionWidget):
        self.gridLayout = QtGui.QGridLayout(oas_versionWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.oas_versionTree = QtGui.QTreeView(oas_versionWidget)
        self.oas_versionTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.oas_versionTree.setProperty("showDropIndicator", QtCore.QVariant(False))
        self.oas_versionTree.setAlternatingRowColors(True)
        self.oas_versionTree.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.oas_versionTree.setWordWrap(True)
        self.oas_versionTree.setHeaderHidden(True)
        self.gridLayout.addWidget(self.oas_versionTree, 0, 0, 1, 1)
        QtCore.QMetaObject.connectSlotsByName(oas_versionWidget)
	QtCore.QObject.connect(self.oas_versionTree, QtCore.SIGNAL("clicked(const QModelIndex &)"), self.comments_event)

    def comments_event(self,index):
		try:
			item = self.m.itemFromIndex(index)
			self.selected=item
			if self.getPathBack()!="":
				self.onClickEvent()
		except:
			self.selected=""

    def generateTree(self,attributes):
		if attributes.has_key("pathList"):
			dbpath=attributes["pathList"]
		else:
			return 0

		hier=[]
		for itempath in dbpath:
			co=getComs(itempath)
			cl={}
			for i in co:
				if cl.has_key(str(i[0])):
					cl[i[0]].append([i[1],i[2],i[3],i[4]])
				else:
					cl[i[0]]=[[i[1],i[2],i[3],i[4]]]

			hier.append([ itempath, cl])

		self.m=QtGui.QStandardItemModel()
		iroot=self.m.invisibleRootItem()
		self.com=iroot		
		self.oas_versionTree.setModel(self.m)

		for element in hier:
			e=QtGui.QStandardItem((str(element[0]).split(":")[-1]))
			e.setToolTip(str(element[0]))
			e.setSelectable(0)
			self.com.appendRow(e)
			vL=verList(str(element[0]))
			vL.sort()
			vL.reverse()
			for ite in vL:
					v=QtGui.QStandardItem((str(ite[0])))
					icn = QtGui.QIcon()
					if ite[1]=="live":
						icn.addPixmap(QtGui.QPixmap(self.iconPath+"/new32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
					else:
						icn.addPixmap(QtGui.QPixmap(self.iconPath+"/grey32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
					v.setIcon(icn)
					e.appendRow(v)
					try:
						for itt in element[1][ite[0]]:
							z=QtGui.QStandardItem((str(itt[3])))
							z.setToolTip(str(itt[0])+" ("+str(itt[1])+") \n"+str(itt[3]))
							icon = QtGui.QIcon()
							if itt[2]=="done":
								icon.addPixmap(QtGui.QPixmap(self.iconPath+"/agt_action_success-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
							else:
								icon.addPixmap(QtGui.QPixmap(self.iconPath+"/red-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
							z.setIcon(icon)
							v.appendRow(z)
					except:
						pass

		#self.oas_versionTree.expandAll()

    def getPathBack(self):
		if self.selected=="":
			return ""
		path=""
		version=""
		try:
			path=str(self.selected.parent().parent().toolTip())
			version=str(self.selected.parent().text())
		except:
			try:
				path=str(self.selected.parent().toolTip())
				version=str(self.selected.text())
			except:
				return ""
		if path=="" or version=="":
			return ""
		return path+"@"+version

    def access(self,**attributes):
	if attributes.has_key("callName"):
		if attributes["callName"]=="generateTree":
			return self.generateTree(attributes)
		if attributes["callName"]=="getPathBack":
			return self.getPathBack()
	else:
		return 0

def verList(Path):
	return getVersionList().getVersionList_main(Path=Path)

def getComs(Path):
	return getComments().getComments_main(Path=Path)