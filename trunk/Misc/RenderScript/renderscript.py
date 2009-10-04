###OpenAssembler RenderScript###

import os, sys

class renderscript():
   def renderscript_main(self, args):

	#----------------args------------------------
	try:
		file=str(args[1])
		nodepath=str(args[2])
	except:
		print "Not enough argument!"
		return 0
	try:
		mode=str(args[3])
	except:
		mode="Normal"
	#---------------drqueue-------------------
	try:
		frame=int(os.environ.get("DRQUEUE_FRAME"))
	except:
		frame=""
	#---------------houdini---------------------
	print os.system("export")
	hou.hipFile.load(file)
	print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
	print "RenderStarts with parameters: "+str(args)
	print "Hip file is loaded!!!!:"+str(file)
	hou.setFrame(int(frame))
	print "Frame is set to:" +str(frame)
	if mode=="Normal" or mode=="Render":
		print "Render will start now!"
		hou.node(nodepath).render(frame_range=(frame,frame))
	elif mode=="Dynamic" or mode=="Cache":
		print "Cache will start now!"
		hou.node(nodepath).render()

	print "Render is ready for now!"

	hou.exit()
		
	print "Houdini exits!"

if __name__ == "__main__":
	renderscript().renderscript_main(sys.argv)
 