#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    Gui Starting script....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#---------------------------------------------------------------------------------------------------------------------

from Tkinter import *
from WindowFrames.NodeSliderBar import CanvasInitSliderBar
from WindowFrames.NodeEditorCanvas import CanvasInitNodeEditor
from WindowFrames.TimeLine import CanvasInitTimeLine
from WindowFrames.MenuLine import CanvasInitMenuLine
from WindowFrames.PreferencePanel import CanvasInitPreferencePanel
from WindowFrames.MicroViewer import CanvasInitMicroViewer
from Dbase.DBaseManagement import RuntimeNodeRegister
#
#
#  Module Developement Test Part
#
#
class _Application(Frame,CanvasInitSliderBar,CanvasInitNodeEditor,CanvasInitTimeLine,CanvasInitMenuLine,CanvasInitPreferencePanel,CanvasInitMicroViewer):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=1)
        print "SetEditor Starting up...."
        print "Owner: Laszlo Mates, laszlo.mates@gmail.com"
        self._createWidgets()


    def _createWidgets(self):
        self.lastx=30
        self.lasty=30
        self.GlobalScale=.5
        self.origin_node=""
        self.origin_out=""
        self.origin_uni=""
        self.Create_RuntimeDBase()
        self.RuntimeLines=[]
        self.startFrame=IntVar()
        self.startFrame.set(1)
        self.endFrame=IntVar()
        self.endFrame.set(100)
        self.currentFrame=IntVar()
        self.currentFrame.set(25)
        self.nodeInPreferences=StringVar()
        self.nodeInPreferences.set("SetEditorGUI")

        menuline=self.StartUpMenuLineCanvas("MenuLineCanvas","top")
        mview=self.StartUpMicroViewerCanvas("MicroViewer", "right")


        ppanel=self.StartUpPreferencePanelCanvas("PreferencePanel", "right")
        editorcanvas=self.StartUpNodeEditorCanvas("NodeEditorCanvas", "top",ppanel)

        tline=self.StartUpTimeLineCanvas("TimeLineCanvas", "bottom",editorcanvas)
        slider=self.StartUpSliderBarCanvas("SliderBar", "bottom",editorcanvas)

        print "Application Started!"



app= _Application()
app.master.title("OpenAssembler 0.1beta")
app.tk_setPalette("gray35")
app.master.wm_resizable(width=False ,height=False)
app.mainloop()
print "SetEditor Closed."
print "---Thank You!---"

