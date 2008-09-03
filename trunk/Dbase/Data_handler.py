######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import os
import sys
from random import *
from copy import deepcopy
	
class oas_data_handler:

	def generate_random_with_check(self):
		randomized=0
		chk=True
		while chk==True:
			randomized=randrange(1000,1000000)
			chk=self.oas_rt.has_key(str("Node"+str(randomized)))
		return randomized
		
	def generate_random_with_check_for_connection(self):
		randomized=0
		chk=True
		while chk==True:
			randomized=randrange(1000,1000000)
			chk=self.oas_rt_connections.has_key(str("Connection"+str(randomized)))
		return randomized

	def oas_data_list(self,mode,inputs):
		if mode=="1":
			part=inputs[1]
			if part == "nodetypes":
				print ""
				if len(inputs)>2:
					for ndtps in self.oas_node_list.keys():
						if ndtps.find(inputs[2])>-1:
							print ndtps
				else:
					for ndtps in self.oas_node_list.keys():
						print ndtps
				print ""
			elif part == "scene":
				print ""
				if len(inputs)>2:
					for ndtps in self.oas_rt.keys():
						if self.oas_rt[ndtps]['name'].find(inputs[2])>-1:
							print self.oas_rt[ndtps]['name']
				else:
					for ndtps in self.oas_rt.keys():
						print self.oas_rt[ndtps]['name']
				print ""
			
			elif part == "connections":
				print ""
				if len(inputs)>2:
					for cns in self.oas_rt_connections.keys():
						if (self.oas_rt[(str(self.oas_rt_connections[cns]['in_node']))]['name'].find(inputs[2])>-1) or (self.oas_rt[(str(self.oas_rt_connections[cns]['out_node']))]['name'].find(inputs[2])>-1):
							print str(cns)+"\t"+str(self.oas_rt[str(self.oas_rt_connections[cns]['out_node'])]['name'])+"."+str(self.oas_rt_connections[cns]['out_value'])+"\t"+str(self.oas_rt[str(self.oas_rt_connections[cns]['in_node'])]['name'])+"."+str(self.oas_rt_connections[cns]['in_value'])
				else:
					for cns in self.oas_rt_connections.keys():
						print str(cns)+"\t"+str(self.oas_rt[str(self.oas_rt_connections[cns]['out_node'])]['name'])+"."+str(self.oas_rt_connections[cns]['out_value'])+"\t"+str(self.oas_rt[str(self.oas_rt_connections[cns]['in_node'])]['name'])+"."+str(self.oas_rt_connections[cns]['in_value'])
				print ""
			
			else:
				print "None-valid list option given."
		else:
			part=inputs[1]
			returnvalue=[]
			if part=="nodetypes":
				for ndtps in self.oas_node_list.keys():		
					if len(inputs)>2:
						if ndtps.find(inputs[2])>-1:
							returnvalue.append(ndtps)
					else:
						returnvalue.append(ndtps)		
			elif part=="scene":
				for ndtps in self.oas_rt.keys():		
					if len(inputs)>2:
						if ndtps.find(inputs[2])>-1:
							returnvalue.append(ndtps)
					else:
						returnvalue.append(ndtps)
			
			elif part=="connections":
				if len(inputs)>2:
					for cns in self.oas_rt_connections.keys():		
						if (self.oas_rt[(str(self.oas_rt_connections[cns]['in_node']))]['name'].find(inputs[2])>-1) or (self.oas_rt[(str(self.oas_rt_connections[cns]['out_node']))]['name'].find(inputs[2])>-1):
							returnvalue.append(cns)				
			return returnvalue
		

	def oas_data_show(self,mode,inputs):
		if mode=="1":
			try:
				for kes in self.oas_rt.keys():
					if str(self.oas_rt[kes]['name'])==str(inputs[1]):
						inputs[1]=str(kes)
			except:
				pass
			if self.oas_rt.has_key(str(inputs[1])):
				print ""
				print "ID of the node: "+str(inputs[1])
				print "Name of the node: "+str(self.oas_rt[inputs[1]]['name'])
				print "This node is a scene node!"
				print "Inputs:"
				for ins in self.oas_rt[str(inputs[1])]['inputs'].keys():
					con_chk=0
					for con in self.oas_rt_connections.keys():
						if (self.oas_rt_connections[con]['in_node']==str(inputs[1]) and self.oas_rt_connections[con]['in_value']==str(ins)):
							con_chk=1
					if con_chk==1:
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(inputs[1])]['inputs'][str(ins)]['value'])+"\tConnected"
					else:
						print "\t"+str(ins)+" = "+str(self.oas_rt[str(inputs[1])]['inputs'][str(ins)]['value'])
				print "Outputs:"
				for ins in self.oas_rt[str(inputs[1])]['outputs'].keys():
					print "\t"+str(ins)+" = "+str(self.oas_rt[str(inputs[1])]['outputs'][str(ins)]['value'])
				print ""
			elif self.oas_node_list.has_key(str(inputs[1])):
				print ""
				print "Name of the node: "+str(inputs[1])
				print "This node is a nodetype template node!"
				print "Path to the sourcefile: "+str(self.oas_node_list[str(inputs[1])]['path'])
				print "Inputs:"
				for ins in self.oas_node_list[str(inputs[1])]['inputs'].keys():
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(inputs[1])]['inputs'][str(ins)]['value'])
				print "Outputs:"
				for ins in self.oas_node_list[str(inputs[1])]['outputs'].keys():
					print "\t"+str(ins)+" = "+str(self.oas_node_list[str(inputs[1])]['outputs'][str(ins)]['value'])
				print ""
			elif inputs[1]=="setup":
				print ""
				for ks in self.oas_scene_setup.keys():
					print str(ks)+" = "+ str(self.oas_scene_setup[ks])
				print ""
			else:
				print "No node named: "+str(inputs[1])
		else:
			try:
				return self.oas_node_list[str(inputs[1])]
			except:
				return

	def oas_data_count(self,mode,inputs):
		if mode=="1":
			if inputs[1]=="nodetypes":
				print "There is "+str(len(self.oas_node_list.keys()))+" node in memory."
			elif inputs[1]=="scene":
				pass
			elif inputs[1]=="connections":
				print "There is "+str(len(self.oas_rt_connections.keys()))+" connection."
			else: 
				print "None-valid option given."
		else:
			if inputs[1]=="nodetypes":
				return str(len(self.oas_node_list.keys()))
			elif inputs[1]=="scene":
				pass
			elif inputs[1]=="connections":
				pass
			else: 
				return
				
	def oas_data_create(self,mode,inputs):
		if mode=="1":
			result=0
			for nds in self.oas_node_list.keys():
				if str(nds)==str(inputs[1]):
					generated_random=0
					generated_random=str(self.generate_random_with_check())
					self.oas_rt["Node"+generated_random]=deepcopy(self.oas_node_list[nds])
					self.oas_rt["Node"+generated_random]['nodetype']=str(nds)
					self.oas_rt["Node"+generated_random]['name']=str(str(nds)+generated_random)
					del self.oas_rt["Node"+generated_random]['tag']
					del self.oas_rt["Node"+generated_random]['path']
					print "Node "+str(str(nds)+generated_random)+" created."
					result=1
			if result==0:
				print "Unknown nodetype"
					
		else:
			for nds in self.oas_node_list.keys():
				if str(nds)==str(inputs[1]):
					generated_random=0
					generated_random=str(self.generate_random_with_check())
					self.oas_rt["Node"+generated_random]=deepcopy(self.oas_node_list[nds])
					self.oas_rt["Node"+generated_random]['nodetype']=str(nds)
					self.oas_rt["Node"+generated_random]['name']=str(str(nds)+generated_random)
					del self.oas_rt["Node"+generated_random]['tag']
					del self.oas_rt["Node"+generated_random]['path']
					return str("Node"+generated_random)

	def oas_data_delete(self,mode,inputs):
		if mode=="1":
			if str(inputs[1])=="node":
				nodename=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(inputs[2]):
						nodename=str(nds)
				if self.oas_rt.has_key(nodename):
					line_delete_list=self.oas_data_list("0",["","connections",str(inputs[2])])
					del self.oas_rt[nodename]
					for connss in line_delete_list:
						self.oas_data_delete("1",["","connection",str(connss)])
					print "Node "+str(inputs[2])+" deleted."

				else:
					print "Node "+str(inputs[2])+" not found."
			elif str(inputs[1])=="connection":
				if self.oas_rt_connections.has_key(str(inputs[2])):
					del self.oas_rt_connections[str(inputs[2])]
					print "Connection "+str(inputs[2])+" deleted."
				else:
					print "Wrong connection name."
				
			else:
				print "Wrong type option."
		else:
			if str(inputs[1])=="node":
				nodename=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(inputs[2]):
						nodename=str(nds)
				if self.oas_rt.has_key(nodename):
					line_delete_list=self.oas_data_list("0",["","connections",str(inputs[2])])
					del self.oas_rt[nodename]
					for connss in line_delete_list:
						self.oas_data_delete("0",["","connection",str(connss)])
			elif str(inputs[1])=="connection":
				nodename=""
				if self.oas_rt_connections.has_key(str(inputs[2])):
					del self.oas_rt_connections[str(inputs[2])]
					nodename=str(inputs[2])
			return nodename
			
	def oas_data_rename(self,mode,inputs):
		if mode=="1":
			if len(inputs)>2:
				ref_string="qwertyuiopasdfghjklzxcvbnm1234567890"
				numb="1234567890"
				result_new_name=""
				for char in str(inputs[2]):
					if ref_string.find(char)>-1:
						result_new_name+=char
				try:
					if numb.find(result_new_name[0])>-1:
						result_new_name=""
				except:
					result_new_name=""		
				inputs[2]=result_new_name
				node=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(inputs[1]):
						node=str(nds)
				chk=False
				if str(inputs[2])!="":
					chk=True
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(inputs[2]):
							chk=False
				if self.oas_rt.has_key(node) and chk:
					self.oas_rt[node]['name']=str(inputs[2])
					print "Node "+str(inputs[1])+" is known as "+str(inputs[2])+" now."
				else:
					print "Problem with the parameters!"
			else:
				print "Not enough parameter!"
		else:
			if len(inputs)>2:
				ref_string="qwertyuiopasdfghjklzxcvbnm1234567890"
				numb="1234567890"
				result_new_name=""
				for char in str(inputs[2]):
					if ref_string.find(char)>-1:
						result_new_name+=char
				try:
					if numb.find(result_new_name[0])>-1:
						result_new_name=""
				except:
					result_new_name=""		
				inputs[2]=result_new_name
				node=""
				for nds in self.oas_rt.keys():
					if str(self.oas_rt[nds]['name'])==str(inputs[1]):
						node=str(nds)
				chk=False
				if inputs[2]!="":
					chk=True
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(inputs[2]):
							chk=False		
				if self.oas_rt.has_key(node) and chk:
					self.oas_rt[node]['name']=str(inputs[2])
					return str(inputs[2])
				else:
					return 

	def oas_data_connect(self,mode,inputs):
		if mode=="1":
			if len(inputs)>2:
				node_out=""
				value_out=""
				if str(inputs[1]).find(".")>-1:
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(inputs[1].split(".")[0]):
							node_out=str(nds)
							for ots in self.oas_rt[node_out]['outputs'].keys():
								if str(ots)==str(inputs[1].split(".")[1]):
									value_out=str(ots)
				else:
					pass
				
				node_in=""
				value_in=""
				if str(inputs[2]).find(".")>-1:
					for nds in self.oas_rt.keys():
						if str(self.oas_rt[nds]['name'])==str(inputs[2].split(".")[0]):
							node_in=str(nds)
							for ots in self.oas_rt[node_in]['inputs'].keys():
								if str(ots)==str(inputs[2].split(".")[1]):
									value_in=str(ots)
				else:
					pass
				
				if node_out=="" or node_in=="" or value_out=="" or value_in=="":
					print "Wrong parameters!"
				else:
					#self.oas_rt[node_in]['inputs'][value_in]['value']=self.oas_rt[node_out]['outputs'][value_out]['value']
					rnd=self.generate_random_with_check_for_connection()
					self.oas_rt_connections[str("Connection"+str(rnd))]={'in_node':node_in,'out_node':node_out,'in_value':value_in,'out_value':value_out}
			else:
				print "Not enough parameter."
		else:
			return


	def oas_Startup(self):
		self.oas_userhome=os.environ.get("HOME")
		self.oas_home=str(self.oas_userhome)+"/.OpenAssembler"
		self.oas_rt={}
		self.oas_rt_connections={}
		self.oas_scene_setup={'startframe': 100, 'endframe':200,'endnode':""}
		
	    	if os.path.isdir(self.oas_home):
			pass
	    	else:
			os.mkdir(self.oas_home)
		
		oas_setupFile=self.oas_home+"/OpenAssembler.ini"
		self.setup_contents=[]
		if os.path.isfile(oas_setupFile)==True:
			self.setup_contents=self.oas_load_setup(oas_setupFile)
		else:
			self.oas_create_setup(oas_setupFile)
			self.setup_contents=self.oas_load_setup(oas_setupFile)
		
		self.oas_collect_node_dirs(self.setup_contents)
		self.oas_node_list=self.oas_collect_nodes_from_dirs(self.oas_collect_node_dirs(self.setup_contents))