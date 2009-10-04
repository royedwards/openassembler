###OpenAssembler Node python file###

'''
define
{
	name multiMath
	tags math
	input float A "1" ""
	input float B "1" ""
	output float mult "1" ""
	output float add "1" ""
	output float sub "1" ""
	output float div "1" ""
	output float pow "1" ""

}
'''


class multiMath:
   def multiMath_main(self,**connections):
	try:
	    A=float(connections["A"])
	except:
	    A=1
	try:
	    B=float(connections["B"])
	except:
	    B=1
	try:
	    oas_output=str(connections["oas_output"])
	except:
	    oas_output="mult"
	    
	if oas_output=="mult":
		try:
			return float(A)*float(B)
		except:
			return "Fail"

	elif oas_output=="add":
		try:
			return float(A)+float(B)
		except:
			return "Fail"
			
	elif oas_output=="sub":
		try:
			return float(A)-float(B)
		except:
			return "Fail"	
			
	elif oas_output=="div":
		try:
			return float(A)/float(B)
		except:
			return "Fail"
			
	if oas_output=="pow":
		try:
			return float(A)**float(B)
		except:
			return "Fail"
			
	else:
		return "Fail"
