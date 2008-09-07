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

class oas_execute(oas_data_handler):
	
	def oas_run_execute(self,mode,inputs):
		if mode=="1" or mode=="0":
			node_cross_list={}
			for nds in self.oas_rt.keys():
				node_cross_list[self.oas_rt[nds]['name']]=nds
			if node_cross_list!={}:
				if node_cross_list.has_key(str(self.oas_scene_setup['endnode'])):
					piramid=self.oas_make_piramid(node_cross_list,self.oas_scene_setup['endnode'])
					optimized=self.oas_make_optimization(piramid)
					self.oas_prepare_folders()
					return True
				else:
					if mode=="1":
						print "No end-node!!"
					return False
			else:
				if mode=="1":
					print "There is no node in the scene."
				return False

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
		for n in range (0, len(timmee)):
			fintime+="_"+str(timmee[n])
		try:
			if os.path.isfile(self.oas_save_filename):
				basesave=self.oas_save_filename
			else:
				basesave="~/tmp/tmp.oas"
	    		tmpfilder=self.oas_userhome+"/tmp/"+os.path.basename(basesave)[:-4]+fintime
	    		os.makedirs(str(tmpfilder))
            		print "--  --  TMP cache folder are created..."
        	except:
            		print "Error: Problem with the temp dir creation!!"
        	try:
            		self.oas_data_save("1",["save","oas",tmpfilder+"/tmp_run.oas"])
            		print "--  --  OAS saved..."
        	except:
            		print "Error: Problem with copying files!!!"
            		sys.exit(1)
		sys.exit(0)
'''		
        jobscriptvar="#! /usr/bin/env python\n"
        jobscriptvar+=("# OpenAssembler Job-Script\n")
        try:
            jsfile=open((str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/jobscript.py","w")
            jsfile.write(jobscriptvar)
            jsfile.close()
            print "--  --  Job-script are created..."
            print "--  --  Job-script: "+(str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/jobscript.py"
        except:
            print "Error: Problem with js file!!!"
            sys.exit(1)
        return (((str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/"),str(splt[1]))

'''
