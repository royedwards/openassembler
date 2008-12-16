######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################


from PreferencePanel import LoadPreferences

class old_preferences_interpreter(LoadPreferences):

	def old_gui_do(self,command):
		print command
		try:
			if command.split()[0]=="set":
				if command.split()[1].split(".")[0]==self.nodeInPreferences.get():
					tmp=self.nodeInPreferences.get()
					ParameterFrame=self.old_preferences_refresh()
					attrList,node_datas=self.old_preferences_build("showpreferences "+str(tmp))
					self.old_preferences_addattributes(ParameterFrame,attrList,node_datas)
				
			elif command.split()[0]=="rename":
				if command.split()[1]==self.nodeInPreferences.get():
					self.nodeInPreferences.set(command.split()[2])
					self.nip.set(command.split()[2])
					
			elif (command.split()[0]=="delete") or (command.split()[0]=="connect"):
				ParameterFrame=self.old_preferences_refresh()
				
			elif command.split()[0]=="refresh":
				tmp=self.nodeInPreferences.get()
				ParameterFrame=self.old_preferences_refresh()
				attrList,node_datas=self.old_preferences_build("showpreferences "+str(tmp))
				self.old_preferences_addattributes(ParameterFrame,attrList,node_datas)
				
			elif command.split()[0]=="showpreferences":
				ParameterFrame=self.old_preferences_refresh()
				attrList,node_datas=self.old_preferences_build(command)
				self.old_preferences_addattributes(ParameterFrame,attrList,node_datas)
				
		except:
			pass
