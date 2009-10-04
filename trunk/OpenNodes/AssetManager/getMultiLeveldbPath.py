###OpenAssembler Node python file###

'''
define
{
	name getMultiLeveldbPath
	tags amanage
	input string MultiLevelName "" ""
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Type "" ""
	output dbPath dbPath "" ""
	output string assetName "" ""

}
'''

from OpenProject.getElementList import getElementList

class getMultiLeveldbPath():
	def getMultiLeveldbPath_main(self, **connections):
		try:
			MultiLevelName=str(connections["MultiLevelName"])
		except:
			MultiLevelName=""
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
			oas_output="dbPath"		


		retpath=[]

		if MultiLevelName.split(" ")[1].strip()=="(General)":
			retpath=":General:Assets:"+Type+":"+MultiLevelName.split(" ")[0].strip()
		elif MultiLevelName.split(" ")[1].strip()=="(Show)":
			retpath=":"+Project+":Movie:Assets:"+Type+":"+MultiLevelName.split(" ")[0].strip()
		elif MultiLevelName.split(" ")[1].strip()=="(Sequence)":
			retpath=":"+Project+":Movie:"+Sequence+":Assets:"+Type+":"+MultiLevelName.split(" ")[0].strip()
		elif MultiLevelName.split(" ")[1].strip()=="(Shot)":
			retpath=":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type+":"+MultiLevelName.split(" ")[0].strip()


		if oas_output=="dbPath":
			return retpath
		else:
			return MultiLevelName.split(" ")[0].strip()


def getEL(Path):
	return getElementList().getElementList_main(Path=Path)