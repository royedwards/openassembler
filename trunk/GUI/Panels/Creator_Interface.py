# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openassembler_creator.ui'
#
# Created: Mon Sep 15 01:04:45 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.17.4
#
# WARNING! All changes made in this file will be lost!


from qt import *


class OpenAssembler_Creator(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("OpenAssembler_Creator")

        self.setMinimumSize(QSize(180,150))
        self.setMaximumSize(QSize(180,150))


        self.lineEdit1 = QLineEdit(self,"lineEdit1")
        self.lineEdit1.setGeometry(QRect(0,0,180,20))
        self.lineEdit1.setPaletteBackgroundColor(QColor(182,182,182))

        self.pushButton1_3_2 = QPushButton(self,"pushButton1_3_2")
        self.pushButton1_3_2.setGeometry(QRect(0,130,180,20))
        self.pushButton1_3_2.setPaletteBackgroundColor(QColor(122,230,107))
        self.pushButton1_3_2.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1_3_2.setToggleButton(0)

        self.listView1_3 = QListView(self,"listView1_3")
        self.listView1_3.addColumn(self.__tr("Nodetypes"))
        self.listView1_3.header().setClickEnabled(0,self.listView1_3.header().count() - 1)
        self.listView1_3.header().setResizeEnabled(0,self.listView1_3.header().count() - 1)
        self.listView1_3.setGeometry(QRect(0,20,180,110))
        self.listView1_3.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1_3.setSelectionMode(QListView.Extended)
        self.listView1_3.setResizeMode(QListView.LastColumn)

        self.languageChange()

        self.resize(QSize(180,150).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("OpenAssembler Creator"))
        self.lineEdit1.setText(self.__tr("Search"))
        self.pushButton1_3_2.setText(self.__tr("Create"))
        self.listView1_3.header().setLabel(0,self.__tr("Nodetypes"))
        self.listView1_3.clear()
        item_2 = QListViewItem(self.listView1_3,None)
        item_2.setOpen(1)
        item = QListViewItem(item_2,None)
        item.setText(0,self.__tr("Node3"))
        item_2.setOpen(1)
        item = QListViewItem(item_2,item)
        item.setText(0,self.__tr("Node2"))
        item_2.setText(0,self.__tr("Category"))

        item_3 = QListViewItem(self.listView1_3,item_2)
        item_3.setOpen(1)
        item = QListViewItem(item_3,item_2)
        item.setText(0,self.__tr("Node01"))
        item_3.setText(0,self.__tr("Category2"))



    def __tr(self,s,c = None):
        return qApp.translate("OpenAssembler_Creator",s,c)
