###OpenAssembler Node python file###

'''
define
{
	name copyFile
	tags pymod
	input file _from "" ""
	input file _to "" ""
	output any result "" ""

}
'''
import os, sys,shutil

class copyFile():
   def copyFile_main(self, **connections):
	try:
		 _from=str(connections["_from"])
	except:
		 _from=""
	try:
		_to=str(connections["_to"])
	except:
		_to=""

	if os.path.isfile(_from):
		pass
	else:
		return 0

	try:
		shutil.copy(_from,_to)
	except:
		return 0

	return 1
