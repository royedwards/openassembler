# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextEditor_v003.ui'
#
# Created: Tue Jan 27 17:24:58 2009
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_text_editor(object):
    def setupUi(self, text_editor):
        text_editor.setObjectName("text_editor")
        text_editor.resize(QtCore.QSize(QtCore.QRect(0,0,602,421).size()).expandedTo(text_editor.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(text_editor)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(1)
        self.gridlayout.setObjectName("gridlayout")

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")

        self.gridlayout1 = QtGui.QGridLayout(self.tab1)
        self.gridlayout1.setMargin(1)
        self.gridlayout1.setObjectName("gridlayout1")

        self.text_ed = Qsci.QsciScintilla(self.tab1)
        self.text_ed.setAcceptDrops(True)
        self.text_ed.setMidLineWidth(1)
        self.text_ed.setObjectName("text_ed")
        self.gridlayout1.addWidget(self.text_ed,0,0,1,1)
        self.tabWidget.addTab(self.tab1,"")
        self.gridlayout.addWidget(self.tabWidget,0,0,1,1)
        text_editor.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(text_editor)
        self.menubar.setGeometry(QtCore.QRect(0,0,602,19))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuLanguages_2 = QtGui.QMenu(self.menubar)
        self.menuLanguages_2.setObjectName("menuLanguages_2")

        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        text_editor.setMenuBar(self.menubar)

        self.actionOpen = QtGui.QAction(text_editor)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(text_editor)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_As = QtGui.QAction(text_editor)
        self.actionSave_As.setObjectName("actionSave_As")

        self.actionClose = QtGui.QAction(text_editor)
        self.actionClose.setObjectName("actionClose")

        self.actionClose_All = QtGui.QAction(text_editor)
        self.actionClose_All.setObjectName("actionClose_All")

        self.actionExit = QtGui.QAction(text_editor)
        self.actionExit.setCheckable(False)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setObjectName("actionExit")

        self.actionRun = QtGui.QAction(text_editor)
        self.actionRun.setObjectName("actionRun")

        self.actionPython = QtGui.QAction(text_editor)
        self.actionPython.setObjectName("actionPython")

        self.actionC = QtGui.QAction(text_editor)
        self.actionC.setObjectName("actionC")

        self.actionNew = QtGui.QAction(text_editor)
        self.actionNew.setObjectName("actionNew")

        self.actionAbout = QtGui.QAction(text_editor)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionClose_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuLanguages_2.addAction(self.actionPython)
        self.menuLanguages_2.addAction(self.actionC)
        self.menuTools.addAction(self.actionRun)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLanguages_2.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(text_editor)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(text_editor)

    def retranslateUi(self, text_editor):
        text_editor.setWindowTitle(QtGui.QApplication.translate("text_editor", "OpenTools TextEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QtGui.QApplication.translate("text_editor", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("text_editor", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLanguages_2.setTitle(QtGui.QApplication.translate("text_editor", "Languages", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("text_editor", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("text_editor", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("text_editor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("text_editor", "Save As..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("text_editor", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_All.setText(QtGui.QApplication.translate("text_editor", "Close All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_All.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+Shift+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("text_editor", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("text_editor", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython.setText(QtGui.QApplication.translate("text_editor", "Python", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC.setText(QtGui.QApplication.translate("text_editor", "C++", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("text_editor", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("text_editor", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("text_editor", "About", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qsci
