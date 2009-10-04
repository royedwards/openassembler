###OpenAssembler Node python file###

'''
define
{
	name int_if
	tags pymod
	input int A "0" ""
	input int B "0" ""
	input functionCall callIfTrue "" ""
	input functionCall callIfFalse "" ""
	output any A_equal_B "" ""
	output any A_isLess "" ""
	output any A_isMore "" ""

}
'''

class int_if():
	def int_if_main(self, **connections):
		callIfTrue=connections["callIfTrue"]
		callIfFalse=connections["callIfFalse"]
		A=float(connections["A"])
		B=float(connections["B"])
		if callIfTrue=="":
			return 0
		if callIfFalse=="":
			return 0
		try: 
		    oas_output=connection["oas_output"]
		except:
		    oas_output="A_equal_B"

		passt={}
		for key in connections.keys():
			if key=="_cache" or key=="_do_cache" or key=="_frame" or key=="A" or key=="B" or key=="oas_output" or key=="callIfTrue" or key=="callIfFalse":
				pass
			else:
				passt[key]=connections[key]
		passt["_A"]=A
		passt["_B"]=B

		if oas_output=="A_equal_B":
			if A==B:
				return callIfTrue(**passt)
			else:
				return callIfFalse(**passt)
		
		if oas_output=="A_isLess":
			if A<B:
				return callIfTrue(**passt)
			else:
				return callIfFalse(**passt)

		if oas_output=="A_isMore":
			if A>B:
				return callIfTrue(**passt)
			else:
				return callIfFalse(**passt)