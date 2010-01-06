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
	input int Priority "99" ""
	input int startFrame "1" ""
	input int endFrame "10" ""
	input int blockSize "1" ""
	input int memory "4096" ""
	input int maxMult "4" ""
	input int Capacity "1000" ""
	input string PostCommand "" ""
	input string EmailCommand "" ""
	input string Comment "" ""
	input int MaxHosts "8" ""
	input int autoDOD "0" ""
	input string DODCommand "" ""
	input string HostMask "" ""
	input string HostExcludeMask "" ""
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
			HostMask=str(connections["HostMask"])
		except:
			HostMask=""
		try:
			HostExcludeMask=str(connections["HostExcludeMask"])
		except:
			HostExcludeMask=""
		try:
			DODCommand=str(connections["DODCommand"])
		except:
			DODCommand=""
		try:
			autoDOD=int(connections["autoDOD"])
		except:
			autoDOD=0
		try:
			EmailCommand=str(connections["EmailCommand"])
		except:
			EmailCommand=""
		try:
			MaxHosts=int(connections["MaxHosts"])
		except:
			MaxHosts=8
		try:
			Comment=str(connections["Comment"])
		except:
			Comment=""
		try:
			PostCommand=str(connections["PostCommand"])
		except:
			PostCommand=""
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
			Priority=99
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
			if Comment!="":
				job.setDescription(Comment)
			else:
				job.setDescription('Afanasy Job.')
			job.setMaxHosts(MaxHosts)
			if HostMask!="":
				job.setHostsMask(HostMask)
			if HostExcludeMask!="":
				job.setHostsMaskExclude(HostExcludeMask)
			block1 = job.addBlock( Name+" "+BlockName, Type)
			block1.setCommand(Command)
			if DependOn!="":
				block1.setTasksDependMask(DependOn)
			block1.setWorkingDirectory(workDir)
			if PostCommand!="":
				block1.setCmdPost(PostCommand)
			block1.setNeedMemory(memory)
			block1.setVariableCapacity(1, maxMult)
			block1.setCapacity(Capacity)
			block1.setNumeric( startFrame, endFrame, blockSize)

			if autoDOD!=0:
				block_dod= job.addBlock( Name+" "+"autoDOD", "nuke")
				block_dod.setCommand(DODCommand)
				block_dod.setDependMask(Name+" "+BlockName)
				block_dod.setWorkingDirectory(workDir)
				block_dod.setNeedMemory(memory)
				block_dod.setCapacity(500)
				block_dod.setNumeric( startFrame, endFrame, 10)				

			if EmailCommand!="":
				block_email= job.addBlock( Name+" "+"Email", "generic")
				block_email.setCommand(EmailCommand)
				if autoDOD!=0:
					block_email.setDependMask(Name+" "+"autoDOD")
				else:
					block_email.setDependMask(Name+" "+BlockName)
				block_email.setWorkingDirectory(workDir)
				block_email.setCapacity(10)
				block_email.setNumeric( 1, 1, 1)


			job.send()

			return Name
		except:
			return None
			pass
