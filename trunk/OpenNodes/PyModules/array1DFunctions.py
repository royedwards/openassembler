###OpenAssembler Node python file###

'''
define
{
	name array1DFunctions
	tags pymod
	input array1D input "[]" ""
	output array1D sort "" ""
	output array1D reverse "" ""
}
'''

class array1DFunctions():
	def array1DFunctions_main(self, **connections):
		input=connections["input"]
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="sort"

		if oas_output=="sort":
			tmp=input
			try:
				tmp.sort()
			except:
				pass
			return tmp

		if oas_output=="reverse":
			tmp=input
			try:
				tmp.reverse()
			except:
				pass
			return tmp