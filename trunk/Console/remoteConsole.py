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
import thread

######################################################################################
# this file is for the console loop
######################################################################################

class oas_remote_console(oas_gateway):
	def oas_remoteConsole(self,imp="",mode=0):
		
####################################################################################
# we are starting a loop and then we are lsitening and sorting out the given commands
####################################################################################
		x=1
		while x==1:	
			if imp=="":
				input_command=raw_input ("OpenAssembler:").strip()
				mode=1
			else:
				input_command=imp
				x=0
				mode=0
			if input_command=="":
				input_command="no character given"
			if input_command=="exit":
				return "OpenAssembler now quiting..."
				sys.exit(0)
			elif input_command=="help" or input_command=="?":
				return '''
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
			
			elif input_command.split()[0]=="list":
				if len(input_command.split())>1:
					return self.oas_list(mode,input_command.split()) 
			
				else:
					return "Wrong command parameter."
			
			elif input_command.split()[0]=="count":
				if len(input_command.split())>1:
					return self.oas_count(mode,input_command.split()) 
			
				else:
					return "Wrong command parameter."
			
			elif input_command.split()[0]=="create" or input_command.split()[0]=="cr":
				if len(input_command.split())>1:
					return self.oas_create(mode,input_command.split()) 
			
				else:
					return "Wrong command parameter."
			
			elif input_command.split()[0]=="delete" or input_command.split()[0]=="del":
				if len(input_command.split())>1:
					return self.oas_delete(mode,input_command.split()) 
			
				else:
					return "Wrong command parameter."
			
			elif input_command.split()[0]=="rename" or input_command.split()[0]=="rn":
				if len(input_command.split())>1:
					return self.oas_rename(mode,input_command.split()) 
			
				else:
					return "Wrong command parameter."
								
			elif input_command.split()[0]=="show" or input_command.split()[0]=="sh":
				if len(input_command.split())>1:
					return self.oas_show(mode,input_command.split()) 
				else:
					return "Wrong command parameter."
													
			elif input_command.split()[0]=="connect" or input_command.split()[0]=="cn":
				if len(input_command.split())>1:
					return self.oas_connect(mode,input_command.split()) 
				else:
					return "Wrong command parameter."
					
			elif input_command.split()[0]=="ls":
				if len(input_command.split())>0:
					return self.oas_list(mode,["ls","scene"]) 
				else:
					return "Wrong command parameter."
					
			elif input_command.split()[0]=="lc":
				if len(input_command.split())>0:
					return self.oas_list(mode,["ls","connections"]) 
				else:
					return "Wrong command parameter."
					
			elif input_command.split()[0]=="ln":
				if len(input_command.split())>0:
					return self.oas_list(mode,["ls","nodetypes"]) 
				else:
					print "Wrong command parameter."

			elif input_command.split()[0]=="end":
				if len(input_command.split())>1:
					return self.oas_end(mode,input_command.split()) 
				else:
					return "Wrong command parameter."

			elif input_command.split()[0]=="set":
				if len(input_command.split())>2:
					return self.oas_set(mode,input_command.split()) 
				else:
					return "Wrong command parameter."

			elif input_command.split()[0]=="framerange":
				if len(input_command.split())>2:
					return self.oas_framerange(mode,input_command.split()) 
				else:
					return "Wrong command parameter."

			elif input_command.split()[0]=="frame":
				if len(input_command.split())>1:
					return self.oas_frame(mode,input_command.split()) 
				else:
					return "Wrong command parameter."

			elif input_command.split()[0]=="run":
				if len(input_command.split())==1:
					return self.oas_run(mode,["run",str(self.oas_scene_setup['endnode'])]) 
				elif len(input_command.split())>1:
					return self.oas_run(mode,input_command.split())
				else:
					return "Wrong command parameter."
			
			elif input_command.split()[0]=="new":
				if len(input_command.split())>0:
					return self.oas_new(mode,input_command.split()) 
				else:
					return "Wrong command parameter."
					
			elif input_command.split()[0]=="open":
				if len(input_command.split())>2:
					return self.oas_open(mode,input_command.split()) 
				elif len(input_command.split())==2:
					return self.oas_open(mode,["open",str(input_command.split()[1][-3:]),str(input_command.split()[1])])
				else:
					return "Wrong command parameter."
					
			elif input_command.split()[0]=="save":
				
				if (str(self.oas_save_filename)!="") and (len(input_command.split())<2):
					return self.oas_save(mode,["save",str(self.oas_save_filename)[-3:],str(self.oas_save_filename)])
				elif len(input_command.split())>2:
					return self.oas_save(mode,input_command.split())  
				else:
					return "Wrong command parameter."
			
			else:
				if input_command!="no character given":
					return "Command not found. --> "+input_command
