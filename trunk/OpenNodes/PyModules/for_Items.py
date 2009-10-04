###OpenAssembler Node python file###

'''
define
{
	name for_Items
	tags pymod
	input array1D Items "[]" ""
	input functionCall FunctionCall "" ""
	output array1D returnValues "" ""

}
'''

class for_Items():
	def for_Items_main(self, **connections):
		Items=connections["Items"]
		FunctionCall=connections["FunctionCall"]
		ret=[]
		passt={}
		for key in connections.keys():
			if key=="_cache" or key=="_do_cache" or key=="_frame" or key=="Items" or key=="oas_output" or key=="FunctionCall":
				pass
			else:
				passt[key]=connections[key]
		for _item in Items:
			passt["_item"]=_item
			a=FunctionCall(**passt)
			ret.append(a)
		return ret
		
			