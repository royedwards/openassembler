from Tkinter import *
from MouseEvents import NodeEditorCanvasEvents
import tkFont

class CanvasInitMicroViewer(NodeEditorCanvasEvents):
    def __init__(self):
        pass
    def _name(self):
        return "MicroViewerCanvasInit"

    def _initMicroViewerCanvas(self,TargetCanvas,TargetSide):
        iofont = tkFont.Font ( family="mincho", size=8 )
        TargetCanvas = Canvas (self, width=150, height=150,relief=RIDGE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=2,rowspan=60,sticky=N)
        TargetCanvas.create_text(75,15,text="SetEditor v0.01 early-alpha \n EEEpc mode (half sized)", fill="black",font=iofont)
        print "MicroViewer Initialised."
        return TargetCanvas

    def _ForgetMicroViewerCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "MicroViewer Closed."

    def StartUpMicroViewerCanvas(self,Name,Side):
        TargetCanvas=self._initMicroViewerCanvas(Name,Side)
        return TargetCanvas