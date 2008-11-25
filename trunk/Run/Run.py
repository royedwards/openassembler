######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import time
import sys
import os
import shutil
from Dbase.Data_handler import oas_data_handler
from Dbase.FileIO import oas_fileio

class oas_execute(oas_data_handler,oas_fileio):
	
	def oas_run_execute(self,mode="silent",runmode="normal",fixedframe=1):
		back=None
		self.runmode=runmode
		self.fixedframe=fixedframe
		node_cross_list={}
		for nds in self.oas_rt.keys():
			node_cross_list[self.oas_rt[nds]['name']]=nds
		if node_cross_list!={}:
			if node_cross_list.has_key(str(self.oas_scene_setup['endnode'])):
				piramid=self.oas_make_piramid(node_cross_list,self.oas_scene_setup['endnode'])
				optimized=self.oas_make_optimization(piramid)
				cache_folder=self.oas_prepare_folders()
				if cache_folder==False:
					return 0
				else:
					collection=self.oas_collect_nodes(optimized,node_cross_list,cache_folder)
					jsfile_ret=self.oas_create_jobfile(optimized,node_cross_list,collection,cache_folder)
					if self.runmode=="maya":
						dir=cache_folder
						#import compileall
						#compileall.compile_dir(dir)
						if os.path.isdir(dir):
							sys.path.append(dir)
						import oas_run_job as ojs
						runciclecall=ojs.run()
						return runciclecall.run_main()
					else:
						import platform
						if platform.system()=="Windows":
							back=os.system("python \""+str(jsfile_ret)+"\"")
						else:
							back=os.system("python "+str(jsfile_ret)+" &")
						return back
			else:
				if mode=="normal":
					print "No end-node!!"
				return 0
		else:
			if mode=="normal":
				print "There is no node in the scene."
			return 0
		
	def oas_make_piramid(self,node_list,fin_node):
        	level=[]
        	level_number=0
		next_level_counter=1
		level.append([fin_node])
        	while next_level_counter!=0:
                	tmp=self.oas_input_connections(level[level_number])
			if tmp==[]:
				next_level_counter=0
            		else:
				level.append(tmp)
				level_number+=1
            			next_level_counter=len(level[level_number])				
		return level
		
		
