###OpenAssembler Node python file###

'''
define
{
	name compAssistant_comments
	tags qtwidg
	input string commentline "" ""
	input functionCall statusChanged "" ""
	output QtWidget initCall "" ""


}
'''

from PyQt4 import QtCore, QtGui
import sys,os

class compAssistant_comments(object):
    def compAssistant_comments_main(self,**connections):
	self.commentline=str(connections["commentline"])
	self.statusChanged=connections["statusChanged"]
	return self

    def setupUi(self, commentswidget):
        commentswidget.setObjectName("commentswidget")
        commentswidget.resize(528, 28)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(commentswidget.sizePolicy().hasHeightForWidth())
        commentswidget.setSizePolicy(sizePolicy)
        commentswidget.setMinimumSize(QtCore.QSize(0, 28))
        commentswidget.setMaximumSize(QtCore.QSize(16777215, 28))

        self.gridLayout_2 = QtGui.QGridLayout(commentswidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comments = QtGui.QFrame(commentswidget)
        self.comments.setFrameShape(QtGui.QFrame.StyledPanel)
        self.comments.setFrameShadow(QtGui.QFrame.Raised)
        self.comments.setObjectName("comments")
        self.gridLayout = QtGui.QGridLayout(self.comments)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
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

	self.setupDatas()

        QtCore.QMetaObject.connectSlotsByName(commentswidget)
	QtCore.QObject.connect(self.donechecker, QtCore.SIGNAL("stateChanged(int)"), self.makedone)


    def setupDatas(self,**attributes):
	sys.stderr = open("/dev/null", "w")
	devided=self.commentline.split("|")
	self.versiontext.setText(devided[0])
	self.commenttext.setText(devided[1])
	self.comments.setToolTip(str(devided[3])+", submitted by "+str(devided[4]))
	if str(devided[2])=="yes":
		self.donechecker.setCheckState(2)



    def makedone(self):
	devided=self.commentline.split("|")
	if str(devided[2])=="yes":
		self.statusChanged(line=self.commentline,value="no")
	else:
		self.statusChanged(line=self.commentline,value="yes")
