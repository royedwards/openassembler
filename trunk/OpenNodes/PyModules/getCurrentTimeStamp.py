###OpenAssembler Node python file###

'''
define
{
	name getCurrentTimeStamp
	tags pymod
	output string user "" ""

}
'''
import os,sys,time
class getCurrentTimeStamp():
	def getCurrentTimeStamp_main(self, **connections):
			ti=time.time()
			return ti


