###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name sequenceChecker
	tags msc
	input string sequenceName "" ""
	input file Folder "" ""
	input string Padding "" ""
	input string extensionList "" ""
	input string firstItem "" ""
	input string lastItem "" ""
	output file isHealthy "" ""
}
'''
import os,sys

class sequenceChecker:
   def sequenceChecker_main(self,**connections):
	self.sequenceName=connections["sequenceName"]
	self.Folder=connections["Folder"]
	self.Padding=connections["Padding"]
	self.extensionList=connections["extensionList"]
	self.firstItem=str(connections["firstItem"]).zfill(int(self.Padding))
	self.lastItem=str(connections["lastItem"]).zfill(int(self.Padding))

	try:
		list=[]
		self.sequenceName=str(self.sequenceName).lower()
		vl=[]
		list=os.listdir(str(self.Folder))
		for f in list:
			if str(f).split(".")[0]==str(self.sequenceName):
				if str(self.extensionList).find(str(f).split(".")[2])>0:
					vl.append(str(f).split(".")[1])
					
				else:
					return "no"

			else:
				return "no"

		vl.sort()
		if len(vl)!=int(self.lastItem)-int(self.firstItem)+1:
			return "no" 
		if vl[0]!=str(self.firstItem).zfill(int(self.Padding)):
			return "no"
		if vl[-1]!=str(self.lastItem).zfill(int(self.Padding)):
			return "no"
		return "yes"
	except:
		return "no"