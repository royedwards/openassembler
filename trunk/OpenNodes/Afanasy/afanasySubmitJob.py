###OpenAssembler Node python file###

'''
define
{
	name afanasySubmitJob
	tags afa
	input string Command "" ""
	input string workDir "" ""
	input string Name "" ""
	input string Type "" ""
	input string DependOn "" ""
	input string BlockName "" ""
	input int Priority "100" ""
	input int startFrame "1" ""
	input int endFrame "10" ""
	input int blockSize "1" ""
	input int memory "4096" ""
	input int maxMult "4" ""
	input int Capacity "1000" ""
	output any jobID "" ""

}
'''

import sys,os
try:
	import af
except:
	print "There was some problem with loading the Afanasy module..."


class afanasySubmitJob():
	def afanasySubmitJob_main(self, **connections):

		try:
			Command=str(connections["Command"])
		except:
			Command=""
		try:
			workDir=str(connections["workDir"])
		except:
			workDir=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			Type=str(connections["Type"])
		except:
			Type=""
		try:
			Priority=int(connections["Priority"])
		except:
			Priority=100
		try:
			startFrame=int(connections["startFrame"])
		except:
			startFrame=1
		try:
			endFrame=int(connections["endFrame"])
		except:
			endFrame=10
		try:
			blockSize=int(connections["blockSize"])
		except:
			blockSize=1
		try:
			DependOn=str(connections["DependOn"])
		except:
			DependOn=""
		try:
			BlockName=str(connections["BlockName"])
		except:
			BlockName=""
		try:
			Capacity=int(connections["Capacity"])
		except:
			Capacity=1000
		try:
			memory=int(connections["memory"])
		except:
			memory=4096
		try:
			maxMult=int(connections["maxMult"])
		except:
			maxMult=4

		try:

			if Type=="":
				Type="generic"
			job = af.Job(Name)
			job.setDescription('Afanasy Job.')
			block1 = job.addBlock( Name+" "+BlockName, Type)
			block1.setCommand(Command)
			if DependOn!="":
				block1.setTasksDependMask(DependOn)
			block1.setWorkingDirectory(workDir)
			block1.setNeedMemory(memory)
			block1.setVariableCapacity(1, maxMult)
			block1.setCapacity(Capacity)
			block1.setNumeric( startFrame, endFrame, blockSize)
			job.send()

			return Name
		except:
			return None
			pass
