######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Setup import *
import os
from Console.Console import oas_console
from Port.server import oas_server
from Port.client import oas_client
from Gateway.Gateway import oas_gateway
from GUI.Old_GUI.Old_GUI import Old_GUI

import thread

###################################################################################
# oas starts up here this is needed to call, for the basic environment-variable setup
###################################################################################

class oas_start(oas_setup,oas_client,oas_console,oas_server,oas_gateway,Old_GUI):
	def __init__(self,args_list):
		
		if args_list[0]=="client":
			self.oas_Start()
			self.oas_remoteClient(self.server_port)
			
		elif args_list[0]=="run":
			self.oas_run("1",["run"])
		
		if args_list[0]=="old_gui":
			self.start_old_gui()
		else:
		
###################################################################################
# the rest of the services needs the server
###################################################################################
		
			self.oas_Start()
		
			if os.path.isfile(args_list[1]):
				self.oas_open("silent",filetype=args_list[1][-3:],filename=args_list[1])
		
###################################################################################
# the server is starting here with a separate task
###################################################################################

			self.lock=thread.allocate_lock()
			thread.start_new_thread(self.oas_port_server,(self.server_port,self.lock))

		
###################################################################################
# We are checking if we want to start a consol version or the gui version
###################################################################################
		
			if args_list[0]=="console":
				self.oas_Console()


