###OpenAssembler Node python file###

'''
define
{
	name getIntegrityPanic
	tags opdb
	input string Project "" ""
	output array1D result "" ""

}
'''
import os, sys
from Setup import opdb_setup

class getIntegrityPanic(opdb_setup):
   def getIntegrityPanic_main(self, **connections):
	try:
		Project=connections["Project"]
	except:
		Project=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
                        self.AdminROOT=self.opdb_admin_settings(self.opdb_setup_read())
			panicfile=""
                        if Project=="projectRoot":
                                panicfile=self.AdminROOT+"/common/integrity_panic.atr"
                        elif Project!="":
				panicfile=self.AdminROOT+"/"+Project+"/integrity_panic.atr"
                        else:
                                pass
			rea=""
			if panicfile!="":
                                if os.path.isfile(panicfile):
                                	fl=open(panicfile,"r")
                                        rea=fl.read()
                                        fl.close()

                                else:
					pass
					
			ret=[]
			if rea!="":
				lines=rea.strip().lstrip().split("\n")
				for line in lines:
					ret.append(line)
			else:
				return 0
			return ret
		except:
			return 0

	else:
		return 0

if __name__ == "__main__":
	getIntegrityPanic().getIntegrityPanic_main(Project="projectRoot",oas_output="result")
