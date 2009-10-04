###OpenAssembler Node python file###

'''
define
{
	name extendedAssetWidget
	tags qtwidg
	input file iconPath "" ""
	input dbPath dbPath "" ""
	input dbPath shotSetupPath "" ""
	input functionCall delAssetCall "" ""
	input functionCall updateAssetCall "" ""
	input functionCall updateSetupVersionCall "" ""
	input string AssetName "" ""
	input functionCall statusLEDClicked "" ""
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

class extendedAssetWidget(object):
    def extendedAssetWidget_main(self,**connections):
	self.dbPath=connections["dbPath"]
	self.iconPath=connections["iconPath"]
	self.AssetName=connections["AssetName"]
	self.delAssetCall=connections["delAssetCall"]
	self.updateAssetCall=connections["updateAssetCall"]
	self.statusLEDClicked=connections["statusLEDClicked"]
	self.shotSetupPath=connections["shotSetupPath"]
	self.updateSetupVersionCall=connections["updateSetupVersionCall"]
	return self


    def setupUi(self, versionAssetBlock):
        versionAssetBlock.setObjectName("versionAssetBlock")
        versionAssetBlock.setEnabled(True)
        versionAssetBlock.resize(640, 75)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(versionAssetBlock.sizePolicy().hasHeightForWidth())
        versionAssetBlock.setSizePolicy(sizePolicy)
        versionAssetBlock.setMinimumSize(QtCore.QSize(0, 75))
        versionAssetBlock.setMaximumSize(QtCore.QSize(16777215, 75))
        self.gridLayout_2 = QtGui.QGridLayout(versionAssetBlock)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.versionAssetMainFrame = QtGui.QFrame(versionAssetBlock)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionAssetMainFrame.sizePolicy().hasHeightForWidth())
        self.versionAssetMainFrame.setSizePolicy(sizePolicy)
        self.versionAssetMainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.versionAssetMainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.versionAssetMainFrame.setObjectName("versionAssetMainFrame")
        self.gridLayout = QtGui.QGridLayout(self.versionAssetMainFrame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status_indicator = QtGui.QToolButton(self.versionAssetMainFrame)
        self.status_indicator.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status_indicator.setIcon(icon)
        self.status_indicator.setIconSize(QtCore.QSize(32, 32))
        self.status_indicator.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.status_indicator.setAutoRaise(True)
        self.status_indicator.setArrowType(QtCore.Qt.NoArrow)
        self.status_indicator.setObjectName("status_indicator")
        self.horizontalLayout.addWidget(self.status_indicator)
        self.asset_name = QtGui.QLabel(self.versionAssetMainFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.asset_name.setFont(font)
        self.asset_name.setObjectName("asset_name")
        self.horizontalLayout.addWidget(self.asset_name)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.versionlist = QtGui.QComboBox(self.versionAssetMainFrame)
        self.versionlist.setObjectName("versionlist")
        self.horizontalLayout.addWidget(self.versionlist)
        self.getVersion_but = QtGui.QToolButton(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getVersion_but.sizePolicy().hasHeightForWidth())
        self.getVersion_but.setSizePolicy(sizePolicy)
        self.getVersion_but.setMinimumSize(QtCore.QSize(38, 39))
        self.getVersion_but.setMaximumSize(QtCore.QSize(38, 39))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/build-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getVersion_but.setIcon(icon1)
        self.getVersion_but.setIconSize(QtCore.QSize(32, 32))
        self.getVersion_but.setAutoRaise(True)
        self.getVersion_but.setObjectName("getVersion_but")
        self.horizontalLayout.addWidget(self.getVersion_but)
        self.line_3 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.live_label = QtGui.QLabel(self.versionAssetMainFrame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.live_label.setFont(font)
        self.live_label.setObjectName("live_label")
        self.horizontalLayout.addWidget(self.live_label)
        self.getLive_but = QtGui.QToolButton(self.versionAssetMainFrame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.iconPath+"/agt_action_success-256.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getLive_but.setIcon(icon2)
        self.getLive_but.setIconSize(QtCore.QSize(32, 32))
        self.getLive_but.setAutoRaise(True)
        self.getLive_but.setObjectName("getLive_but")
        self.horizontalLayout.addWidget(self.getLive_but)
        self.line = QtGui.QFrame(self.versionAssetMainFrame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.delete_but = QtGui.QToolButton(self.versionAssetMainFrame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.iconPath+"/cnrdelete-all-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_but.setIcon(icon3)
        self.delete_but.setIconSize(QtCore.QSize(32, 32))
        self.delete_but.setAutoRaise(True)
        self.delete_but.setObjectName("delete_but")
        self.horizontalLayout.addWidget(self.delete_but)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.versionAssetMainFrame, 0, 0, 1, 1)
        self.shotSetupFrame = QtGui.QFrame(versionAssetBlock)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotSetupFrame.sizePolicy().hasHeightForWidth())
        self.shotSetupFrame.setSizePolicy(sizePolicy)
        self.shotSetupFrame.setMinimumSize(QtCore.QSize(0, 32))
        self.shotSetupFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.shotSetupFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.shotSetupFrame.setObjectName("shotSetupFrame")
        self.gridLayout_3 = QtGui.QGridLayout(self.shotSetupFrame)
        self.gridLayout_3.setMargin(2)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.littleled = QtGui.QToolButton(self.shotSetupFrame)
        self.littleled.setMinimumSize(QtCore.QSize(16, 16))
        self.littleled.setMaximumSize(QtCore.QSize(16, 16))
        self.littleled.setIcon(icon)
        self.littleled.setIconSize(QtCore.QSize(16, 16))
        self.littleled.setAutoRaise(True)
        self.littleled.setObjectName("littleled")
        self.horizontalLayout_2.addWidget(self.littleled)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.label_2 = QtGui.QLabel(self.shotSetupFrame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.setupversionlist = QtGui.QComboBox(self.shotSetupFrame)
        self.setupversionlist.setMinimumSize(QtCore.QSize(0, 24))
        self.setupversionlist.setMaximumSize(QtCore.QSize(16777215, 24))
        self.setupversionlist.setObjectName("setupversionlist")
        self.horizontalLayout_2.addWidget(self.setupversionlist)
        self.getSetupVersion_but = QtGui.QToolButton(self.shotSetupFrame)
        self.getSetupVersion_but.setMinimumSize(QtCore.QSize(24, 24))
        self.getSetupVersion_but.setMaximumSize(QtCore.QSize(24, 24))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.iconPath+"/kdevelop_down-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getSetupVersion_but.setIcon(icon4)
        self.getSetupVersion_but.setIconSize(QtCore.QSize(16, 16))
        self.getSetupVersion_but.setObjectName("getSetupVersion_but")
        self.horizontalLayout_2.addWidget(self.getSetupVersion_but)
        spacerItem2 = QtGui.QSpacerItem(40, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.shotSetupFrame, 1, 0, 1, 1)

	self.setupDatas()

        QtCore.QMetaObject.connectSlotsByName(versionAssetBlock)
	QtCore.QObject.connect(self.delete_but, QtCore.SIGNAL("clicked()"), self.deleteAsset)
	QtCore.QObject.connect(self.getVersion_but, QtCore.SIGNAL("clicked()"), self.updateToThisVersion)
	QtCore.QObject.connect(self.getLive_but, QtCore.SIGNAL("clicked()"), self.updateToLiveVersion)
	QtCore.QObject.connect(self.getSetupVersion_but, QtCore.SIGNAL("clicked()"), self.updateToAttributeVersion)

    def do_LED_thing(self):
	if statusLEDClicked!="":
		self.statusLEDClicked(_dbPath=self.dbPath,_assetName=self.AssetName)

    def updateToThisVersion(self):
	version=str(self.versionlist.currentText()).split("(")[0].strip()
	cPath=getCPath(self.dbPath)
	if self.updateAssetCall!="":
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)

    def updateToLiveVersion(self):
	cPath=getCPath(self.dbPath)
	version=str(LivVer(cPath))
	if self.updateAssetCall!="":
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)

    def updateToAttributeVersion(self):
	version=str(self.setupversionlist.currentText()).strip()
	if self.updateAssetCall!="":
		self.updateSetupVersionCall(_version=version,_assetName=self.AssetName)

    def setupDatas(self,**attributes):
	if attributes.has_key("dbPath"):
		self.dbPath=attributes["dbPath"]
	if attributes.has_key("shotSetupPath"):
		self.shotSetupPath=attributes["shotSetupPath"]
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

	self.status_indicator.setIcon(icon)

	self.asset_name.setText(str(self.AssetName)+" ("+str(cVers)+")")
	self.live_label.setText("("+str(livVer)+")")

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
			self.setupversionlist.setItemText(n,str(svlist[n][0]))
			if str(svlist[n][0])==str(scVers):
				scurr=n
		self.setupversionlist.setCurrentIndex(scurr)
	except:
		pass

    def deleteAsset(self):
	if self.delAssetCall!="":
		self.delAssetCall(_dbPath=self.dbPath,_assetName=self.AssetName)

    def getName(self,**attributes):
	return str(self.AssetName)

    def access(self,**attributes):
	if attributes.has_key("callName"):
		if attributes["callName"]=="setupDatas":
			return self.setupDatas(**attributes)
		elif attributes["callName"]=="getName":
			return self.getName(**attributes)
		#if attributes["callName"]=="getPathBack":
		#	return self.getPathBack()
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
