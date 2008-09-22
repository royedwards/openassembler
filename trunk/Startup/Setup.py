######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

######################################################################################################################################
#
# This file is to handle the setup file and to init the software, collect the nodes and so..
#
######################################################################################################################################

import os
import sys
import string
from Dbase.variables import oas_variablechecker

class oas_setup(oas_variablechecker):

	def oas_create_setup(self,path):
		setupFile_Content='''
environments SA_SCRIPT_PATH
font Helvetica
fontsize 12
sliderbarrows 1
menucategory Math math
menucategory Mass mass
menucategory Dynamics dynamics:field:wind:flow
menucategory OpenAssembler oas
menucategory Massive massive
menucategory Mesh mesh:geo:surface:curve
manualpath /Users/simanlaci/munka/OpenAssembler/src/OpenNodes
variablecategory red path,string
variablecategory blue int,aint,vint,avint,float,afloat,vfloat,avfloat
variablecategory green matrix,amatrix,vmatrix,avmatrix
variablecategory black color,point,vector,avector,vvector,avvector

'''
		file=open(path,"w")
		file.write(setupFile_Content)
		file.close()
	
######################################################################################################################################
# Here we load and parse the setup file
######################################################################################################################################

	def oas_load_setup(self,path):
		file=open(path,"r")
		setupFile_Content=file.read()
		file.close()
		setupFile_Content=setupFile_Content.split("\n")
		setup_parsed=[]
		for rws in setupFile_Content:
			ret=rws.split()
			if len(ret)>0:
				if str(rws[:1])!=str("#"):
					setup_parsed.append(ret)
		return setup_parsed
		
######################################################################################################################################
# to collect font settings
######################################################################################################################################		

	def oas_font_settings(self,parsed):
		fnt=""
		fntsz=""
		for liness in parsed:
			liness=liness.lstrip().strip()
			if liness.split()[0]=="font":
				fnt=liness.split()[1]
			if liness.split()[0]=="fontsize":
				fntsz=liness.split()[1]
		return [fnt,fntsz]

	def oas_menucategory_settings(self,parsed):
		fnt=""
		fntsz=""
		mncat=[]
		mncline=[]
		for liness in parsed:
			liness=liness.lstrip().strip()
			
			if liness.split()[0]=="menucategory":
				mncline=[liness.split()[1]]
				for ctl in liness.split()[2].split(":"):
					for nd in self.oas_node_list.keys():
						if self.oas_node_list[nd]['tag']==str(ctl):
							mncline.append(str(nd))
			mncat.append(mncline)
		return mncat




######################################################################################################################################
# to collect the variabletypes settings (for the connection check procedure)
######################################################################################################################################		
		
	def oas_register_variable_with_cat(self,setupfilecontent,variablecategory,var):
		cat="undefined"
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="variablecategory":
				if setupfilecontent[i][2].find(str(var))>-1:
					cat=str(setupfilecontent[i][1])
		variablecategory[str(var)]={'variablecategory':cat}

######################################################################################################################################
# This definition is checking the environment variable and the colecting the valid directories
######################################################################################################################################

	def oas_collect_node_dirs(self,setupfilecontent):
		folders=[]
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="environments":
				if len(setupfilecontent[i])>1:
					splitted=setupfilecontent[i][1].split(":")
					for n in range (0,len(splitted)):
						if splitted[n]!="":
							envretun=os.environ.get(splitted[n])
							if envretun!=None:
								envretun=envretun.split(":")
								for m in range (0,len(envretun)):
									if envretun[m]!="":
										if os.path.isdir(envretun[m]):
											folders.append(envretun[m])
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="manualpath":
				if len(setupfilecontent[i])>1:
					splitted=setupfilecontent[i][1].split(":")
					for n in range (0,len(splitted)):
						if splitted[n]!="":
							if os.path.isdir(splitted[n]):
								folders.append(splitted[n])
		return folders
	
######################################################################################################################################
# This definition is collecting all the nodes from the directiories and parse them for the parameters
######################################################################################################################################

	def oas_collect_nodes_from_dirs(self,dirlist):
		nodelist={}
		for singledir in dirlist:
			dir_content=os.listdir(singledir)
			for desc_files in dir_content:
				
