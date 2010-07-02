# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui
from Gui.OAS_Window.oas_attribute_string import Ui_oas_attribute_widget

class attributeEditor(Ui_oas_attribute_widget):
	def loadAttributes(self,attributeset,nodeSet):
		self.inAE=attributeset
		if self.oas_splitter.sizes()[1]==0:
			self.oas_splitter.setSizes([700,300])

		self.oas_nodeName.setText(self.inAE["name"])
		
		self.oas_attribute_nodetype.setText(self.inAE["nodetype"])
		QtCore.QObject.disconnect(self.oas_attribute_cache, QtCore.SIGNAL("stateChanged(int)"),self.nodeSettingE)
		if str(self.inAE["nodesettings"]["_do_cache"])=="True":
			self.oas_attribute_cache.setChecked(True)
		else:
			self.oas_attribute_cache.setChecked(False)
		QtCore.QObject.connect(self.oas_attribute_cache, QtCore.SIGNAL("stateChanged(int)"),self.nodeSettingE)

		sortedinputs=[]
		for key in self.inAE["inputs"].keys():
			sortedinputs.append(key)

		sortedinputs.sort()

		for ins in sortedinputs:
			sts=self.connectionCollector.getConnectionID(self.inAE["ID"],ins)
			if sts==[]:
				status="free"
			else:
				status="connected"
			varT=self.inAE["inputs"][ins]["variable_type"]
			sablock=QtGui.QWidget(self.oas_attribute_area)
			Ui_oas_attribute_widget().setupUi(sablock,str(ins),self.inAE["inputs"][ins]["value"],status,varT,nodeSet)
			self.place_to_widgets.addWidget(sablock)
			self.inAE["widget"][str(ins)]=sablock

		for ins in self.inAE["extras"].keys():
			status="free"
			varT=self.inAE["extras"][ins]["variable_type"]
			sablock=QtGui.QWidget(self.oas_attribute_area)
			Ui_oas_attribute_widget().setupUi(sablock,str(ins),self.inAE["extras"][ins]["value"],status,varT,nodeSet)
			self.place_to_widgets.addWidget(sablock)
			self.inAE["widget"][str(ins)]=sablock


	def cleanAttributes(self):
		self.inAE={}
		self.oas_attribute_nodetype.setText("empty")
		self.oas_attribute_cache.setChecked(False)
		self.oas_nodeName.setText("")