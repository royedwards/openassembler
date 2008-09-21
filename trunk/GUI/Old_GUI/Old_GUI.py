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
import thread, sys
from GUI.Old_GUI.Misc.GUI_Gateway import gui_gateway

class OldGUI(Frame,CanvasInitNodeEditor,gui_gateway):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(expand=1,fill=BOTH)
        self.Startup()
	self._createWidgets()

    def Startup(self):
	    
	    #we need this to pass from open.... not from server.. :)
	    self.main_serverport=23345
	    
    	    self.font="Helvetica"
    	    self.fontsize="12"
	    
	    # we need this to pass from server
            self.MenuNodeItems=[["Math","mult","multiMath"],["Test","TXT_FileIn"]]
    	    
	    self.lastx=30
            self.lasty=30
            self.GlobalScale=.75
            self.origin_node=""
            self.origin_out=""
            self.origin_uni=""
            self.menuopen="0"
	    
	    # we need this to pass from server
	    self.savedfile=""

    def _createWidgets(self):
            self.editorc=self.StartUpNodeEditorCanvas()

class Old_GUI:
	def start_old_gui(self,lock,empty):
		app= OldGUI()
		lock.acquire()
		app.master.title("OpenAssembler NodeEditor Old-Interface")
		lock.release()
		app.mainloop()
		sys.exit()
		



