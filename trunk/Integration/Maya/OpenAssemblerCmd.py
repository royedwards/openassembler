######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import math, sys
from Gateway.Gateway import oas_gateway as oas_gateway
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "openAssemblerCmd"

kTimeFlag = "-t"
kTimeLongFlag = "-time"

class openAssemblerCmd(OpenMayaMPx.MPxCommand,oas_gateway):

	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)
			
	def doIt(self,args):
		
		time=1
		
		argData = OpenMaya.MArgDatabase(self.syntax(), args)
		if argData.isFlagSet(kTimeFlag):
			time = argData.flagArgumentDouble(kTimeFlag, 0)
			
		print time
		#reload(oas_gateway) 
		self.oas_Start()
		self.oas_open(mode="normal",filename="X:\mayatest.oas",filetype="oas")
		result = self.oas_run(mode="normal",runmode="maya",fixedframe=int(time)) 
		
		print result
		

def cmdCreator():
	return OpenMayaMPx.asMPxPtr( openAssemblerCmd() )

def syntaxCreator():
	syntax = OpenMaya.MSyntax()
	syntax.addFlag(kTimeFlag, kTimeLongFlag, OpenMaya.MSyntax.kDouble)
	return syntax
	
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject, "Autodesk", "1.0", "Any")
	try:
		mplugin.registerCommand( kPluginCmdName, cmdCreator, syntaxCreator )
	except:
		sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
		raise

def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand( kPluginCmdName )
		del self
	except:
		sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeTypeName )
		raise
	
