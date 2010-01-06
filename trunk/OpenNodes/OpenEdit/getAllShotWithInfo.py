###OpenAssembler Node python file###

'''
define
{
	name getAllShotWithInfo
	tags oped
	input string Project "" ""
	input int infoType "0" ""
	output array1D shots "" ""

}
'''
import os, sys
from OpenEdit.getSequences import getSequences
from OpenEdit.getShots import getShots
from OpenCoOrdination.getShotsFarmSetup import getShotsFarmSetup

class getAllShotWithInfo():
   def getAllShotWithInfo_main(self, **connections):
	try:
	    Project=connections["Project"]
	except:
	    Project=""
	try:
	    infoType=int(connections["infoType"])
	except:
	    infoType=0

	try:		
		if infoType==0:
			allshot=[]
			seqs=getSeq(Project)
			for sq in seqs:
				tmp=getSh(Project,sq)
				allshot+=tmp
			return allshot
		elif infoType==1:
			allshot=[]
			seqs=getSeq(Project)
			for sq in seqs:
				tmp=getSh(Project,sq)
				for sht in tmp:
					ffs=fs(Project,sq,sht)
					allshot.append(str(sht)+"                       (P:"+str(ffs[0])+", M:"+str(ffs[1])+", hM:\""+str(ffs[2])+"\", hE:\""+str(ffs[3])+"\")")
			return allshot
		return []
	except:
		return []

def getSeq(Project):
	return getSequences().getSequences_main(Project=Project)

def getSh(Project,Sequence):
	return getShots().getShots_main(Project=Project,Sequence=Sequence)

def fs(Project,Sequence,Shot):
	return getShotsFarmSetup().getShotsFarmSetup_main(Project=Project,Sequence=Sequence,Shot=Shot)