######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from GUI.common.GUI_Gateway import gui_gateway
from GUI.Old_GUI.Nodes.NodeTypes.NodeType01 import NodeType01
from GUI.Old_GUI.Nodes.ConnectionLine import ConnectLine

class old_gui_interpreter(gui_gateway,NodeType01,ConnectLine):
	
	def nodeDraw(self,node):
		nsettings=self.oas_gui_scenenode_show(node)
		self.BasicShape01(self.editorc,nsettings[0],nsettings[1],nsettings[2],nsettings[3],nsettings[4],"gray50",nsettings[5][0],nsettings[5][1])
		
	def re_new(self):
		self.editorc.delete("all")
		self.lastx=30
        	self.lasty=30
        	self.GlobalScale=.75
        	self.origin_node=""
        	self.origin_out=""
        	self.origin_uni=""
        	self.menuopen="0"
		self.RuntimeLines=[]
		self.savedfile=self.oas_gui_currentfile()
	
	def conn(self,lineid,out_node,out_value,in_node,in_value):
		self.RuntimeLines.append((lineid,out_node,out_value,out_node+out_value,in_node,in_value,in_node+in_value))
		self.RedrawLines(self.editorc,out_node)
	
	def old_gui_do(self,command):
		try:
			if command.split()[0]=="draw":
				if command.split()[1]=="node":
					self.nodeDraw(command.split()[2])
					
			elif command.split()[0]=="delete":
				if command.split()[1]=="node":
					self.editorc.delete(command.split()[2]+"select")
					self.RuntimeLines=[]
					self.editorc.delete("line")
					c=[]
					c=self.oas_gui_connectionslist()
					for con in c:
						this=self.oas_gui_connection_show(con)
						outnode=self.oas_gui_scenenode_show(this[1])[0]
						innode=self.oas_gui_scenenode_show(this[3])[0]
						self.conn(this[0],outnode,this[2],innode,this[4])
				if command.split()[1]=="connection":
					self.RuntimeLines=[]
					self.editorc.delete("line")
					c=[]
					c=self.oas_gui_connectionslist()
					for con in c:
						this=self.oas_gui_connection_show(con)
						outnode=self.oas_gui_scenenode_show(this[1])[0]
						innode=self.oas_gui_scenenode_show(this[3])[0]
						self.conn(this[0],outnode,this[2],innode,this[4])
				
					
			elif command.split()[0]=="new":
				if command.split()[1]=="scene":
					self.re_new()
					
			elif command.split()[0]=="rename":
				nsettings=self.oas_gui_scenenode_show(command.split()[2])
				self.editorc.itemconfig(command.split()[1], text=command.split()[2],tag=(nsettings[0],"UPPERLABEL",nsettings[2],command.split()[2],str(nsettings[0])+"select"))
				self.editorc.dtag(command.split()[1])
				
			elif command.split()[0]=="connect":
				lineid=command.split()[3]
				out_node=self.oas_gui_scenenode_show(command.split()[1].split(".")[0])[0]
				out_value=command.split()[1].split(".")[1]
				in_node=self.oas_gui_scenenode_show(command.split()[2].split(".")[0])[0]
				in_value=command.split()[2].split(".")[1]
				self.conn(lineid,out_node,out_value,in_node,in_value)
				
			elif command.split()[0]=="refresh":
				self.re_new()
				r=self.oas_gui_scenenodelist()
				self.editorc.delete("all")
				for nds in r:
					self.nodeDraw(nds)
				c=[]
				c=self.oas_gui_connectionslist()
				for con in c:
					this=self.oas_gui_connection_show(con)
					outnode=self.oas_gui_scenenode_show(this[1])[0]
					innode=self.oas_gui_scenenode_show(this[3])[0]
					self.conn(this[0],outnode,this[2],innode,this[4])
		except:
			pass
