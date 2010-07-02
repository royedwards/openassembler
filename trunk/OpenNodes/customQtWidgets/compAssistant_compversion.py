###OpenAssembler Node python file###

'''
define
{
	name compAssistant_compversion
	tags qtwidg
	input file iconPath "" ""
	input string Version "" ""
	input string Status "" ""
	input string Mov "" ""
	input string ClientVersion "" "" 
	input functionCall generateEvent "" ""
	input functionCall openEvent "" ""
	input functionCall sendEvent "" ""
	input functionCall sendOpenEvent "" ""
	output QtWidget initCall "" ""


}
'''

from PyQt4 import QtCore, QtGui
import os, sys


class compAssistant_compversion(object):
    def compAssistant_compversion_main(self,**connections):
	self.iconPath=connections["iconPath"]
	self.Version=connections["Version"]
	self.Status=connections["Status"]
	self.Mov=connections["Mov"]
	self.ClientVersion=connections["ClientVersion"]
	self.generateEvent=connections["generateEvent"]
	self.sendEvent=connections["sendEvent"]
	self.openEvent=connections["openEvent"]
	self.sendOpenEvent=connections["sendOpenEvent"]
	return self

    def setupUi(self, compversionwidget):
        compversionwidget.setObjectName("compversionwidget")
        compversionwidget.resize(528, 35)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(compversionwidget.sizePolicy().hasHeightForWidth())
        compversionwidget.setSizePolicy(sizePolicy)
        compversionwidget.setMinimumSize(QtCore.QSize(0, 35))
        compversionwidget.setMaximumSize(QtCore.QSize(16777215, 35))
        self.gridLayout_2 = QtGui.QGridLayout(compversionwidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.compversion = QtGui.QFrame(compversionwidget)
        self.compversion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.compversion.setFrameShadow(QtGui.QFrame.Raised)
        self.compversion.setObjectName("compversion")
        self.gridLayout = QtGui.QGridLayout(self.compversion)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versiontext = QtGui.QLabel(self.compversion)
        self.versiontext.setObjectName("versiontext")
        self.horizontalLayout.addWidget(self.versiontext)

        #self.line = QtGui.QFrame(self.compversion)
        #self.line.setFrameShape(QtGui.QFrame.VLine)
        #self.line.setFrameShadow(QtGui.QFrame.Sunken)
        #self.line.setObjectName("line")
        #self.horizontalLayout.addWidget(self.line)

        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)

        self.indicator = QtGui.QToolButton(self.compversion)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(str(self.iconPath)+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indicator.setIcon(icon)
        self.indicator.setAutoRaise(True)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout.addWidget(self.indicator)

        #self.line_2 = QtGui.QFrame(self.compversion)
        #self.line_2.setFrameShape(QtGui.QFrame.VLine)
        #self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        #self.line_2.setObjectName("line_2")
        #self.horizontalLayout.addWidget(self.line_2)

        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)

        self.label_2 = QtGui.QLabel(self.compversion)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.generatebutton = QtGui.QToolButton(self.compversion)
        self.generatebutton.setObjectName("generatebutton")
        self.horizontalLayout.addWidget(self.generatebutton)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label_3 = QtGui.QLabel(self.compversion)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sendbutton = QtGui.QToolButton(self.compversion)
        self.sendbutton.setObjectName("sendbutton")
        self.horizontalLayout.addWidget(self.sendbutton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.compversion, 0, 0, 1, 1)

        self.retranslateUi(compversionwidget)
        QtCore.QMetaObject.connectSlotsByName(compversionwidget)
	self.setupDatas()

	QtCore.QObject.connect(self.generatebutton, QtCore.SIGNAL("clicked()"), self.gen)
	QtCore.QObject.connect(self.sendbutton, QtCore.SIGNAL("clicked()"), self.sen)

    def gen(self):
	if os.path.isfile(str(self.Mov)):
			self.openEvent(_version=str(self.Version))
	else:
			self.generateEvent(_version=str(self.Version),_lastword="")

    def sen(self):
	self.generateEvent(_version=str(self.Version),_lastword="client")

    def retranslateUi(self, compversionwidget):
        self.label_2.setText("Mov: ")
        self.generatebutton.setText("Generate")
        self.label_3.setText("Client version: ")
        self.sendbutton.setText("Send")

    def setupDatas(self,**attributes):
        self.versiontext.setText(str(self.Version))
	tms=self.Mov.rsplit("/",1)
	self.Mov=tms[0]+"/"+tms[1].lower()
	if os.path.isfile(str(self.Mov)):
			self.generatebutton.setText("Open")
	else:
			self.generatebutton.setText("Generate")
	if str(self.Status)=="yes":
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(str(self.iconPath)+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.indicator.setIcon(icon)	
	else:
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(str(self.iconPath)+"/red-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.indicator.setIcon(icon)

	if str(self.ClientVersion)=="no":
		self.sendbutton.setText("Send")
	else:
		self.sendbutton.setText(str(self.ClientVersion))
		self.sendbutton.setDisabled(True)

	if str(self.Status)!="yes":
		self.sendbutton.setDisabled(True)
		self.generatebutton.setDisabled(True)