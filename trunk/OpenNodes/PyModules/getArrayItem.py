###OpenAssembler Node python file###

'''
define
{
	name getArrayItem
	tags pymod
	input array1D Array "" ""
	input int itemNumber "0" ""
	output any out_item "" ""
}
'''

class getArrayItem():
	def getArrayItem_main(self, **connections):
		Array=connections["Array"]
		itemNumber=connections["itemNumber"]
		try:
			return Array[itemNumber]
		except:
			return 