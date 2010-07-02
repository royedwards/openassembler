###OpenAssembler Node python file###

'''
define
{
	name getClientVersion
	tags oped
	input string versionLinks "" ""
	input string Version "" ""
	output string ClientVersion "" ""
}
'''
import os, sys, platform

class getClientVersion():
   def getClientVersion_main(self, **connections):
	try:
	    versionLinks=str(connections["versionLinks"])
	except:
	    versionLinks=""
	try:
	    Version=str(connections["Version"])
	except:
	    Version=""

	lines=versionLinks.split("\n")
	for l in lines:
		if l.split("|")[1].strip()==Version:
			return  l.split("|")[0].strip()

	return "no"