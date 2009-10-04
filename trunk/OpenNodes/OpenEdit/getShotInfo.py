###OpenAssembler Node python file###

'''
define
{
	name getShotInfo
	tags oped
	input string Project "" ""
	input string Shot "" ""
	output shotInfo shotinfo "" ""

}
'''
import os, sys, platform
from getEdit import getEdit
from Setup import opdb_setup
from OpenProject.getElementType import getElementType
from OpenProject.getVaultPath import getVaultPath
from OpenCoOrdination.getShotTiming import getShotTiming

class getShotInfo(getEdit,getElementType,opdb_setup,getVaultPath,getShotTiming):
   def getShotInfo_main(self, **connections):
	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Shot=connections["Shot"]
	except:
	    Shot=""
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="shotinfo"

	if oas_output=="shotinfo":
		try:
			shedule={"user":"", "start_date":"", "end_date":"", "status":""}
			ret={
				"name":"",
				"order":"",
				"state":"",
				"on_track":"",
				"inpoint":"",
				"outpoint":"",
				"startframe":"",
				"endframe":"",
				"description":"",
				"due_to":"",
				"design":shedule,
				"layout":shedule,
				"animation":shedule,
				"simulation":shedule,
				"fx":shedule,
				"lighting":shedule,
				"compositing":shedule
					}

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			VaultROOT=self.opdb_vaults_settings(self.opdb_setup_read())
			eT=self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(str(Shot).split("_")[0])+":"+str(Shot))
			editPath=self.getVaultPath_main(Path=":"+str(Project)+":Story:Edit@live")
			if eT!="container":
				return 0
			edit=self.getEdit_main(Project=Project,Version="live")
			for shot in edit:
				if str(shot[1]["name"])==str(Shot):
					ret["name"]=shot[1]["name"]
					ret["order"]=shot[0]
					ret["state"]=shot[1]["state"]
					ret["on_track"]=shot[1]["track"]
					ret["inpoint"]=shot[1]["inpoint"]
					ret["outpoint"]=shot[1]["outpoint"]
					ret["startframe"]=shot[1]["startframe"]
					ret["endframe"]=shot[1]["endframe"]
			try:
				fl=open(editPath+"/"+str(Shot)+".txt","r")
				readed_desc=fl.read()
				fl.close()
				ret["description"]=readed_desc.strip()
			except:
				ret["description"]=""

			timing = self.getShotTiming_main(Project=Project,Shot=Shot)
			for rows in timing:
				ret[rows["category"]]={"user":rows["user"], "start_date":rows["start_date"], "end_date":rows["end_date"], "status":rows["status"]}
			return ret
		except:
			return 0
			
	else:
		return 0
