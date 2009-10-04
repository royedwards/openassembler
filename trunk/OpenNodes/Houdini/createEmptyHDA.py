###OpenAssembler Node python file###

'''
define
{
	name createEmptyHDA
	tags hou
	input string Type "" ""
	input string Name "" ""
	input dbPath dbPath "" ""
	input string nameOverride "" ""
	output any name "" ""

}
'''
try:
	import hou
except:
	print "createEmptyHDA will not work outside Houdini!!"

from OpenProject.getElementType import getElementType

class createEmptyHDA():
	def createEmptyHDA_main(self, **connections):

		try:
			dbPath=connections["dbPath"]
		except:
			dbPath=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			nameOverride=str(connections["nameOverride"])
		except:
			nameOverride=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			oas_output=connections["oas_output"]
		except:
			oas_output="name"		

		if str(geT(dbPath))=="" or str(geT(dbPath))=="0":
			return 0

		if oas_output=="name":
			try:
				a=hou.node("/obj")
				if nameOverride!="":
					b=a.createNode("subnet",nameOverride)
				else:
					b=a.createNode("subnet",Name)

				c=b.createDigitalAsset(Name+"_"+Type+"_v000","Embedded",Name+"_"+Type+"_v000",0,0,False,"","v000",True,False)
				c.allowEditingOfContents()
				    
				path=c.path()

				hou.node(path).type().definition().addParmFolder("projectDB")
				if Type=="Model":
					hou.node(path).type().definition().addParmFolder("Materials")

				parameters=hou.node(path).parmsInFolder(("Subnet",))
				for n in range (0,len(parameters)):
					try:
						hou.node(path).type().definition().removeParmTuple((parameters[n].tuple().name()))
					except:
						pass

				hou.node(path).type().definition().removeParmFolder(("Subnet",))

				pp=hou.StringParmTemplate("dbPath","dbPath",1,(dbPath,))
				hou.node(path).type().definition().addParmTuple(pp,("projectDB",))
				hou.node(path).parm("dbPath").lock(True)
				pt=hou.StringParmTemplate("dbType","dbType",1,(Type,))
				hou.node(path).type().definition().addParmTuple(pt,("projectDB",))
				hou.node(path).parm("dbType").lock(True)

				return Name
			except:
				return 0
		    

def geT(Path):
	return getElementType().getElementType_main(Path=Path)

