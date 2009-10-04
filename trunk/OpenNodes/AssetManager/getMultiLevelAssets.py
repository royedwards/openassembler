###OpenAssembler Node python file###

'''
define
{
	name getMultiLevelAssets
	tags amanage
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Type "" ""
	output array1D list "" ""

}
'''

from OpenProject.getElementList import getElementList

class getMultiLevelAssets():
	def getMultiLevelAssets_main(self, **connections):
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
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="list"		


		retlist=[]

		gn_level_list=getEL(":General:Assets:"+Type)
		if gn_level_list==0:
			pass
		else:
			for item in gn_level_list:
				retlist.append(str(item)+" (General)")

		pr_level_list=getEL(":"+Project+":Movie:Assets:"+Type)
		if pr_level_list==0:
			pass
		else:
			for item in pr_level_list:
				retlist.append(str(item)+" (Show)")

		sq_level_list=getEL(":"+Project+":Movie:"+Sequence+":Assets:"+Type)
		if sq_level_list==0:
			pass
		else:
			for item in sq_level_list:
				retlist.append(str(item)+" (Sequence)")

		sh_level_list=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type)
		if sh_level_list==0:
			pass
		else:
			for item in sh_level_list:
				retlist.append(str(item)+" (Shot)")

		return retlist


def getEL(Path):
	return getElementList().getElementList_main(Path=Path)