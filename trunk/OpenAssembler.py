#! /usr/bin/env python

######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################


import sys
import os
from Startup.Startup import oas_start
from threading import Thread


#-------------------------------------------------------------------------------------
#   Parsing the arg's
#-------------------------------------------------------------------------------------

oas_arg_mode="normal"
oas_arg_inputfile=""
if len(sys.argv)<2:
	pass
else:
	for i in range(1,len(sys.argv)):
		if sys.argv[i]=="-h" or sys.argv[i]=="--h" or sys.argv[i]=="-help" or sys.argv[i]=="--help" or sys.argv[i]=="?" or sys.argv[i]=="-?":
			print '''
OpenAssembler v2 alpha-001
Owner: Laszlo Mates

Options:
   -help 		      :display this screen
   -m <normal/console/no-gui> :this are the modes to start OpenAssembler
   -f <inputfile>	      :open a file during the startup		
		'''
			sys.exit(0)
		elif sys.argv[i]=="-f":
			try:
				oas_arg_inputfile=sys.argv[i+1]
			except:
				oas_arg_inputfile=""
			if os.path.isfile(oas_arg_inputfile)!=True:
				oas_arg_inputfile=""
				
		elif sys.argv[i]=="-m":
			try:
				oas_arg_mode=sys.argv[i+1]
				if oas_arg_mode=="normal" or oas_arg_mode=="console" or oas_arg_mode=="client" or oas_arg_mode=="run":
					pass
				else:
					oas_arg_mode="normal"
			except:
				oas_arg_mode="normal"
		else:
			pass



#-------------------------------------------------------------------------------------
#   Pass thru the arg and call the startup
#-------------------------------------------------------------------------------------

arg_list=[oas_arg_mode,oas_arg_inputfile]
oas_start(arg_list)
