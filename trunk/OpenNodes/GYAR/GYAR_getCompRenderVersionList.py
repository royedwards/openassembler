###OpenAssembler Node python file###
## MODIFIED FOR DIGITALAPES
'''
define
{
	name GYAR_getCompRenderVersionList
	tags gyar
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string serverRootPath "" ""
	output array1D RenderVersion "" ""
}
'''
import os,sys
from DigitalApes.reformatApesProjectName import reformatApesProjectName

class GYAR_getCompRenderVersionList:
   def GYAR_getCompRenderVersionList_main(self,**connections):
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
		serverRootPath=str(connections["serverRootPath"])
	except:
		serverRootPath=""


	wp=str(serverRootPath)+"/"+str(Project)+"/Movie/"+str(Sequence)+"/"+str(Shot)+"/Versions"

	collection=[]
	dlist=[]
	try:
		dlist=os.listdir(wp)
	except:
		pass
	for dr in dlist:
		if os.path.isdir(str(wp)+"/"+str(dr)):
			if versionchecker(dr)==1:
				collection.append(dr)

	collection.sort()
	collection.reverse()
	return collection


def versionchecker(foldername):
	if str(foldername)[0]!="v":
		return 0
	try:
		x=int(str(foldername)[1:])
	except:
		return 0
	if len(str(foldername))!=4:
		return 0
	return 1
