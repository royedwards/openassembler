###OpenAssembler Node python file###

'''
define
{
	name createStoryModule
	tags opm
	input string Project "" ""
	output int result "" ""

}
'''
import os, sys
from OpenProject.getElementType import getElementType
from OpenProject.createElement import createElement

class createStoryModule(getElementType,createElement):
   def createStoryModule_main(self, **connections):
	Project=connections["Project"]
	try:
	    oas_output=connections["oas_output"]
	except:
	    oas_output="result"
	if oas_output=="result":
			s,m,e,q,y,t,a,b,c=1,1,1,1,1,1,1,1,1
			if self.getElementType_main(Path=":"+str(Project))=="" or self.getElementType_main(Path=":"+str(Project))==0:
				return 0
			if self.getElementType_main(Path=":"+str(Project)+":Art")=="" or self.getElementType_main(Path=":"+str(Project)+":Art")==0:
				a=self.createElement_main(Path=":"+str(Project),Type="container",Name="Art")
			if self.getElementType_main(Path=":"+str(Project)+":Art:Concept")=="" or self.getElementType_main(Path=":"+str(Project)+":Art:Concept")==0:
				b=self.createElement_main(Path=":"+str(Project)+":Art",Type="item",Name="Concept")
			if self.getElementType_main(Path=":"+str(Project)+":Art:References")=="" or self.getElementType_main(Path=":"+str(Project)+":Art:References")==0:
				c=self.createElement_main(Path=":"+str(Project)+":Art",Type="item",Name="References")
			if self.getElementType_main(Path=":"+str(Project)+":Story")=="" or self.getElementType_main(Path=":"+str(Project)+":Story")==0:
				s=self.createElement_main(Path=":"+str(Project),Type="container",Name="Story")
			if self.getElementType_main(Path=":"+str(Project)+":Movie")=="" or self.getElementType_main(Path=":"+str(Project)+":Movie")==0:
				m=self.createElement_main(Path=":"+str(Project),Type="container",Name="Movie")
			if self.getElementType_main(Path=":"+str(Project)+":Story:Edit")=="" or self.getElementType_main(Path=":"+str(Project)+":Story:Edit")==0:
				e=self.createElement_main(Path=":"+str(Project)+":Story",Type="item",Name="Edit")
			if self.getElementType_main(Path=":"+str(Project)+":Story:Sequences")=="" or self.getElementType_main(Path=":"+str(Project)+":Story:Sequences")==0:
				q=self.createElement_main(Path=":"+str(Project)+":Story",Type="item",Name="Sequences")
			if self.getElementType_main(Path=":"+str(Project)+":Story:Synopsys")=="" or self.getElementType_main(Path=":"+str(Project)+":Story:Synopsys")==0:
				y=self.createElement_main(Path=":"+str(Project)+":Story",Type="item",Name="Synopsys")
			if self.getElementType_main(Path=":"+str(Project)+":Story:Treatment")=="" or self.getElementType_main(Path=":"+str(Project)+":Story:Treatment")==0:
				t=self.createElement_main(Path=":"+str(Project)+":Story",Type="item",Name="Treatment")

			if s==0 or m==0 or e==0 or q==0 or y==0 or t==0 or a==0 or b==0 or c==0:
				return 0

			return 1
	else:
		return 0
		
