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
		
	def oas_gui_connectionslist(self):
		r=self.oas_gui_interface_client(self.main_serverport,("list connections"))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x)
		return ret

	def oas_gui_attributelist(self,node):
		r=self.oas_gui_interface_client(self.main_serverport,("show_attributes "+str(node)))
		re=r.strip("]").lstrip("[").split("], [",1)
		ret=[]
		for xx in re:
			xx=xx.strip("]").lstrip("[")
			z=xx.split(",")
			for x in z:
				x=x.strip().lstrip().strip("\'").lstrip("\'")
				ret.append(x)
		return ret
		
	def oas_gui_scenenodelist(self):
		r=self.oas_gui_interface_client(self.main_serverport,("list scene"))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x)
		return ret
		
	def oas_gui_connection_show(self,toshow):
		r=self.oas_gui_interface_client(self.main_serverport,("show "+str(toshow)))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x)
		return (toshow,ret[0].split(".")[0],ret[0].split(".")[1],ret[1].split(".")[0],ret[1].split(".")[1])
		
	def oas_gui_scenenode_show(self,toshow):
		r=self.oas_gui_interface_client(self.main_serverport,("show "+str(toshow)))
		re=r.strip("]").lstrip("[").split(",")
		ret=[]
		for x in re:
			x=x.strip().lstrip().strip("\'").lstrip("\'")
			ret.append(x)
		result=[]
		result.append(ret[0].split(":")[2])
		result.append(ret[0].split(":")[0])
		result.append(ret[0].split(":")[1])
		ins=[]
		outs=[]
		for y in ret:
			if y.find("input.")>-1:
				ins.append(y.split(".")[1].split("=")[0])
			if y.find("output.")>-1:
				outs.append(y.split(".")[1].split("=")[0])
		result.append(ins)
		result.append(outs)
		result.append((int(ret[1].split(":")[0]),int(ret[1].split(":")[1])))
		return result
		
	def oas_gui_nodetypes(self):
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
		
	def oas_gui_run(self):
		ret=self.oas_gui_interface_client(self.main_serverport,("run"))
		return ret
		
	def oas_gui_setframerange(self,start,end):
		ret=self.oas_gui_interface_client(self.main_serverport,("framerange "+str(start)+" "+str(end)))
		return ret
		
	def oas_gui_preview(self):
		frangee=self.oas_gui_showframerange()
		curr=self.oas_gui_showframe()
		self.oas_gui_setframerange(curr,curr)
		ret=self.oas_gui_interface_client(self.main_serverport,("run"))
		self.oas_gui_setframerange(frangee[0],frangee[1])
		return ret
		
	def oas_gui_addnode(self,node):
		self.oas_gui_interface_client(self.main_serverport,("create "+str(node)))
		
	def oas_gui_endnode(self,nodein):
		node=self.oas_gui_scenenode_show(nodein)[1]
		self.oas_gui_interface_client(self.main_serverport,("end "+str(node)))
		
	def oas_gui_connect(self,outnode,outvalue,innode,invalue):
		outnode=self.oas_gui_scenenode_show(outnode)[1]
		innode=self.oas_gui_scenenode_show(innode)[1]
		self.oas_gui_interface_client(self.main_serverport,("connect "+str(outnode)+"."+str(outvalue)+" "+str(innode)+"."+str(invalue)))
		
	def oas_gui_refresh(self):
		self.oas_gui_interface_client(self.main_serverport,("refresh"))
		
	def oas_gui_show_in_preferences(self,node):
		self.oas_gui_interface_client(self.main_serverport,("showpreferences "+str(node)))
		
	def oas_gui_deletenode(self,node):
		self.oas_gui_interface_client(self.main_serverport,("delete node "+str(node)))
		
	def oas_gui_deleteline(self,node):
		self.oas_gui_interface_client(self.main_serverport,("delete connection "+str(node)))
		
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

	def oas_gui_set_positions(self,node,posx,posy):
		ret=self.oas_gui_interface_client(self.main_serverport,("positions "+str(node)+" "+str(posx)+" "+str(posy)))
		return ret
		
