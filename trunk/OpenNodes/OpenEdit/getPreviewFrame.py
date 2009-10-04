###OpenAssembler Node python file###

'''
define
{
	name getPreviewFrame
	tags oped
	input string Project "" ""
	input string Shot "" ""
	output string RealPath "" ""

}
'''
import os, sys, shutil
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getLiveVersion import getLiveVersion
from OpenProject.getLatestVersion import getLatestVersion

class getPreviewFrame(getVaultPath,getLiveVersion,getLatestVersion):
   def getPreviewFrame_main(self, **connections):

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
	    oas_output="RealPath"

	if oas_output=="RealPath":
		try:
			fold=""

			if os.name=="nt":
				home=os.environ.get("USERPROFILE")
			elif os.name=="posix":
				home=os.environ.get("HOME")
			if os.path.isdir(home+"/tmp_opentools/img_cache"):
				pass
			else:
				os.makedirs(home+"/tmp_opentools/img_cache")

			seq=str(Shot).split("_")[0]
			liv=self.getLiveVersion_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(Shot)+":Art:Concept")
			lav=self.getLatestVersion_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(Shot)+":Art:Concept")
			if str(liv)!=str(0) and str(liv)!="":
				if os.path.isfile(home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(liv)+"_p.jpg"):
					fold=home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(liv)+"_p.jpg"
				else:
					shutil.copy(str(self.getVaultPath_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(Shot)+":Art:Concept@live"))+"/proxy/0001.jpg",home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(liv)+"_p.jpg")
					fold=home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(liv)+"_p.jpg"
			else:
				if str(lav)=="0" and str(lav)=="":
					return 0
				else:
					if os.path.isfile(home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(lav)+"_p.jpg"):
						fold=home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(lav)+"_p.jpg"
					else:
						shutil.copy(str(self.getVaultPath_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(Shot)+":Art:Concept@latest"))+"/proxy/0001.jpg",home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(lav)+"_p.jpg")
						fold=home+"/tmp_opentools/img_cache/"+str(Project)+"_"+str(Shot)+"_"+str(lav)+"_p.jpg"
			return fold
		except:
			return 0
			
	else:
		return 0
