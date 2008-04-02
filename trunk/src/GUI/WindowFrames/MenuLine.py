from Tkinter import *
#from MouseEvents import NodeEditorCanvasEvents
from GUI.WindowFrames.PreferencePanel import LoadPreferences

import tkFont


class CanvasInitMenuLine(LoadPreferences):

    def menuLine_init(self,TargetCanvas,preferencescanvas):
        timelineFrame=Frame(TargetCanvas,height=11,width=180,bg="gray35")
        timelineFrame.grid_propagate(0)

        iofont = tkFont.Font ( family="mincho", size=6 )

        r= Button (timelineFrame,width=3,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="New",font=iofont)
        r.grid(row=1,column=1)
        #r.bind('<Button-1>',lambda event:(self.currentFrame.set(self.startFrame.get())))
        o= Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Open",font=iofont)
        o.grid(row=1,column=2)
        #o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))

        b=backfor=Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Save",font=iofont)
        b.grid(row=1,column=3)
        #b.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()+1)))
        o2=onefor=Button(timelineFrame,width=10,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Save as...",font=iofont)
        o2.grid(row=1,column=4)
        #o2.bind('<Button-1>',lambda event:(self.currentFrame.set(self.endFrame.get())))


        pref=Button(timelineFrame,width=11,bd=1,padx=0,pady=0,text="Preferences",font=iofont)
        pref.grid(row=1,column=5,padx=15)
        pref.bind('<Button-1>',lambda event:self.loadPreferences(preferencescanvas, "0000000"))


        TargetCanvas.create_window(5,10,window=timelineFrame,anchor='w')

    def _initMenuLineCanvas(self,TargetCanvas,TargetSide,preferencescanvas):
        TargetCanvas = Canvas (self, width=540, height=15,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=1,rowspan=6,sticky=N)
        self.menuLine_init(TargetCanvas, preferencescanvas)
        print "MenuLine Initialised."
        return TargetCanvas

    def _ForgetMenuLineCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "MenuLine Closed."

    def StartUpMenuLineCanvas(self,Name,Side,preferencescanvas):
        TargetCanvas=self._initMenuLineCanvas(Name,Side,preferencescanvas)
        return TargetCanvas