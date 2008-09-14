######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import sys, time, readline
from Gateway.Gateway import oas_gateway
from Port.server import oas_common_port_communication

######################################################################################
# this file is for the console loop
######################################################################################

class oas_console(oas_gateway,oas_common_port_communication):
	def oas_Console(self,imput_to_parse="",mode="normal"):
		
####################################################################################
# we are starting a loop and then we are lsitening and sorting out the given commands
####################################################################################
		x=1
		while x==1:	
			if imput_to_parse=="":
				input_command=raw_input ("OpenAssembler--->").strip()
			else:
				input_command=imput_to_parse
			if input_command=="":
				input_command="no character given"
			if input_command=="exit":
				self.oas_server_halt(self.server_port)
				sys.exit(0)
			elif input_command=="help" or input_command=="?":
				if mode=="normal":
					print '''
OpenAssembler V2 Console v0.1beta
Owner: Laszlo Mates
email: laszlo.mates@gmail.com

You can use the following commands:

help				:show this message

show <nodename> or <setup>	:display a node parameterlist
			 	 nodename can be a nodetype or
			 	 a node from the scene
				 if "setup" is written then
				 it shows the scene settings
				 
list <type> <nodename> <...> 	:lists all the nodes or nodetypes 
				 in the scene or nodetypelist, 
				 you can filter with a search-tag
				 as the last option.
				 type can be:
				 	nodetype
					scene
					connections
										
count <type>		 	:counts all the nodes or nodetypes 
				 in the scene or nodetypelist.
				 type can be:
				 	nodetype
					scene
					connections
					
create <nodetype>		:creates a node to the scene with
				 a given nodetype.

delete <type> <nodename>	:delete a node from the scene.
				 type can be:
				 	node
					connection
					
rename <old> <new>		:renames the node: old to the
				 name: new
					
connect <from> <to>		:make a connection from a node 
				 output to a node input
				 example: 
				 connect mult1.out mult2.in1
					
new				:create a new scene
										
exit				:quit from the application 
				'''
			
			elif input_command.split()[0]=="list" or input_command.split()[0]=="ls" or input_command.split()[0]=="lc" or input_command.split()[0]=="ln":
				try:
					ltyp=input_command.split()[1]
				except:
					ltyp=""
				if input_command.split()[0]=="ln":
					ltyp="nodetypes"
				elif input_command.split()[0]=="lc":
					ltyp="connections"
				elif input_command.split()[0]=="ls":
					ltyp="scene"
				try:
					src=input_command.split()[2]
				except:
					src=""	
				if mode=="normal":
					self.oas_list(mode=mode,listtype=ltyp,searchtag=src)
				else:
					return  self.oas_list(mode=mode,listtype=ltyp,searchtag=src)
					
			elif input_command.split()[0]=="count":
				try:
					ltyp=input_command.split()[1]
				except:
					ltyp="nodetypes"
				if mode=="normal":
					self.oas_count(mode=mode,counttype=ltyp)
				else:
					return  self.oas_count(mode=mode,counttype=ltyp)			
			
			elif input_command.split()[0]=="create" or input_command.split()[0]=="cr":
				try:
					ndtp=input_command.split()[1]
				except:
					ndtp=""
					
				if mode=="normal":
					self.oas_create(mode=mode,nodetype=ndtp) 
				else:
					return self.oas_create(mode=mode,nodetype=ndtp) 

			
			elif input_command.split()[0]=="delete" or input_command.split()[0]=="del":
				try:
					ndtp=input_command.split()[1]
				except:
					ndtp="node"	
				try:
					trg=input_command.split()[2]
				except:
					trg=""		
				if mode=="normal":
					self.oas_delete(mode=mode,deletetype=ndtp,target=trg) 
				else:
					return self.oas_delete(mode=mode,deletetype=ndtp,target=trg) 
			
			elif input_command.split()[0]=="rename" or input_command.split()[0]=="rn":
				try:
					old=input_command.split()[1]
				except:
					old="node"	
				try:
					new=input_command.split()[2]
				except:
					new=""		
				if mode=="normal":
					self.oas_rename(mode=mode,old=old,new=new) 
				else:
					return self.oas_rename(mode=mode,old=old,new=new) 			
			
			elif input_command.split()[0]=="show" or input_command.split()[0]=="sh":
				if len(input_command.split())>1:
					self.oas_show("1",input_command.split()) 
				else:
					print "Wrong command parameter."
													
			elif input_command.split()[0]=="connect" or input_command.split()[0]=="cn":
				if len(input_command.split())>1:
					self.oas_connect("1",input_command.split()) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="end":
				if len(input_command.split())>1:
					self.oas_end("1",input_command.split()) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="set":
				if len(input_command.split())>2:
					self.oas_set("1",input_command.split()) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="framerange":
				if len(input_command.split())>2:
					self.oas_framerange("1",input_command.split()) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="frame":
				if len(input_command.split())>1:
					self.oas_frame("1",input_command.split()) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="run":
				if len(input_command.split())==1:
					self.oas_run("1",["run",str(self.oas_scene_setup['endnode'])]) 
				elif len(input_command.split())>1:
					self.oas_run("1",input_command.split())
				else:
					print "Wrong command parameter."
			
			elif input_command.split()[0]=="new":
				if len(input_command.split())>0:
					self.oas_new("1",input_command.split()) 
				else:
					print "Wrong command parameter."
					
			elif input_command.split()[0]=="open":
				if len(input_command.split())>2:
					self.oas_open("1",input_command.split()) 
				elif len(input_command.split())==2:
					self.oas_open("1",["open",str(input_command.split()[1][-3:]),str(input_command.split()[1])])
				else:
					print "Wrong command parameter."
					
			elif input_command.split()[0]=="save":
				
				if (str(self.oas_save_filename)!="") and (len(input_command.split())<2):
					self.oas_save("1",["save",str(self.oas_save_filename)[-3:],str(self.oas_save_filename)])
				elif len(input_command.split())>2:
					self.oas_save("1",input_command.split())  
				else:
					print "Wrong command parameter."
			
			else:
				if input_command!="no character given":
					print "Command not found. --> "+input_command
