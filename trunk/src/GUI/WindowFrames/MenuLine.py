from Tkinter import *
from MouseEvents import NodeEditorCanvasEvents


class CanvasInitMenuLine(NodeEditorCanvasEvents):
    def __init__(self):
        pass
    def _name(self):
        return "MenuLineCanvasInit"

    def _initMenuLineCanvas(self,TargetCanvas,TargetSide):
        TargetCanvas = Canvas (self, width=540, height=15,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=1,rowspan=6,sticky=N)
        #TargetCanvas.pack(expand=0,side=TargetSide)
        print "MenuLine Initialised."
        return TargetCanvas

    def _ForgetMenuLineCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "MenuLine Closed."

    def StartUpMenuLineCanvas(self,Name,Side):
        TargetCanvas=self._initMenuLineCanvas(Name,Side)
        return TargetCanvas