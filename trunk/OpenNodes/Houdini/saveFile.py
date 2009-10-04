###OpenAssembler Node python file###

'''
define
{
	name saveFile
	tags hou
	input string thanCopyTo "" ""
	output string resultPath "" ""
}
'''

try:
	import hou
except:
	print "saveFile will not work outside Houdini!!"

import os, sys, shutil

class saveFile():
	def saveFile_main(self, **connections):
		try:
			thanCopyTo=str(connections["thanCopyTo"])
		except:
			thanCopyTo=""

		hou.hipFile.save()

		if thanCopyTo!="":
			origfilepath=hou.hipFile.name()
			try:
				shutil.copyfile(origfilepath, thanCopyTo)
			except:
				return 0
		return thanCopyTo
