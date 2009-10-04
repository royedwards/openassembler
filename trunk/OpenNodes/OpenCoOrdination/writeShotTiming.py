###OpenAssembler Node python file###

'''
define
{
	name writeShotTiming
	tags ocoo
	input string Project "" ""
	input string Shot "" ""
	input multyShedule Timing "" ""
	output int result "" ""

}
'''
import os, sys, time
from Setup import opdb_setup
from OpenProject.getElementType import getElementType


class writeShotTiming(opdb_setup,getElementType):
   def writeShotTiming_main(self, **connections):

	try:
	    Project=str(connections["Project"])
	except:
	    Project=""
	try:
	    Shot=str(connections["Shot"])
	except:
	    Shot=""
	try:
	    Timing=connections["Timing"]
	except:
	    Timing=[{"category":"","user":"None","start_date":"", "end_date":"","status":"Waiting"}]
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="result"
	    
	if oas_output=="result":
		try:
			eT=self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(str(Shot).split("_")[0])+":"+str(Shot))
			if eT=="" or eT==0:
				return 0
			currenttime=str(time.gmtime()[0])+"."+str(time.gmtime()[1]).zfill(2)+"."+str(time.gmtime()[2])
			if time.gmtime()[1]==12:
				newyear=str(time.gmtime()[0]+1)
				newmonth=str(1)
			else:
				newyear=str(time.gmtime()[0]).zfill(2)
				newmonth=str(time.gmtime()[1]+1)
			endtime=newyear+"."+newmonth+"."+str(time.gmtime()[2])
			categories=["design","layout","animation","simulation","fx","lighting","compositing"]
			if Timing=="":
				Timing=[]
				for cats in categories:
					Timing.append({"category":str(cats),"user":"None", "start_date":str(currenttime), "end_date":str(endtime), "status":"Waiting"})
			to_file=""
			for items in Timing:
				to_file+=str(items["category"])+" | "+str(items["user"])+" | "+str(items["start_date"])+" | "+str(items["end_date"])+" | "+str(items["status"])+"\n"

			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())

			path=ProjectROOT+"/"+str(Project)+"/Movie/"+str(str(Shot).split("_")[0])+"/"+str(Shot)+"/shedule.atr"

			ff=open(path,"w")
			ff.write(to_file)
			ff.close()

			return 1
		except:
			return 0
			
	else:
		return 0
