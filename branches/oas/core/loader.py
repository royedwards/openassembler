import os,copy,inspect

class nodeCataloge:
	def buildCataloge(self):
		NODE_CATALOG={'low_level':{},'high_level':{}}
		for file in os.listdir("./Nodes"):
			if file[-3:] == ".py":
				if file!="__init__.py":
					exec('from Nodes.'+file[:-3]+' import *')
		returnDict={}
		for key in locals().keys():
			if key[:4]==("oas_"):
				returnDict[key]=nodeDefault(locals()[key](),key)
		return returnDict

class nodeDefault:
	def __init__(self,function,nodetype):
		self.parent=None
		self.nodetype=nodetype
		self.function=function
		self.nodename=nodetype
		self.error=False
		self.position=[500,500]
		self.inputs={}
		args, varargs,keyords,defaults=self._input_check()
		try:
			exceptions=function.exceptions()
		except:
			exceptions=""
		try: 
			args.remove("self");
		except: 
			pass
		for n in range(0,len(args)):
			if exceptions.split(",").count(args[n])>0:
				flag=True
			else:
				flag=False
			if defaults!=None:
				self.inputs[args[n]]={"value":defaults[n],"connection":"","flag":flag,"route_to_parent":False}
			else:
				self.inputs[args[n]]={"value":None,"connection":"","flag":flag,"route_to_parent":False}
		if varargs!=None or keyords!=None:
			self.extendable_connections=True
		else:
			self.extendable_connections=False
	def get_inputs(self):
		return self.inputs
	def _input_check(self):
		return inspect.getargspec(self.function.run)
	def _run(self,level):
		if level.cache.has_key(self.nodename):
			pass
		else:
			new_arg_values=[]
			keys=self.get_inputs().keys()
			keys.sort()
			for key in keys:
				item=self.get_inputs()[key]
				if item["flag"]==False:
					if item["connection"]=="":
						new_arg_values.append(item["value"])
					else:
						if level.cache.has_key(item["connection"]):
							new_arg_values.append(level.cache[item["connection"]])
						else:
							if item["route_to_parent"]==False:
								level.cache[item["connection"]]=level.run_network(start_node=item["connection"])
								new_arg_values.append(level.cache[item["connection"]])
							else:
								if level.parent.cache.has_key(item["connection"]):
									new_arg_values.append(level.parent.cache[item["connection"]])
								else:
									level.cache[item["connection"]]=level.run_parent_network(start_node=item["connection"])
									new_arg_values.append(level.cache[item["connection"]])
				else:
					if item["connection"]=="":
						new_arg_values.append(item["value"])
					else:
						if level.cache.has_key(item["connection"]):
							if item["route_to_parent"]==False:
								new_arg_values.append([level.run_network,item["connection"],level.cache[item["connection"]]])
							else:
								new_arg_values.append([level.run_parent_network,item["connection"],level.cache[item["connection"]]])
						else:
							if item["route_to_parent"]==False:
								new_arg_values.append([level.run_network,item["connection"],None])
							else:
								new_arg_values.append([level.run_parent_network,item["connection"],None])
			try:
				level.cache[self.nodename]=self.function.run(*tuple(new_arg_values))
				self.error=False
			except:
				self.error=True
		return level.cache[self.nodename]
	def set_value(self,variable,val):
		self.inputs[variable]['value']=val
	def set_route_to_parent(self,variable,value):
		self.inputs[variable]['route_to_parent']=value
	def add_connection(self,variable,connected_node):
		self.inputs[variable]['connection']=connected_node
	def del_connection(self,node,variable):
		self.inputs[variable]['connection']=""
	def add_input(self,name=None,default_value=None):
		if name==None or name=="":
			return False
		keys=self.get_inputs().keys()
		keys.sort()
		for key in keys:
			if key==name:
				return False
		self.inputs[name]={"value":default_value,"connection":"","flag":False,"route_to_parent":False}
		return True






