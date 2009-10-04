###OpenAssembler Node python file###

'''
define
{
	name breakIfZero
	tags pymod
	input any input "" ""
	input functionCall callIfZero "" ""
	output any output "" ""

}
'''

class breakIfZero():
	def breakIfZero(self, **connections):
		callIfZero=connections["callIfZero"]
		input=connections["input"]
		if callIfZero=="":
			return 0

		passt={}
		for key in connections.keys():
			if key=="_cache" or key=="_do_cache" or key=="_frame" or key=="input" or key=="oas_output" or key=="callIfZero":
				pass
			else:
				passt[key]=connections[key]
		passt["_input"]=input

		if str(input)=="0":
			return callIfZero(**passt)

		return input