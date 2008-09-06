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

class oas_setup:

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
				setup_parsed.append(ret)
		return setup_parsed

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
                						important_line=im_part[z].split()
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
									deff=""
									default=""
									option=""
									for d in range (3,len(cleanpart[w])):
										deff+=cleanpart[w][d]+" "
									deff=deff.strip()
					
######################################################################################################################################
# Recognize the optinos in the inputs values
######################################################################################################################################
									
									if (deff.find("\"min"))>0:
										option=deff[(deff.find("\"min")):]
										default=deff[:(deff.find("\"min"))]
										if default.lstrip("\"").strip("\"").strip("\n")==" ":
											default="0"
									elif (deff.find("\"ext"))>0:
										option=deff[(deff.find("\"ext")):]
										default=deff[:(deff.find("\"ext"))]
										if default.lstrip("\"").strip("\"").strip("\n")==" ":
											default="0"
									elif (deff.find("\"hidden"))>0:
										option=deff[(deff.find("\"hidden")):]
										default=deff[:(deff.find("\"hidden"))]
										if default.lstrip("\"").strip("\"").strip("\n")==" ":
											default="0"
									else:
										default=deff
											
									default= default.lstrip("\"").strip("\"")
									if default=="" or default=="\"\"" or default==None:
										default="0"
										
######################################################################################################################################
# It will convert the different format of variables to the one we can understand
######################################################################################################################################

									if str(cleanpart[w][1]).find("vector")>-1 or str(cleanpart[w][1]).find("point")>-1 or str(cleanpart[w][1]).find("color")>-1:
										if len(default.split())>1:
											default=str(default.split()[0])+";"+str(default.split()[1])+";"+str(default.split()[2])
										elif len(default.split(","))>1:
											default=str(default.split(",")[0])+";"+str(default.split(",")[1])+";"+str(default.split(",")[2])
										else:
											default="0;0;0"
									
									if str(cleanpart[w][1]).find("matrix")>-1:
										if len(default.split())>1:
											default=str(default.split(" ")[0])+";"+str(default.split(" ")[1])+";"+str(default.split(" ")[2])+";"+str(default.split(" ")[3])+";"+str(default.split(" ")[4])+";"+str(default.split(" ")[5])+";"+str(default.split(" ")[6])+";"+str(default.split(" ")[7])+";"+str(default.split(" ")[8])+";"+str(default.split(" ")[9])+";"+str(default.split(" ")[10])+";"+str(default.split(" ")[11])+";"+str(default.split(" ")[12])+";"+str(default.split(" ")[13])+";"+str(default.split(" ")[14])+";"+str(default.split(" ")[15])
										elif len(default.split(","))>1:
											default=str(default.split(",")[0])+";"+str(default.split(",")[1])+";"+str(default.split(",")[2])+";"+str(default.split(",")[3])+";"+str(default.split(",")[4])+";"+str(default.split(",")[5])+";"+str(default.split(",")[6])+";"+str(default.split(",")[7])+";"+str(default.split(",")[8])+";"+str(default.split(",")[9])+";"+str(default.split(",")[10])+";"+str(default.split(",")[11])+";"+str(default.split(",")[12])+";"+str(default.split(",")[13])+";"+str(default.split(",")[14])+";"+str(default.split(",")[15])
										elif len(default.split("_"))>1:
											default=str(default.split("_")[0])+";"+str(default.split("_")[1])+";"+str(default.split("_")[2])+";"+str(default.split("_")[3])+";"+str(default.split("_")[4])+";"+str(default.split("_")[5])+";"+str(default.split("_")[6])+";"+str(default.split("_")[7])+";"+str(default.split("_")[8])+";"+str(default.split("_")[9])+";"+str(default.split("_")[10])+";"+str(default.split("_")[11])+";"+str(default.split("_")[12])+";"+str(default.split("_")[13])+";"+str(default.split("_")[14])+";"+str(default.split("_")[15])
										else:
											default="0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0"
																											
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

