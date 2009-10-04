###OpenAssembler Node python file###

'''
define
{
	name keyParentTransformAnim
	tags hou
	input string nodeToKey "" ""
	input string TMatrixNode "" ""
	output int BakeTransform "" ""

}
'''
try:
	import hou
except:
	print "keyParentTransformAnim will not work outside Houdini!!"

class keyParentTransformAnim():
	def keyParentTransformAnim_main(self, **connections):

		try:
			nodeToKey=str(connections["nodeToKey"])
		except:
			nodeToKey=""
		try:
			TMatrixNode=str(connections["TMatrixNode"])
		except:
			TMatrixNode=""	
		try:
			ntc=hou.node(nodeToKey)
			tn=hou.node(TMatrixNode)
			for val in ntc.parm("tx").keyframes():
				hou.setFrame(val.frame())
				ntc.parm("tx").set(val.value()*tn.parm("sx").eval()+tn.parm("tx").eval())
			for val in ntc.parm("ty").keyframes():
				hou.setFrame(val.frame())
				ntc.parm("ty").set(val.value()*tn.parm("sy").eval()+tn.parm("ty").eval())
			for val in ntc.parm("tz").keyframes():
				hou.setFrame(val.frame())
				ntc.parm("tz").set(val.value()*tn.parm("sz").eval()+tn.parm("tz").eval())
			return 1

		except:
			return 0

