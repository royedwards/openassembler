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

		
		if args_list[0]=="gui":
			self.start_old_gui()
		else:
			self.oas_Start()
		
			if os.path.isfile(args_list[1]):
				self.oas_open("silent",filetype=args_list[1][-3:],filename=args_list[1])

			if args_list[0]=="run":
				self.oas_run("normal")
						
			elif args_list[0]=="console":

				self.lock=thread.allocate_lock()
				thread.start_new_thread(self.oas_port_server,(self.server_port,self.lock))

				self.oas_Console()

