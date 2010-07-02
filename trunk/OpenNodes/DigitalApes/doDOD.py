###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name doDOD
	tags apes
	input string seqPath "" ""
	input string nukePath "" ""
	input int firstFrame "1" ""
	input int lastFrame "2" ""
	output int return "" ""
}
'''
import os,sys

class doDOD():
	def doDOD_main(self,**connections):
		try:
			seqPath=str(connections["seqPath"])
		except:
			seqPath=""
		try:
			nukePath=str(connections["nukePath"])
		except:
			nukePath=""
		try:
			firstFrame=int(connections["firstFrame"])
		except:
			firstFrame=1
		try:
			lastFrame=int(connections["lastFrame"])
		except:
			lastFrame=2

		return str("nuke -t /W/Projects/projectDb/Softwares/OpenNodes/Nuke/autoDOD.py "+str(seqPath)+","+str(nukePath)+","+str(firstFrame)+","+str(lastFrame))

