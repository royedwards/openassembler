# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oas_attribute_string.ui'
#
# Created: Fri Jun 12 20:30:46 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os,sys

class Ui_oas_attribute_widget(object):
    def setupUi(self, oas_attribute_widget,name,value,status,variabletype,nodeSet):

	self.nodeSet=nodeSet	pathname = os.path.dirname(sys.argv[0])	print pathname	fullpath=os.path.abspath(pathname)	print fullpath
	if os.name=="nt":
		iconPath=fullpath+"/Icons"
	elif os.name=="posix":
		iconPath=fullpath+"/Icons"
	self.name=name


        oas_attribute_widget.setObjectName("oas_attribute_widget")
        oas_attribute_widget.resize(400, 40)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(oas_attribute_widget.sizePolicy().hasHeightForWidth())
        oas_attribute_widget.setSizePolicy(sizePolicy)
        oas_attribute_widget.setMinimumSize(QtCore.QSize(0, 40))
        oas_attribute_widget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.gridLayout = QtGui.QGridLayout(oas_attribute_widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.oas_widget_main_layout = QtGui.QHBoxLayout()
        self.oas_widget_main_layout.setObjectName("oas_widget_main_layout")
        self.oas_widget_led = QtGui.QToolButton(oas_attribute_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_widget_led.sizePolicy().hasHeightForWidth())
        self.oas_widget_led.setSizePolicy(sizePolicy)
        self.oas_widget_led.setMinimumSize(QtCore.QSize(16, 16))
        self.oas_widget_led.setMaximumSize(QtCore.QSize(16, 16))
        icon = QtGui.QIcon()

	self.oas_widget_led.setToolTip(str(variabletype))
	if status=="connected":
		icon.addPixmap(QtGui.QPixmap(iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	else:
		icon.addPixmap(QtGui.QPixmap(iconPath+"/white-off-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.oas_widget_led.setIcon(icon)
        self.oas_widget_led.setAutoRaise(True)
        self.oas_widget_led.setObjectName("oas_widget_led")
        self.oas_widget_main_layout.addWidget(self.oas_widget_led)
        spacerItem = QtGui.QSpacerItem(10, 5, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.oas_widget_main_layout.addItem(spacerItem)
        self.oas_name_w_label = QtGui.QLabel(oas_attribute_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_name_w_label.sizePolicy().hasHeightForWidth())
        self.oas_name_w_label.setSizePolicy(sizePolicy)
        self.oas_name_w_label.setObjectName("oas_name_w_label")
        self.oas_widget_main_layout.addWidget(self.oas_name_w_label)
        self.oas_widget_editor = QtGui.QLineEdit(oas_attribute_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oas_widget_editor.sizePolicy().hasHeightForWidth())
        self.oas_widget_editor.setSizePolicy(sizePolicy)
        self.oas_widget_editor.setObjectName("oas_widget_editor")
        self.oas_widget_main_layout.addWidget(self.oas_widget_editor)
        self.gridLayout.addLayout(self.oas_widget_main_layout, 0, 0, 1, 1)
	self.oas_widget_editor.setText(str(value))
	if status=="connected":
		self.oas_widget_editor.setReadOnly(True)

        self.retranslateUi(oas_attribute_widget)
        QtCore.QMetaObject.connectSlotsByName(oas_attribute_widget)
	QtCore.QObject.connect(self.oas_widget_editor, QtCore.SIGNAL("returnPressed()"),lambda entr=self.oas_widget_editor,nodeSet=nodeSet,name=self.name :setValue(nodeSet,entr,name))

    def retranslateUi(self, oas_attribute_widget):
        oas_attribute_widget.setWindowTitle(QtGui.QApplication.translate("oas_attribute_widget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.oas_widget_led.setText(QtGui.QApplication.translate("oas_attribute_widget", "...", None, QtGui.QApplication.UnicodeUTF8))

        self.oas_name_w_label.setText(QtGui.QApplication.translate("oas_attribute_widget", self.name, None, QtGui.QApplication.UnicodeUTF8))

def setValue(nodeSet,entr,name):
	val=str(entr.text())
	nodeSet(name,val)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    oas_attribute_widget = QtGui.QWidget()
    ui = Ui_oas_attribute_widget()
    ui.setupUi(oas_attribute_widget)
    oas_attribute_widget.show()
    sys.exit(app.exec_())

