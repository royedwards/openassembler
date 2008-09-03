######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import sys
from Gateway.Gateway import oas_gateway
import readline

class oas_console(oas_gateway):
	def oas_Console(self):
		x=1
		while x==1:
			input_command=raw_input ("OpenAssembler:").strip()
			if input_command=="":
				input_command="no character given"
			if input_command=="exit":
				print "OpenAssembler now quiting..."
				sys.exit()
			elif input_command=="help" or input_command=="?":
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
					
ls				:same as  the "list scene" command
					
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
										
exit				:quit from the application 
				'''
			
			elif input_command.split()[0]=="list":
				if len(input_command.split())>1:
					self.oas_list("1",input_command.split()) 
			
				else:
					print "Wrong command parameter."
			
			elif input_command.split()[0]=="count":
				if len(input_command.split())>1:
					self.oas_count("1",input_command.split()) 
			
				else:
					print "Wrong command parameter."
			
			elif input_command.split()[0]=="create" or input_command.split()[0]=="cr":
				if len(input_command.split())>1:
					self.oas_create("1",input_command.split()) 
			
				else:
					print "Wrong command parameter."
			
			elif input_command.split()[0]=="delete" or input_command.split()[0]=="del":
				if len(input_command.split())>1:
					self.oas_delete("1",input_command.split()) 
			
				else:
					print "Wrong command parameter."
			
			elif input_command.split()[0]=="rename" or input_command.split()[0]=="rn":
				if len(input_command.split())>1:
					self.oas_rename("1",input_command.split()) 
			
				else:
					print "Wrong command parameter."
								
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
					
			elif input_command.split()[0]=="ls":
				if len(input_command.split())>0:
					self.oas_list("1",["ls","scene"]) 
				else:
					print "Wrong command parameter."
					
			elif input_command.split()[0]=="lc":
				if len(input_command.split())>0:
					self.oas_list("1",["ls","connections"]) 
				else:
					print "Wrong command parameter."
					
			elif input_command.split()[0]=="ln":
				if len(input_command.split())>0:
					self.oas_list("1",["ls","nodetypes"]) 
				else:
					print "Wrong command parameter."
					
			elif input_command.split()[0]=="new":
				self.oas_new("1",input_command.split()) 
			
			else:
				if input_command!="no character given":
					print "Command not found. --> "+input_command
