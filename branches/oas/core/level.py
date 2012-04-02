import time,copy

class levelBase:
	def __init__(self,parent):
		self.parent=parent
		self.nodelist={}
		self.cache={}
		self.error=False
		self.extendable_connections=False
		self.exitnode=""
		self.position=[500,500]
		self.nodetype="network"
		self.function=self
		self.nodename="root"
		self.inputs={}


	def get_inputs(self):
		inputs={}
		for key in self.nodelist.keys():
			for in_key in self.nodelist[key].get_inputs().keys():
				if self.nodelist[key].get_inputs()[in_key]["route_to_parent"]==True:
					inputs[self.nodelist[key].nodename+"."+in_key]={"value":self.nodelist[key].get_inputs()[in_key]["value"],"connection":self.nodelist[key].get_inputs()[in_key]["connection"],"flag":False,"route_to_parent":False}
		self.inputs=inputs
		return inputs

	def add_node(self,node=None,name=None):
		result=False
		while result==False: 
			timestamp=str(time.time())
			name_gen=node.nodetype+"_"+timestamp
			if self.nodelist.has_key(timestamp):
				result=False
			else:
				parent=node.parent
				self.nodelist[timestamp]=copy.deepcopy(node)
				self.nodelist[timestamp].nodename=name_gen
				self.nodelist[timestamp].parent=parent
				result=True
		if name!=None:
			self.rename_node(old=name_gen,new=name)
		return self.nodelist[timestamp]

	def del_node(self,node=None):
		if node==None:
			return
		rem=""
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==node:
				rem=key
		del self.nodelist[rem]
		for key in self.nodelist.keys():
			iNNs=self.nodelist[key].get_inputs()
			for key_ins in iNNs.keys():
				if iNNs[key_ins]["connection"]==node:
					self.nodelist[key].del_connection(node,key_ins)
		if self.exitnode==node:
			self.exitnode=""

	def rename_node(self,old=None,new=None):
		if old==None or new==None:
			return None
		else:
			for key in self.nodelist.keys():
				if self.nodelist[key].nodename==new:
					return old
			for key in self.nodelist.keys():
				if self.nodelist[key].nodename==old:
					self.nodelist[key].nodename=new
					for key_c in self.nodelist.keys():
						for vari in self.nodelist[key_c].get_inputs().keys():
							if self.nodelist[key_c].get_inputs()[vari]["connection"]==old:
								self.add_connection(outnode=new,innode=self.nodelist[key_c].nodename,variable=vari)
					if self.exitnode==old:
						self.exitnode=new
					return new
		return old

	def add_connection(self,outnode=None,innode=None,variable=None):
		if outnode==None or innode==None or variable==None:
			return False
		if outnode==innode:
			return False
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==innode:
				if self.nodelist[key].nodetype=="network":
					for in_key in self.nodelist[key].nodelist.keys():
						if self.nodelist[key].nodelist[in_key].nodename==variable.rsplit(".",1)[0]:
							self.nodelist[key].add_connection(outnode=outnode,innode=variable.rsplit(".",1)[0],variable=variable.split(".")[-1])
				else:
					self.nodelist[key].add_connection(variable,outnode)
		return True

	def del_connection(self,node=None,variable=None):
		if node==None or variable==None:
			return
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==node:
				if self.nodelist[key].nodetype=="network":
					for in_key in self.nodelist[key].nodelist.keys():
						if self.nodelist[key].nodelist[in_key].nodename==variable.rsplit(".",1)[0]:
							self.nodelist[key].del_connection(variable.rsplit(".",1)[0],variable.split(".")[-1])
				else:
					self.nodelist[key].del_connection(node,variable)

	def _run(self,start_node=None):
		return self.run_network(start_node=self.exitnode)

	def run(self,start_node=None):
		self.error=False
		if start_node==None:
			return False
		self.cache_cleaner(self)
		self.exitnode=start_node
		return self.run_network(start_node=start_node)

	def cache_cleaner(self,level):
		level.cache={}
		for key in level.nodelist.keys():
			if level.nodelist[key].nodetype=="network":
				self.cache_cleaner(level.nodelist[key])

	def run_network(self,start_node=None):
		if start_node==None:
			return
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==start_node:	
				try:
					self.error=False
					return self.nodelist[key]._run(self)
				except:
					self.error=True

	def run_parent_network(self,start_node=None):
		if start_node==None:
			return
		for key in self.parent.nodelist.keys():
			if self.parent.nodelist[key].nodename==start_node:	
				return self.parent.nodelist[key]._run(self.parent)

	def set_value(self,node=None,variable=None,value=None):
		if node==None or variable==None:
			return False
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==node:	
				self.nodelist[key].set_value(variable,value)
		return True

	def set_route_to_parent(self,node=None,variable=None,value=None):
		if node==None or variable==None or value==None:
			return
		for key in self.nodelist.keys():
			if self.nodelist[key].nodename==node:	
				self.nodelist[key].set_route_to_parent(variable,value)

	def node_statistics(self):
		ret_stat='-----------------------------------------------------------------------\n'+"    LevelName: "+self.nodename+" ExitNode: "+self.exitnode+"\n"+'-----------------------------------------------------------------------\n'
		for key in self.nodelist.keys():
			ret_stat+= '-----------------------------------------------------------------------\n'
			ret_stat+= '   '+str(self.nodelist[key].nodename)+"\n"
			ret_stat+= '-----------------------------------------------------------------------\n'
			for name, value in self.nodelist[key].get_inputs().items():
				ret_stat+= '{0:15} ==> {1:15} @ {2:15} | {3:6} | {4:6}\n'.format(str(name), str(value['value']),str(value['connection']),str(value['flag']),str(value['route_to_parent']))
			ret_stat+= '-----------------------------------------------------------------------\n'
		return ret_stat

