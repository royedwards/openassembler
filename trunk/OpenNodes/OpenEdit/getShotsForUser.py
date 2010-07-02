###OpenAssembler Node python file###

'''
define
{
	name getShotsForUser
	tags oped
	input string User "" ""
	output any shots "" ""

}
'''
import os, sys, platform
from OpenProject.getProjects import getProjects
from OpenProject.getAttribute import getAttribute
from OpenEdit.getSequences import getSequences
from OpenEdit.getShots import getShots

class getShotsForUser(getProjects,getSequences,getShots,getAttribute):
   def getShotsForUser_main(self, **connections):

	try:
	    User=connections["User"]
	except:
	    User=""
	try: 
	    oas_output=connection["oas_output"]
	except:
	    oas_output="shots"
	
	outshots=[]

	prs=self.getProjects_main()
	for p in prs:
		sqs=self.getSequences_main(Project=p)
		sqs.sort()
		for s in sqs:
			shts=self.getShots_main(Project=p,Sequence=s)
			shts.sort()
			for ss in shts:
				usr=str(self.getAttribute_main(Path=":"+str(p)+":Movie:"+str(s)+":"+str(ss)+".user")).strip()
				if usr == str(User).strip() or str(User).strip()=="All" or str(User).strip()=="":
					stats=str(self.getAttribute_main(Path=":"+str(p)+":Movie:"+str(s)+":"+str(ss)+".status")).strip()
					prio=str(self.getAttribute_main(Path=":"+str(p)+":Movie:"+str(s)+":"+str(ss)+".priority")).strip()
					due=str(self.getAttribute_main(Path=":"+str(p)+":Movie:"+str(s)+":"+str(ss)+".dueto")).strip()
					outshots.append([p,s,ss,stats,prio,due,usr])

	tmp_prH=[]
	tmp_prN=[]
	tmp_prL=[]
	tmp_ap=[]

	for o in outshots:
		if o[3]=="Approved" or o[3]=="OnHold" or o[3]=="Omited":
			tmp_ap.append(o)
		elif o[4]=="High":
			tmp_prH.append(o)
		elif o[4]=="Normal":
			tmp_prN.append(o)
		elif o[4]=="Low":
			tmp_prL.append(o)

	outshots=tmp_prH+tmp_prN+tmp_prL+tmp_ap

	return outshots

