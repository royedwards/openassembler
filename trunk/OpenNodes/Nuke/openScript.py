###OpenAssembler Node python file###

'''
define
{
	name openScript
	tags nuke
	input file file "" ""
	output string result "" ""

}
'''
try:
	import nuke
except:
	print "openScript will not work outside of Nuke!!!"

class openScript():
	def openScript_main(self, **connections):
		try:
			file=str(connections["file"])
		except:
			file=""
		try:
			nuke.openScript(file)
			return 1
		except:
			return 0
