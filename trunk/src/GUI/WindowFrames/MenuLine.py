from Tkinter import *
from GUI.WindowFrames.PreferencePanel import LoadPreferences, CanvasInitPreferencePanel
from Dbase.DBaseManagement import RuntimeNodeRegister, openScene
from GUI.Nodes.NodeList import NodeListCategoriser


import tkFont
import tkFileDialog


class CanvasInitMenuLine(LoadPreferences,CanvasInitPreferencePanel,RuntimeNodeRegister,openScene,NodeListCategoriser):

    def NewScene(self,ppanel,editor):
        self.lastx=30
        self.lasty=30
        self.GlobalScale=.5
        self.origin_node=""
        self.origin_out=""
        self.origin_uni=""
        self.Create_RuntimeDBase()
        self.CreateGlobalPreferences(1, 100, "Basic scene setup...")
        self.RuntimeLines=[]
        self.startFrame.set(self.getFrameRange()[0])
        self.endFrame.set(self.getFrameRange()[1])
        self.currentFrame.set(self.startFrame.get())
        self.nodeInPreferences.set("OpenAssembler")
        ppanel.delete(ALL)
        self.controllerNodeHeader(ppanel)
        editor.delete(ALL)
        self.sceneFileName=""

    def SaveAsScene(self):
            fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                print "Save canceled..."
            else:
                patth=str(self.runtimeDBasePath())
                xmlfileoutput=open(patth,"r")
                savefileoutput=open(fdiagback,"w")
                savefileoutput.write(xmlfileoutput.read())
                xmlfileoutput.close()
                savefileoutput.close()
                self.sceneFileName=str(fdiagback)
                print "OpenAssembler scene saved at: "+str(fdiagback)

    def SaveScene(self):
        if self.sceneFileName=="":
            fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                print "Save canceled..."
            else:
                patth=str(self.runtimeDBasePath())
                xmlfileoutput=open(patth,"r")
                savefileoutput=open(fdiagback,"w")
                savefileoutput.write(xmlfileoutput.read())
                xmlfileoutput.close()
                savefileoutput.close()
                self.sceneFileName=str(fdiagback)
                print "OpenAssembler scene saved at: "+str(fdiagback)
        else:
            patth=str(self.runtimeDBasePath())
            xmlfileoutput=open(patth,"r")
            savefileoutput=open(self.sceneFileName,"w")
            savefileoutput.write(xmlfileoutput.read())
            xmlfileoutput.close()
            savefileoutput.close()
            print "OpenAssembler scene saved at: "+str(self.sceneFileName)

    def OpenScene(self,ppanel, editor):
        fdiagback=tkFileDialog.Open(filetypes=[('OpenAssembler Scene','*.oas')], title="Open OpenAssembler Scene:").show()
        if fdiagback==():
            pass
        else:
            print "Loading file: "+ fdiagback
            mainprefs=self.OpenexamineSettings(fdiagback, "0000000")
            self.lastx=30
            self.lasty=30
            self.GlobalScale=.5
            self.origin_node=""
            self.origin_out=""
            self.origin_uni=""
            self.Create_RuntimeDBase()
            for n in range (0, len(mainprefs)):
                if mainprefs[n][1]=="StartFrame":
                    strtfrm= mainprefs[n][2]
                if mainprefs[n][1]=="EndFrame":
                    ndfrm= mainprefs[n][2]
                if mainprefs[n][1]=="Note":
                    nt= mainprefs[n][2]
            self.CreateGlobalPreferences(strtfrm, ndfrm, nt)
            self.RuntimeLines=[]
            self.startFrame.set(self.getFrameRange()[0])
            self.endFrame.set(self.getFrameRange()[1])
            self.currentFrame.set(self.startFrame.get())
            self.nodeInPreferences.set("OpenAssembler")
            ppanel.delete(ALL)
            self.controllerNodeHeader(ppanel)
            editor.delete(ALL)
            self.sceneFileName=fdiagback
            print "-> Global Scene Preferences loaded..."


            nodelist=self.OpenGetIDList(fdiagback)
            for n in range (0,len(nodelist)):
                defvars=self.OpensettingsforGeneration(fdiagback, nodelist[n],editor)
                self.PutNode(defvars)
                self.OpenCopyNode(fdiagback, nodelist[n])
                #self.RegisterRuntimeNode(defvars)
        # put nodes to screen

        # connect lines

        # new runtime base..

    def menuLine_init(self,TargetCanvas,preferencescanvas,editor):
        timelineFrame=Frame(TargetCanvas,height=11,width=220,bg="gray35")
        timelineFrame.grid_propagate(0)

        iofont = tkFont.Font ( family="mincho", size=6 )

        newb= Button (timelineFrame,width=3,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="New",font=iofont)
        newb.grid(row=1,column=1)
        newb.bind('<B1-ButtonRelease>',lambda event:self.NewScene(preferencescanvas,editor))

        o= Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Open",font=iofont)
        o.grid(row=1,column=2)
        o.bind('<B1-ButtonRelease>',lambda event:self.OpenScene(preferencescanvas,editor))

        savb=backfor=Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save",font=iofont)
        savb.grid(row=1,column=3)
        savb.bind('<B1-ButtonRelease>',lambda event:self.SaveScene())

        sas=onefor=Button(timelineFrame,width=10,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save as...",font=iofont)
        sas.grid(row=1,column=4)
        sas.bind('<B1-ButtonRelease>',lambda event:self.SaveAsScene())


        pref=Button(timelineFrame,width=11,bd=1,padx=5,pady=1,text="Preferences",font=iofont)
        pref.grid(row=1,column=5,padx=15)
        pref.bind('<Button-1>',lambda event:self.loadPreferences(preferencescanvas, "0000000"))


        TargetCanvas.create_window(5,10,window=timelineFrame,anchor='w')

    def _initMenuLineCanvas(self,TargetCanvas,TargetSide,preferencescanvas,editor):
        TargetCanvas = Canvas (self, width=540, height=15,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=1,rowspan=6,sticky=N)
        self.menuLine_init(TargetCanvas, preferencescanvas,editor)
        print "MenuLine Initialised."
        return TargetCanvas

    def _ForgetMenuLineCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "MenuLine Closed."

    def StartUpMenuLineCanvas(self,Name,Side,preferencescanvas,editor):
        TargetCanvas=self._initMenuLineCanvas(Name,Side,preferencescanvas,editor)
        return TargetCanvas