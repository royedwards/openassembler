######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import math, sys
from Gateway.Gateway import oas_gateway
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaUI as OpenMayaUI

kPluginNodeTypeName = "openAssemblerNode"

openAssemblerNodeId = OpenMaya.MTypeId(0x87021)

class openAssemblerNode(OpenMayaMPx.MPxLocatorNode,oas_gateway):
	input = OpenMaya.MObject()
	output = OpenMaya.MObject()
	time = OpenMaya.MObject()
	
	def __init__(self):
		OpenMayaMPx.MPxLocatorNode.__init__(self)
			
	def compute(self,plug,dataBlock):
		if ( plug == openAssemblerNode.output ):
		
			timeData = dataBlock.inputValue(openAssemblerNode.time)
			tempTime = timeData.asTime()
			frame = int(tempTime.as(OpenMaya.MTime.kFilm))
			
			dataHandle = dataBlock.inputValue( openAssemblerNode.input )
			inputFloat = dataHandle.asFloat()
			
			self.oas_Start()
			self.oas_open(mode="normal",filename="X:\mayatest.oas",filetype="oas")
			result = self.oas_run(mode="normal",runmode="maya",fixedframe=(frame*inputFloat))
									
			outputHandle = dataBlock.outputValue( openAssemblerNode.output )
			outputHandle.setFloat( result )
			dataBlock.setClean( plug )
			
			#OpenMaya.MGlobal.displayInfo("--- success")
			
			return OpenMaya.MStatus.kSuccess

		
		else:	
			#OpenMaya.MGlobal.displayInfo("--- failure")
			return OpenMaya.MStatus.kUnknownParameter


def nodeCreator():
	return OpenMayaMPx.asMPxPtr( openAssemblerNode() )

def nodeInitializer():

	unitAttr = OpenMaya.MFnUnitAttribute()
	openAssemblerNode.time = unitAttr.create("time", "tm", OpenMaya.MFnUnitAttribute.kTime, 0.0)
	unitAttr.setWritable(1)
	unitAttr.setConnectable(1)

	nAttr = OpenMaya.MFnNumericAttribute()
	openAssemblerNode.input = nAttr.create( "input", "in", OpenMaya.MFnNumericData.kFloat, 1.0 )
	nAttr.setStorable(1)
	nAttr.setWritable(1)
	nAttr.setConnectable(1)
	nAttr.setKeyable(1)
	nAttr.setChannelBox(1)

	nAttr = OpenMaya.MFnNumericAttribute()
	openAssemblerNode.output = nAttr.create( "output", "out", OpenMaya.MFnNumericData.kFloat, 0.0 )
	nAttr.setStorable(1)
	nAttr.setWritable(1)
	nAttr.setConnectable(1)
	nAttr.setCached(0)
	nAttr.setInternal(0)

	openAssemblerNode.addAttribute( openAssemblerNode.input )
	openAssemblerNode.addAttribute( openAssemblerNode.output )
	openAssemblerNode.addAttribute( openAssemblerNode.time )
	openAssemblerNode.attributeAffects( openAssemblerNode.input, openAssemblerNode.output )
	openAssemblerNode.attributeAffects( openAssemblerNode.time, openAssemblerNode.output )
	
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerNode( kPluginNodeTypeName, openAssemblerNodeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kLocatorNode)
	except:
		sys.stderr.write( "Failed to register node: %s" % kPluginNodeTypeName )
		raise

def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode( openAssemblerNodeId )
	except:
		sys.stderr.write( "Failed to deregister node: %s" % kPluginNodeTypeName )
		raise
	
