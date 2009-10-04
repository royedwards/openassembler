###OpenAssembler Node python file###

'''
define
{
	name try_except
	tags pymod
	input functionCall _try_ "" ""
	input functionCall _except_ "" ""
	output any result "" ""

}
'''

class try_except():
	def try_except_main(self, **connections):
		_try_=connections["_try_"]
		_except_=connections["_except_"]

		try:
			return _try_()
		except:
			return _except_()