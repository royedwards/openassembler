###OpenAssembler Node python file###

'''
define
{
	name addComment
	tags opdb
	input dbPath Path "" ""
	input string Comment "" ""
	output int result "" ""

}
'''
import os, sys,time
from Setup import opdb_setup
from getCleanPath import getCleanPath

class addComment(opdb_setup,getCleanPath):
   def addComment_main(self, **connections):

	try:
	    Path=connections["Path"]
	except:
	    Path=""
	try:
	    Comment=connections["Comment"]
	except:
	    Comment=""
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="result"

	if oas_output=="result":
		try:
			readed=""
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			cleanpath=self.getCleanPath_main(Path=Path)
			if cleanpath==0:
				return 0
			if str(cleanpath)==str(Path):
				return 0
			path=ProjectROOT+cleanpath.replace(":","/")
			ltime=time.strftime("%Y%m%d%H%M%S",time.gmtime())
			cuser=""
			if os.name=="nt":
				cuser=os.environ.get("USERNAME")
			else:	
				cuser=os.environ.get("USER")

			if os.path.isfile(path+"/comments.atr"):
				pf=open(path+"/comments.atr","r")
				readed=pf.read()
				pf.close()
				readed=readed.strip().lstrip()
			ver=Path.split("@")[1]
			comm=str(Comment).strip().lstrip().replace("\n"," | ").replace("\r","")
			newline="- "+str(cuser)+" "+str(ver)+" "+str(ltime)+" || "+comm
			
			textbody=newline+"\n"+readed+"\n"

			pf=open(path+"/comments.atr","w")
			pf.write(textbody)
			pf.close()

			return 1
		except:
			return 0
			
	else:
		return 0
