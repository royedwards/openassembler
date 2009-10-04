###OpenAssembler Node python file###

'''
define
{
	name printer
	tags msc
	input any A "" ""
	output any A_Out "" ""
}
'''


class printer:
   def printer_main(self,**connections):
	try:
	    A=str(connections["A"])
	except:
	    A=""
	print "---------------------------------------"
	for key in connections.keys():
	    if key=="oas_output" or key=="_frame" or key=="_do_cache" or key=="_cache":
		pass
	    else:
		print key+": "+str(connections[key])
		print "---------------------------------------"
	return A