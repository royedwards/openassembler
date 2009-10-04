###OpenAssembler Node python file###

'''
define
{
	name writeIntegrityPanic
	tags opdb
	input dbPath Path "" ""
	input string Problem "" ""
        input string Description "" ""
	output int result "" ""

}
'''
import os, sys
from Setup import opdb_setup
from  getElementType import getElementType
from checkLogPath import checkLogPath

class writeIntegrityPanic(checkLogPath,opdb_setup,getElementType):
   def writeIntegrityPanic_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Problem=connections["Problem"]
	except:
		Problem=""
	try:
		Description=connections["Description"]
	except:
		Description=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
                        self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			panicfile=""
                        if self.getElementType_main(Path=Path)=="projectRoot":
                                panicfile=self.AdminROOT+"/common/integrity_panic.atr"
                        elif self.getElementType_main(Path=Path)!="":
                                pr=Path.split(":")[1]
				panicfile=self.AdminROOT+"/"+pr+"/integrity_panic.atr"
                        else:
                                pass

                        if Path==":":
                                wpath=Path+Problem
                        else:
                                wpath=Path+":"+Problem

			if panicfile!="":
                                if os.path.isfile(panicfile):
					xx=self.checkLogPath_main(logSystemPath=panicfile,Path=wpath)
					if xx==0:
                                                fl=open(panicfile,"r")
                                                rea=fl.read()
                                                fl.close()
                                                tolog=rea.strip().lstrip()+"\n"+str(wpath)+"   "+Description+"\n"

                                                fl=open(panicfile,"w")
                                                fl.write(tolog)
                                                fl.close()
                                        else:
                                                pass


                                else:
                                        tolog=str(wpath)+"   "+panicdescription+"\n"

                                        fl=open(panicfile,"w")
                                        fl.write(tolog)
                                        fl.close()

			return 1
		except:
			return 0

	else:
		return 0
