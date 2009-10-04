###OpenAssembler Node python file###

'''
define
{
	name array1DMath
	tags pymod
	input array1D A "[]" ""
	input array1D B "[]" ""
	output array1D A_plus_B "" ""
	output array1D A_minus_B "" ""
}
'''

class array1DMath():
	def array1DMath_main(self, **connections):
		A=connections["A"]
		B=connections["B"]
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="A_plus_B"

		if oas_output=="A_plus_B":
			try:
				return (A+B)
			except:
				return []

		if oas_output=="A_minus_B":
			try:
				C=[]
				for inA in A:
					chk=0
					for inB in B:
						if inA==inB:
							chk=1
					if chk==0:
						C.append(inA)
				return C
			except:
				return []