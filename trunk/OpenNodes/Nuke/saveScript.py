###OpenAssembler Node python file###

'''
define
{
	name saveScript
	tags nuke
	input file file "" ""
	input int Overwrite "0" ""
	output string result "" ""

}
'''
try:
	import nuke
except:
	print "saveScript will not work outside of Nuke!!!"

class saveScript():
	def saveScript_main(self, **connections):
		try:
			file=str(connections["file"])
		except:
			file=""
		try:
			Overwrite=int(connections["Overwrite"])
		except:
			Overwrite=0
		try:
			ret=nuke.scriptSaveAs(filename = file, overwrite = Overwrite)
			if ret==True:
				return 1
			else:
				return 0
		except:
			return 0
