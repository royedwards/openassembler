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
from nodeFunctions import nodeFunctions
from nodeMouseEvents import nodeMouseEvents
from nodePainter import nodePainter

class DrawNode(QtGui.QGraphicsItem,nodeFunctions,nodeMouseEvents,nodePainter):
	def __init__(self,ID,NodeUpperLabel,Input,Output,collectedFunctions):
		QtGui.QGraphicsItem.__init__(self)
		sizex=200
		iz=[]
		for key in Input.keys():
			iz.append(key)
		oz=[]
		for key in Output.keys():
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
		self.setZValue(1)
		self.ID=ID
		self.nodeUpperLabel=NodeUpperLabel
		self.Input=Input
		self.Output=Output
		self.outs=[]
		self.ins=[]
		self.connected_outs=[]
		self.connected_ins=[]
		self.out_register=""
		self.in_register=""
		self.final_connect=collectedFunctions["connect_finally"]
		self.tmp_connect=collectedFunctions["connect_tmp"]
		self.delete_connection=collectedFunctions["delete_connection"]
		self.tmp_pos=collectedFunctions["pos_tmp"]
		self.delete_node=collectedFunctions["delete_node"]
		self.del_tmp=collectedFunctions["del_tmp"]
		self.scene=collectedFunctions["oas_scene"]
		self.duplicateNode=collectedFunctions["duplicateNode"]
		self.node_position=collectedFunctions["node_position"]
		self.setEndNode=collectedFunctions["setEndNode"]
		self.attributeE=collectedFunctions["attributeE"]
		self.add_newAttribute=collectedFunctions["add_newAttribute"]
		self.remove_Attribute=collectedFunctions["remove_Attribute"]
		self.varCategory=collectedFunctions["varCategory"]
		self.setFlags(QtGui.QGraphicsItem.ItemIsSelectable | QtGui.QGraphicsItem.ItemIsMovable | QtGui.QGraphicsItem.ItemIsFocusable)
		self.setAcceptsHoverEvents(True)
