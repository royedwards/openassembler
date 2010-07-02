# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

from Core.Dbase.Data_handler import oas_data_handler
from Core.Dbase.FileIO import oas_fileio
from Core.Run.Run import oas_execute

class oas_gateway(oas_data_handler,oas_fileio,oas_execute):
	def oas_list(self,mode="normal",listtype="",searchtag=""):			
		return self.oas_data_list(mode=mode,listtype=listtype,searchtag=searchtag)
		
	def oas_show(self,mode="normal",showtype=""):
		return self.oas_data_show(mode=mode,showtype=showtype)

	def oas_count(self,mode="normal",counttype=""):
		return self.oas_data_count(mode=mode,counttype=counttype)

	def oas_create(self,mode="normal",nodetype=""):
		return self.oas_data_create(mode=mode,nodetype=nodetype)

	def oas_duplicate(self,mode="normal",node=""):
		return self.oas_data_duplicate(mode=mode,node=node)

	def oas_delete(self,mode="normal",deletetype="node",target=""):
		return self.oas_data_delete(mode=mode,deletetype=deletetype,target=target)

	def oas_rename(self,mode="normal",old="",new=""):
		return self.oas_data_rename(mode=mode,old=old,new=new)

	def oas_connect(self,mode="normal",from_variable="",to_variable=""):
		return self.oas_data_connect(mode=mode,from_variable=from_variable,to_variable=to_variable)
		
	def oas_new(self,mode="normal"):
		return self.dBase_builder()

	def oas_reloadMenucats(self,mode="normal"):
		return self.reloadMenucats()

	def oas_end(self,mode="normal",endnode=""):
		return self.oas_data_end(mode=mode,endnode=endnode)

	def oas_save(self,mode="normal",filename="",filetype=""):
		return self.oas_file_save(mode=mode,filename=filename,filetype=filetype)
		
	def oas_open(self,mode="normal",filename="",filetype=""):
		return self.oas_file_open(mode=mode,filename=filename,filetype=filetype)
	
	def oas_import(self,mode="normal",filename="",filetype=""):
		return self.oas_file_import(mode=mode,filename=filename,filetype=filetype)

	def oas_run(self,mode="normal"):
		return self.oas_run_execute()

	def oas_houdini(self,mode="normal"):
		return self.oas_run_execute(runmode="houdini")

	def oas_generate(self,mode="normal",file=""):
		return self.oas_run_execute(save_file=file)

	def oas_finalize(self,mode="finalize",file="",softwarename=""):
		return self.oas_run_execute(runmode=mode,save_file=file,softwarename=softwarename)

	def oas_set(self,mode="normal",nodevalue="",value=""):
		return self.oas_data_set(mode=mode,nodevalue=nodevalue,value=value)
		
	def oas_positions(self,mode="normal",nodevalue="",posx=100,posy=100):
		return self.oas_data_positions(mode=mode,nodevalue=nodevalue,posx=posx,posy=posy)

	def oas_getPositions(self,mode="normal",node=""):
		return self.oas_get_positions(mode=mode,nodevalue=node)

	def oas_framerange(self,mode="normal",firstframe="",endframe=""):
		return self.oas_data_framerange(mode=mode,firstframe=firstframe,endframe=endframe)

	def oas_frame(self,mode="normal",frame=""):
		return self.oas_data_frame(mode=mode,frame=frame)

	def oas_addInput(self,mode="normal",node="",variablename="",variabletype="string",defaultvalue=""):
		return self.oas_data_addInput(mode=mode,node=node,variablename=variablename,variabletype=variabletype,defaultvalue=defaultvalue)

	def oas_delInput(self,mode="normal",node="",variablename=""):
		return self.oas_data_delInput(mode=mode,node=node,variablename=variablename)

	def oas_menucats(self,mode="normal"):
		return self.oas_menucategories

	def oas_variableCategory(self,mode="normal",variabletype=""):
		try:
			return self.oas_variablecategory[variabletype]
		except:
			return {'variablecategory': 'undefined'}

	def oas_name2ID(self,mode="normal",name=""):
		return self.oas_data_name2ID(mode=mode,name=name)

	def oas_ID2name(self,mode="normal",ID=""):
		return self.oas_data_ID2name(mode=mode,ID=ID)

	def oas_nodeSettings(self,mode="normal",node=""):
		return self.oas_rt[self.oas_name2ID(name=node)]["settings"]

	def oas_nodeInputs(self,mode="normal",ID=""):
		return self.oas_data_nodeInputs(mode=mode,ID=ID)

	def oas_nodeOutputs(self,mode="normal",ID=""):
		return self.oas_data_nodeOutputs(mode=mode,ID=ID)

	def oas_currentFileName(self,mode="normal"):
		return self.oas_save_filename

	def oas_nodeType(self,mode="normal",node=""):
		return self.oas_rt[self.oas_name2ID(name=node)]["nodetype"]
