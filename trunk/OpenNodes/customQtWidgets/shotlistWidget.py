###OpenAssembler Node python file###

'''
define
{
	name shotlistWidget
	tags qtwidg
	input any inputarray "" ""
	input functionCall jumpPressed "" ""
	input string iconPath "" ""
	input string serverPath "" ""
	output QtWidget initCall "" ""	


}
'''

from PyQt4 import QtCore, QtGui
import sys,os


class shotlistWidget(object):

    def shotlistWidget_main(self,**connections):
	self.inputarray=connections["inputarray"]
	self.iconPath=str(connections["iconPath"])
	self.serverPath=str(connections["serverPath"])
	self.jumpPressed=connections["jumpPressed"]
	return self

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(861, 58)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toolButton_2 = QtGui.QToolButton(self.frame)
        self.toolButton_2.setMinimumSize(QtCore.QSize(96, 54))
        self.toolButton_2.setMaximumSize(QtCore.QSize(96, 54))
        self.toolButton_2.setIconSize(QtCore.QSize(96, 54))
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout.addWidget(self.toolButton_2)
        spacerItem = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.prname = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prname.sizePolicy().hasHeightForWidth())
        self.prname.setSizePolicy(sizePolicy)
        self.prname.setMinimumSize(QtCore.QSize(100, 0))
        self.prname.setMaximumSize(QtCore.QSize(100, 16777215))
        self.prname.setObjectName("prname")
        self.horizontalLayout.addWidget(self.prname)
        self.line = QtGui.QFrame(self.frame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.shotname = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotname.sizePolicy().hasHeightForWidth())
        self.shotname.setSizePolicy(sizePolicy)
        self.shotname.setMinimumSize(QtCore.QSize(100, 0))
        self.shotname.setMaximumSize(QtCore.QSize(100, 16777215))
        self.shotname.setObjectName("shotname")
        self.horizontalLayout.addWidget(self.shotname)
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)

        spacerItem = QtGui.QSpacerItem(10, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.prioritiindicator = QtGui.QToolButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(24)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.prioritiindicator.sizePolicy().hasHeightForWidth())
        self.prioritiindicator.setSizePolicy(sizePolicy)
        self.prioritiindicator.setMinimumSize(QtCore.QSize(24, 24))
        self.prioritiindicator.setMaximumSize(QtCore.QSize(24, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prioritiindicator.setIcon(icon1)
        self.prioritiindicator.setIconSize(QtCore.QSize(24, 24))
        self.prioritiindicator.setAutoRaise(True)
        self.prioritiindicator.setObjectName("prioritiindicator")
        self.horizontalLayout.addWidget(self.prioritiindicator)

        spacerItem = QtGui.QSpacerItem(10, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)

        spacerItem = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)



        self.username = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QtCore.QSize(60, 0))
        self.username.setMaximumSize(QtCore.QSize(60, 16777215))
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)

        spacerItem = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.duetovalue = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.duetovalue.sizePolicy().hasHeightForWidth())
        self.duetovalue.setSizePolicy(sizePolicy)
        self.duetovalue.setMinimumSize(QtCore.QSize(85, 0))
        self.duetovalue.setMaximumSize(QtCore.QSize(85, 16777215))
        self.duetovalue.setObjectName("duetovalue")
        self.horizontalLayout.addWidget(self.duetovalue)
        self.line_5 = QtGui.QFrame(self.frame)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)

        spacerItem = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.statusname = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusname.sizePolicy().hasHeightForWidth())
        self.statusname.setSizePolicy(sizePolicy)
        self.statusname.setMinimumSize(QtCore.QSize(80, 0))
        self.statusname.setMaximumSize(QtCore.QSize(80, 16777215))
        self.statusname.setObjectName("statusname")
        self.horizontalLayout.addWidget(self.statusname)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.jumptothisshot = QtGui.QToolButton(self.frame)
        self.jumptothisshot.setMinimumSize(QtCore.QSize(24, 24))
        self.jumptothisshot.setMaximumSize(QtCore.QSize(24, 24))
        self.jumptothisshot.setObjectName("jumptothisshot")
        self.horizontalLayout.addWidget(self.jumptothisshot)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

	self.setupDatas()

	QtCore.QObject.connect(self.jumptothisshot, QtCore.SIGNAL("clicked()"), self.jum)

    def jum(self):
	self.jumpPressed(_project=self.inputarray[0],_sequence=self.inputarray[1],_shot=self.inputarray[2])

    def retranslateUi(self, Form):
        self.toolButton_2.setText("[ Preview ]")
        self.prname.setText("Project")
        self.shotname.setText("Shot")
        self.prioritiindicator.setText("...")
        self.label_3.setText("User: ")
        self.username.setText("user")
        self.label_5.setText("DueTo: ")
        self.duetovalue.setText("date")
        self.statusname.setText("Status")
        self.jumptothisshot.setText("->")


    def setupDatas(self,**attributes):
        self.prname.setText(self.inputarray[0])
	self.shotname.setText(self.inputarray[2])
	self.username.setText(self.inputarray[6])
        self.duetovalue.setText(self.inputarray[5])
        self.statusname.setText(self.inputarray[3])
	if self.inputarray[4]=="Normal":
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/yellow-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.prioritiindicator.setIcon(icon1)
	elif self.inputarray[4]=="High":
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/red-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.prioritiindicator.setIcon(icon1)
	else:
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.prioritiindicator.setIcon(icon1)

	if self.inputarray[3]=="Approved" or self.inputarray[3]=="OnHold":
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/white-off-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.prioritiindicator.setIcon(icon1)		

	prframe=self.serverPath+"/"+self.inputarray[0]+"/Movie/"+self.inputarray[1]+"/"+self.inputarray[2]+"/prF/prF.jpg"

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(prframe), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
