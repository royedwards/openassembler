###OpenAssembler Node python file###

'''
define
{
	name getCurrentUser
	tags pymod
	output string user "" ""

}
'''
import os,sys
class getCurrentUser():
	def getCurrentUser_main(self, **connections):
			user="unknown"
			try:
				user=os.getenv('USER')
			except:
				pass
			return user


