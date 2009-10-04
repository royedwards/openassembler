###OpenAssembler Node python file###

'''
define
{
	name drqueueEnvironment
	tags drqueue
	output string frame

}
'''

import sys,os
try:
	import drqueue.base.libdrqueue as drqueue
except:
	print "There was some problem with loading the drqueue module..."


class drqueueEnvironment():
	def drqueueEnvironment_main(self, **connections):

		return 0

