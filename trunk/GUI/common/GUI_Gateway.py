######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from GUI_Interface import GUI_Interface_client

class gui_gateway(GUI_Interface_client):
	def oas_gui_new(self):
		self.oas_gui_interface_client(self.main_serverport,"new")

	def oas_gui_open(self,path):
		self.oas_gui_interface_client(self.main_serverport,("open "+str(path)+" "+str(path)[-3:]))

	def oas_gui_save(self,path):
		self.oas_gui_interface_client(self.main_serverport,("save "+str(path)+" "+str(path)[-3:]))
		
	def oas_gui_showframe(self):
		ret=self.oas_gui_interface_client(self.main_serverport,("show frame"))
		ret=ret.strip("]").lstrip("[").strip("\'").lstrip("\'")
		return ret

	def oas_gui_nodetypelist(self):
		r=self.oas_gui_interface_client(self.main_serverport,("list nodetypes"))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x)
		return ret
		
	def oas_gui_nodelist(self):
		nods={}
		for no in self.oas_gui_nodetypelist():
			noderet=self.oas_gui_interface_client(self.main_serverport,("show "+str(no)))
			re=noderet.strip("]").lstrip("[").split(",")
			ret=[]
			for x in re:
				x=x.strip().lstrip().strip("\'").lstrip("\'")
				ret.append(x)
			nods[ret[0].split(":")[0]]={'tag':ret[0].split(":")[1]}
		return nods

	def oas_gui_showframerange(self):
		ret=self.oas_gui_interface_client(self.main_serverport,("show framerange"))
		ret1=str(ret).strip("]").lstrip("[").split(",")[0].strip().lstrip().lstrip("\'").strip("\'")
		ret2=str(ret).strip("]").lstrip("[").split(",")[1].strip().lstrip().lstrip("\'").strip("\'")
		return [ret1,ret2]
		
	def oas_gui_addnode(self,node):
		self.oas_gui_interface_client(self.main_serverport,("create "+str(node)))
		
		
	def oas_gui_currentfile(self):
		ret=self.oas_gui_interface_client(self.main_serverport,("current_file"))
		return ret
		
	def oas_gui_variabletypes(self):
		r=self.oas_gui_interface_client(self.main_serverport,("variabletypes"))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x.split(":"))
		return ret

	def oas_gui_server_check(self,port):
		ret=self.oas_gui_interface_client(self.main_serverport,("check "+str(port)))
		return ret
