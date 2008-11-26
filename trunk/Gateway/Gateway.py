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
from Port.Broadcaster import oas_broadcaster

###################################################################################
# this is a collection of our shared python definitions
# most common syntax is : command(mode,input_list)
# if mode is "1" then it will produce text outputs for the consol
# if mode is "0", this is the "silent" mode no error, no confirmation outputed
###################################################################################

class oas_gateway(oas_data_handler,oas_fileio,oas_execute,oas_broadcaster):

	def oas_list(self,mode,listtype="",searchtag=""):			
		return self.oas_data_list(mode=mode,listtype=listtype,searchtag=searchtag)
		
	def oas_show(self,mode,showtype=""):
		return self.oas_data_show(mode=mode,showtype=showtype)

	def oas_count(self,mode,counttype=""):
		return self.oas_data_count(mode=mode,counttype=counttype)

	def oas_create(self,mode,nodetype=""):
		rv=self.oas_data_create(mode=mode,nodetype=nodetype)
		if rv!=0:
			self.oas_Broadcast(self.broadcast_ports,"draw node "+str(rv[0]))
		return rv

	def oas_delete(self,mode,deletetype="node",target=""):
		rv=self.oas_data_delete(mode=mode,deletetype=deletetype,target=target)
		if rv!=0:
			if deletetype=="node":
				self.oas_Broadcast(self.broadcast_ports,"delete node "+str(rv[0]))
			elif deletetype=="connection":
				self.oas_Broadcast(self.broadcast_ports,"delete connection "+str(rv[0]))
			else:
				pass	
		return rv

	def oas_rename(self,mode,old="",new=""):
		rv=self.oas_data_rename(mode=mode,old=old,new=new)
		if rv!=0:
			self.oas_Broadcast(self.broadcast_ports,"rename "+str(old)+" "+str(rv[0]))		
		return rv

	def oas_connect(self,mode,from_variable="",to_variable=""):
		rv=self.oas_data_connect(mode=mode,from_variable=from_variable,to_variable=to_variable)
		if rv!=0:
			self.oas_Broadcast(self.broadcast_ports,"connect "+rv[0]+" "+rv[1]+" "+rv[2])		
		return rv
		
	def oas_new(self,mode="normal"):
		rv=self.oas_Startup()
		if rv!=0:
			self.oas_Broadcast(self.broadcast_ports,"new scene")		
		return rv

	def oas_end(self,mode,endnode=""):
		return self.oas_data_end(mode=mode,endnode=endnode)

	def oas_save(self,mode,filename="",filetype=""):
		return self.oas_file_save(mode=mode,filename=filename,filetype=filetype)
		
	def oas_open(self,mode,filename="",filetype=""):
		rv=self.oas_file_open(mode=mode,filename=filename,filetype=filetype)
		if rv!=0:
			self.oas_Broadcast(self.broadcast_ports,"refresh")		
		return rv
	
	def oas_run(self,mode,runmode="normal",fixedframe=1):
		return self.oas_run_execute(mode=mode,runmode=runmode,fixedframe=fixedframe)

	def oas_set(self,mode,nodevalue="",value=""):
		return self.oas_data_set(mode=mode,nodevalue=nodevalue,value=value)	
		
	def oas_positions(self,mode,nodevalue="",posx=100,posy=100):
		return self.oas_data_positions(mode=mode,nodevalue=nodevalue,posx=posx,posy=posy)

	def oas_framerange(self,mode,firstframe="",endframe=""):
		return self.oas_data_framerange(mode=mode,firstframe=firstframe,endframe=endframe)

	def oas_frame(self,mode,frame=""):
		return self.oas_data_frame(mode=mode,frame=frame)
		
	def oas_Start(self):
		return self.oas_Startup()
		
	def oas_server_chk(self,port):
		return self.oas_broadcast_chk(port)
		
	def oas_ui_refresh(self):
		self.oas_Broadcast(self.broadcast_ports,"refresh")
	def oas_core_tester(self):
		try:
			self.oas_frame(mode="silent",frame=1)
			return 1
		except:
			return 0
		
