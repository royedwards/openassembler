###OpenAssembler Node python file###

'''
define
{
	name assetWidget
	tags qtwidg
	input file iconPath "" ""
	input dbPath dbPath "" ""
	input functionCall delAssetCall "" ""
	input functionCall updateAssetCall "" ""
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

class assetWidget(object):
    def assetWidget_main(self,**connections):
	self.dbPath=connections["dbPath"]
	self.iconPath=connections["iconPath"]
	self.AssetName=connections["AssetName"]
	self.delAssetCall=connections["delAssetCall"]
	self.updateAssetCall=connections["updateAssetCall"]
	self.statusLEDClicked=connections["statusLEDClicked"]
	return self

    def setupUi(self, versionAssetBlock):
	self.versionAssetBlock=versionAssetBlock
        versionAssetBlock.setEnabled(True)
        versionAssetBlock.resize(510, 56)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(versionAssetBlock.sizePolicy().hasHeightForWidth())
        versionAssetBlock.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(versionAssetBlock)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.versionAssetMainFrame = QtGui.QFrame(versionAssetBlock)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionAssetMainFrame.sizePolicy().hasHeightForWidth())
        self.versionAssetMainFrame.setSizePolicy(sizePolicy)
        self.versionAssetMainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.versionAssetMainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.versionAssetMainFrame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setMargin(0)
        self.status_indicator = QtGui.QToolButton(self.versionAssetMainFrame)
        self.status_indicator.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.iconPath+"/green-on-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.status_indicator.setIcon(icon)
        self.status_indicator.setIconSize(QtCore.QSize(32, 32))
        self.status_indicator.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.status_indicator.setAutoRaise(True)
        self.status_indicator.setArrowType(QtCore.Qt.NoArrow)
        self.horizontalLayout_2.addWidget(self.status_indicator)
        self.asset_name = QtGui.QLabel(self.versionAssetMainFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.asset_name.setFont(font)
        self.horizontalLayout_2.addWidget(self.asset_name)
        spacerItem = QtGui.QSpacerItem(66, 35, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizontalLayout_2.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.versionlist = QtGui.QComboBox(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionlist.sizePolicy().hasHeightForWidth())
        self.versionlist.setSizePolicy(sizePolicy)
        self.versionlist.setMaximumSize(QtCore.QSize(55, 20))
        self.verticalLayout.addWidget(self.versionlist)
        self.getVersion_but = QtGui.QToolButton(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getVersion_but.sizePolicy().hasHeightForWidth())
        self.getVersion_but.setSizePolicy(sizePolicy)
        self.getVersion_but.setMinimumSize(QtCore.QSize(22, 22))
        self.getVersion_but.setMaximumSize(QtCore.QSize(1000, 22))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.iconPath+"/1rightarrow-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getVersion_but.setIcon(icon1)
        self.getVersion_but.setAutoRaise(True)
        self.verticalLayout.addWidget(self.getVersion_but)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_3 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.live_label = QtGui.QLabel(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.live_label.sizePolicy().hasHeightForWidth())
        self.live_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.live_label.setFont(font)
        self.verticalLayout_2.addWidget(self.live_label)
        self.getLive_but = QtGui.QToolButton(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getLive_but.sizePolicy().hasHeightForWidth())
        self.getLive_but.setSizePolicy(sizePolicy)
        self.getLive_but.setMinimumSize(QtCore.QSize(0, 0))
        self.getLive_but.setMaximumSize(QtCore.QSize(1000, 22))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.iconPath+"/build-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getLive_but.setIcon(icon2)
        self.getLive_but.setIconSize(QtCore.QSize(32, 32))
        self.getLive_but.setAutoRaise(True)
        self.verticalLayout_2.addWidget(self.getLive_but)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_4 = QtGui.QFrame(self.versionAssetMainFrame)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizontalLayout.addWidget(self.line_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.latest_label = QtGui.QLabel(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.latest_label.sizePolicy().hasHeightForWidth())
        self.latest_label.setSizePolicy(sizePolicy)
        self.verticalLayout_3.addWidget(self.latest_label)
        self.getLatest_but = QtGui.QToolButton(self.versionAssetMainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getLatest_but.sizePolicy().hasHeightForWidth())
        self.getLatest_but.setSizePolicy(sizePolicy)
        self.getLatest_but.setMinimumSize(QtCore.QSize(22, 22))
        self.getLatest_but.setMaximumSize(QtCore.QSize(1000, 22))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.iconPath+"/2rightarrow-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.getLatest_but.setIcon(icon3)
        self.getLatest_but.setIconSize(QtCore.QSize(32, 32))
        self.getLatest_but.setAutoRaise(True)
        self.verticalLayout_3.addWidget(self.getLatest_but)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.versionAssetMainFrame)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizontalLayout_2.addWidget(self.line)
        self.delete_but = QtGui.QToolButton(self.versionAssetMainFrame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.iconPath+"/cnrdelete-all-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_but.setIcon(icon4)
        self.delete_but.setIconSize(QtCore.QSize(32, 32))
        self.delete_but.setAutoRaise(True)
        self.horizontalLayout_2.addWidget(self.delete_but)
        self.gridLayout.addWidget(self.versionAssetMainFrame, 0, 0, 1, 1)

	self.setupDatas()

        QtCore.QMetaObject.connectSlotsByName(versionAssetBlock)
	QtCore.QObject.connect(self.delete_but, QtCore.SIGNAL("clicked()"), self.deleteAsset)
	QtCore.QObject.connect(self.getVersion_but, QtCore.SIGNAL("clicked()"), self.updateToThisVersion)
	QtCore.QObject.connect(self.getLive_but, QtCore.SIGNAL("clicked()"), self.updateToLiveVersion)
	QtCore.QObject.connect(self.getLatest_but, QtCore.SIGNAL("clicked()"), self.updateToLatestVersion)
	if self.statusLEDClicked!="":
		QtCore.QObject.connect(self.getLatest_but, QtCore.SIGNAL("clicked()"), self.deleteAsset)

    def do_LED_thing(self):
	if statusLEDClicked!="":
		self.statusLEDClicked(_dbPath=self.dbPath,_assetName=self.AssetName)

    def updateToThisVersion(self):
	version=str(self.versionlist.currentText())
	cPath=getCPath(self.dbPath)
	if self.updateAssetCall!="":
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)

    def updateToLiveVersion(self):
	cPath=getCPath(self.dbPath)
	version=str(LivVer(cPath))
	if self.updateAssetCall!="":
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)

    def updateToLatestVersion(self):
	cPath=getCPath(self.dbPath)
	version=str(LatVer(cPath))
	if self.updateAssetCall!="":
		self.updateAssetCall(_dbPath=cPath+"@"+version,_assetName=self.AssetName,_version=version)

    def setupDatas(self,**attributes):
	if attributes.has_key("dbPath"):
		self.dbPath=attributes["dbPath"]
	cPath=getCPath(self.dbPath)
	cVers=getVerP(self.dbPath)
	vlist=verList(cPath)
	livVer=LivVer(cPath)
	latVer=LatVer(cPath)

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
	self.latest_label.setText("("+str(latVer)+")")

	curr=0
	self.versionlist.clear()
	for n in range(0,len(vlist)):
		self.versionlist.addItem(QtCore.QString())
		self.versionlist.setItemText(n,str(vlist[n][0]))
		if str(vlist[n][0])==str(cVers):
			curr=n
	self.versionlist.setCurrentIndex(curr)

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