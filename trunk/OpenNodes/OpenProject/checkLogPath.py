###OpenAssembler Node python file###

'''
define
{
	name checkLogPath
	tags opdb
	input file logSystemPath "" ""
	input dbPath Path "" ""
	output int result "" ""

}
'''
import os, sys


class checkLogPath:
   def checkLogPath_main(self, **connections):

	try:
		logSystemPath=connections["logSystemPath"]
	except:
		logSystemPath=""
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
			ret=0
			fle=open(logSystemPath,"r")
			rdd=fle.read()
			fle.close()
		
			rdd=rdd.strip().lstrip()
			lines=rdd.split("\n")
		
			if lines==['']:
				pass
			else:
				for line in lines:
					if line.strip().lstrip().split()[0]==Path:
						ret=1
			return ret
		except:
			return -1
			
	else:
		return -1