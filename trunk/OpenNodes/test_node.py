###OpenAssembler Node python file###

'''
define
{
	name test_node
	tags math
	input int number 1
	input string string 1
	input boolean boolean 1
	input vector vector (1,2,3)
	input text text "nagyonhoszutext"
	input path file "no-path"
	output int out 1

}
'''


class test_node:
   def test_node_main(self,A=1, B=1, out=1,oas_output="out"):

	if oas_output=="out":
		try:
			return float(A)*float(B)
		except:
			return 0
	else:
		return 0
