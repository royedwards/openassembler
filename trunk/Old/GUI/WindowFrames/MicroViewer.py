#------------------------------------------------------------------------------------------------------------------------------------
#
#    MicroViewer for OpenAssembler. 
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
from MouseEvents import NodeEditorCanvasEvents
import tkFont

class CanvasInitMicroViewer(NodeEditorCanvasEvents):
    def __init__(self):
        pass
    def _name(self):
        return "MicroViewerCanvasInit"

    def _initMicroViewerCanvas(self,TargetCanvas,TargetSide):
        iofont = tkFont.Font ( family=self.font, size=self.fontsize )
        TargetCanvas = Canvas (self, width=300, height=int(140/3*int(self.sliderbarrows)),relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=130,column=2,rowspan=60,sticky=S)
        TargetCanvas.create_text(150,30,text="OpenAssember v0.04beta \n Linux mode (full size)", fill="black",font=iofont)
        print "MicroViewer Initialised."
        return TargetCanvas

    def _ForgetMicroViewerCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "MicroViewer Closed."

    def StartUpMicroViewerCanvas(self,Name,Side):
        TargetCanvas=self._initMicroViewerCanvas(Name,Side)
        return TargetCanvas
