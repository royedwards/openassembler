###OpenAssembler Node python file###

'''
define
{
	name getInstalled
	tags opsw
	output array1D installedSoftwares "[]" ""

}
'''
import os, sys,shutil,platform

class getInstalled():
   def getInstalled_main(self, **connections):
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="installedSoftwares"

	if oas_output=="installedSoftwares":
		try:
			if os.name=="nt":
				pp="c:/OpenTools"
			elif os.name=="posix":
				pp="/opt/OpenTools"
			if os.path.isdir(pp):
				pass
			else:
				os.makedirs(pp)
				os.makedirs(pp+"/Icons")
				os.makedirs(pp+"/bin")
				os.makedirs(pp+"/OpenNodes")

				fl=open(pp+"/installed.atr","w")
				fl.write("")
				fl.close()
	
			fl=open(pp+"/installed.atr","r")
			r=fl.read()
			fl.close()

			r=r.strip().lstrip()
			rs=r.split("\n")
			ret=[]
			for ls in rs:
				tmp=ls.strip().lstrip()
				if tmp!="":
					ret.append(str(tmp))

			return ret
		except:
			return 0	
	else:
		return 0

if __name__ == "__main__":
	print getInstalled().getInstalled_main(oas_output="installedSoftwares")
 