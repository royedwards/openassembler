class oas_plus:
	def run(self,a=1,b=1):
		return a+b

class oas_minus:
	def run(self,a=1,b=1):
		return a-b

class oas_mult:
	def run(self,a=2,b=2):
		return a*b

class oas_div:
	def run(self,a=2,b=2):
		return a/b

class oas_print:
	def run(self,*connections):
		for key in connections:
			print 'Result:',key
		return connections[0]

class oas_pass:
	def run(self):
		return None

class oas_expression:
	def run(self,_expression="",*connections):
		exec("value"+_expression)
		return value		

class oas_if:
	def run(self,a=None,b=None,expression="",if_true=None,if_false=None):
		exec("value"+expression)
		if value==True:
			if if_true[2]!=None:
				return if_true[2]
			else:
				return if_true[0](if_true[1])
		else:
			if if_false[2]!=None:
				return if_false[2]
			else:
				return if_false[0](if_false[1])
	def exceptions(self):
		return 'if_true,if_false'
