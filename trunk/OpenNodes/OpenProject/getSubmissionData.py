###OpenAssembler Node python file###

'''
define
{
	name getSubmissionData
	tags opdb
	input dbPath dbPath "" ""
	output dict result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from OpenProject.getElementType import getElementType

class getSubmissionData(opdb_setup,getElementType):
   def getSubmissionData_main(self, **connections):

	dbPath=str(connections["dbPath"])

	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":

		ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
		VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
		path_type=self.getElementType_main(Path=dbPath)	
		if path_type!="version":
			return 0
		fn=VaultROOT+dbPath.replace(":","/").replace("@","/")+"/submissioncomment.atr"

		if os.path.isfile(fn):
			fl=open(fn,"r")
			ree=fl.read()
			fl.close()

			if ree.strip()=="":
				return 0
			reelines=ree.strip().split("\n",1)
			fline=reelines[0]
			try:
				sline=reelines[1]
			except:
				sline=""
			path=fline.split(" | ")[0]
			user=fline.split(" | ")[1]
			timestemp=fline.split(" | ")[2]
			dte=timestemp[:4]+"."+timestemp[4:6]+"."+timestemp[6:8]+"--"+timestemp[8:10]+":"+timestemp[10:12]+" ("+timestemp[12:]+")"

			return {"Path":path,"User":user,"Comment":sline,"Time":dte}
	else:
		return 0


