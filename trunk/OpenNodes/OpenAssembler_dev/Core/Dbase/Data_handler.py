# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

import os
import sys
from random import *
from copy import deepcopy
from variables import oas_variablechecker

# ###################################################################################
# this module is responsible for the runtime data management (and for all other data
# which is stored in memory)
# ##################################################################################
	
class oas_data_handler(oas_variablechecker):
	def oas_data_name2ID(self,mode="normal",name=""):
		ret=""
		for key in self.oas_rt.keys():
			if str(self.oas_rt[key]["name"])==str(name):
				ret=key
		if ret=="":
			if mode=="normal":
				print "[Error] Problem with name2ID with name: "+str(name)
			return 0
		else:
			return ret

	def oas_data_ID2name(self,mode="normal",ID=""):
		try:
			return str(self.oas_rt[str(ID)]["name"])
		except:
			if mode=="normal":
				print "[Error] Problem with ID2name with ID: "+str(ID)
			return 0

	def oas_data_nodeInputs(self,mode="normal",ID=""):
		try:
			return self.oas_rt[str(ID)]["inputs"]
		except:
			if mode=="normal":
				print "[Error] Problem with nodeInputs request on ID: "+str(ID)
			return 0

	def oas_data_nodeOutputs(self,mode="normal",ID=""):
		try:
			return self.oas_rt[str(ID)]["outputs"]
		except:
			if mode=="normal":
				print "[Error] Problem with nodeOutputs request on ID: "+str(ID)
			return 0

# ###########################################
# random generator for the nodes
# ###########################################

	def generate_random_with_check(self):
		randomized=0
		chk=True
		while chk==True:
			randomized=randrange(1000,1000000)
			chk=self.oas_rt.has_key(str("Node"+str(randomized)))
		return randomized
		
# ###############################################
# random generator for the connections
# maybe this 2 ran generator can be solved 
# in one function but for now, it is better
# ###############################################

	def generate_random_with_check_for_connection(self):
		randomized=0
		chk=True
		while chk==True:
			randomized=randrange(1000,1000000)
			chk=self.oas_rt_connections.has_key(str("Connection"+str(randomized)))
		return randomized

# ##################################################
# list the nodes or connections
# if the modde is 0 it will give you back a list
# of the sorted nodes/connections
# ###################################################

	def oas_data_list(self,mode="normal",listtype="nodetypes",searchtag=""):
		returnvalue=[]
		if listtype=="nodetypes":
			for ndtps in self.oas_node_list.keys():		
				if searchtag!="":
					if ndtps.find(searchtag)>-1:
						returnvalue.append(ndtps)
				else:
					returnvalue.append(ndtps)
		elif listtype=="scene":
			for ndtps in self.oas_rt.keys():		
				if searchtag!="":
					if ndtps.find(searchtag)>-1:
						returnvalue.append(self.oas_rt[ndtps]['name'])
				else:
					returnvalue.append(self.oas_rt[ndtps]['name'])			
		elif listtype == "variables":
			for vtps in self.oas_variablecategory.keys():
				returnvalue.append(vtps)
		elif listtype=="connections":
			for cns in self.oas_rt_connections.keys():		
				if searchtag!="":
					if self.oas_rt[(str(self.oas_rt_connections[cns]['in_node']))]['name']==str(searchtag) or self.oas_rt[(str(self.oas_rt_connections[cns]['out_node']))]['name']==str(searchtag):
						returnvalue.append(cns)	
				else:
						returnvalue.append(cns)		
		if mode=="normal":
			print ""
			print "List ("+str(listtype)+"):"
			for v in returnvalue:
				print v	
			print ""
		return returnvalue
		
