###OpenAssembler Node python file###

'''
define
{
	name printer
	tags viewer
	input any A 1

}
'''


class printer:
   def printer_main(self,A="",oas_output=""):

	print str(A)
	return A