#------------------------------------------------------------------------------------------------------------------------------------
#
#    Menubar for OpenAssembler.
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------

from Tkinter import *
import tkFont
import tkFileDialog
from GUI.Old_GUI.Misc.GUI_Gateway import gui_gateway

class CanvasInitMenuLine(gui_gateway):

    def NewScene(self):
	self.oas_gui_new()

    def SaveScene(self):
            if self.savedfile=="":
	    	fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            	if fdiagback==():
                	pass
            	else:
			self.oas_gui_save(fdiagback)
			self.savedfile=fdiagback
	    else:
	    	self.oas_gui_save(self.savedfile)
			
    def SaveAsScene(self):
            fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                pass
            else:
		self.oas_gui_save(fdiagback)
		self.savedfile=fdiagback
		
    def OpenScene(self):
            fdiagback=tkFileDialog.Open(filetypes=[('OpenAsembler Scene','*.oas')],title="Open OpenAssembler scene file as:").show()
            if fdiagback==():
                pass
            else:
		self.oas_gui_open(fdiagback)
		self.savedfile=fdiagback

    def StartUpMenuLineCanvas(self):
        TargetCanvas = Canvas (self, width=1280, height=30,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=1,rowspan=6,sticky=N)
        timelineFrame=Frame(TargetCanvas,height=22,width=1270,bg="gray35")
        timelineFrame.grid_propagate(0)

        iofont = tkFont.Font ( family=self.font , size=int(self.fontsize)-2 )

        newb= Button (timelineFrame,width=3,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="New",font=iofont)
        newb.grid(row=1,column=1)
        newb.bind('<B1-ButtonRelease>',lambda event:self.NewScene())

        o= Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Open",font=iofont)
        o.grid(row=1,column=2)
        o.bind('<B1-ButtonRelease>',lambda event:self.OpenScene())

        savb=backfor=Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save",font=iofont)
        savb.grid(row=1,column=3)
        savb.bind('<B1-ButtonRelease>',lambda event:self.SaveScene())

        sas=onefor=Button(timelineFrame,width=10,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save as...",font=iofont)
        sas.grid(row=1,column=4)
        sas.bind('<B1-ButtonRelease>',lambda event:self.SaveAsScene())

        TargetCanvas.create_window(8,18,window=timelineFrame,anchor='w')
	
        return TargetCanvas

