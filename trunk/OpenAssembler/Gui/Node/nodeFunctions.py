#! /usr/bin/env python

# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui

class nodeFunctions():
	def addInput(self,attributeName,variabletype):
		# it is connected to the main dbase, so it automatically get the new
		#self.Input[attributeName]={"variable_type":variabletype,"options":"","value":""}
		self.recalculateSize()
		self.update()

	def removeInput(self,attributeName):
		# it is connected to the main dbase, so it automatically deleted
		self.recalculateSize()
		self.update()

	def recalculateSize(self):
		sizex=200
		iz=[]
		for key in self.Input.keys():
			iz.append(key)
		oz=[]
		for key in self.Output.keys():
			oz.append(key)
		if len(iz)>len(oz):
			sizey=len(iz)*40+60
		elif len(iz)<len(oz):
			sizey=len(oz)*40+60
		else:
			sizey=len(oz)*40+60
		if sizey<100:
			sizey=100
		sizey+=20
		self.sizex=sizex
		self.sizey=sizey

	def getArrtibuteColor(self,vartype):
		cat=self.varCategory(vartype)
		if vartype=="any":
			return QtGui.QColor(210,210,210)
		elif cat=="Text":
			return QtGui.QColor(143,89,2)
		elif cat=="Number":
			return QtGui.QColor(89,1,143)
		elif cat=="1DArray":
			return QtGui.QColor(207,114,159)
		elif cat=="2DArray":
			return QtGui.QColor(163,52,100)
		elif cat=="MultyEdit":
			return QtGui.QColor(92,53,102)
		elif cat=="ShotInfo":
			return QtGui.QColor(102,92,53)
		elif cat=="MultyShedule":
			return QtGui.QColor(53,102,92)
		elif cat=="MultyUser":
			return QtGui.QColor(223,185,110)
		else:
			return QtGui.QColor(0,0,0)

	def renameNode(self,name):
		self.nodeUpperLabel=name
		self.update()

	def markInput(self,input):
		self.connected_ins.append(input)

	def markOutput(self,output):
		self.connected_outs.append(output)

	def unMarkConnection(self,Connection):
		retin=[]
		retout=[]
		counter=0
		for item in self.connected_ins:
			if item==Connection:
				if counter==0:
					counter=1
				else:
					retin.append(item)
			else:
				retin.append(item)
		counter=0
		for item in self.connected_outs:
			if item==Connection:
				if counter==0:
					counter=1
				else:
					retout.append(item)
			else:
				retout.append(item)
		self.connected_outs=retout
		self.connected_ins=retin

	def boundingRect(self):
		return QtCore.QRectF(0, 0, self.sizex, self.sizey)

	def sceneSpaceRect(self):
		return self.mapToScene(QtCore.QRectF(0, 0, self.sizex, self.sizey))

	def do_oas_del_sel(self,ID):
		self.delete_node(ID)

	def do_oas_duplicate(self,ID):
		self.duplicateNode(ID)

	def do_oas_endnode(self,ID):
		self.setEndNode(ID)

	def define_ins(self,x,y):
		ax=x
		ay=y
		result=""
		for ots in self.ins:
			if ots[0]<ax<ots[0]+ots[2] and ots[1]<ay<ots[1]+ots[3]:
				result=ots[4]
		if result!="":
			return str(result)
		else:
			return ""

	def in_center(self,connection):
		center=[]
		for ins in self.ins:
			if str(ins[4])==str(connection):
				center=self.mapToScene(QtCore.QPointF(ins[0]+ins[2]/2,ins[1]+ins[3]/2))
		return center

	def out_center(self,connection):
		center=[]
		for ins in self.outs:
			if str(ins[4])==str(connection):
				center=self.mapToScene(QtCore.QPointF(ins[0]+ins[2]/2,ins[1]+ins[3]/2))
		return center

	def backID(self):
		return self.ID

	def allConnection(self):
		iz=[]
		for key in self.Input.keys():
			iz.append(key)
		oz=[]
		for key in self.Output.keys():
			oz.append(key)
		return iz+oz