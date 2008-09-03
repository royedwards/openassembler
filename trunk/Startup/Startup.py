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


class oas_start(oas_setup,oas_console,oas_data_handler):
	def __init__(self,args_list):
		self.oas_Startup()
		if args_list[1]!="":
			pass
			# here we will load up a file specified at startup with a gateway command
		if args_list[0]=="console":
			self.oas_Console()


