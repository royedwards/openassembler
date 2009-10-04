###OpenAssembler Node python file###

'''
define
{
	name getShots
	tags oped
	input string Project "" ""
	input string Sequence "" ""
	output array1D shots "" ""

}
'''
import os, sys, platform
from OpenProject.getElementList import getElementList

class getShots():
   def getShots_main(self, **connections):

	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Sequence=connections["Sequence"]
	except:
	    Sequence=""
	try: 
	    oas_output=connection["oas_output"]
	except:
	    oas_output="shots"
	
	if oas_output=="shots":
		try:
			elem=geT(":"+str(Project)+":Movie:"+str(Sequence))
			ret=[]
			for item in elem:
				if item=="Art" or item=="Assets" or item=="Attributes":
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