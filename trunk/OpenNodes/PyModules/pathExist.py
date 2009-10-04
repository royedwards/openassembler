###OpenAssembler Node python file###

'''
define
{
	name pathExist
	tags pymod
	input file Path "" ""
	output int isDir "" ""
	output int isFile "" ""

}
'''
import os,sys

class pathExist():
	def pathExist_main(self, **connections):
		Path=str(connections["Path"])
		try: 
		    oas_output=connections["oas_output"]
		except:
		    oas_output="isFile"

		if oas_output=="isFile":
			if os.path.isfile(Path):
				return 1
			else:
				return 0
		if oas_output=="isDir":
			if os.path.isdir(Path):
				return 1
			else:
				return 0