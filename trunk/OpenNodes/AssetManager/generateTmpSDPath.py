###OpenAssembler Node python file###

'''
define
{
	name generateTmpSDPath
	tags amanage
	output file tmppath "" ""

}
'''
import time, sys, os, shutil, time

class generateTmpSDPath():
	def generateTmpSDPath_main(self, **connections):
		try:
			if os.name=="nt":
				self.oas_userhome=os.environ.get("USERPROFILE")	
			else:
				self.oas_userhome=os.environ.get("HOME")

			self.oas_tmp=str(self.oas_userhome)+"/tmp_opentools"

			if os.path.isdir(self.oas_tmp):
				pass
			else:
				os.makedirs(self.oas_tmp)

			lt=time.localtime()
			loct=""
			for i in lt:
				loct+=str(i)

			filename=self.oas_tmp+"/"+loct+".atr"

			return filename

		except:
			return 0

