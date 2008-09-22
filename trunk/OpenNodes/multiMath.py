###OpenAssembler Node python file###

'''
define
{
	name multiMath
	tags math
	input int A 1
	input int B 1
	output int mult 1
	output int add 1
	output int sub 1
	output int div 1
	output int pow 1

}
'''


class multiMath:
   def multiMath_main(self,A=1, B=1, out=1,oas_output="mult"):

	if oas_output=="mult":
		try:
			return float(A)*float(B)
		except:
			return 0

	elif oas_output=="add":
		try:
			return float(A)+float(B)
		except:
			return 0
			
	elif oas_output=="sub":
		try:
			return float(A)-float(B)
		except:
			return 0	
			
	elif oas_output=="div":
		try:
			return float(A)/float(B)
		except:
			return 0
			
	if oas_output=="pow":
		try:
			return float(A)**float(B)
		except:
			return 0
			
	else:
		return 0
