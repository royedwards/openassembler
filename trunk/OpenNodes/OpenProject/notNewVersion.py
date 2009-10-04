###OpenAssembler Node python file###

'''
define
{
	name notNewVersion
	tags opdb
	input string Project "" ""
	input string Category "" ""
	input dbPath dbPath "" ""
	output int result "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class notNewVersion(opdb_setup):
   def notNewVersion_main(self, **connections):

		project=connections["Project"]
		category=connections["Category"]
		dbPath=connections["dbPath"]

		self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())

		dircont=(self.AdminROOT+"/"+str(project)+"/Review/"+str(category))
		dfi=dircont+"/newsubmissionspath.atr"
		ret=[]
		if os.path.isdir(dircont):
			if os.path.isfile(dfi):
				fl=open(dfi,"r")
				redd=fl.read()
				fl.close()
				ofile=""
				if redd.strip()!="":
					for lines in redd.strip().split("\n"):
						if dbPath.find("@")>-1:
							dbPath=dbPath.split("@")[0]
						if lines.strip()!=dbPath:
							ofile+=lines.strip()+"\n"
				
				fl=open(dfi,"w")
				fl.write(ofile)
				fl.close()
				return 1

		return 0
