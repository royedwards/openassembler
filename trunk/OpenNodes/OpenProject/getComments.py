###OpenAssembler Node python file###

'''
define
{
	name getComments
	tags opdb
	input dbPath Path "" ""
	output array2D Comments "" ""

}
'''
import os, sys,time
from Setup import opdb_setup
from getCleanPath import getCleanPath

class getComments(opdb_setup,getCleanPath):
   def getComments_main(self, **connections):

	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="Comments"

	if oas_output=="Comments":
		try:
			readed=""
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			cleanpath=self.getCleanPath_main(Path=Path)
			if cleanpath==0:
				return 0
			path=ProjectROOT+cleanpath.replace(":","/")

			if os.path.isfile(path+"/comments.atr"):
				pf=open(path+"/comments.atr","r")
				readed=pf.read()
				pf.close()
				readed=readed.strip().lstrip()
			if readed=="":
				return []
			lines=readed.split("\n")
			comments_ret=[]
			for line in lines:
				if line.split(" ")[0]=="-":
					status="active"
				else:
					status="done"
				user=line.split(" ")[1]
				version=line.split(" ")[2]
				date=line.split(" ")[3]
				comment=line.split(" || ")[1].replace(" | ","\n")
				comments_ret.append([version,user,date,status,comment])

			comments_ret.sort()
			comments_ret.reverse()
			return comments_ret
		except:
			return 0
			
	else:
		return 0
