###OpenAssembler Node python file###

'''
define
{
	name string_switch
	tags pymod
	input string Value "" ""
	output any result "" ""

}
'''

class string_switch():
	def string_switch_main(self, **connections):
		try:
			Value=connections["Value"]
		except:
			Value=""

		passt={}
		for key in connections.keys():
			if key=="_cache" or key=="_do_cache" or key=="_frame" or key=="Value" or key=="oas_output":
				pass
			else:
				passt[key]=connections[key]
		passt["_Value"]=Value

		for key in connections.keys():
			if str(key)==str(Value):
				connections[key](**passt)