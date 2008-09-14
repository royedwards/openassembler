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
		
	def oas_show(self,mode,showtype=""):
		return self.oas_data_show(mode=mode,showtype=showtype)

	def oas_count(self,mode,counttype=""):
		return self.oas_data_count(mode=mode,counttype=counttype)

	def oas_create(self,mode,nodetype=""):
		return self.oas_data_create(mode=mode,nodetype=nodetype)

	def oas_delete(self,mode,deletetype="node",target=""):
		return self.oas_data_delete(mode=mode,deletetype=deletetype,target=target)

	def oas_rename(self,mode,old="",new=""):
		return self.oas_data_rename(mode=mode,old=old,new=new)

	def oas_connect(self,mode,from_variable="",to_variable=""):
		return self.oas_data_connect(mode=mode,from_variable=from_variable,to_variable=to_variable)
		
	def oas_new(self,mode):
		return self.oas_Startup()

	def oas_end(self,mode,endnode=""):
		return self.oas_data_end(mode=mode,endnode=endnode)

	def oas_save(self,mode,filename="",filetype=""):
		return self.oas_file_save(mode=mode,filename=filename,filetype=filetype)
		
	def oas_open(self,mode,filename="",filetype=""):
		return self.oas_file_open(mode=mode,filename=filename,filetype=filetype)
	
	def oas_run(self,mode):
		return self.oas_run_execute(mode=mode)

	def oas_set(self,mode,nodevalue="",value=""):
		return self.oas_data_set(mode=mode,nodevalue=nodevalue,value=value)	

	def oas_framerange(self,mode,firstframe="",endframe=""):
		return self.oas_data_framerange(mode=mode,firstframe=firstframe,endframe=endframe)

	def oas_frame(self,mode,frame=""):
		return self.oas_data_frame(mode=mode,frame=frame)
		
	def oas_Start(self):
		return self.oas_Startup()
		
