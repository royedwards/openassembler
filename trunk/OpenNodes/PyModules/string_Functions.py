###OpenAssembler Node python file###

'''
define
{
	name string_Functions
	tags pymod
	input string A "" ""
	input string B "" ""
	output string A_strip "" ""
	output string B_strip "" ""
	output array1D split_A_with_B "" ""
	output array1D split_to_lines "" ""
	output array1D sp_and_st "" ""
	output string A_lower "" ""

}
'''

class string_Functions():
	def string_Functions_main(self, **connections):
		A=str(connections["A"])
		B=str(connections["B"])
		try: 
		    oas_output=connections["oas_output"]
		except:
		    oas_output="A_strip"

		if oas_output=="A_strip":
			return A.strip()

		if oas_output=="B_strip":
			return B.strip()
		
		if oas_output=="split_A_with_B":
			return A.split(B)

		if oas_output=="split_to_lines":
			b=A.split("\n")
			return b

		if oas_output=="sp_and_st":
			b=A.strip().split("\n")
			fin=[]
			for item in b:
				if item!="":
					fin.append(item.strip())
			return fin

		if oas_output=="A_lower":
			return A.lower()