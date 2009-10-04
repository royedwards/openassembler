###OpenAssembler Node python file###

'''
define
{
	name homeFolder
	tags pymod
	output file home "" ""

}
'''

class homeFolder():
	def homeFolder_main(self, **connections):
		opdb_userhome=""
		if os.name=="nt":
			opdb_userhome=os.environ.get("USERPROFILE")
		else:
			opdb_userhome=os.environ.get("HOME")
		return opdb_userhome