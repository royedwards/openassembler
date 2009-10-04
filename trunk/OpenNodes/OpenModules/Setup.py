######################################################################################
#
#  OpenProjectDb V1
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.01.08
#
######################################################################################

######################################################################################################################################
#
# This file is to handle the setup file and to init the software
#
######################################################################################################################################

import os
import sys
import string
import platform

class opdb_setup:
	
######################################################################################################################################
# Here we load and parse the setup file
######################################################################################################################################

	def opdb_setup_read(self):
		plat=""
		try:
			plat=platform.system()
		except:
			#print "There was some problem with the platform command, anyway we continue it..."
			plat="problematic"
		
		if plat=="Windows":
			opdb_userhome=os.environ.get("USERPROFILE")
			opdb_home=str(opdb_userhome)+"/OpenAssembler"
		else:
			opdb_userhome=os.environ.get("HOME")
			opdb_home=str(opdb_userhome)+"/.OpenAssembler"
	    	
		if os.path.isdir(opdb_home):
			pass
	    	else:
			print "There is no settings directory presented in your home folder... we are stopping now."
			sys.exit()
		
		opdb_setupFile=opdb_home+"/OpenProjectDb.ini"
		setup_contents_opdb=[]
		
		
		if os.path.isfile(opdb_setupFile)==True:
			setup_contents_opdb=self.opdb_load_setup(opdb_setupFile)
		else:
			print "There is no settings file presented in your home folder... we are stopping now."
			sys.exit()		
		return 	setup_contents_opdb
	
	
	def opdb_load_setup(self,path):
		file=open(path,"r")
		setupFile_Content=file.read()
		setupFile_Content=setupFile_Content.replace("\r\n","\n")
		file.close()
		setupFile_Content=setupFile_Content.split("\n")
		setup_parsed=[]
		for rws in setupFile_Content:
			ret=rws.split()
			if len(ret)>0:
				if str(rws[:1])!=str("#"):
					setup_parsed.append(ret)
		return setup_parsed
		
######################################################################################################################################
# to collect font settings
######################################################################################################################################		

	def opdb_projects_settings(self,parsed):
		pr=""
		for liness in parsed:
			if liness[0]=="project_root":
				pr=liness[1]
		return pr

		
	def opdb_vaults_settings(self,parsed):
		vr=""
		for liness in parsed:
			if liness[0]=="vault_root":
				vr=liness[1]
		return vr

		
	def opdb_admin_settings(self,parsed):
		ar=""
		for liness in parsed:
			if liness[0]=="admin_root":
				ar=liness[1]
		return ar
		

	def opdb_dev_settings(self,parsed):
		dv=""
		for liness in parsed:
			if liness[0]=="dev_root":
				dv=liness[1]
		return dv
		
