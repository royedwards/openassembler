###OpenAssembler Node python file###

'''
define
{
	name mult
	tags oas:math
	input int A 1
	input int B 1
	output int out 1

}
'''


class mult:
   def mult_main(self,A=1, B=1, out=1):

	return out=A*B