#####################################################################################################################################
# This is bad, but I need to check if I have acces or not for an sa file. 
# it is quite slow, so later maybe I need to change this with a more inteeligent one
#####################################################################################################################################

				checker_perm=False
				try:
					node_file=open(str(singledir+"/"+desc_files),"r")
					node_file.close()
					checker_perm=True
				except:
					checker_perm=False
				
				if os.path.isfile(str(singledir+"/"+desc_files))==True and checker_perm:
					if os.path.splitext(desc_files)[1][1:][:2]=="sa" or os.path.splitext(desc_files)[1][1:][:2]=="py":
						node_file=open(str(singledir+"/"+desc_files),"r")
						node_file_content=node_file.read()
						node_file.close()
						if len(node_file_content.split("define\n{",1))>1:
							im_part=node_file_content.split("define\n{",1)[1].split("}",1)[0]
							im_part=im_part.split("\n")
							for k in range (0,len(im_part)):
								if im_part[k]!="":
									im_part[k]=im_part[k].lstrip().strip()
							cleanpart=[]
							for z in range(0, len(im_part)):
								important_line=im_part[z].split(" ",3)
                						cleanline=[]
                						for y in range(0,len(important_line)):
                	    						if important_line[y]=="":
                	        						pass
                	    						else:
                	        						cleanline.append(important_line[y])
                						if len(cleanline)!=0:
                	    						cleanpart.append(cleanline)
                						else:
                	    						pass
            						entry_name=""
							entry_firsttag=""
							inputs={}
							outputs={}
							for w in range(0,len(cleanpart)):
								if cleanpart[w][0]=="name":
									entry_name=cleanpart[w][1]
								if cleanpart[w][0]=="tags":
									entry_firsttag=cleanpart[w][1].split(":")[0]
								if cleanpart[w][0]=="input" or cleanpart[w][0]=="output":
									default=""
									option=""
######################################################################################################################################
# Recognize the optinos in the inputs values
######################################################################################################################################
									
									if len(cleanpart[w])>3:
										cleanarray=[]
										if "\"" in cleanpart[w][3]:
											for porc in cleanpart[w][3].split("\""):
												if porc=="":
													pass
												else:
													cleanarray.append(porc)
										else:
											for porc in cleanpart[w][3].split():
												if porc=="":
													pass
												else:
													cleanarray.append(porc)	
													
										if len(cleanarray)>1:
												default=cleanarray[0]
												option=cleanarray[1]		
										else:
												default=cleanarray[0]
																	
									default= default.lstrip("\"").strip("\"")
									if default=="" or default=="\"\"" or default==None:
										default="0"
										
######################################################################################################################################
# It will convert the different format of variables to the one we can understand
######################################################################################################################################
									default=self.oas_variable(str(cleanpart[w][1]),default)
															
######################################################################################################################################
# Store the settings depending on if it is input or output
######################################################################################################################################									
										
									self.oas_register_variable_with_cat(self.setup_contents,self.oas_variablecategory,str(cleanpart[w][1]))
									if cleanpart[w][0]=="input":
										inputs[str(cleanpart[w][2])]={'variable_type':str(cleanpart[w][1]),'value':str(default),'options':str(option)}
									if cleanpart[w][0]=="output":
										outputs[str(cleanpart[w][2])]={'variable_type':str(cleanpart[w][1]),'value':str(default),'options':str(option)}
									
							nodelist[str(entry_name)]={'tag':str(entry_firsttag),'path':str(singledir+"/"+desc_files),'inputs':inputs,'outputs':outputs}
		return nodelist

	def oas_setup_port(self,parsed,element):
		ret=0
		for lns in parsed:
			if lns[0].strip().lstrip()=="port":
				if lns[1].strip().lstrip()==element:
					ret=int(lns[2].strip().lstrip())
		if ret==0:
			sys.exit()
		return ret
	
	def oas_setup_broadcast(self,parsed):
		ret=0
		br_col=[]
		for lns in parsed:
			if lns[0].strip().lstrip()=="port":
				if lns[1].strip().lstrip()!="server":
					br_col.append(int(lns[2].strip().lstrip()))
		return br_col
		
		
		