###############################################################################
# calculate the final order from the levels, check vhen the node firs appear
###############################################################################
	def oas_make_optimization(self,level):	
		finallist=[]
		for x in range(0,len(level)):
			reverse_x=len(level)-x-1
			exist_chk=0
			for lev in level[reverse_x]:
				for flm in finallist:
					if flm==lev:
						exist_chk=1
				if exist_chk==1:
					exist_chk=0
				else:
					finallist.append(lev)
					exist_chk=0
		return finallist
	
	def oas_input_connections(self,node_ins):
		ret=[]
		for node in node_ins:
			for con in self.oas_rt_connections.keys():
				if self.oas_rt[self.oas_rt_connections[con]['in_node']]['name']==str(node):
					ret.append(self.oas_rt[self.oas_rt_connections[con]['out_node']]['name'])
		return ret
		
		
	def oas_prepare_folders(self):
		timmee = time.gmtime()
		fintime=""
		tmpfilder=""
		for n in range (0, len(timmee)):
			fintime+="_"+str(timmee[n])
		try:
			if os.path.isfile(self.oas_save_filename):
				basesave=self.oas_save_filename
			else:
				basesave="~/tmp/tmp.oas"
	    		if self.runmode=="maya":
				tmpfilder=self.oas_userhome+"/tmp"
			else:
				tmpfilder=self.oas_userhome+"/tmp/"+os.path.basename(basesave)[:-4]+fintime
			if os.path.isdir(tmpfilder):
				pass
			else:
				os.makedirs(str(tmpfilder))
			if self.runmode=="maya":
				if os.path.isfile(str(tmpfilder)+"/__init__.py"):
					pass
				else:
					ifile=open(str(tmpfilder)+"/__init__.py","w")
					ifile.write("__all__=['oas_run_job'] \n")
					ifile.close()
			else:
				pass
				
        	except:
            		print "Error: Problem with the temp dir creation!!"
			return False
        	try:
			self.oas_file_save(mode="silent",filename=str(tmpfilder)+"/tmp_run.oas")
            		#print "--  --  OAS saved..."
        	except:
            		print "Error: Problem with copying files!!!"
            		return False
		return tmpfilder

	def oas_collect_nodes(self,nodelist,crosslist,path):
		collection={}
		for nds in nodelist:
			collection[nds]={'path':self.oas_node_list[self.oas_rt[crosslist[nds]]['nodetype']]['path'],'nodetype':self.oas_rt[crosslist[nds]]['nodetype']}
		for clt in collection:
			if os.path.isfile(str(path)+"/"+str(os.path.basename(collection[clt]['path']))):
				pass
			else:
				shutil.copy(collection[clt]['path'],path+"/")
		return collection	
		
		
	def oas_create_jobfile(self,nodelist,crosslist,collection,path):
		js='''
##OpenAssembler Job Script
#
# Created with OpenAssembler v2
#
#

'''
		modules=[]
		for nds in nodelist:
			chk=0
			for mds in modules:
				if str(mds)==str(collection[nds]['nodetype']):
					chk=1
				else:
					pass
			if chk==0:
				modules.append(collection[nds]['nodetype'])
				js+="from "+collection[nds]['nodetype']+" import "+collection[nds]['nodetype']+"\n"
			else:
				pass
		mds=""
		for mms in modules:
			mds+=mms+","
		mds=mds.strip(",")
		js+="\n"
		self.lastoutput=""
		if self.runmode=="maya":
			srtfame=self.fixedframe
			edframe=self.fixedframe
		else:
			srtfame=self.oas_scene_setup['startframe']
			edframe=self.oas_scene_setup['endframe']
		for cf in range(int(srtfame),int(edframe)+1):
			js+="# ------------------------------ Frame "+str(cf)+" ------------------------------\n"
			if self.runmode=="maya":
				js+="class run"+"("+str(mds)+"):\n"
			else:
				js+="class run"+str(cf)+"("+str(mds)+"):\n"
			if self.runmode=="maya":
				pass
			else:
				js+="\tdef __init__(self):\n"
				js+="\t\tself.run_main()\n"
			js+="\tdef run_main(self):\n"
			js+="\t\toas_current_frame="+str(cf)+"\n"
			for n in range (0,len(nodelist)):
				outs=[]
				for cns in self.oas_rt_connections.keys():
					if self.oas_rt_connections[cns]['out_node']==str(crosslist[nodelist[n]]):
						c=0
						for o in outs:
							if str(o)==str(self.oas_rt_connections[cns]['out_value']):
								c=1
						if c==0:
							outs.append(str(self.oas_rt_connections[cns]['out_value']))
				if outs==[]:
					outs=["out"]
				for out in outs:
					js+="\t\t"+str(nodelist[n])+"_variable_"+str(out)+"="+"self."+str(collection[nodelist[n]]['nodetype'])+"_main(oas_output=\""+str(out)+"\""
					self.lastoutput=str(nodelist[n])+"_variable_"+str(out)
					for ins in self.oas_rt[crosslist[nodelist[n]]]['inputs'].keys():
						js+=","+str(ins)+"="
						hascon=""
						for cns in self.oas_rt_connections.keys():
							
							if (self.oas_rt_connections[cns]['in_node']==str(crosslist[nodelist[n]])) and (self.oas_rt_connections[cns]['in_value']==str(ins)):
								hascon=self.oas_rt[self.oas_rt_connections[cns]['out_node']]['name']+"_variable_"+self.oas_rt_connections[cns]['out_value']
							else:
								pass 
						if hascon=="":
							vl=str(self.oas_rt[crosslist[nodelist[n]]]['inputs'][ins]['value'])
							if vl[:1]=="=":
								vl=vl[1:]
							js+=vl
						else:
							js+=hascon
					js+=")\n"
				if (n+1)==len(nodelist):
					js+="\t\t"+"return "+str(self.lastoutput)+"\n"
			if self.runmode=="maya":
				pass
			else:
				js+="run"+str(cf)+"()\n"
		jsfile=open(path+"/oas_run_job.py","w")
		jsfile.write(js)
		jsfile.close()
		return path+"/oas_run_job.py"
