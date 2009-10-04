# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

# #####################################################################################################################################
#
# This file is to handle the setup file and to init the software, collect the nodes and so..
#
# #####################################################################################################################################

import os,sys,string
from Core.Dbase.variables import oas_variablechecker

class oas_setup(oas_variablechecker):

# #####################################################################################################################################
# Here we load and parse the setup file
# #####################################################################################################################################

	def oas_load_setup(self):
		if os.name=="nt":
			self.oas_userhome=os.environ.get("USERPROFILE")
			self.oas_home=str(self.oas_userhome)+"/OpenAssembler"
		else:
			self.oas_userhome=os.environ.get("HOME")
			self.oas_home=str(self.oas_userhome)+"/.OpenAssembler"
	    	if os.path.isdir(self.oas_home):
			pass
	    	else:
			os.mkdir(self.oas_home)
		oas_setupFile=self.oas_home+"/OpenAssembler.ini"
		if os.path.isfile(oas_setupFile)!=True:
			sys.exit()
		file=open(oas_setupFile,"r")
		setupFile_Content=file.read()
		setupFile_Content=setupFile_Content.replace("\r\n","\n")
		file.close()
		setupFile_Content=setupFile_Content.split("\n")
		setup_parsed=[]
		for rws in setupFile_Content:
			ret=rws.split()
			if len(ret)>0:
				if str(rws[:1])!=str("#"):
					setup_parsed.append(ret)
		return setup_parsed

	def oas_menucategory_settings(self,parsed):
		mncline={}
		for liness in parsed:
			if liness[0]=="menucategory":
				mncline[liness[1]]=[]
				for i in range (2, len(liness)):
					for nd in self.oas_node_list.keys():
						if self.oas_node_list[nd]['tag']==str(liness[i]):
							mncline[liness[1]].append(str(nd))
		mncline["OpenAssembler Core"]=["_def"]
		return mncline

# #####################################################################################################################################
# to collect the variabletypes settings (for the connection check procedure)
# #####################################################################################################################################		
		
	def oas_register_variable_with_cat(self,setupfilecontent,variablecategory,var):
		cat="undefined"
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="variablecategory":
				if setupfilecontent[i][2].find(str(var))>-1:
					cat=str(setupfilecontent[i][1])
		variablecategory[str(var)]=cat


	def manuPath(self,setupfilecontent):
		folders=[]
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="manualpath":
				for it in setupfilecontent[i][1].split(","):
					folders.append(it)
		return folders

# #####################################################################################################################################
# This definition is checking the environment variable and the colecting the valid directories
# #####################################################################################################################################

	def oas_collect_node_dirs(self,setupfilecontent):
		folders=[]
		for i in range (0,len(setupfilecontent)):
			if setupfilecontent[i][0]=="manualpath":
				if len(setupfilecontent[i])>1:
					splitted=setupfilecontent[i][1].split(",")
					for n in range (0,len(splitted)):
						if splitted[n]!="":
							if os.path.isdir(splitted[n]):
								folders.append(splitted[n])
								dirlist=os.listdir(splitted[n])
								for item in dirlist:
									if os.path.isdir(splitted[n]+"/"+item):
										folders.append(splitted[n]+"/"+item)
		return folders
	
# #####################################################################################################################################
# This definition is collecting all the nodes from the directiories and parse them for the parameters
# #####################################################################################################################################

	def oas_collect_nodes_from_dirs(self,dirlist):
		nodelist={}
		for singledir in dirlist:
			dir_content=os.listdir(singledir)
			for desc_files in dir_content:
				
# ####################################################################################################################################
# This is bad, but I need to check if I have acces or not for an sa file. 
# it is quite slow, so later maybe I need to change this with a more inteeligent one
# ####################################################################################################################################

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
						node_file_content=node_file_content.replace("\r\n","\n")
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
# #####################################################################################################################################
# Recognize the optinos in the inputs values
# #####################################################################################################################################
									
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
												default=""
																	
									default= default.lstrip("\"").strip("\"")
									#if default=="" or default=="\"\"" or default==None:
									#	default="0"
										
# #####################################################################################################################################
# It will convert the different format of variables to the one we can understand
# #####################################################################################################################################
									default=self.oas_variable(str(cleanpart[w][1]),default)
															
# #####################################################################################################################################
# Store the settings depending on if it is input or output
# #####################################################################################################################################									
										
									self.oas_register_variable_with_cat(self.setup_contents,self.oas_variablecategory,str(cleanpart[w][1]))
									if cleanpart[w][0]=="input":
										inputs[str(cleanpart[w][2])]={'variable_type':str(cleanpart[w][1]),'value':str(default),'options':str(option)}
									if cleanpart[w][0]=="output":
										outputs[str(cleanpart[w][2])]={'variable_type':str(cleanpart[w][1]),'value':str(default),'options':str(option)}
									
							settings={"_do_cache":"False"}
							nodelist[str(entry_name)]={'tag':str(entry_firsttag),'path':str(singledir+"/"+desc_files),'inputs':inputs,'outputs':outputs, "settings":settings}
		settings_def={"_do_cache":"False","QtMainWindowUi":""}
		nodelist["_def"]={'tag':str("oascore"),'path':str("OpenAssembler internal function"),'inputs':{"Input":{'variable_type':"any",'value':"",'options':""},"Hython":{'variable_type':"int",'value':"0",'options':""}},'outputs':{},"settings":settings_def}
		return nodelist
