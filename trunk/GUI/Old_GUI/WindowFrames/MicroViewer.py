#------------------------------------------------------------------------------------------------------------------------------------
#
#    MicroViewer for OpenAssembler. 
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
import tkFont

class CanvasInitMicroViewer:

    def StartUpMicroViewerCanvas(self):
        iofont = tkFont.Font ( family=self.font, size=self.fontsize )
        TargetCanvas = Canvas (self, width=300, height=int(140/3*int(self.sliderbarrows)),relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=130,column=2,rowspan=60,sticky=S)
        TargetCanvas.create_text(150,30,text="OpenAssember v2.0.01beta-mod \n Linux mode (full size)", fill="black",font=iofont)
        return TargetCanvas


