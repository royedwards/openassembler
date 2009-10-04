###OpenAssembler Node python file###

'''
define
{
	name setCommentDone
	tags opdb
	input dbPath Path "" ""
	input string TimeIdent "" ""
	output int result "" ""

}
'''
import os, sys,time
from Setup import opdb_setup
from getCleanPath import getCleanPath

class setCommentDone(opdb_setup,getCleanPath):
   def setCommentDone_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		TimeIdent=connections["TimeIdent"]
	except:
		TimeIdent=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			readed=""
			if TimeIdent=="":
				return 0
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			cleanpath=self.getCleanPath_main(Path=Path)
			if cleanpath==0:
				return 0
			path=ProjectROOT+cleanpath.replace(":","/")

			if os.path.isfile(path+"/comments.atr"):
				pf=open(path+"/comments.atr","r")
				readed=pf.read()
				pf.close()
				readed=readed.strip()
			if readed=="":
				return 0
			lines=readed.split("\n")
			retlines=[]
			for line in lines:
				rl=line
				if line.split(" ")[3]==str(TimeIdent):
					if rl[:1]=="-":
						rl=rl.replace("-","+",1)
				retlines.append(rl)

			otxt=""

			for lin in retlines:
				otxt+=str(lin)+"\n"

			if os.path.isfile(path+"/comments.atr"):
				pf=open(path+"/comments.atr","w")
				pf.write(otxt)
				pf.close()
			return 1
		except:
			return 0
			
	else:
		return 0
