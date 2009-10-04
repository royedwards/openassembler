###OpenAssembler Node python file###

'''
define
{
	name in_out
	tags pymod
	input any _in "" ""
	output any out_ "" ""

}
'''

class in_out():
	def in_out_main(self, **connections):
		return connections["_in"]