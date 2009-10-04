###OpenAssembler Node python file###

'''
define
{
	name if_equals
	tags pymod
	input string A "" ""
	input string B "" ""
	input any TrueValue "" ""
	input any ElseValue "" ""
	output any result "" ""

}
'''

class if_equals():
	def if_equals_main(self, **connections):
		TrueValue=connections["TrueValue"]
		ElseValue=connections["ElseValue"]
		A=connections["A"]
		B=connections["B"]
		try: 
		    oas_output=connection["oas_output"]
		except:
		    oas_output="result"
		
		if A==B:
			return TrueValue
		else:
			return ElseValue