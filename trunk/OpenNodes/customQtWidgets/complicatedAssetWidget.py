###OpenAssembler Node python file###

'''
define
{
	name complicatedAssetWidget
	tags qtwidg
	input file iconPath "" ""
	input dbPath dbPath "" ""
	input string dbType "" ""
	input dbPath shotSetupPath "" ""
	input functionCall delAssetCall "" ""
	input functionCall updateAssetCall "" ""
	input functionCall updateSetupVersionCall "" ""
	input string AssetName "" ""
	input array1D Passes "" ""
	input string PassBelonging "" ""
	input functionCall passChangeCall "" ""
	input functionCall buildChangeCall "" ""
	input functionCall saveCall "" ""
	input functionCall publishCall "" ""
	input string BuildBelonging "111" ""
	output QtWidget initCall "" ""


}
'''

from PyQt4 import QtCore, QtGui
from OpenProject.getVersionList import getVersionList
from OpenProject.getElementType import getElementType
from OpenProject.getLatestVersion import getLatestVersion
from OpenProject.getLiveVersion import getLiveVersion
from OpenProject.getCleanPath import getCleanPath
from OpenProject.getVersionFromPath import getVersionFromPath
from OpenProject.getVersionComment import getVersionComment


class complicatedAssetWidget(object):
    def complicatedAssetWidget_main(self,**connections):
	self.dbPath=connections["dbPath"]
	self.dbType=connections["dbType"]
	self.iconPath=connections["iconPath"]
	self.AssetName=connections["AssetName"]
	self.delAssetCall=connections["delAssetCall"]
	self.updateAssetCall=connections["updateAssetCall"]
	self.shotSetupPath=connections["shotSetupPath"]
	self.Passes=connections["Passes"]
	self.BuildBelonging=connections["BuildBelonging"]
	self.updateSetupVersionCall=connections["updateSetupVersionCall"]
	self.PassBelonging=str(connections["PassBelonging"]).split(",")
	self.passChangeCall=connections["passChangeCall"]
	self.buildChangeCall=connections["buildChangeCall"]
	self.saveCall=connections["saveCall"]
	self.publishCall=connections["publishCall"]
	self.vis=0
	self.sel=0
	if connections["_cache"].has_key("filterAssets"):
		self.filterAssets=connections["_cache"]["filterAssets"]
	else:
		self.filterAssets="all"
	return self


    def setupUi(self, versionAssetBlock):
	self.vab=versionAssetBlock
        versionAssetBlock.setObjectName("versionAssetBlock")
        versionAssetBlock.setEnabled(True)
        versionAssetBlock.resize(584, 173)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(versionAssetBlock.sizePolicy().hasHeightForWidth())
        versionAssetBlock.setSizePolicy(sizePolicy)
        versionAssetBlock.setMinimumSize(QtCore.QSize(0, 0))
        versionAssetBlock.setMaximumSize(QtCore.QSize(16777215, 173))
        self.gridLayout_3 = QtGui.QGridLayout(versionAssetBlock)
        self.gridLayout_3.setMargin(1)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.versionAssetMainFrame = QtGui.QFrame(versionAssetBlock)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionAssetMainFrame.sizePolicy().hasHeightForWidth())
        self.versionAssetMainFrame.setSizePolicy(sizePolicy)
        self.versionAssetMainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.versionAssetMainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.versionAssetMainFrame.setLineWidth(2)
        self.versionAssetMainFrame.setObjectName("versionAssetMainFrame")
        self.gridLayout = QtGui.QGridLayout(self.versionAssetMainFrame)
        self.gridLayout.setMargin(1)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.asset_selector = QtGui.QCheckBox(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asset_selector.sizePolicy().hasHeightForWidth())
        self.asset_selector.setSizePolicy(sizePolicy)
        self.asset_selector.setMaximumSize(QtCore.QSize(20, 20))
        self.asset_selector.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.asset_selector.setObjectName("asset_selector")
        self.horizontalLayout.addWidget(self.asset_selector)
        self.status_indicator = QtGui.QToolButton(self.versionAssetMainFrame)
        self.status_indicator.setEnabled(True)
        self.status_indicator.setMinimumSize(QtCore.QSize(24, 24))
        self.status_indicator.setMaximumSize(QtCore.QSize(24, 24))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status_indicator.setIcon(icon)
        self.status_indicator.setIconSize(QtCore.QSize(24, 24))
        self.status_indicator.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.status_indicator.setAutoRaise(True)
        self.status_indicator.setArrowType(QtCore.Qt.NoArrow)
        self.status_indicator.setObjectName("status_indicator")
        self.horizontalLayout.addWidget(self.status_indicator)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.asset_name = QtGui.QLabel(self.versionAssetMainFrame)
        self.asset_name.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.asset_name.setFont(font)
        self.asset_name.setObjectName("asset_name")
        self.horizontalLayout.addWidget(self.asset_name)
        spacerItem1 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line_2 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.versionlist = QtGui.QComboBox(self.versionAssetMainFrame)
        self.versionlist.setMaximumSize(QtCore.QSize(65, 24))
        self.versionlist.setObjectName("versionlist")
        self.horizontalLayout.addWidget(self.versionlist)
        self.line_3 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.getLive_but = QtGui.QToolButton(self.versionAssetMainFrame)
        self.getLive_but.setMinimumSize(QtCore.QSize(24, 24))
        self.getLive_but.setMaximumSize(QtCore.QSize(24, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/agt_action_success-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getLive_but.setIcon(icon1)
        self.getLive_but.setIconSize(QtCore.QSize(24, 24))
        self.getLive_but.setAutoRaise(True)
        self.getLive_but.setObjectName("getLive_but")
        self.horizontalLayout.addWidget(self.getLive_but)
        self.line_4 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.pub_but = QtGui.QToolButton(self.versionAssetMainFrame)
        self.pub_but.setMinimumSize(QtCore.QSize(24, 24))
        self.pub_but.setMaximumSize(QtCore.QSize(24, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.iconPath+"/cnruninstall-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pub_but.setIcon(icon2)
        self.pub_but.setIconSize(QtCore.QSize(24, 24))
        self.pub_but.setAutoRaise(True)
        self.pub_but.setObjectName("pub_but")
        self.horizontalLayout.addWidget(self.pub_but)
        self.line_5 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.save_but = QtGui.QToolButton(self.versionAssetMainFrame)
        self.save_but.setMinimumSize(QtCore.QSize(24, 24))
        self.save_but.setMaximumSize(QtCore.QSize(24, 24))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.iconPath+"/filesave-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_but.setIcon(icon3)
        self.save_but.setAutoRaise(True)
        self.save_but.setObjectName("save_but")
        self.horizontalLayout.addWidget(self.save_but)
        self.line = QtGui.QFrame(self.versionAssetMainFrame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.delete_but = QtGui.QToolButton(self.versionAssetMainFrame)
        self.delete_but.setMinimumSize(QtCore.QSize(24, 24))
        self.delete_but.setMaximumSize(QtCore.QSize(24, 24))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.iconPath+"/cnrdelete-all-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_but.setIcon(icon4)
        self.delete_but.setIconSize(QtCore.QSize(24, 24))
        self.delete_but.setAutoRaise(True)
        self.delete_but.setObjectName("delete_but")
        self.horizontalLayout.addWidget(self.delete_but)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.versionAssetMainFrame)
        self.shotSetupFrame = QtGui.QFrame(versionAssetBlock)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotSetupFrame.sizePolicy().hasHeightForWidth())
        self.shotSetupFrame.setSizePolicy(sizePolicy)
        self.shotSetupFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.shotSetupFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.shotSetupFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.shotSetupFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.shotSetupFrame.setObjectName("shotSetupFrame")
        self.gridLayout_2 = QtGui.QGridLayout(self.shotSetupFrame)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.littleled = QtGui.QToolButton(self.shotSetupFrame)
        self.littleled.setMinimumSize(QtCore.QSize(16, 16))
        self.littleled.setMaximumSize(QtCore.QSize(16, 16))
        self.littleled.setIcon(icon)
        self.littleled.setIconSize(QtCore.QSize(16, 16))
        self.littleled.setAutoRaise(True)
        self.littleled.setObjectName("littleled")
        self.horizontalLayout_3.addWidget(self.littleled)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_2 = QtGui.QLabel(self.shotSetupFrame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 24))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.setupversionlist = QtGui.QComboBox(self.shotSetupFrame)
        self.setupversionlist.setMinimumSize(QtCore.QSize(0, 24))
        self.setupversionlist.setMaximumSize(QtCore.QSize(65, 24))
        self.setupversionlist.setObjectName("setupversionlist")
        self.horizontalLayout_3.addWidget(self.setupversionlist)
        spacerItem4 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.main_box = QtGui.QCheckBox(self.shotSetupFrame)
        self.main_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.main_box.setObjectName("main_box")
        self.horizontalLayout_3.addWidget(self.main_box)
        self.effect_box = QtGui.QCheckBox(self.shotSetupFrame)
        self.effect_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.effect_box.setObjectName("effect_box")
        self.horizontalLayout_3.addWidget(self.effect_box)
        self.env_box = QtGui.QCheckBox(self.shotSetupFrame)
        self.env_box.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.env_box.setObjectName("env_box")
        self.horizontalLayout_3.addWidget(self.env_box)
        spacerItem5 = QtGui.QSpacerItem(40, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_6 = QtGui.QFrame(self.shotSetupFrame)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_2.addWidget(self.line_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtGui.QSpacerItem(45, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.shotSetupFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.pass_list = QtGui.QListWidget(self.shotSetupFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pass_list.sizePolicy().hasHeightForWidth())
        self.pass_list.setSizePolicy(sizePolicy)
        self.pass_list.setMaximumSize(QtCore.QSize(16777215, 100))
        self.pass_list.setAlternatingRowColors(True)
        self.pass_list.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.pass_list.setObjectName("pass_list")
        self.horizontalLayout_2.addWidget(self.pass_list)
        spacerItem9 = QtGui.QSpacerItem(90, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.shotSetupFrame)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.status_indicator.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Toggle Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_name.setText(QtGui.QApplication.translate("versionAssetBlock", "Software_test_name", None, QtGui.QApplication.UnicodeUTF8))
        self.versionlist.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Switch Asset Version", None, QtGui.QApplication.UnicodeUTF8))
        self.getLive_but.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Switch to Latest Asset Version", None, QtGui.QApplication.UnicodeUTF8))
        self.getLive_but.setText(QtGui.QApplication.translate("versionAssetBlock", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.pub_but.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Publish Assset", None, QtGui.QApplication.UnicodeUTF8))
        self.pub_but.setText(QtGui.QApplication.translate("versionAssetBlock", "Pub", None, QtGui.QApplication.UnicodeUTF8))
        self.save_but.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Save Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.save_but.setText(QtGui.QApplication.translate("versionAssetBlock", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_but.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Delete Asset", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_but.setText(QtGui.QApplication.translate("versionAssetBlock", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.littleled.setText(QtGui.QApplication.translate("versionAssetBlock", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("versionAssetBlock", "Animation: ", None, QtGui.QApplication.UnicodeUTF8))
        self.setupversionlist.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Switch to Preferences Version", None, QtGui.QApplication.UnicodeUTF8))
        self.main_box.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Is this in the Main Shot?", None, QtGui.QApplication.UnicodeUTF8))
        self.main_box.setText(QtGui.QApplication.translate("versionAssetBlock", "Main", None, QtGui.QApplication.UnicodeUTF8))
        self.effect_box.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Is this in the Effect Shot?", None, QtGui.QApplication.UnicodeUTF8))
        self.effect_box.setText(QtGui.QApplication.translate("versionAssetBlock", "Effect", None, QtGui.QApplication.UnicodeUTF8))
        self.env_box.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Is this in the Environment Shot?", None, QtGui.QApplication.UnicodeUTF8))
        self.env_box.setText(QtGui.QApplication.translate("versionAssetBlock", "Env", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("versionAssetBlock", "Passes:", None, QtGui.QApplication.UnicodeUTF8))
        self.pass_list.setToolTip(QtGui.QApplication.translate("versionAssetBlock", "Select the Passes where the Item plays (Very important!)", None, QtGui.QApplication.UnicodeUTF8))

	self.setupDatas()
	self.hideLowParts()

        QtCore.QMetaObject.connectSlotsByName(versionAssetBlock)
	QtCore.QObject.connect(self.status_indicator, QtCore.SIGNAL("clicked()"), self.hideLowParts)
	QtCore.QObject.connect(self.versionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToThisVersion)
	QtCore.QObject.connect(self.setupversionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToAttributeVersion)
	QtCore.QObject.connect(self.getLive_but, QtCore.SIGNAL("clicked()"), self.updateToLiveVersion)
	QtCore.QObject.connect(self.pub_but, QtCore.SIGNAL("clicked()"), self.pubAssT)
	QtCore.QObject.connect(self.save_but, QtCore.SIGNAL("clicked()"), self.saveAnimT)
	QtCore.QObject.connect(self.delete_but, QtCore.SIGNAL("clicked()"), self.deleteAsset)
	QtCore.QObject.connect(self.pass_list, QtCore.SIGNAL("itemSelectionChanged()"), self.passselchanged)

	QtCore.QObject.connect(self.main_box, QtCore.SIGNAL("stateChanged(int)"), self.buichanged)
	QtCore.QObject.connect(self.effect_box, QtCore.SIGNAL("stateChanged(int)"), self.buichanged)
	QtCore.QObject.connect(self.env_box, QtCore.SIGNAL("stateChanged(int)"), self.buichanged)

    def passselchanged(self):
	passesback=""
	for item in self.pass_list.selectedItems():
		passesback+=str(item.text())+","
	try:
		if passesback[-1:]==",":
			passesback=passesback[:-1]
	except:
		pass
	if self.passChangeCall!="":
		ret1=self.passChangeCall(_assetName=self.AssetName,_passBelongings=passesback)


    def buichanged(self):
	buildback=""
	if self.main_box.isChecked()==True:
		buildback+="1"
	else:
		buildback+="0"

	if self.effect_box.isChecked()==True:
		buildback+="1"
	else:
		buildback+="0"

	if self.env_box.isChecked()==True:
		buildback+="1"
	else:
		buildback+="0"

	if self.buildChangeCall!="":
		ret1=self.buildChangeCall(_assetName=self.AssetName,_buildBelongings=buildback)


    def updateToThisVersion(self):
	version=str(self.versionlist.currentText()).split("(")[0].strip()
	cPath=getCPath(self.dbPath)
	if self.updateAssetCall!="":
		QtCore.QObject.disconnect(self.versionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToThisVersion)
		ret1=self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)
		QtCore.QObject.connect(self.versionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToThisVersion)

    def updateToLiveVersion(self):
	cPath=getCPath(self.dbPath)
	version=str(LivVer(cPath))
	if self.updateAssetCall!="":
		QtCore.QObject.disconnect(self.versionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToThisVersion)
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)
		QtCore.QObject.connect(self.versionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToThisVersion)

    def updateToAttributeVersion(self):
	cPath=getCPath(self.dbPath)
	version=str(self.setupversionlist.currentText()).split("(")[0].strip()
	if self.updateSetupVersionCall!="":
		QtCore.QObject.disconnect(self.setupversionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToAttributeVersion)
		ret2=self.updateSetupVersionCall(_version=version,_assetName=self.AssetName,_dbPath=cPath+"@"+version)
		QtCore.QObject.connect(self.setupversionlist, QtCore.SIGNAL("currentIndexChanged(QString)"), self.updateToAttributeVersion)

    def pubAssT(self):
	if self.delAssetCall!="":
		self.publishCall(_dbPath=self.dbPath,_assetName=self.AssetName)

    def saveAnimT(self):
	if self.delAssetCall!="":
		self.saveCall(_dbPath=self.dbPath,_assetName=self.AssetName)

    def deleteAsset(self):
	if self.delAssetCall!="":
		self.delAssetCall(_dbPath=self.dbPath,_assetName=self.AssetName)

    def hideLowParts(self):
	if self.vis==0:
		self.shotSetupFrame.hide()
		self.vis=1
	elif self.vis==1:
		self.shotSetupFrame.show()
		self.vis=0

    def setupDatas(self,**attributes):
	if attributes.has_key("dbPath"):
		self.dbPath=attributes["dbPath"]
	if attributes.has_key("shotSetupPath"):
		self.shotSetupPath=attributes["shotSetupPath"]

	if self.dbType=="Pass" or self.dbType=="Misc":
		self.pub_but.setDisabled(True)

	cPath=getCPath(self.dbPath)
	cVers=getVerP(self.dbPath)

	scPath=getCPath(self.shotSetupPath)
	scVers=getVerP(self.shotSetupPath)

	vlist=verList(cPath)
	livVer=LivVer(cPath)
	latVer=LatVer(cPath)

	svlist=verList(scPath)
	slivVer=LivVer(scPath)
	slatVer=LatVer(scPath)

	try:
		nC=int(cVers[1:])
	except:
		nC=0
	try:
		nLi=int(livVer[1:])
	except:
		nLi=0
	try:
		nLa=int(latVer[1:])
	except:
		nLa=0

        icon = QtGui.QIcon()
        
	if nC==0:
		icon.addPixmap(QtGui.QPixmap(self.iconPath+"/white-off-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	elif nC==nLa:
		icon.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	elif nC<nLi:
		icon.addPixmap(QtGui.QPixmap(self.iconPath+"/red-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	else:
		icon.addPixmap(QtGui.QPixmap(self.iconPath+"/yellow-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	try:
		try:
			snC=int(scVers[1:])
		except:
			snC=0
		try:
			snLi=int(slivVer[1:])
		except:
			snLi=0
		try:
			snLa=int(slatVer[1:])
		except:
			snLa=0
		
		if snC<snLa:
			if self.vis==0:
				icon.addPixmap(QtGui.QPixmap(self.iconPath+"/blue-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	except:
		pass

	self.status_indicator.setIcon(icon)

	self.asset_name.setText(str(self.AssetName))

	curr=0
	self.versionlist.clear()
	for n in range(0,len(vlist)):
		self.versionlist.addItem(QtCore.QString())
		scom=gVC(cPath,str(vlist[n][0]))
		self.versionlist.setItemText(n,str(vlist[n][0])+" ("+str(scom)+")")
		if str(vlist[n][0])==str(cVers):
			curr=n
	self.versionlist.setCurrentIndex(curr)

        icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(self.iconPath+"/white-off-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.littleled.setIcon(icon)

	if str(self.BuildBelonging)[0]=="1":
		self.main_box.setChecked(True)
	else:
		self.main_box.setChecked(False)
	if str(self.BuildBelonging)[1]=="1":
		self.effect_box.setChecked(True)
	else:
		self.effect_box.setChecked(False)
	if str(self.BuildBelonging)[2]=="1":
		self.env_box.setChecked(True)
	else:
		self.env_box.setChecked(False)

	self.pass_list.clear()
	try:
		n=0
		for item in self.Passes:
			QtGui.QListWidgetItem(self.pass_list)
			self.pass_list.item(n).setText(str(item))
			for psez in self.PassBelonging:
				if psez.strip()==item:
					self.pass_list.item(n).setSelected(True)
			n+=1
	except:
		self.pass_list.clear()	

	try:

		try:
			snC=int(scVers[1:])
		except:
			snC=0
		try:
			snLi=int(slivVer[1:])
		except:
			snLi=0
		try:
			snLa=int(slatVer[1:])
		except:
			snLa=0

		icon = QtGui.QIcon()
		
		if snC==0:
			icon.addPixmap(QtGui.QPixmap(self.iconPath+"/white-off-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		elif snC==snLa:
			icon.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		elif snC<snLa:
			icon.addPixmap(QtGui.QPixmap(self.iconPath+"/red-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		else:
			icon.addPixmap(QtGui.QPixmap(self.iconPath+"/yellow-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		self.littleled.setIcon(icon)

		scurr=0
		self.setupversionlist.clear()
		for n in range(0,len(svlist)):
			self.setupversionlist.addItem(QtCore.QString())
			sscom=gVC(scPath,str(svlist[n][0]))
			self.setupversionlist.setItemText(n,str(svlist[n][0])+" ("+str(sscom)+")")
			if str(svlist[n][0])==str(scVers):
				scurr=n
		self.setupversionlist.setCurrentIndex(scurr)
	
	except:
		pass
	self.vab
	if self.filterAssets==self.dbType or self.filterAssets=="all":
		self.vab.show()

	elif self.dbType=="Deform" and self.filterAssets=="Setup":
		self.vab.show()

	elif self.dbType=="Misc" and self.filterAssets=="Model":
		self.vab.show()

	elif self.dbType=="Shader" and self.filterAssets=="Material":
		self.vab.show()

	else:
		self.vab.hide()

		self.toDeselect()



    def getName(self,**attributes):
	return str(self.AssetName)

    def isSelectede(self,**attributes):
	if self.asset_selector.isChecked()==True:
		return 1
	else:
		return 0

    def toSelect(self,**attributes):
	self.asset_selector.setChecked(True)

    def toDeselect(self,**attributes):
	self.asset_selector.setChecked(False)

    def access(self,**attributes):
	if attributes.has_key("callName"):
		if attributes["callName"]=="setupDatas":
			return self.setupDatas(**attributes)
		elif attributes["callName"]=="getName":
			return self.getName(**attributes)
		elif attributes["callName"]=="isSelected":
			return self.isSelectede(**attributes)
		elif attributes["callName"]=="select":
			return self.toSelect(**attributes)
		elif attributes["callName"]=="deselect":
			return self.toDeselect(**attributes)
	else:
		return 0

def verList(Path):
	return getVersionList().getVersionList_main(Path=Path)

def LatVer(Path):
	return getLatestVersion().getLatestVersion_main(Path=Path)

def LivVer(Path):
	return getLiveVersion().getLiveVersion_main(Path=Path)

def eType(Path):
	return getElementType.getElementType_main(Path=Path)

def getCPath(Path):
	return getCleanPath().getCleanPath_main(Path=Path)

def getVerP(Path):
	return getVersionFromPath().getVersionFromPath_main(Path=Path)

def gVC(Path,Version):
	return getVersionComment().getVersionComment_main(Path=Path,Version=Version)

