######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Dbase.Data_handler import oas_data_handler

class oas_gateway(oas_data_handler):

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
