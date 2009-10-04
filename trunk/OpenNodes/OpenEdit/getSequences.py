###OpenAssembler Node python file###

'''
define
{
	name getSequences
	tags oped
	input string Project "" ""
	output array1D sequences "" ""

}
'''
import os, sys, platform
from OpenProject.getElementList import getElementList

class getSequences():
   def getSequences_main(self, **connections):

	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try: 
	    oas_output=connection["oas_output"]
	except:
	    oas_output="sequences"
	
	if oas_output=="sequences":
		try:
			seques=geT(":"+str(Project)+":Movie")
			ret=[]
			for item in seques:
				if item=="Assets" or item=="Art" or item=="Attributes":
					pass
				else:
					ret.append(item)
			return ret
		except:
			return 0
			
	else:
		return 0

def geT(Path):
	return getElementList().getElementList_main(Path=Path)