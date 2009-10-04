###OpenAssembler Node python file###

'''
define
{
	name getReviewCategories
	tags opdb
	input string Project "" ""
	output array1D reviewCategories "" ""

}
'''
import os, sys, platform
from Setup import opdb_setup

class getReviewCategories(opdb_setup):
   def getReviewCategories_main(self, **connections):

		Project=connections["Project"]

		self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())

		dircont=[]

		if os.path.isdir(self.AdminROOT+"/"+str(Project)+"/Review"):
			dircont=os.listdir(self.AdminROOT+"/"+str(Project)+"/Review")
		else: 
			return []
		ret=[]
		for itm in dircont:
			if os.path.isdir(self.AdminROOT+"/"+str(Project)+"/Review/"+str(itm)):
				ret.append(itm)
		return ret
