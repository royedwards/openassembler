###OpenAssembler Node python file###

'''
define
{
	name getShotsFarmSetup
	tags ocoo
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	output array1D farmsetup "" ""

}
'''
import os, sys
from OpenProject.getAttribute import getAttribute

class getShotsFarmSetup():
   def getShotsFarmSetup_main(self, **connection):   
	try:
	    Project=str(connection["Project"])
	except:
	    Project=""
	try:
	    Sequence=str(connection["Sequence"])
	except:
	    Sequence=""
	try:
	    Shot=str(connection["Shot"])
	except:
	    Shot=""

	try:
		dpath=":"+str(Project)+":Movie:"+str(Sequence)+":"+str(Shot)

		pri=gA(dpath+".farm_priority")
		if pri=="" or str(pri)=="0":
			pri="99"
		mem=gA(dpath+".farm_memory")
		if mem=="" or str(mem)=="0":
			mem="3000"
		hm=gA(dpath+".farm_hostmask")
		if str(hm)=="0":
			hm=""
		he=gA(dpath+".farm_hostexclude")
		if str(he)=="0":
			he=""

		return [pri,mem,hm,he]

	except:
		return ["99","3000","",""]

def gA(Path):
	return getAttribute().getAttribute_main(Path=Path)