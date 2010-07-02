# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compAssistant_compversion_v001.ui'
#
# Created: Thu Jun 17 11:10:55 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_compversionwidget(object):
    def setupUi(self, compversionwidget):
        compversionwidget.setObjectName("compversionwidget")
        compversionwidget.resize(528, 45)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(compversionwidget.sizePolicy().hasHeightForWidth())
        compversionwidget.setSizePolicy(sizePolicy)
        compversionwidget.setMinimumSize(QtCore.QSize(0, 45))
        compversionwidget.setMaximumSize(QtCore.QSize(16777215, 45))
        self.gridLayout_2 = QtGui.QGridLayout(compversionwidget)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.compversion = QtGui.QFrame(compversionwidget)
        self.compversion.setFrameShape(QtGui.QFrame.StyledPanel)
        self.compversion.setFrameShadow(QtGui.QFrame.Raised)
        self.compversion.setObjectName("compversion")
        self.gridLayout = QtGui.QGridLayout(self.compversion)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versiontext = QtGui.QLabel(self.compversion)
        self.versiontext.setObjectName("versiontext")
        self.horizontalLayout.addWidget(self.versiontext)
        self.line = QtGui.QFrame(self.compversion)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.indicator = QtGui.QToolButton(self.compversion)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../Volumes/projects/assetManager/projectDb/GYAR_Pipeline/compAssistant/Icons/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indicator.setIcon(icon)
        self.indicator.setAutoRaise(True)
        self.indicator.setObjectName("indicator")
        self.horizontalLayout.addWidget(self.indicator)
        self.line_2 = QtGui.QFrame(self.compversion)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.label_2 = QtGui.QLabel(self.compversion)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.generatebutton = QtGui.QToolButton(self.compversion)
        self.generatebutton.setObjectName("generatebutton")
        self.horizontalLayout.addWidget(self.generatebutton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
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

    def retranslateUi(self, compversionwidget):
        compversionwidget.setWindowTitle(QtGui.QApplication.translate("compversionwidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.versiontext.setText(QtGui.QApplication.translate("compversionwidget", "v001", None, QtGui.QApplication.UnicodeUTF8))
        self.indicator.setText(QtGui.QApplication.translate("compversionwidget", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("compversionwidget", "Mov:", None, QtGui.QApplication.UnicodeUTF8))
        self.generatebutton.setText(QtGui.QApplication.translate("compversionwidget", "Generate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("compversionwidget", "Client version:", None, QtGui.QApplication.UnicodeUTF8))
        self.sendbutton.setText(QtGui.QApplication.translate("compversionwidget", "Send", None, QtGui.QApplication.UnicodeUTF8))

