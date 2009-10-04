###OpenAssembler Node python file###

'''
define
{
	name getShotTiming
	tags ocoo
	input string Project "" ""
	input string Shot "" ""
	output multyShedule Timing "" ""

}
'''
import os, sys, time
from Setup import opdb_setup
from writeShotTiming import writeShotTiming


class getShotTiming(opdb_setup,writeShotTiming):
   def getShotTiming_main(self, **connection):
   
	try:
	    Project=str(connection["Project"])
	except:
	    Project=""
	try:
	    Shot=str(connection["Shot"])
	except:
	    Shot=""
	try:
	    oas_output=connection["oas_output"]
	except:
	    oas_output="Timing"

	if oas_output=="Timing":
		try:
			readed=""
			ret=[]
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			path=ProjectROOT+"/"+str(Project)+"/Movie/"+str(str(Shot).split("_")[0])+"/"+str(Shot)+"/shedule.atr"
			if os.path.isfile(path):
				pass
			else:
				x=self.writeShotTiming_main(Project=Project,Shot=Shot)
				if x==0 or x=="":
					return 0

			fl=open(path,"r")
			readed=fl.read()
			fl.close()

			if readed.strip()!="":
				for line in readed.strip().split("\n"):
					ret.append({"category":str(line.split(" | ")[0].strip()),"user":str(line.split(" | ")[1].strip()), "start_date":str(line.split(" | ")[2].strip()), "end_date":str(line.split(" | ")[3].strip()), "status":str(line.split(" | ")[4].strip())})
			return ret
		except:
			return 0
			
	else:
		return 0
