###OpenAssembler Node python file###

'''
define
{
	name globalFramerange
	tags hou
	output array1D framerange "" ""

}
'''

try:
	import hou
except:
	print "globalFramerange will not work outside Houdini!!"

from OpenEdit.sequenceFromShot import sequenceFromShot

class globalFramerange():
	def globalFramerange_main(self, **connections):
		try:
			range=[]
			fr=hou.hscript("frange")
			fr=fr[0]
			range.append(int(fr.split("Frame range: ")[1].split(" to")[0]))
			range.append(int(fr.split("to ")[1].strip()))
			return range
		except:
			return 0


def getS(Project,Shot):
	return sequenceFromShot().sequenceFromShot_main(Project=Project,Shot=Shot)