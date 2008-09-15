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

class CanvasInitMenuLine:

    def NewScene(self):
	pass

    def SaveAsScene(self):
	pass

    def SaveScene(self):
	pass

    def OpenScene(self):
	pass
	
    def Preferences(self):
	pass

    def swiss(self):
	pass
	
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

        pref=Button(timelineFrame,width=11,bd=1,padx=5,pady=1,text="Preferences",font=iofont)
        pref.grid(row=1,column=5,padx=15)
        pref.bind('<B1-ButtonRelease>',lambda event:self.Preferences())

        iofont2 = tkFont.Font ( family=self.font , size=int(self.fontsize)-2, weight=tkFont.BOLD)

        swiss=Button(timelineFrame,width=11,bd=1,padx=5,pady=1,text="Swiss",font=iofont2,fg="gray90",bg = "darkred")
        swiss.grid(row=1,column=6,padx=815)
        swiss.bind('<B1-ButtonRelease>',lambda event:self.swiss())

        TargetCanvas.create_window(8,18,window=timelineFrame,anchor='w')
	
        return TargetCanvas

