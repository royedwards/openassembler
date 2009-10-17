###OpenAssembler Node python file###

'''
define
{
	name autoDOD
	tags nuke
	input file input "" ""
	input file output "" ""
	input file savePath "" ""
	output string result "" ""

}
'''
try:
	import nuke
except:
	print "autoDOD will not work outside of Nuke!!!"

class autoDOD():
	def autoDOD_main(self, **connections):
		try:
			input=str(connections["input"])
		except:
			input=""
		try:
			output=str(connections["output"])
		except:
			output=""
		try:
			#nuke.scriptNew()
			re=nuke.createNode("Read")
			wr=nuke.createNode("Write")

			re["file"].setValue(input)
			wr["file"].setValue(output)

			re["colorspace"].setValue("linear")
			wr["channels"].setValue("all")
			wr["colorspace"].setValue("linear")
			wr["datatype"].setValue("32 bit float")
			wr["compression"].setValue("Zip (1 scanline)")
			wr["autocrop"].setValue(True)

		except:
			return 0
