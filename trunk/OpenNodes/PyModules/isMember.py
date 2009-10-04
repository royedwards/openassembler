###OpenAssembler Node python file###

'''
define
{
	name isMember
	tags pymod
	input array1D Array "[]" ""
	input any Input "" ""
	output any output "" ""

}
'''

class isMember():
	def isMember_main(self, **connections):
		res= "False"
		for item in connections["Array"]:
			if item==connections["Input"]:
				res="True"
		return res
		
			