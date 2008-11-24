#! /usr/bin/env python

######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Tkinter import *
from PreferencePanel import CanvasInitPreferencePanel
import thread,os,sys,string
from GUI.common.GUI_Gateway import gui_gateway
from GUI.common.GUI_Setup import oas_GUI_setup
from GUI.common.GUI_Interface import GUI_Interface_server
from Old_Preferences_Interpreter import old_preferences_interpreter


class OldPreferences(Frame,CanvasInitPreferencePanel,gui_gateway,oas_GUI_setup,GUI_Interface_server,old_preferences_interpreter):
    def __init__(self, master=None):
        Frame.__init__(self, master)
	self.grid()
        self.Startup()
	self._createWidgets()
	#self.oas_gui_refresh()

    def Startup(self):  
	
	import platform
	if platform.system()=="Windows":
		self.oas_userhome=os.environ.get("USERPROFILE")
		self.oas_home=str(self.oas_userhome)+"/OpenAssembler"
	else:
		self.oas_userhome=os.environ.get("HOME")
		self.oas_home=str(self.oas_userhome)+"/.OpenAssembler"

	parsedret=self.oas_gui_setup(self.oas_home+"/OpenAssembler.ini")
	fnt=self.oas_gui_font(parsedret)
	self.main_serverport=self.oas_gui_serverport(parsedret,"server")
	self.preferencesport=self.oas_gui_serverport(parsedret,"preferences")
	
	ch=str(self.oas_gui_server_check(self.preferencesport))
	if ch=="1":
		sys.exit(0)
		
	self.font=fnt[0]
	self.fontsize=int(fnt[1])
	self.nodeInPreferences=StringVar()
	self.nodeInPreferences.set("OpenAssembler")
	llock=thread.allocate_lock()
	thread.start_new_thread(self.oas_gui_interface_server,(self.preferencesport,llock))
	
	c="0"
	#while c=="0":
		#c="1"
		#c=str(self.oas_gui_server_check(self.preferencesport))

    def _createWidgets(self):
            self.preferencec=self.StartUpPreferencePanelCanvas()

class Old_Preferences(GUI_Interface_server):
	def start_old_preferences(self):
		app= OldPreferences() 
		app.master.title("OpenAssembler Preferences Old-Interface")
		def killer():
			app.master.destroy()
		app.bind("<<cloose>>", lambda app=app:killer())
		app.mainloop()
		sys.exit(0)
		
		



