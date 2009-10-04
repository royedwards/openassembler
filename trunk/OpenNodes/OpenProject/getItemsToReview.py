###OpenAssembler Node python file###

'''
define
{
	name getItemsToReview
	tags opdb
	input string Project "" ""
	input string Category "" ""
	output array1D reviewCategories "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getItemsToReview(opdb_setup):
   def getItemsToReview_main(self, **connections):

		project=connections["Project"]
		category=connections["Category"]

		self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())

		dircont=(self.AdminROOT+"/"+str(project)+"/Review/"+str(category))
		dfi=dircont+"/newsubmissionspath.atr"
		ret=[]
		if os.path.isdir(dircont):
			if os.path.isfile(dfi):
				fl=open(dfi,"r")
				redd=fl.read()
				fl.close()
				if redd.strip()!="":
					return redd.strip().split("\n")
		return ret
