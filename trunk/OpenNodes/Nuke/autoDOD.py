###OpenAssembler Node python file###

'''
define
{
	name autoDOD
	tags nuke
	input file input "" ""
	input file output "" ""
	input int firstFrame "1" ""
	input int lastFrame "1" ""
	input file savePath "" ""
	output string result "" ""

}
'''
try:
	import nuke
except:
	print "autoDOD will not work outside of Nuke!!!"

import os,sys

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
			savePath=str(connections["savePath"])
		except:
			savePath=""
		try:
			firstFrame=int(connections["firstFrame"])
		except:
			firstFrame=""
		try:
			lastFrame=int(connections["lastFrame"])
		except:
			lastFrame=""
		try:
			re=nuke.createNode("Read")
			wr=nuke.createNode("Write")

			re["file"].setValue(input)
			wr["file"].setValue(output)

			re["colorspace"].setValue("linear")

			re["first"].setValue(firstFrame)
			re["last"].setValue(lastFrame)

			wr["channels"].setValue("all")

			wr["colorspace"].setValue("linear")
			wr["file_type"].setValue("exr")

			wr["datatype"].setValue("32 bit float")
			
			wr["compression"].setValue("Zip (1 scanline)")
			wr["autocrop"].setValue(True)

			nuke.scriptSaveAs(filename = savePath, overwrite = 1)

		except:
			return 0


if __name__ == "__main__":
	args=sys.argv[1:]
	a=args[0].split(",")
	autoDOD().autoDOD_main(input=a[0],output=a[0],savePath=a[1],firstFrame=a[2],lastFrame=a[3])