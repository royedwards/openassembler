###OpenAssembler Node python file###

'''
define
{
	name generateMovCmd
	tags oped
	input dbPath shotDbPath "" ""
	input string Version "" ""
	input string nukePrefixCMD "" ""
	input string nukeTemplate "" ""
	input string pythonFile "" ""
	output string command "" ""
}
'''
import os, sys, platform

class generateMovCmd():
   def generateMovCmd_main(self, **connections):
	try:
	    versionLinks=str(connections["versionLinks"])
	except:
	    versionLinks=""
	try:
	    Version=str(connections["Version"])
	except:
	    Version=""
	try:
	    nukePrefixCMD=str(connections["nukePrefixCMD"])
	except:
	    nukePrefixCMD=""
