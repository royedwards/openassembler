###OpenAssembler Node python file###

'''
define
{
	name getCurrentTime
	tags pymod
	output string user "" ""

}
'''
import os,sys,time
class getCurrentTime():
	def getCurrentTime_main(self, **connections):
			ti=time.localtime()
			t=str(ti.tm_year)+"."+str(ti.tm_mon).zfill(2)+"."+str(ti.tm_mday).zfill(2)
			return t


