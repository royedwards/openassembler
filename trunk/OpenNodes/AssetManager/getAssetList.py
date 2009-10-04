###OpenAssembler Node python file###

'''
define
{
	name getAssetList
	tags amanage
	input string Project "" ""
	input string Sequence "" ""
	input string Shot "" ""
	input string Type "" ""
	output array1D list "" ""

}
'''

from OpenProject.getElementList import getElementList

class getAssetList():
	def getAssetList_main(self, **connections):
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

		if Type=="Items" or Type=="Engines":
			retlist=getEL(":"+Project+":Assets:"+Type)
			if retlist==0:
				retlist=[]
			

		elif Type=="LightSetups" or Type=="CameraSetups" or Type=="RenderSetups":
			retlist=getEL(":General:Assets:"+Type)
			if retlist==0:
				retlist=[]

		elif Type=="Passes" or Type=="Misc":
			gn_level_list=getEL(":General:Assets:"+Type)
			if gn_level_list==0:
				pass
			else:
				for item in gn_level_list:
					retlist.append(str(item)+" (General)")

			try:
				pr_level_list=getEL(":"+Project+":Movie:Assets:"+Type)
				if pr_level_list==0:
					pass
				else:
					for item in pr_level_list:
						retlist.append(str(item)+" (Show)")
			except:
				pass

			try:
				sq_level_list=getEL(":"+Project+":Movie:"+Sequence+":Assets:"+Type)
				if sq_level_list==0:
					pass
				else:
					for item in sq_level_list:
						retlist.append(str(item)+" (Sequence)")
			except:
				pass

			try:
				sh_level_list=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Assets:"+Type)
				if sh_level_list==0:
					pass
				else:
					for item in sh_level_list:
						retlist.append(str(item)+" (Shot)")
			except:
				pass

		elif Type=="Caches":
			try:
				cachednodes=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches")
				if cachednodes==0:
					return []
				for node in cachednodes:
					cachedparams=getEL(":"+Project+":Movie:"+Sequence+":"+Shot+":Caches:"+node)
					if cachedparams==0:
						return []
					for param in cachedparams:
						retlist.append(node+" >>> "+param)
			except:
				pass

		elif Type=="Shaders":
			retlist=getEL(":General:Assets:"+Type)
			if retlist==0:
				retlist=[]

		return retlist


def getEL(Path):
	return getElementList().getElementList_main(Path=Path)