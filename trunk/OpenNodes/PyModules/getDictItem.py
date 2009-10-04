###OpenAssembler Node python file###

'''
define
{
	name getDictItem
	tags pymod
	input dict Dictionary "" ""
	input any item "" ""
	output any out_item "" ""
}
'''

class getDictItem():
	def getDictItem_main(self, **connections):
		Dictionary=connections["Dictionary"]
		item=connections["item"]
		try:
			return Dictionary[item]
		except:
			return 