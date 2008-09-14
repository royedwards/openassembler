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
from Run.Run import oas_execute


###################################################################################
# this is a collection of our shared python definitions
# most common syntax is : command(mode,input_list)
# if mode is "1" then it will produce text outputs for the consol
# if mode is "0", this is the "silent" mode no error, no confirmation outputed
###################################################################################

class oas_gateway(oas_data_handler,oas_fileio,oas_execute):

	def oas_list(self,mode,listtype="",searchtag=""):			
		return self.oas_data_list(mode=mode,listtype=listtype,searchtag=searchtag)
		
	def oas_show(self,mode,inputs):
		return self.oas_data_show(mode,inputs)

	def oas_count(self,mode,counttype=""):
		return self.oas_data_count(mode,counttype)

	def oas_create(self,mode,nodetype=""):
		return self.oas_data_create(mode,nodetype)

	def oas_delete(self,mode,deletetype="node",target=""):
		return self.oas_data_delete(mode,deletetype,target)

	def oas_rename(self,mode,old="",new=""):
		return self.oas_data_rename(mode,old,new)

	def oas_connect(self,mode,inputs):
		return self.oas_data_connect(mode,inputs)
		
	def oas_new(self,mode,inputs):
		return self.oas_Startup()

	def oas_end(self,mode,inputs):
		return self.oas_data_end(mode,inputs)

	def oas_save(self,mode,inputs):
		return self.oas_file_save(mode,inputs)
		
	def oas_open(self,mode,inputs):
		return self.oas_file_open(mode,inputs)
	
	def oas_run(self,mode,inputs):
		return self.oas_run_execute(mode,inputs)

	def oas_set(self,mode,inputs):
		return self.oas_data_set(mode,inputs)	

	def oas_framerange(self,mode,inputs):
		return self.oas_data_framerange(mode,inputs)

	def oas_frame(self,mode,inputs):
		return self.oas_data_frame(mode,inputs)
		
	def oas_Start(self):
		return self.oas_Startup()
		
