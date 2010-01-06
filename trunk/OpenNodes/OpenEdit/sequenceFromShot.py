###OpenAssembler Node python file###

'''
define
{
	name sequenceFromShot
	tags oped
	input string Project "" ""
	input string Shot "" ""
	output any sequence "" ""

}
'''
import os, sys, platform
from OpenProject.getElementList import getElementList
from OpenEdit.getSequences import getSequences

class sequenceFromShot():
   def sequenceFromShot_main(self, **connections):

	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    Shot=connections["Shot"]
	except:
	    Shot=""
	try: 
	    oas_output=connection["oas_output"]
	except:
	    oas_output="sequence"
	
	if oas_output=="sequence":
		try:
			sequences=getS(Project)
			seq=""
			for Sequence in sequences:
				elem=geT(":"+str(Project)+":Movie:"+str(Sequence))
				for item in elem:
					if item==Shot:
						seq=Sequence
			return seq
		except:
			return 0
			
	else:
		return 0

def geT(Path):
	return getElementList().getElementList_main(Path=Path)

def getS(Project):
	return getSequences().getSequences_main(Project=Project)