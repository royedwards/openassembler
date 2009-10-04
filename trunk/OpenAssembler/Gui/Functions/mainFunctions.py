# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui
import Gui.Node.drawNode as DN
from Core.Gateway.Gateway import oas_gateway
from Gui.AttributeEditor.attributeEditor import attributeEditor

class mainFunctions(oas_gateway,attributeEditor):

	def reloadMCat(self):
		self.oas_reloadMenucats()

	def do_search(self):
		text=str(self.oas_search_entry.text())
		if text.strip()=="":
			return
		for item in self.oas_scene.items():
			if item.backID()=="connection":
				pass
			elif str(self.oas_ID2name(ID=item.backID())).find(text)>-1:
				item.setSelected(True)

	def attributeE(self,ID):
		try:
			for widget in self.inAE["widget"].keys():
				self.inAE["widget"][widget].close()
		except:
			pass
		name=self.oas_ID2name(ID=ID)
		nodesettings=self.oas_nodeSettings(node=name)
		nodetype=self.oas_nodeType(node=name)
		ins=self.oas_nodeInputs(mode="silent",ID=ID)
		widgets={}
		extra={}
		if name=="__init__":
			value=self.oas_nodeSettings(mode="normal",node="__init__")["QtMainWindowUi"]
			extra["QtMainWindowUi"]={"variable_type":"file","value":value,"options":""}
		attributeset={"ID":ID,"name":name,"nodetype":nodetype,"nodesettings":nodesettings,"inputs":ins,"widget":widgets,"extras":extra}
		self.loadAttributes(attributeset,self.nodeSetE)

	def nodeSettingE(self):
		try:
			self.oas_set(mode="normal",nodevalue=self.inAE["name"]+"._do_cache",value=str(self.oas_attribute_cache.isChecked()))
		except:
			pass

	def nodeSetE(self,attribute,value):
		self.oas_set(mode="normal",nodevalue=self.inAE["name"]+"."+str(attribute),value=str(value))
		self.attributeE(self.inAE["ID"])

	def cleanE(self):
		try:
			for widget in self.inAE["widget"].keys():
				self.inAE["widget"][widget].close()
		except:
			pass
		widgets={}
		self.cleanAttributes()

	def varCategory(self,vartype):
		return self.oas_variableCategory(mode="", variabletype=vartype)

	def add_newAttribute(self,ID,type=""):
		name=self.oas_ID2name(ID=ID)
		if name==0:
			return
		ret_name=QtGui.QInputDialog.getText(self,"AddAttribute","Name of the attribute:")
		if str(ret_name[1])!="True" or str(ret_name[0]).strip()=="":
			return
		ret_type=QtGui.QInputDialog.getText(self,"AddAttribute","Type of the attribute:")
		if str(ret_type[1])!="True" or str(ret_type[0]).strip()=="":
			return
		for item in self.oas_scene.items():
			if item.backID()==ID:
				ret=self.oas_addInput(mode="normal",node=name,variablename=str(ret_name[0]),variabletype=str(ret_type[0]),defaultvalue="")
				if ret!=0:
					item.addInput(str(ret_name[0]),str(ret_type[0]))

		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass

	def remove_Attribute(self,ID,attribute):
		name=self.oas_ID2name(ID=ID)
		if name==0:
			return		
		ret=self.oas_delInput(mode="normal",node=name,variablename=attribute)
		if ret==0:
			return
		self.connectionCollector.removeConnection(ID,attribute)
		for item in self.oas_scene.items():
			if item.backID()==ID:
				item.removeInput(attribute)

		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass

	def connect_finally(self,outpoint,inpoint):
		ots=outpoint.split(".")
		its=inpoint.split(".")
		name_fr=self.oas_ID2name(ID=ots[0])
		name_to=self.oas_ID2name(ID=its[0])
		re=self.oas_connect(mode="normal",from_variable=str(name_fr+"."+ots[1]),to_variable=str(name_to+"."+its[1]))
		if re==0:
			return
		for item in self.oas_scene.items():
			if item.backID()==ots[0]:
				oitem=item
			elif item.backID()==its[0]:
				iitem=item
		oitem.markOutput(ots[1])
		iitem.markInput(its[1])
		self.connectionCollector.addConnection(oitem,ots[1],iitem,its[1],re[2])
		self.oas_scene.update()

		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass

	def addNode(self,nodetype):
		name= self.oas_create(mode="normal",nodetype=nodetype)
		ID=self.oas_name2ID(name=name)
		if ID==0:
			return 0
		ins=self.oas_nodeInputs(mode="normal",ID=ID)
		outs=self.oas_nodeOutputs(mode="normal",ID=ID)
		item = DN.DrawNode( ID,name,ins,outs,self.nodeDraw_inputs_collection)
		item.setPos(self.last_point)
		self.oas_positions(mode="normal",nodevalue=name,posx=self.last_point.x(),posy=self.last_point.y())
		self.oas_scene.addItem(item)

	def duplicateNode(self,ID):
		node=self.oas_ID2name(ID=ID)
		name= self.oas_duplicate(mode="normal",node=node)
		ID=self.oas_name2ID(name=name)
		if ID==0:
			return 0
		ins=self.oas_nodeInputs(mode="normal",ID=ID)
		outs=self.oas_nodeOutputs(mode="normal",ID=ID)
		item = DN.DrawNode( ID,name,ins,outs,self.nodeDraw_inputs_collection)
		item.setPos(self.last_point)
		self.oas_positions(mode="normal",nodevalue=name,posx=self.last_point.x(),posy=self.last_point.y())
		self.oas_scene.addItem(item)

	def do_run(self):
		self.oas_run(mode="normal")

	def do_generate(self):
		currentfile = QtGui.QFileDialog.getSaveFileName(self, 'Save Python Script from Network!','untitled.py')	
		if currentfile=="":
			return 0
		self.oas_generate(mode="normal",file=currentfile)

	def delete_internalNode(self,ID):
		try:
			if ID==self.inAE["ID"]:
				self.cleanE()
		except:
			pass
		for item in self.oas_scene.items():
			if item.backID()==ID:
				for con in item.allConnection():
					self.delete_internalConnection(ID,con)
				self.oas_scene.removeItem(item)


	def delete_node(self,ID):
		name=self.oas_ID2name(ID=ID)
		ret=self.oas_delete(mode="normal",deletetype="node",target=name)
		if ret==0:
			return
		try:
			if ID==self.inAE["ID"]:
				self.cleanE()
		except:
			pass
		for item in self.oas_scene.items():
			if item.backID()==ID:
				for con in item.allConnection():
					self.delete_internalConnection(ID,con)
				self.oas_scene.removeItem(item)

	def delete_internalConnection(self,ID,Connection):
		self.connectionCollector.removeConnection(ID,Connection)

	def delete_connection(self,ID,Connection):
		cIDList=self.connectionCollector.getConnectionID(ID,Connection)
		chk=0
		for ids in cIDList:
			res=self.oas_delete(mode="normal",deletetype="connection",target=ids)
			if res==0:
				chk+=1
		if chk!=0:
			print "Serious Problem with the nodes and connections, please restart!"
			return 0
		self.connectionCollector.removeConnection(ID,Connection)
		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass

	def setEndNode(self,ID):
		name=self.oas_ID2name(ID=ID)
		return self.oas_end(mode="normal",endnode=name)

	def node_position(self):
		for item in self.oas_scene.selectedItems():
			if item.backID()!="connection":
				posx=item.sceneSpaceRect().value(0).x()
				posy=item.sceneSpaceRect().value(0).y()
				name=self.oas_ID2name(ID=item.backID())
				self.oas_positions(mode="normal",nodevalue=name,posx=posx,posy=posy)
		
	def save_file(self):
		currentfile=self.oas_currentFileName()
		currentfile
		if currentfile=="" or currentfile==0:
			currentfile = QtGui.QFileDialog.getSaveFileName(self, 'Save OpenAssebler Network!','untitled.oas')	
			if currentfile=="":
				return 0
		self.oas_save(mode="normal",filename=currentfile,filetype="oas")

	def save_fileAs(self):
		currentfile = QtGui.QFileDialog.getSaveFileName(self, 'Save OpenAssebler Network!','untitled.oas')	
		if currentfile=="":
			return 0
		self.oas_save(mode="normal",filename=currentfile,filetype="oas")

	def new_file(self):
		self.oas_new(mode="normal")
		nodelist=[]
		for item in self.oas_scene.items():
			if item.backID()=="connection":
				pass 
			else:
				nodelist.append(item.backID())
		for node in nodelist:
			self.delete_internalNode(node)
		self.timeline_start()

	def rename(self):
		try:
			ID=self.inAE["ID"]
		except:
			return 0
		oldname=self.oas_ID2name(ID=ID)
		newname=str(self.oas_nodeName.text())
		if newname.strip()=="":
			return 0
		ret=self.oas_rename(mode="normal",old=oldname,new=newname)
		if ret==0:
			self.oas_nodeName.setText(oldname)
		else:
			self.oas_nodeName.setText(str(ret[0]))
			self.inAE["name"]=str(ret[0])
			for item in self.oas_scene.items():
				if item.backID()==ID:
					item.renameNode(str(ret[0]))

	def open_file(self):
		currentfile = QtGui.QFileDialog.getOpenFileName(self, 'Open OpenAssembler Nerwork!','',self.tr("OpenAssembler Files (*.oas)"))
		if currentfile=="":
			return
		ret=self.oas_open(mode="normal",filename=str(currentfile),filetype="oas")
		if ret==0:
			self.oas_new(mode="normal")
			return
		nodelist=[]
		for item in self.oas_scene.items():
			if item.backID()=="connection":
				pass 
			else:
				nodelist.append(item.backID())
		for node in nodelist:
			self.delete_internalNode(node)
		scene_nodes=self.oas_list(mode="normal",listtype="scene",searchtag="")
		for name in scene_nodes:
			ID=self.oas_name2ID(mode="normal",name=name)
			ins=self.oas_nodeInputs(mode="normal",ID=ID)
			outs=self.oas_nodeOutputs(mode="normal",ID=ID)
			pos=self.oas_getPositions(mode="normal",node=name)
			if pos==0:
				pos=[-2000,-2000]
			item = DN.DrawNode( ID,name,ins,outs,self.nodeDraw_inputs_collection)
			item.setPos(QtCore.QPointF(pos[0],pos[1]))
			self.oas_scene.addItem(item)
		scene_connections=self.oas_list(mode="normal",listtype="connections",searchtag="")
		for con in scene_connections:
			cret=self.oas_show(mode="normal",showtype=con)
			ots=cret[0].split(".")
			its=cret[1].split(".")
			for item in self.oas_scene.items():
				if item.backID()==self.oas_name2ID(name=ots[0]):
					oitem=item
				elif item.backID()==self.oas_name2ID(name=its[0]):
					iitem=item
			oitem.markOutput(ots[1])
			iitem.markInput(its[1])
			self.connectionCollector.addConnection(oitem,ots[1],iitem,its[1],con)
		self.timeline_start()
		self.solveConnectionBug()
		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass
	
	def import_file(self):
		currentfile = QtGui.QFileDialog.getOpenFileName(self, 'Import OpenAssembler Nerwork!','',self.tr("OpenAssembler Files (*.oas)"))
		if currentfile=="":
			return
		ret=self.oas_import(mode="normal",filename=str(currentfile),filetype="oas")
		if ret==0:
			self.oas_new(mode="normal")
			return
		nodelist=[]
		for item in self.oas_scene.items():
			if item.backID()=="connection":
				pass 
			else:
				nodelist.append(item.backID())
		for node in nodelist:
			self.delete_internalNode(node)
		scene_nodes=self.oas_list(mode="normal",listtype="scene",searchtag="")
		for name in scene_nodes:
			ID=self.oas_name2ID(name=name)
			ins=self.oas_nodeInputs(mode="normal",ID=ID)
			outs=self.oas_nodeOutputs(mode="normal",ID=ID)
			pos=self.oas_getPositions(mode="normal",node=name)
			if pos==0:
				pos=[-2000,-2000]
			item = DN.DrawNode( ID,name,ins,outs,self.nodeDraw_inputs_collection)
			item.setPos(QtCore.QPointF(pos[0],pos[1]))
			self.oas_scene.addItem(item)
		scene_connections=self.oas_list(mode="normal",listtype="connections",searchtag="")
		for con in scene_connections:
			cret=self.oas_show(mode="normal",showtype=con)
			ots=cret[0].split(".")
			its=cret[1].split(".")
			for item in self.oas_scene.items():
				if item.backID()==self.oas_name2ID(name=ots[0]):
					oitem=item
				elif item.backID()==self.oas_name2ID(name=its[0]):
					iitem=item
			oitem.markOutput(ots[1])
			iitem.markInput(its[1])
			self.connectionCollector.addConnection(oitem,ots[1],iitem,its[1],con)

		self.solveConnectionBug()
		try:
			self.attributeE(self.inAE["ID"])
		except:
			pass

