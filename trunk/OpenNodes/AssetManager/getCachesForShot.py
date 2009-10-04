###OpenAssembler Node python file###

'''
define
{
	name getCachesForShot
	tags amanage
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	output array1D list "" ""

}
'''

from OpenProject.getElementList import getElementList

class getCachesForShot():
	def getCachesForShot_main(self, **connections):
		try:
			Project=str(connections["Project"])
		except:
			Project=""
		try:
			Sequence=str(connections["Sequence"])
		except:
			Sequence=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
	
		try:
			retlist=[]

			cachednodes=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches")

			for node in cachednodes:
				cachedparams=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+node)
				for param in cachedparams:
					retlist.append(node+" >>> "+param)

			return retlist
		except:
			return []

def getEL(Path):
	return getElementList().getElementList_main(Path=Path)