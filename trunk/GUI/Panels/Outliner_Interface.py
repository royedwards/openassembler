# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openassembler_outliner.ui'
#
# Created: Fri Sep 12 10:53:49 2008
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class OpenAssembler_Outliner(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("OpenAssembler_Outliner")

        self.setSizePolicy(QSizePolicy(1,1,0,0,self.sizePolicy().hasHeightForWidth()))
        self.setMinimumSize(QSize(350,480))
        self.setMaximumSize(QSize(350,480))


        self.pushButton1_2_2_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2_2_2.setGeometry(QRect(0,440,50,20))
        self.pushButton1_2_2_2_2_2_2_2.setPaletteBackgroundColor(QColor(225,227,230))
        self.pushButton1_2_2_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2_2_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2_2_2_2.setGeometry(QRect(50,440,50,20))
        self.pushButton1_2_2_2_2_2_2_2_2.setPaletteBackgroundColor(QColor(230,173,140))
        self.pushButton1_2_2_2_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2_2_2_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2_2_2_2_2.setGeometry(QRect(100,440,50,20))
        self.pushButton1_2_2_2_2_2_2_2_2_2.setPaletteBackgroundColor(QColor(87,95,230))
        self.pushButton1_2_2_2_2_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2_2_2_2_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2_2_2_2_2_2.setGeometry(QRect(150,440,50,20))
        self.pushButton1_2_2_2_2_2_2_2_2_2_2.setPaletteBackgroundColor(QColor(143,138,230))
        self.pushButton1_2_2_2_2_2_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1 = QPushButton(self,"pushButton1")
        self.pushButton1.setGeometry(QRect(200,440,50,20))
        self.pushButton1.setPaletteBackgroundColor(QColor(230,223,92))
        self.pushButton1.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1.setToggleButton(0)

        self.pushButton1_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2")
        self.pushButton1_2_2_2_2.setGeometry(QRect(50,0,50,30))
        self.pushButton1_2_2_2_2.setPaletteBackgroundColor(QColor(229,207,230))
        pushButton1_2_2_2_2_font = QFont(self.pushButton1_2_2_2_2.font())
        self.pushButton1_2_2_2_2.setFont(pushButton1_2_2_2_2_font)
        self.pushButton1_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2_2.setGeometry(QRect(300,0,50,30))
        self.pushButton1_2_2_2_2_2_2.setPaletteBackgroundColor(QColor(151,230,153))
        self.pushButton1_2_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_3 = QPushButton(self,"pushButton1_2_3")
        self.pushButton1_2_3.setGeometry(QRect(250,0,50,30))
        self.pushButton1_2_3.setPaletteBackgroundColor(QColor(210,230,171))
        self.pushButton1_2_3.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2_2 = QPushButton(self,"pushButton1_2_2_2")
        self.pushButton1_2_2_2.setGeometry(QRect(200,0,50,30))
        self.pushButton1_2_2_2.setPaletteBackgroundColor(QColor(230,158,169))
        self.pushButton1_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2 = QPushButton(self,"pushButton1_2")
        self.pushButton1_2.setGeometry(QRect(100,0,50,30))
        self.pushButton1_2.setPaletteBackgroundColor(QColor(200,230,214))
        self.pushButton1_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_2_2 = QPushButton(self,"pushButton1_2_2")
        self.pushButton1_2_2.setGeometry(QRect(0,0,50,30))
        self.pushButton1_2_2.setPaletteBackgroundColor(QColor(188,211,230))
        self.pushButton1_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.listView1 = QListView(self,"listView1")
        self.listView1.addColumn(self.__tr("Nodes"))
        self.listView1.header().setResizeEnabled(0,self.listView1.header().count() - 1)
        self.listView1.setGeometry(QRect(0,30,175,410))
        self.listView1.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1.setSelectionMode(QListView.Extended)
        self.listView1.setResizeMode(QListView.LastColumn)

        self.pushButton1_2_2_2_2_2 = QPushButton(self,"pushButton1_2_2_2_2_2")
        self.pushButton1_2_2_2_2_2.setGeometry(QRect(150,0,50,30))
        self.pushButton1_2_2_2_2_2.setPaletteBackgroundColor(QColor(230,210,186))
        self.pushButton1_2_2_2_2_2.setFocusPolicy(QPushButton.NoFocus)

        self.pushButton1_3_2 = QPushButton(self,"pushButton1_3_2")
        self.pushButton1_3_2.setGeometry(QRect(250,440,50,20))
        self.pushButton1_3_2.setPaletteBackgroundColor(QColor(122,230,107))
        self.pushButton1_3_2.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1_3_2.setToggleButton(0)

        self.pushButton1_3 = QPushButton(self,"pushButton1_3")
        self.pushButton1_3.setGeometry(QRect(300,440,50,20))
        self.pushButton1_3.setPaletteBackgroundColor(QColor(230,91,91))
        self.pushButton1_3.setFocusPolicy(QPushButton.NoFocus)
        self.pushButton1_3.setToggleButton(0)

        self.listView1_2 = QListView(self,"listView1_2")
        self.listView1_2.addColumn(self.__tr("Connections"))
        self.listView1_2.header().setResizeEnabled(0,self.listView1_2.header().count() - 1)
        self.listView1_2.setGeometry(QRect(175,30,175,410))
        self.listView1_2.setPaletteBackgroundColor(QColor(182,182,182))
        self.listView1_2.setSelectionMode(QListView.Extended)
        self.listView1_2.setResizeMode(QListView.LastColumn)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(0,460,350,20))
        self.textLabel1.setFrameShape(QLabel.StyledPanel)
        self.textLabel1.setFrameShadow(QLabel.Sunken)
        self.textLabel1.setLineWidth(1)
        self.textLabel1.setMargin(0)
        self.textLabel1.setMidLineWidth(2)

        self.languageChange()

        self.resize(QSize(350,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("OpenAssembler Outliner"))
        self.pushButton1_2_2_2_2_2_2_2.setText(self.__tr("New"))
        self.pushButton1_2_2_2_2_2_2_2_2.setText(self.__tr("Open"))
        self.pushButton1_2_2_2_2_2_2_2_2_2.setText(self.__tr("Save"))
        self.pushButton1_2_2_2_2_2_2_2_2_2_2.setText(self.__tr("Save As"))
        self.pushButton1.setText(self.__tr("Settings"))
        self.pushButton1_2_2_2_2.setText(self.__tr("Rename"))
        self.pushButton1_2_2_2_2_2_2.setText(self.__tr("Run"))
        self.pushButton1_2_3.setText(self.__tr("EndNode"))
        self.pushButton1_2_2_2.setText(self.__tr("Delete"))
        self.pushButton1_2.setText(self.__tr("Attr."))
        self.pushButton1_2_2.setText(self.__tr("Add"))
        self.listView1.header().setLabel(0,self.__tr("Nodes"))
        self.listView1.clear()
        item = QListViewItem(self.listView1,None)
        item.setText(0,self.__tr("Item"))

        item_2 = QListViewItem(self.listView1,item)
        item_2.setOpen(1)
        item = QListViewItem(item_2,item)
        item.setText(0,self.__tr("Fortest"))
        item_2.setText(0,self.__tr("Test"))

        self.pushButton1_2_2_2_2_2.setText(self.__tr("(De)Con."))
        self.pushButton1_3_2.setText(self.__tr("Terminal"))
        self.pushButton1_3.setText(self.__tr("Close"))
        self.listView1_2.header().setLabel(0,self.__tr("Connections"))
        self.listView1_2.clear()
        item = QListViewItem(self.listView1_2,None)
        item.setText(0,self.__tr("Item"))

        item_3 = QListViewItem(self.listView1_2,item)
        item_3.setOpen(1)
        item = QListViewItem(item_3,item)
        item.setText(0,self.__tr("Fortest"))
        item_3.setText(0,self.__tr("Test"))

        self.textLabel1.setText(self.__tr("Message line"))


    def __tr(self,s,c = None):
        return qApp.translate("OpenAssembler_Outliner",s,c)
