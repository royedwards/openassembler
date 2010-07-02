###OpenAssembler Node python file###

'''
define
{
	name getCurrentDate
	tags pymod
	output string user "" ""

}
'''
import os,sys,time
class getCurrentDate():
	def getCurrentDate_main(self, **connections):
			ti=time.localtime()
			t=str(ti.tm_year)+"."+str(ti.tm_mon).zfill(2)+"."+str(ti.tm_mday).zfill(2)
			return t


