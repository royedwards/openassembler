###OpenAssembler Node python file###

'''
define
{
	name check_img
	tags opsub
	input file Picture "" ""
	input string Project "" ""
	input string Category "" ""
	input string Type "" ""
	output int result "" ""

}
'''
import os, sys,time, Image
from Setup import opdb_setup

class check_img(opdb_setup):
   def check_img_main(self, **connections):
	try:
		Picture=connections["Picture"]
	except:
		Picture=""
	try:
		Project=connections["Project"]
	except:
		Project=""
	try:
		Category=connections["Category"]
	except:
		Category=""
	try:
		Type=connections["Type"]
	except:
		Type=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
			ProjectROOT=self.opdb_projects_settings(self.opdb_setup_read())
			if os.path.isfile(Picture):
				image=Image.open(str(Picture))
				size=image.size
				if Type=="Art":
					if os.path.isfile(ProjectROOT+"/"+str(Project)+"/resolution.atr"):
						fl=open(ProjectROOT+"/"+str(Project)+"/resolution.atr","r")
						cont= fl.read()
						fl.close()
						c=cont.strip().lstrip().split("x")
						#modification for digitalapes
						return 1
						# modification ends

						if int(size[0])==int(c[0]) and int(size[1])==int(c[1]):
							return 1
						else:
							return 0
					else:
						return 0
			else: 
				return 0
			return 1
		except:
			return 0
			
	else:
		return 0


if __name__ == "__main__":
	print check_img().check_img_main( Picture="/home/simanlaci/test.jpg", Project="Suicide", Category="Shot", Type="Art", oas_output="result")
 
