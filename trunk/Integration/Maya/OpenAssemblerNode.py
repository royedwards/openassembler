######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import math, sys

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginNodeTypeName = "openAssemblerNode"

openAssemblerNodeId = OpenMaya.MTypeId(0x87021)

class openAssemblerNode(OpenMayaMPx.MPxNode):
	# class variables
	input = OpenMaya.MObject()
	output = OpenMaya.MObject()
	def __init__(self):
		OpenMayaMPx.MPxNode.__init__(self)
	def compute(self,plug,dataBlock):
		if ( plug == openAssemblerNode.output ):
			dataHandle = dataBlock.inputValue( openAssemblerNode.input )
			
			inputFloat = dataHandle.asFloat()
			result = math.sin( inputFloat ) * 10.0
			outputHandle = dataBlock.outputValue( openAssemblerNode.output )
			outputHandle.setFloat( result )
			dataBlock.setClean( plug )

		return OpenMaya.kUnknownParameter

# creator
def nodeCreator():
	return OpenMayaMPx.asMPxPtr( openAssemblerNode() )
	
	

# initializer
def nodeInitializer():
	# input
	nAttr = OpenMaya.MFnNumericAttribute()
	openAssemblerNode.input = nAttr.create( "input", "in", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(1)
	# output
	nAttr = OpenMaya.MFnNumericAttribute()
	openAssemblerNode.output = nAttr.create( "output", "out", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(1)
	nAttr.setWritable(1)
	# add attributes
	openAssemblerNode.addAttribute( openAssemblerNode.input )
	openAssemblerNode.addAttribute( openAssemblerNode.output )
	openAssemblerNode.attributeAffects( openAssemblerNode.input, openAssemblerNode.output )
	
# initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerNode( kPluginNodeTypeName, openAssemblerNodeId, nodeCreator, nodeInitializer )
	except:
		sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
		raise

# uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode( openAssemblerNodeId )
	except:
		sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeTypeName )
		raise
	
