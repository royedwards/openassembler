from PyQt4 import QtCore, QtGui,uic
import os,sys,copy
ROOTPATH=os.path.realpath(os.path.dirname(sys.argv[0]))

class variable_widget(QtGui.QWidget):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags(),globalSettings=None,paramname=None):
        QtGui.QWidget.__init__(self, parent, f)
	self.globalSettings=globalSettings
	self.paramname=paramname
	self.widget=uic.loadUi(ROOTPATH+"/oas/gui/design/attribute_widget.ui",self)
	QtCore.QObject.connect(self.widget.lineEdit, QtCore.SIGNAL("returnPressed()"), self.setParam)

    def get(self):
	return self.widget

    def setParam(self):
	value=str(self.widget.lineEdit.text())
	self.globalSettings['current_level'].set_value(node=self.globalSettings['attribute_content'].function.nodename,variable=self.paramname,value=value)


class variable_widget_number(QtGui.QWidget):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags(),globalSettings=None,paramname=None):
        QtGui.QWidget.__init__(self, parent, f)
	self.globalSettings=globalSettings
	self.paramname=paramname
	self.widget=uic.loadUi(ROOTPATH+"/oas/gui/design/attribute_widget_number.ui",self)
	QtCore.QObject.connect(self.widget.doubleSpinBox, QtCore.SIGNAL("valueChanged(double)"), self.setParamNum)

    def get(self):
	return self.widget

    def setParamNum(self):
	value=float(self.widget.doubleSpinBox.value())
	self.globalSettings['current_level'].set_value(node=self.globalSettings['attribute_content'].function.nodename,variable=self.paramname,value=value)

class variable_editor:
	def loadAttributes(self,globalSettings):
		self.globalSettings=globalSettings
		if self.globalSettings['window'].splitter.sizes()[1]==0:
			self.globalSettings['window'].splitter.setSizes([700,200])
		self.globalSettings['window'].oas_nodeName.setText(str(self.globalSettings['attribute_content'].function.nodename))
		self.globalSettings['window'].oas_attribute_nodetype.setText(str(self.globalSettings['attribute_content'].function.nodetype))
		QtCore.QObject.disconnect(self.globalSettings['window'].oas_nodeName, QtCore.SIGNAL("returnPressed()"), self.rename)
		QtCore.QObject.connect(self.globalSettings['window'].oas_nodeName, QtCore.SIGNAL("returnPressed()"), self.rename)
		keys=self.globalSettings['attribute_content'].function.get_inputs().keys()
		keys.sort()
		for wid in self.globalSettings['widgets']:
			wid.close()
		self.globalSettings['widgets']=[]
		for key in keys:
			if (self.globalSettings['attribute_content'].function.get_inputs()[key]['flag']!=True) and (self.globalSettings['attribute_content'].function.get_inputs()[key]['route_to_parent']!=True):
				if isinstance(self.globalSettings['attribute_content'].function.get_inputs()[key]['value'],int) or isinstance(self.globalSettings['attribute_content'].function.get_inputs()[key]['value'],float):
					widget=variable_widget_number(globalSettings=self.globalSettings,paramname=key).get()
					widget.label.setText(str(key))
					widget.doubleSpinBox.setValue((self.globalSettings['attribute_content'].function.get_inputs()[key]['value']))
				else:
					widget=variable_widget(globalSettings=self.globalSettings,paramname=key).get()
					widget.label.setText(str(key))
					widget.lineEdit.setText(str(self.globalSettings['attribute_content'].function.get_inputs()[key]['value']))
					
				self.globalSettings['window'].place_to_widgets.addWidget(widget)
				self.globalSettings['widgets'].append(widget)

	def rename(self):
		new=str(self.globalSettings['window'].oas_nodeName.text())
		ret=self.globalSettings['current_level'].rename_node(self.globalSettings['attribute_content'].function.nodename,new)
		self.globalSettings['connection_visualizer'].rename_node(self.globalSettings['attribute_content'].name,ret)
		self.globalSettings['attribute_content'].name=ret
		self.globalSettings['attribute_content'].update()


