#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    OpenAssembler v2 mod
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#---------------------------------------------------------------------------------------------------------------------

from Tkinter import *
from WindowFrames.NodeEditorCanvas import CanvasInitNodeEditor
import thread,os,sys,string
from GUI.common.GUI_Gateway import gui_gateway
from GUI.common.GUI_Setup import oas_GUI_setup
from GUI.common.GUI_Interface import GUI_Interface_server
from GUI.Old_GUI.Misc.Old_GUI_Interpreter import old_gui_interpreter


class OldGUI(Frame,CanvasInitNodeEditor,gui_gateway,oas_GUI_setup,GUI_Interface_server,old_gui_interpreter):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=1,fill=BOTH)
        self.Startup()
	self._createWidgets()
	self.oas_gui_refresh()

    def Startup(self):
	self.lastx=30
        self.lasty=30
        self.GlobalScale=.75
        self.origin_node=""
        self.origin_out=""
        self.origin_uni=""
        self.menuopen="0"
	self.RuntimeLines=[]
	
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
	self.editorport=self.oas_gui_serverport(parsedret,"editor")
	self.oas_node_list=self.oas_gui_nodetypes()
	self.font=fnt[0]
	self.fontsize=int(fnt[1])
	self.MenuNodeItems=self.oas_gui_menucategory(parsedret)
	self.savedfile=self.oas_gui_currentfile()
    	self.variable_categories=self.oas_gui_variabletypes()
	llock=thread.allocate_lock()
	thread.start_new_thread(self.oas_gui_interface_server,(self.editorport,llock))
	c="0"
	while c=="0":
		c="1"
		c=str(self.oas_gui_server_check(self.editorport))

    def _createWidgets(self):
            self.editorc=self.StartUpNodeEditorCanvas()

class Old_GUI(GUI_Interface_server):
	def start_old_gui(self):
		app= OldGUI() 
		def deleteWindow():
			pass
		app.master.protocol("WM_DELETE_WINDOW",deleteWindow)
		app.master.title("OpenAssembler NodeEditor Old-Interface")
		def killer():
			app.master.destroy()
		def killer_all():
			app.master.destroy()
		app.bind("<<cloose>>", lambda app=app:killer())
		app.bind("<<cloose_all>>", lambda app=app:killer_all())
		app.mainloop()
		sys.exit(0)
		
		



