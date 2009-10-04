###OpenAssembler Node python file###

'''
define
{
	name actualShot
	tags hou
	output string Project "" ""
	output string Shot "" ""
	output string Sequence "" ""
	output string ShotType "" ""

}
'''

try:
	import hou
except:
	print "actualShot will not work outside Houdini!!"

from OpenEdit.sequenceFromShot import sequenceFromShot

class actualShot():
	def actualShot_main(self, **connections):
		try:
			oas_output=str(connections["oas_output"])
		except:
			oas_output="Project"
		try:
			shotnode=hou.node("/obj/ShotData")
			project=shotnode.parm("dbProject").eval()
			shot=shotnode.parm("dbShot").eval()
			stype=shotnode.parm("dbShotType").eval()
			seq=getS(project,shot)

			if oas_output=="Project":
				return project
			elif oas_output=="Shot":
				return shot
			elif oas_output=="Sequence":
				return seq
			elif oas_output=="ShotType":
				return stype
			
		except:
			return 0 


def getS(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)