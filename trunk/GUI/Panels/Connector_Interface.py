# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openassembler_connector.ui'
#
# Created: Fri Sep 12 10:54:11 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class OpenAssembler_Connector(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("OpenAssembler_Connector")

        self.setMinimumSize(QSize(360,290))
        self.setMaximumSize(QSize(360,290))


        self.pushButton1_3_2 = QPushButton(self,"pushButton1_3_2")
        self.pushButton1_3_2.setGeometry(QRect(0,250,180,20))
        self.pushButton1_3_2.setPaletteBackgroundColor(QColor(122,230,107))
        self.pushButton1_3_2.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1_3_2.setToggleButton(0)

        self.pushButton1_3 = QPushButton(self,"pushButton1_3")
        self.pushButton1_3.setGeometry(QRect(180,250,180,20))
        self.pushButton1_3.setPaletteBackgroundColor(QColor(230,91,91))
        self.pushButton1_3.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1_3.setToggleButton(0)

        self.listView1_2 = QListView(self,"listView1_2")
        self.listView1_2.addColumn(self.__tr("To"))
        self.listView1_2.header().setClickEnabled(0,self.listView1_2.header().count() - 1)
        self.listView1_2.header().setResizeEnabled(0,self.listView1_2.header().count() - 1)
        self.listView1_2.setGeometry(QRect(180,110,180,140))
        self.listView1_2.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1_2.setSelectionMode(QListView.Extended)
        self.listView1_2.setResizeMode(QListView.LastColumn)

        self.listView1_3 = QListView(self,"listView1_3")
        self.listView1_3.addColumn(self.__tr("Connections"))
        self.listView1_3.header().setClickEnabled(0,self.listView1_3.header().count() - 1)
        self.listView1_3.header().setResizeEnabled(0,self.listView1_3.header().count() - 1)
        self.listView1_3.setGeometry(QRect(0,0,360,110))
        self.listView1_3.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1_3.setSelectionMode(QListView.Extended)
        self.listView1_3.setResizeMode(QListView.LastColumn)

        self.listView1 = QListView(self,"listView1")
        self.listView1.addColumn(self.__tr("From"))
        self.listView1.header().setClickEnabled(0,self.listView1.header().count() - 1)
        self.listView1.header().setResizeEnabled(0,self.listView1.header().count() - 1)
        self.listView1.setGeometry(QRect(0,110,180,140))
        self.listView1.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1.setSelectionMode(QListView.Extended)
        self.listView1.setResizeMode(QListView.LastColumn)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(0,270,360,20))
        self.textLabel1.setFrameShape(QLabel.StyledPanel)
        self.textLabel1.setFrameShadow(QLabel.Sunken)
        self.textLabel1.setLineWidth(1)
        self.textLabel1.setMargin(0)
        self.textLabel1.setMidLineWidth(2)

        self.languageChange()

        self.resize(QSize(360,290).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("OpenAssembler Connector"))
        self.pushButton1_3_2.setText(self.__tr("Connect"))
        self.pushButton1_3.setText(self.__tr("DeConnect"))
        self.listView1_2.header().setLabel(0,self.__tr("To"))
        self.listView1_2.clear()
        item = QListViewItem(self.listView1_2,None)
        item.setText(0,self.__tr("Item"))

        item_2 = QListViewItem(self.listView1_2,item)
        item_2.setOpen(1)
        item = QListViewItem(item_2,item)
        item.setText(0,self.__tr("Fortest"))
        item_2.setText(0,self.__tr("Test"))

        self.listView1_3.header().setLabel(0,self.__tr("Connections"))
        self.listView1_3.clear()
        item = QListViewItem(self.listView1_3,None)
        item.setText(0,self.__tr("Item"))

        item_3 = QListViewItem(self.listView1_3,item)
        item_3.setOpen(1)
        item = QListViewItem(item_3,item)
        item.setText(0,self.__tr("Fortest"))
        item_3.setText(0,self.__tr("Test"))

        self.listView1.header().setLabel(0,self.__tr("From"))
        self.listView1.clear()
        item = QListViewItem(self.listView1,None)
        item.setText(0,self.__tr("Item"))

        item_4 = QListViewItem(self.listView1,item)
        item_4.setOpen(1)
        item = QListViewItem(item_4,item)
        item.setText(0,self.__tr("Fortest"))
        item_4.setText(0,self.__tr("Test"))

        self.textLabel1.setText(self.__tr("Message line"))


    def __tr(self,s,c = None):
        return qApp.translate("OpenAssembler_Connector",s,c)
