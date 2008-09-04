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
		
###################################################################################
# oas starts up here this is needed to call, for the basic environment-variable setup
###################################################################################
		
		self.oas_Startup()
		
###################################################################################
# this will load up a network later
###################################################################################
	
		if args_list[1]!="":
			pass
			# here we will load up a file specified at startup with a gateway command
		
###################################################################################
# We are checking if we want to start a consol version or the gui version
###################################################################################
		
		if args_list[0]=="console":
			self.oas_Console()