# ###################################################################
# this will show you the inputs and the outputs of the scene
# if mode is "silent" thna doing nothing at this time maybe later...
# ###################################################################

	def oas_show_attribute_parameters(self, mode="normal",node=""):
		global_return=[]
		for nodes in self.oas_rt.keys():
			if str(self.oas_rt[nodes]['name'])==str(node):
				for ins in self.oas_rt[nodes]['inputs']:
					con_chk=0
					for con in self.oas_rt_connections.keys():
						if (self.oas_rt[self.oas_rt_connections[con]['in_node']]['name']==str(node) and self.oas_rt_connections[con]['in_value']==str(ins)):
							con_chk=1
					re=[ins,self.oas_rt[nodes]['inputs'][ins]['variable_type'],self.oas_rt[nodes]['inputs'][ins]['value'],self.oas_rt[nodes]['inputs'][ins]['options'],str(con_chk)]
					global_return.append(re)
		if mode=="normal":
			print global_return
		else:
			return global_return
			
	def oas_data_show(self,mode="normal",showtype="node"):
		nodlist=[]
		try:
			for kes in self.oas_rt.keys():
				if str(self.oas_rt[kes]['name'])==str(showtype):
					showtype=str(kes)
		except:
			pass
		if self.oas_rt.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print "ID of the node: "+str(showtype)
				print "Name of the node: "+str(self.oas_rt[showtype]['name'])
				print "This node is a scene node!"
				print "Inputs:"
			nodlist.append(str(self.oas_rt[showtype]['name'])+":"+str(self.oas_rt[showtype]['nodetype'])+":"+str(showtype))
			nodlist.append(str(self.oas_rt[showtype]['posx'])+":"+str(self.oas_rt[showtype]['posy']))
			for ins in self.oas_rt[str(showtype)]['inputs'].keys():
				con_chk=0
				for con in self.oas_rt_connections.keys():
					if (self.oas_rt_connections[con]['in_node']==str(showtype) and self.oas_rt_connections[con]['in_value']==str(ins)):
						con_chk=1
				if con_chk==1:
					if mode=="normal":
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value'])+"\tConnected"
					nodlist.append("input."+str(ins)+"=*"+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value']))
				else:
					if mode=="normal":
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value'])
					nodlist.append("input."+str(ins)+"="+str(self.oas_rt[str(showtype)]['inputs'][str(ins)]['value']))
			if mode=="normal":
				print "Outputs:"
			for ins in self.oas_rt[str(showtype)]['outputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_rt[str(showtype)]['outputs'][str(ins)]['value'])
				nodlist.append("output."+str(ins)+"="+str(self.oas_rt[str(showtype)]['outputs'][str(ins)]['value']))
			if mode=="normal":
				print ""	
			return nodlist
		elif self.oas_node_list.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print "Name of the node: "+str(showtype)
				print "This node is a nodetype template node!"
				print "Path to the sourcefile: "+str(self.oas_node_list[str(showtype)]['path'])
				print "Inputs:"
			nodlist.append((str(showtype)+":"+str(self.oas_node_list[showtype]['tag'])))
			for ins in self.oas_node_list[str(showtype)]['inputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(showtype)]['inputs'][str(ins)]['value'])
				nodlist.append("input."+str(ins)+"="+str(self.oas_node_list[str(showtype)]['inputs'][str(ins)]['value']))
			if mode=="normal":
				print "Outputs:"
			for ins in self.oas_node_list[str(showtype)]['outputs'].keys():
				if mode=="normal":
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(showtype)]['outputs'][str(ins)]['value'])
				nodlist.append("output."+str(ins)+"="+str(self.oas_node_list[str(showtype)]['outputs'][str(ins)]['value']))
			if mode=="normal":
				print ""
			return nodlist
		elif self.oas_rt_connections.has_key(str(showtype)):
			if mode=="normal":
				print ""
				print self.oas_rt[self.oas_rt_connections[str(showtype)]['out_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['out_value']+" --> "+self.oas_rt[self.oas_rt_connections[str(showtype)]['in_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['in_value']
			nodlist=[str(self.oas_rt[self.oas_rt_connections[str(showtype)]['out_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['out_value']),str(self.oas_rt[self.oas_rt_connections[str(showtype)]['in_node']]['name']+"."+self.oas_rt_connections[str(showtype)]['in_value'])]
			return nodlist
		elif showtype=="endnode":
			if mode=="normal":
				print "Endnode is: "+str(self.oas_scene_setup['endnode'])
			nodlist=[str(self.oas_scene_setup['endnode'])]
			return nodlist
		elif showtype=="framerange":
			if mode=="normal":
				print "From: "+str(self.oas_scene_setup['startframe'])+" to: "+str(self.oas_scene_setup['endframe'])
			return [str(self.oas_scene_setup['startframe']),str(self.oas_scene_setup['endframe'])]
		elif showtype=="frame":
			if mode=="normal":
				print "Frame: "+str(self.oas_scene_setup['frame'])
			return [str(self.oas_scene_setup['frame'])]
		elif showtype=="setup":
			if mode=="normal":
				print ""
			for ks in self.oas_scene_setup.keys():
				if mode=="normal":
					print str(ks)+" = "+ str(self.oas_scene_setup[ks])
				nodlist.append(str(ks)+" = "+ str(self.oas_scene_setup[ks]))
			if mode=="normal":
				print ""
			return nodlist
		else:
			if mode=="normal":
				print "[Error] In show: No node named: "+str(showtype)
			return 0
		
		
# ########################################################################################
# counts a node or a connection in the scene or in the oas_node_list
# if the mode is "silent" it is doing nothing. (this ones are realy just for visualization)
# ########################################################################################

	def oas_data_count(self,mode="normal",counttype="nodetypes"):
		if counttype=="nodetypes":
			if mode=="normal":
				print "There is "+str(len(self.oas_node_list.keys()))+" node in memory."
			return [str(len(self.oas_node_list.keys()))]
		elif counttype=="scene":
			if mode=="normal":
				print "There is "+str(len(self.oas_rt.keys()))+" node in the scene."
			return [str(len(self.oas_rt.keys()))]
		elif counttype=="connections":
			if mode=="normal":
				print "There is "+str(len(self.oas_rt_connections.keys()))+" connection."
			return [str(len(self.oas_rt_connections.keys()))]
		else: 
			if mode=="normal":
				print "[Error] In count: None-valid option given."
			return 0			
				
# ##########################################################################################
# this function creates a node with a given type
# if mode is 0 it will create the node, but in "silent" mode
# ##########################################################################################			
				
	def oas_data_create(self,mode="normal",nodetype="",posx=100,posy=100):
		result=0
		for nds in self.oas_node_list.keys():
			if str(nds)==str(nodetype):
				generated_random=0
				generated_random=str(self.generate_random_with_check())
				self.oas_rt["Node"+generated_random]=deepcopy(self.oas_node_list[nds])
				self.oas_rt["Node"+generated_random]['nodetype']=str(nds)
				self.oas_rt["Node"+generated_random]['name']=str(str(nds)+generated_random)
				self.oas_rt["Node"+generated_random]['posx']=posx
				self.oas_rt["Node"+generated_random]['posy']=posy
				del self.oas_rt["Node"+generated_random]['tag']
				del self.oas_rt["Node"+generated_random]['path']
				self.oas_last_node_created=str(str(nds)+generated_random)
				if mode=="normal":
					print "Node "+str(str(nds)+generated_random)+" created."
				result=1
				return str(str(nds)+generated_random)
		if result==0:
			if mode=="normal":
				print "[Error] In create: Unknown nodetype"
			return 0

	def oas_data_duplicate(self,mode="normal",node="",posx=100,posy=100):
		result=0
		for nds in self.oas_rt.keys():
			if self.oas_rt[nds]["name"]==str(node):
				generated_random=0
				new_name=self.nameChecker(mode="silent",name=self.oas_rt[nds]["name"])
				generated_random=str(self.generate_random_with_check())
				self.oas_rt["Node"+generated_random]=deepcopy(self.oas_rt[nds])
				self.oas_rt["Node"+generated_random]['name']=new_name
				self.oas_rt["Node"+generated_random]['posx']=posx
				self.oas_rt["Node"+generated_random]['posy']=posy
				self.oas_last_node_created=new_name
				if mode=="normal":
					print "Node "+str(new_name)+" created."
				result=1
				return new_name
		if result==0:
			if mode=="normal":
				print "[Error] In duplicate:Unknown nodetype"
			return 0

	def nameChecker(self,mode="normal",name=""):
		nameout=name
		for key in self.oas_rt.keys():
			if self.oas_rt[key]["name"]==name:
				n=1
				while n==1:
					if self.oas_rt[key]["name"]==name+str(n).zfill(3):
						pass
					else:
						nameout=name+str(n).zfill(3)
						n=2
		return str(nameout)
# #######################################################################################
# this is deleting a node or connection (disconnect)
# mode 0 is silence
# #######################################################################################

	def oas_data_delete(self,mode="normal",deletetype="node",target=""):
		if str(deletetype)=="node":
			nodename=""
			for nds in self.oas_rt.keys():
				if nds==target:
					nodename=nds
				elif str(self.oas_rt[nds]['name'])==str(target):
					nodename=str(nds)
			if self.oas_rt.has_key(nodename):
				line_delete_list=self.oas_data_list(mode="silent",listtype="connections",searchtag=str(self.oas_rt[nodename]['name']))
				del self.oas_rt[nodename]
				for connss in line_delete_list:
					x=self.oas_data_delete(mode=mode,deletetype="connection",target=str(connss))
				if mode=="normal":
					print "Node "+str(target)+" deleted."
				return [nodename]
			else:
				if mode=="normal":
					print "[Error] In delete: Node "+str(target)+" not found."
				return 0
		elif str(deletetype)=="connection":
			if self.oas_rt_connections.has_key(str(target)):
				del self.oas_rt_connections[str(target)]
				if mode=="normal":
					print "Connection "+str(target)+" deleted."
				return [target]
			else:
				if mode=="normal":
					print "[Error] In delete: Wrong connection name."
				return 0
		else:
			if mode=="normal":
				print "[Error] In delete: Wrong type option."
			return 0
			
# ##########################################################################################
# this will set the node input value
# ##########################################################################################			
				
	def oas_data_addInput(self,mode="normal",node="",variablename="",variabletype="string",defaultvalue=""):
		if node!="" and variablename!="":
			ref_string="qwertyuiopasdfghjklzxcvbnm1234567890_QWERTYUIOPASDFGHJKLZXCVBNM"
			numb="1234567890"
			result_new_name=""
			for char in str(variablename):
				if ref_string.find(char)>-1:
					result_new_name+=char
			variablename=result_new_name
			ID=""
			for id in self.oas_rt.keys():
				if str(self.oas_rt[id]["name"])==str(node):
					ID=id
			if ID=="":
				if mode=="normal":
					print "[Error] In addInput: Node not existing..."
				return 0
			if self.oas_rt[ID]["inputs"].has_key(str(variablename)):
				if mode=="normal":
					print "[Error] In addInput: Attribute already exsisting."
				return 0
			self.oas_rt[ID]["inputs"][variablename]={'variable_type':variabletype,'value':defaultvalue,'options':''}
			if mode=="normal":
				print "Attribute "+str(variablename)+" was added to node "+str(node)+" !"
			return variablename
		else:
			if mode=="normal":
				print "[Error] In addInput: Problematic description.."
			return 0

	def oas_data_delInput(self,mode="normal",node="",variablename=""):
		if node!="" and variablename!="":
			ID=""
			for id in self.oas_rt.keys():
				if str(self.oas_rt[id]["name"])==str(node):
					ID=id
			if ID=="":
				if mode=="normal":
					print "[Error] In delInput: Node not existing..."
				return 0
			if self.oas_rt[ID]["inputs"].has_key(str(variablename)):
				pass
			else:
				if mode=="normal":
					print "[Error] In delInput: Attribute not existing."
				return 0
			nodetype=self.oas_rt[ID]["nodetype"]
			if self.oas_node_list[nodetype]["inputs"].has_key(variablename):
				if mode=="normal":
					print "[Error] In delInput: This is an original attribute for the node, you can not delete it!"
				return 0
			contodelete=""
			for cons in self.oas_rt_connections.keys():
				if self.oas_rt[str(self.oas_rt_connections[cons]["in_node"])]["name"]==str(node):
					if str(self.oas_rt_connections[cons]["in_value"])==str(variablename): 
						contodelete=cons
			if contodelete!="":
				cdret=self.oas_data_delete(mode=mode,deletetype="connection",target=contodelete)
				if cdret==0:
					if mode=="normal":
						print "[Error] In delInput: Problem during the conneciton deletion"
					return 0
			del self.oas_rt[ID]["inputs"][variablename]
			if mode=="normal":
				print "Attribute "+str(variablename)+" was deleted!"
			return variablename
		else:
			if mode=="normal":
				print "[Error] In delInput: Problematic description.."
			return 0

	def oas_data_set(self,mode="normal",nodevalue="",value=""):
		if nodevalue!="":
			if len(nodevalue.split(".")):
				nodelists={}
				for noddd in self.oas_rt.keys():
					nodelists[self.oas_rt[noddd]['name']]=noddd
				if nodelists.has_key(nodevalue.split(".")[0]):
					if self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'].has_key(nodevalue.split(".")[1]):
						value=self.oas_variable(self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'][nodevalue.split(".")[1]]['variable_type'],value)
						self.oas_rt[nodelists[nodevalue.split(".")[0]]]['inputs'][nodevalue.split(".")[1]]['value']=value
						if mode=="normal":
							print str(nodevalue)+" was set to "+str(value)
						return [str(value)]
					elif self.oas_rt[nodelists[nodevalue.split(".")[0]]]['settings'].has_key(nodevalue.split(".")[1]):
						self.oas_rt[nodelists[nodevalue.split(".")[0]]]['settings'][nodevalue.split(".")[1]]=value
						if mode=="normal":
							print str(nodevalue)+" was set to "+str(value)
						return [str(value)]
					else:
						if mode=="normal":
							print "[Error] In set: Non existing input variable"
						return 0
				else:
					if mode=="normal":
						print "[Error] In set: None existing node..."
					return 0
			else:
				if mode=="normal":
					print "[Error] In set: Problematic description.."
				return 0

	def oas_data_positions(self,mode="normal",nodevalue="",posx=100,posy=100):
		if nodevalue!="" and posx!="" and posy!="":
				nodelists={}
				for noddd in self.oas_rt.keys():
					nodelists[self.oas_rt[noddd]['name']]=noddd
				if nodelists.has_key(nodevalue):
						try:
							self.oas_rt[nodelists[nodevalue]]['posx']=int(posx)
							self.oas_rt[nodelists[nodevalue]]['posy']=int(posy)
						except:
							return 0
						if mode=="normal":
							pass
							#print "New position for "+str(nodevalue)+" is: ", posx, posy 
						return [posx,posy]
				else:
					if mode=="normal":
						print "[Error] In positions: None existing node..."
					return 0

	def oas_get_positions(self,mode="normal",nodevalue=""):
		if nodevalue!="":
				nodelists={}
				x=0
				y=0
				for noddd in self.oas_rt.keys():
					nodelists[self.oas_rt[noddd]['name']]=noddd
				if nodelists.has_key(nodevalue):
						try:
							x=self.oas_rt[nodelists[nodevalue]]['posx']
							y=self.oas_rt[nodelists[nodevalue]]['posy']
						except:
							return 0
						return [x,y]
				else:
					if mode=="normal":
						print "[Error] In getpositions: None existing node..."
					return 0

# ##########################################################################
# rename a node can be normal 1 or silent 0 mode
# ##########################################################################
	
	def oas_data_rename(self,mode="normal",old="",new=""):
			if old!="" and new!="":
				ref_string="qwertyuiopasdfghjklzxcvbnm1234567890_QWERTYUIOPASDFGHJKLZXCVBNM"
				numb="1234567890"
				result_new_name=""
				for char in str(new):
					if ref_string.find(char)>-1:
						result_new_name+=char
				try:
					if numb.find(result_new_name[0])>-1:
						result_new_name=""
				except:
					result_new_name=""		
				new=result_new_name
				node=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(old):
						node=str(nds)
				chk=False
				if str(new)!="":
					chk=True
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(new):
							chk=False
				if self.oas_rt.has_key(node) and chk:
					self.oas_rt[node]['name']=str(new)
					if str(self.oas_last_node_created)==str(old):
						self.oas_last_node_created=str(new)
					if str(self.oas_scene_setup['endnode'])==str(old):
						self.oas_scene_setup['endnode']=str(new)
					if mode =="normal":
						print "Node "+str(old)+" is known as "+str(new)+" now."
					return [str(new)]
				else:
					if mode=="normal":
						print "[Error] In rename: Problem with the parameters!"
					return 0
			else:
				if mode =="normal":
					print "[Error] In rename: Not enough parameter!"
				return 0

# ####################################################################################
# this call will mark a node as an end node
# ####################################################################################
				
	def oas_data_end(self,mode="normal",endnode=""):
		chk=0
		if endnode!="":
			for nds in self.oas_rt.keys():
				if str(self.oas_rt[nds]['name'])==str(endnode):
					self.oas_scene_setup['endnode']=str(endnode)
					chk=1
		if chk==1:
			if mode=="normal":
				print "Node "+str(endnode)+" marked as endnode."
			return [str(endnode)]
		else:
			if mode=="normal":
				print "[Error] In set end: Wrong node."
			return 0	
		
		
# ####################################################################################
# set the framerange
# ####################################################################################
				
	def oas_data_framerange(self,mode="normal",firstframe="",endframe=""):
			if firstframe!="" and endframe!="":
				try:
					a=int(firstframe)
					b=int(endframe)
					if a>b:
						if mode=="normal":
							print "[Error] In framerange: Startframe is bigger than endframe!!"
						return 0
					else:
						self.oas_scene_setup['startframe']=a
						self.oas_scene_setup['endframe']=b
						if mode=="normal":
							print "Frame range are set."
						return [a,b]
				except:
					if mode=="normal":
						print "[Error] In framerange: Framerange values are wrong!"
					return 0
			else:
				if mode=="normal":
					print "[Error] In framerange: Wrong parameterlist!"
				return 0
		
		
# ####################################################################################
# set the currentframe
# ####################################################################################
				
	def oas_data_frame(self,mode="normal",frame=""):
		if frame!="":
			try:
				a=int(frame)
				self.oas_scene_setup['frame']=a
				if mode=="normal":
					print "Frame is set."
				return [a]
			except:
				if mode=="normal":
					print "[Error] In frame: Frame value are wrong!"
				return 0
		else:
			if mode=="normal":
				print "[Error] In frame: Wrong parameterlist!"
			return 0
		
				
# ####################################################################################
# create a connection between the nodes
# ####################################################################################
				
	def oas_data_connect(self,mode="normal",from_variable="",to_variable=""):
		if from_variable!="" and to_variable!="":
			node_out=""
			value_out=""
			if str(from_variable).find(".")>-1:
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(from_variable.split(".")[0]):
						node_out=str(nds)
						for ots in self.oas_rt[node_out]['outputs'].keys():
							if str(ots)==str(from_variable.split(".")[1]):
								value_out=str(ots)
			else:
				pass
			node_in=""
			value_in=""
			if str(to_variable).find(".")>-1:
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(to_variable.split(".")[0]):
						node_in=str(nds)
						for ots in self.oas_rt[node_in]['inputs'].keys():
							if str(ots)==str(to_variable.split(".")[1]):
								value_in=str(ots)
			else:
				pass
			con_chk=0
			for con in self.oas_rt_connections.keys():
				if (self.oas_rt_connections[con]['in_node']==str(node_in) and self.oas_rt_connections[con]['in_value']==str(value_in)):
					con_chk=1
			if con_chk==1:
				if mode=="normal":
					print "[Error] In connect: This node input is already connected, you need to disconnect first."
				return 0
			if node_out=="" or node_in=="" or value_out=="" or value_in=="" or node_in==node_out:
				if mode =="normal":
					print "[Error] In connect: Wrong parameters!"
				return 0
			else:
				# uncomment this if you want the: "input gets the output value on connection"
				#self.oas_rt[node_in]['inputs'][value_in]['value']=self.oas_rt[node_out]['outputs'][value_out]['value']
				in_type=str(self.oas_rt[node_in]['inputs'][value_in]['variable_type'])
				out_type=str(self.oas_rt[node_out]['outputs'][value_out]['variable_type'])
				if self.oas_variablecategory[in_type]==self.oas_variablecategory[out_type] or in_type=="any" or out_type=="any":
					rnd=self.generate_random_with_check_for_connection()
					self.oas_rt_connections[str("Connection"+str(rnd))]={'in_node':node_in,'out_node':node_out,'in_value':value_in,'out_value':value_out}
				else:
					if mode =="normal":
						print "[Error] In connect: You can not connect different parametertypes!"
					return 0
			if mode=="normal":
				print str(from_variable)+" ---> "+ str(to_variable) +" Connected."
			return [node_out+"."+value_out,node_in+"."+value_in,str("Connection"+str(rnd))]
		else:
			if mode =="normal":
				print "[Error] In connect: Not enough parameter."
			return 0
