# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compAssistant_comments_v001.ui'
#
# Created: Thu Jun 17 11:10:24 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_commentswidget(object):
    def setupUi(self, commentswidget):
        commentswidget.setObjectName("commentswidget")
        commentswidget.resize(528, 34)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(commentswidget.sizePolicy().hasHeightForWidth())
        commentswidget.setSizePolicy(sizePolicy)
        commentswidget.setMinimumSize(QtCore.QSize(0, 34))
        commentswidget.setMaximumSize(QtCore.QSize(16777215, 34))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(155, 255, 155))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        commentswidget.setPalette(palette)
        self.gridLayout_2 = QtGui.QGridLayout(commentswidget)
        self.gridLayout_2.setMargin(2)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comments = QtGui.QFrame(commentswidget)
        self.comments.setFrameShape(QtGui.QFrame.StyledPanel)
        self.comments.setFrameShadow(QtGui.QFrame.Raised)
        self.comments.setObjectName("comments")
        self.gridLayout = QtGui.QGridLayout(self.comments)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.versiontext = QtGui.QLabel(self.comments)
        self.versiontext.setObjectName("versiontext")
        self.horizontalLayout.addWidget(self.versiontext)
        self.line = QtGui.QFrame(self.comments)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.commenttext = QtGui.QLabel(self.comments)
        self.commenttext.setObjectName("commenttext")
        self.horizontalLayout.addWidget(self.commenttext)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.comments)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.donechecker = QtGui.QCheckBox(self.comments)
        self.donechecker.setObjectName("donechecker")
        self.horizontalLayout.addWidget(self.donechecker)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.comments, 0, 0, 1, 1)

        self.retranslateUi(commentswidget)
        QtCore.QMetaObject.connectSlotsByName(commentswidget)

    def retranslateUi(self, commentswidget):
        commentswidget.setWindowTitle(QtGui.QApplication.translate("commentswidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        commentswidget.setToolTip(QtGui.QApplication.translate("commentswidget", "2010.06.17 submitted by Gergo", None, QtGui.QApplication.UnicodeUTF8))
        self.versiontext.setText(QtGui.QApplication.translate("commentswidget", "v003 (v017)", None, QtGui.QApplication.UnicodeUTF8))
        self.commenttext.setText(QtGui.QApplication.translate("commentswidget", "Bla bla bla...", None, QtGui.QApplication.UnicodeUTF8))

