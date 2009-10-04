###OpenAssembler Node python file###

'''
define
{
	name stringAdder
	tags pymod
	input any in01 "" ""
	input any in02 "" ""
	input any in03 "" ""
	output string sum "" ""

}
'''

class stringAdder():
	def stringAdder_main(self, **connections):
		ret=""
		array=[]
		for key in connections.keys():
			if str(key[:2])=="in":
				array.append(key)
		array.sort()
		for item in array:
			ret+=str(connections[item])
		return ret


