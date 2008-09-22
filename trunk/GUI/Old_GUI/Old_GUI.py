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



class OldGUI(Frame,CanvasInitNodeEditor,gui_gateway,oas_GUI_setup,GUI_Interface_server):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=1,fill=BOTH)
        self.Startup()
	self._createWidgets()

    def Startup(self):
	self.lastx=30
        self.lasty=30
        self.GlobalScale=.75
        self.origin_node=""
        self.origin_out=""
        self.origin_uni=""
        self.menuopen="0"
	    
	self.oas_userhome=os.environ.get("HOME")
	self.oas_home=str(self.oas_userhome)+"/.OpenAssembler"
	parsedret=self.oas_gui_setup(self.oas_home+"/OpenAssembler.ini")
	fnt=self.oas_gui_font(parsedret)
	self.main_serverport=self.oas_gui_serverport(parsedret,"server")
	self.editorport=self.oas_gui_serverport(parsedret,"editor")
	self.oas_node_list=self.oas_gui_nodelist()
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
	def start_old_gui(self,lock,empty):
		lock.acquire()
		app= OldGUI() 
		app.master.title("OpenAssembler NodeEditor Old-Interface")
		def killer():
			app.master.destroy()
		def killer_all():
			app.master.destroy()
			thread.interrupt_main()
		app.bind("<<cloose>>", lambda app=app:killer())
		app.bind("<<cloose_all>>", lambda app=app:killer_all())

		lock.release()
		app.mainloop()
		
		



