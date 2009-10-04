###OpenAssembler Node python file###

'''
define
{
	name string_if
	tags pymod
	input string A "" ""
	input string B "" ""
	input functionCall callIfTrue "" ""
	input functionCall callIfFalse "" ""
	output string A_equal_B "" ""
	output string B_part_A "" ""

}
'''

class string_if():
	def string_if_main(self, **connections):
		callIfTrue=connections["callIfTrue"]
		callIfFalse=connections["callIfFalse"]
		A=str(connections["A"])
		B=str(connections["B"])
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
		
		if oas_output=="B_part_A":
			if A.find(B)>-1:
				return callIfTrue(**passt)
			else:
				return callIfFalse(**passt)