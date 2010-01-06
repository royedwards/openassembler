###OpenAssembler Node python file###

'''
define
{
	name writeTextFile
	tags pymod
	input file dir "" ""
	input string name "" ""
	input string content "" ""
	output any result "" ""

}
'''
import os, sys,shutil

class writeTextFile():
   def writeTextFile_main(self, **connections):
	try:
		 dir=str(connections["dir"])
	except:
		 dir=""
	try:
		 name=str(connections["name"])
	except:
		 name=""
	try:
		content=str(connections["content"])
	except:
		content=""

	if os.path.isdir(dir):
		pass
	else:
		return 0
	if file=="":
		return 0
	try:
		fl=open(dir+"/"+name,"w")
		fl.write(content)
		fl.close()
		return 1
	except:
		return 0

