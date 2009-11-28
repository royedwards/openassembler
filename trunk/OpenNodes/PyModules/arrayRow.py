###OpenAssembler Node python file###

'''
define
{
	name arrayRow
	tags pymod
	input any input "" ""
	input int row "0" ""
	output array1D result "" ""
}
'''

class arrayRow():
	def arrayRow_main(self, **connections):
		input=connections["input"]
		row=int(connections["row"])

		try:
			ret=[]
			for line in input:
				ret.append(line[row])
			return ret
		except:
			return []