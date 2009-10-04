###OpenAssembler Node python file###

'''
define
{
	name createShots
	tags opm
	input string Project "" ""
	output int result "" ""

}
'''
import os, sys
from OpenProject.getElementType import getElementType
from OpenProject.createElement import createElement
from OpenProject.getVaultPath import getVaultPath

class createShots(getElementType,createElement,getVaultPath):
   def createShots_main(self, **connections):
	Project=connections["Project"]
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="result"

	if oas_output=="result":
			livefolder=self.getVaultPath_main(Path=":"+str(Project)+":Story:Edit@live")
			if livefolder==0:
				return 0
			flcontant=""
			if os.path.isfile(livefolder+"/edit.atr"):
				fl=open(livefolder+"/edit.atr","r")
				flcontant=fl.read()
				fl.close()
			else:
				return 0
			if flcontant=="":
				return 0

			lines=flcontant.strip().lstrip().split("\n")
			
			for line in lines:
				splitted=line.split(" | ")
				seq=splitted[1].split("_")[0]
				if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq))=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq))==0:
					self.createElement_main(Path=":"+str(Project)+":Movie",Type="container",Name=str(seq))
				if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art")=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art")==0:
					self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq),Type="container",Name="Art")
				if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art:Concept")=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art:Concept")==0:
					self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art",Type="item",Name="Concept")
				if self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art:References")=="" or self.getElementType_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art:References")==0:
					self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":Art",Type="item",Name="References")
				x=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq),Type="container",Name=str(splitted[1]))
				y=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1]),Type="container",Name="Art")
				z=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1]),Type="container",Name="Render")
				q=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1]),Type="container",Name="Additional")
				u=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1]),Type="container",Name="Build")
				t=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Art",Type="item",Name="References")
				w=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Art",Type="item",Name="Concept")
				e=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="container",Name="CG")
				r=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="item",Name="Animatic")
				i=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="item",Name="Layout")
				o=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="item",Name="Anim")
				p=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="item",Name="Compose")
				k=self.createElement_main(Path=":"+str(Project)+":Movie:"+str(seq)+":"+str(splitted[1])+":Render",Type="item",Name="Other")

			return 1			
	else:
		return 0
		
