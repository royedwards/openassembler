######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Tkinter import *

class old_preferences_interpreter:
		
	def old_gui_do(self,command):
		try:
			if command.split()[0]=="set":
				pass
			elif command.split()[0]=="showpreferences":
				node_datas=self.oas_gui_scenenode_show(command.split()[1])
				self.nodeInPreferences.set(node_datas[1])
				attrList=self.oas_gui_attributelist(node_datas[1])
				self.preferencec.delete("all")
				ipszilon=20
				for item in attrList:
					self.preferencec.create_text(10,ipszilon,text=str(item))
					ipszilon+=10
				
		except:
			pass
