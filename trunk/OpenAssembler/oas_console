#! /usr/bin/env python

# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

import sys,os
from Core.Console.Console import oas_console
from Core.Dbase.Dbase_init import dBase_Init

class main_app_start(dBase_Init,oas_console):
	def __init__(self,args):

		# ################################
		# it builds up the data structure for the core sofware
		# ################################

		self.dBase_builder()

		# ################################
		# load the console
		# ################################

		self.oas_Console()    

def main(args):
	app = main_app_start(args)
	sys.exit()

if __name__ == "__main__":
	main(sys.argv)
