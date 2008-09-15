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
from WindowFrames.NodeSliderBar import CanvasInitSliderBar
#from WindowFrames.NodeEditorCanvas import CanvasInitNodeEditor
from WindowFrames.TimeLine import CanvasInitTimeLine
from WindowFrames.MenuLine import CanvasInitMenuLine
#from WindowFrames.PreferencePanel import CanvasInitPreferencePanel
from WindowFrames.MicroViewer import CanvasInitMicroViewer



class _Application(Frame,CanvasInitMicroViewer,CanvasInitMenuLine,CanvasInitTimeLine,CanvasInitSliderBar):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.Startup()
	self._createWidgets()

    def Startup(self):

	    self.menulink=""
	    self.swiss_file=""

    	    self.font="Helvetica"
    	    self.fontsize="12"
	    self.sliderbarrows="1"
	    self.menucats=[["OpenAssembler","Math","Test","Misc"]]
            self.MenuNodeItems=[["Math","mult","multiMath"],["Test","TXT_FileIn"]]
	    self.SliderBarNodeList=[["mult","multiMath"],[],[]]
	    
    	    self.lastx=30
            self.lasty=30
            self.GlobalScale=.75
            self.origin_node=""
            self.origin_out=""
            self.origin_uni=""
            self.sceneFileName=""
            	        
            #self.CreateGlobalPreferences(1, 100, "Basic scene setup...","...")
            self.RuntimeLines=[]
            self.startFrame=IntVar()
            self.startFrame.set(1)
            self.endFrame=IntVar()
            self.endFrame.set(100)
            self.currentFrame=IntVar()
            self.currentFrame.set(self.startFrame.get())
            self.nodeInPreferences=StringVar()
            self.nodeInPreferences.set("OpenAssembler")
            self.eott=StringVar()
            self.eott.set("...")
    	    self.GUI_definition=""
    	    self.GUI_slider=""
            self.menuopen="0"
	    
    	    #sliderfile=open(self.sliderbarDescriptionFile,"r")
    	    #self.GUI_slider=sliderfile.read()
    	    #sliderfile.close()
	    
	    self.bigc=[]
	    self.smallc=[]


    def _createWidgets(self):

    	    mview=self.StartUpMicroViewerCanvas()
            #ppanel=self.StartUpPreferencePanelCanvas("PreferencePanel", "right")
            #editorcanvas=self.StartUpNodeEditorCanvas("NodeEditorCanvas", "top",ppanel)
            menuline=self.StartUpMenuLineCanvas()
            tline=self.StartUpTimeLineCanvas()
            slider=self.StartUpSliderBarCanvas()            
            #self.sldr=slider
	    #self.pplane=ppanel
	    self.editorc=""
	    #self.editorc=editorcanvas


app= _Application()
app.master.title("OpenAssembler v2.0.01beta")
app.tk_strictMotif(1)
app.tk_setPalette("gray35")
app.master.wm_resizable(width=False ,height=False)
app.mainloop()

