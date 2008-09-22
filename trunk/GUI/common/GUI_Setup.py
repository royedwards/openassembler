######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import os
import sys
import string

class oas_GUI_setup:
	def oas_gui_setup(self,path):
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

	def oas_gui_font(self,parsed):
		fnt=""
		fntsz=""
		for liness in parsed:
			if liness[0].strip().lstrip()=="font":
				fnt=liness[1]
			if liness[0].strip().lstrip()=="fontsize":
				fntsz=liness[1]
		return [fnt,fntsz]

	def oas_gui_menucategory(self,parsed):
		fnt=""
		fntsz=""
		mncat=[]
		mncline=[]
		for liness in parsed:	
			if liness[0].strip().lstrip()=="menucategory":
				mncline=[liness[1]]
				sl=liness[2].split(":")
				for ctl in sl:
					for nd in self.oas_node_list.keys():
						if self.oas_node_list[nd]['tag']==str(ctl):
							mncline.append(str(nd))
				if len(mncline)>1:
					mncat.append(mncline)
		return mncat


	def oas_gui_serverport(self,parsed,element):
		ret=0
		for lns in parsed:
			if lns[0].strip().lstrip()=="port":
				if lns[1].strip().lstrip()==element:
					ret=int(lns[2].strip().lstrip())
		if ret==0:
			sys.exit()
		return ret
	
