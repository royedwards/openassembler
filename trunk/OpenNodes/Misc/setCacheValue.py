###OpenAssembler Node python file###

'''
define
{
	name setCacheValue
	tags msc
	output any result "" ""
}
'''


class setCacheValue:
   def setCacheValue_main(self,**connections):
	try:
		for key in connections.keys():
		    if key=="oas_output" or key=="_frame" or key=="_do_cache" or key=="_cache":
				pass
		    else:
				connections["_cache"][str(key)]=str(connections[key])
		return 1
	except:
		return 0