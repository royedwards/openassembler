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
from Dbase.Data_handler import oas_data_handler
from Run.Run import oas_execute
from Dbase.FileIO import oas_fileio
from Port.server import oas_server
from Port.client import oas_client
import thread


###################################################################################
# oas starts up here this is needed to call, for the basic environment-variable setup
###################################################################################

class oas_start(oas_setup,oas_client,oas_console,oas_execute,oas_fileio,oas_server,oas_data_handler):
	def __init__(self,args_list):
		
		if args_list[0]=="client":
			self.oas_Startup()
			self.oas_remoteClient(self.server_port)
		else:
		
			self.oas_Startup()
		
			if os.path.isfile(args_list[1]):
				self.oas_file_open("0",["open",args_list[1][-3:],args_list[1]])
		
		
			lock=thread.allocate_lock()
			thread.start_new_thread(self.oas_port_server,(self.server_port,lock))

		
###################################################################################
# We are checking if we want to start a consol version or the gui version
###################################################################################
		
			if args_list[0]=="console":
				self.oas_Console()

			elif args_list[0]=="run":
				self.oas_run_execute("1",["run"])
			
