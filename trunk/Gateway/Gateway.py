######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Dbase.Data_handler import oas_data_handler
from Dbase.FileIO import oas_fileio


###################################################################################
# this is a collection of our shared python definitions
# most common syntax is : command(mode,input_list)
# if mode is "1" then it will produce text outputs for the consol
# if mode is "0", this is the "silent" mode no error, no confirmation outputed
###################################################################################

class oas_gateway(oas_data_handler,oas_fileio):

	def oas_list(self,mode,inputs):		
		return self.oas_data_list(mode,inputs)
		
	def oas_show(self,mode,inputs):
		return self.oas_data_show(mode,inputs)

	def oas_count(self,mode,inputs):
		return self.oas_data_count(mode,inputs)

	def oas_create(self,mode,inputs):
		return self.oas_data_create(mode,inputs)

	def oas_delete(self,mode,inputs):
		return self.oas_data_delete(mode,inputs)

	def oas_rename(self,mode,inputs):
		return self.oas_data_rename(mode,inputs)

	def oas_connect(self,mode,inputs):
		return self.oas_data_connect(mode,inputs)
		
	def oas_new(self,mode,inputs):
		return self.oas_Startup()

	def oas_save(self,mode,inputs):
		return self.oas_file_save(mode,inputs)
		
	def oas_open(self,mode,inputs):
		return self.oas_file_open(mode,inputs)
