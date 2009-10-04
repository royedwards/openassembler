###OpenAssembler Node python file###

'''
define
{
	name mult
	tags math
	input float A "1" ""
	input float B "1" ""
	output float out "1" ""

}
'''


class mult:
   def mult_main(self,**connections):
	try:
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
		oas_output="out"
	
	    if oas_output=="out":
	    	    try:
			    return float(A)*float(B)
		    except:
			    return "Fail"
	    else:
		    return "Fail"
	except:
		return "Fail"