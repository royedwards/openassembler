###OpenAssembler Node python file###

'''
define
{
	name CRTemplateFrame
	tags amanage
	input string LorF "" ""
	input string TemplateOAS "" ""
	input string renderBuilderScript "" ""
	input string Project "" ""
	input string Shot "" ""
	input string Type "" ""
	input string Node_Pass "" ""
	input string Param_Setup "" ""
	input any FirstFrame "100" ""
	input any Endframe "200" ""
	input any Increment "1" ""
	input any Head_n_Tail "5" ""
	input file pathOverride "" ""
	input string Comment "" ""
	output any result "" ""

}
'''
import os,sys

class CRTemplateFrame():
	def CRTemplateFrame_main(self, **connections):
		try:
			pathOverride=str(connections["pathOverride"])
		except:
			pathOverride=""
		try:
			renderBuilderScript=str(connections["renderBuilderScript"])
		except:
			renderBuilderScript=""
		try:
			TemplateOAS=str(connections["TemplateOAS"])
		except:
			TemplateOAS=""
		try:
			LorF=str(connections["LorF"])
		except:
			LorF=""
		try:
			Project=str(connections["Project"])
		except:
			Project=""
		try:
			Shot=str(connections["Shot"])
		except:
			Shot=""
		try:
			Node_Pass=str(connections["Node_Pass"])
		except:
			Node_Pass=""
		try:
			Param_Setup=str(connections["Param_Setup"])
		except:
			Param_Setup=""
		try:
			FirstFrame=int(connections["FirstFrame"])
		except:
			FirstFrame=100
		try:
			Endframe=int(connections["Endframe"])
		except:
			Endframe=200
		try:
			Increment=int(connections["Increment"])
		except:
			Increment=1
		try:
			Head_n_Tail=int(connections["Head_n_Tail"])
		except:
			Head_n_Tail=5
		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""



		try:

			os.system("hython "+str(renderBuilderScript)+" "+str(TemplateOAS)+" "+str(LorF)+" "+str(Project)+" "+str(Shot)+" "+str(Node_Pass)+" "+str(Param_Setup)+" "+str(FirstFrame)+" "+str(Endframe)+" "+str(Increment)+" "+str(Head_n_Tail)+" "+str(Type)+" "+str(pathOverride)+" "+str(Comment))

			return 1

		except:
			return 0

