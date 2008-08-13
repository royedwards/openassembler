from Tkinter import *
from GUI.WindowFrames.PreferencePanel import LoadPreferences, CanvasInitPreferencePanel
from Dbase.DBaseManagement import RuntimeNodeRegister, openScene, PreferencesManagement
from GUI.Nodes.NodeList import NodeListCategoriser
from GUI.Nodes.ConnectionLine import ConnectLine


import tkFont
import tkFileDialog


class CanvasInitMenuLine(LoadPreferences,CanvasInitPreferencePanel,RuntimeNodeRegister,openScene,PreferencesManagement,NodeListCategoriser,ConnectLine):

    def NewScene(self,ppanel,editor):
        self.lastx=30
        self.lasty=30
        self.GlobalScale=.75
        self.origin_node=""
        self.origin_out=""
        self.origin_uni=""
        self.Create_RuntimeDBase()
        self.CreateGlobalPreferences(1, 100, "Basic scene setup...","...")
        self.RuntimeLines=[]
        self.startFrame.set(self.getFrameRange()[0])
        self.endFrame.set(self.getFrameRange()[1])
        self.currentFrame.set(self.startFrame.get())
        self.eott.set("...")
        self.nodeInPreferences.set("OpenAssembler")
        ppanel.delete(ALL)
        self.controllerNodeHeader(ppanel)
        editor.delete(ALL)
        self.sceneFileName=""

    def SaveAsScene(self,editor):
            fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                print "Save canceled..."
            else:
		self.writeBackNodePositions(editor)
                savefileoutput=open(fdiagback,"w")
                savefileoutput.write(self.rt)
                savefileoutput.close()
                self.sceneFileName=str(fdiagback)
                print "OpenAssembler scene saved at: "+str(fdiagback)

    def SaveScene(self,editor):
        if self.sceneFileName=="":
            fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],defaultextension="oas",title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                print "Save canceled..."
            else:
		self.writeBackNodePositions(editor)
                savefileoutput=open(fdiagback,"w")
                savefileoutput.write(self.rt)
                savefileoutput.close()
                self.sceneFileName=str(fdiagback)
                print "OpenAssembler scene saved at: "+str(fdiagback)
        else:
            savefileoutput=open(self.sceneFileName,"w")
            savefileoutput.write(self.rt)
            savefileoutput.close()
            print "OpenAssembler scene saved at: "+str(self.sceneFileName)

    def OpenScene(self,ppanel, editor):
        fdiagback=tkFileDialog.Open(filetypes=[('OpenAssembler Scene','*.oas')], title="Open OpenAssembler Scene:",defaultextension="oas").show()
        if (fdiagback=="") or (fdiagback==()):
            pass
        else:
            print "Loading file: "+ fdiagback
            mainprefs=self.OpenexamineSettings(fdiagback, "0000000")
            self.lastx=30
            self.lasty=30
            self.GlobalScale=.75
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
                if mainprefs[n][1]=="EndOfTheTree":
                    eo= mainprefs[n][2]
            self.CreateGlobalPreferences(strtfrm, ndfrm, nt, eo)
            self.RuntimeLines=[]
            self.startFrame.set(self.getFrameRange()[0])
            self.endFrame.set(self.getFrameRange()[1])
            self.currentFrame.set(self.startFrame.get())
            self.eott.set(str(eo))
            self.nodeInPreferences.set("OpenAssembler")
            ppanel.delete(ALL)
            self.controllerNodeHeader(ppanel)
            editor.delete(ALL)
            self.sceneFileName=fdiagback
            print "-> Global Scene Preferences loaded..."


            nodelist=self.OpenGetIDList(fdiagback)
            for n in range (0,len(nodelist)):
                if self.OpenGetFuncType(fdiagback, nodelist[n])=="NodeConnectionLine":
                    pass
                else:
                    defvars=self.OpensettingsforGeneration(fdiagback, nodelist[n],editor)
                    self.PutNode(defvars)
                    self.OpenCopyNode(fdiagback, nodelist[n])
                    startText=str(self.OpenGetFuncType(fdiagback, nodelist[n]))+str(nodelist[n])
                    nam=self.getNodeName(nodelist[n])
                    if startText != nam:
                        editor.itemconfig(startText, text=nam,tag=(str(nodelist[n]),'UPPERLABEL',str(self.OpenGetFuncType(fdiagback, nodelist[n])),nam,(str(startText)+"select")))
                        editor.dtag(startText)
                    else:
                        pass

            print "-> Nodes loaded..."

            for n in range(0,len(nodelist)):
                if self.OpenGetFuncType(fdiagback, nodelist[n])=="NodeConnectionLine":
                    lingen=self.OpenGetgenerationDataforLines(fdiagback, nodelist[n])
                    self.ChangeSettings(lingen[3], "Data", lingen[4], "...")
                else:
                    pass

            for n in range(0,len(nodelist)):
                if self.OpenGetFuncType(fdiagback, nodelist[n])=="NodeConnectionLine":
                    lingen=self.OpenGetgenerationDataforLines(fdiagback, nodelist[n])
                    self.DrawNewLine(editor, lingen[0], lingen[1], lingen[2], lingen[3], lingen[4], lingen[5])
                else:
                    pass
            print "-> Connections loaded..."


    def menuLine_init(self,TargetCanvas,preferencescanvas,editor):
        timelineFrame=Frame(TargetCanvas,height=22,width=340,bg="gray35")
        timelineFrame.grid_propagate(0)

        iofont = tkFont.Font ( family="Helvetica" , size=10 )

        newb= Button (timelineFrame,width=3,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="New",font=iofont)
        newb.grid(row=1,column=1)
        newb.bind('<B1-ButtonRelease>',lambda event:self.NewScene(preferencescanvas,editor))

        o= Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Open",font=iofont)
        o.grid(row=1,column=2)
        o.bind('<B1-ButtonRelease>',lambda event:self.OpenScene(preferencescanvas,editor))

        savb=backfor=Button(timelineFrame,width=4,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save",font=iofont)
        savb.grid(row=1,column=3)
        savb.bind('<B1-ButtonRelease>',lambda event:self.SaveScene(editor))

        sas=onefor=Button(timelineFrame,width=10,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Save as...",font=iofont)
        sas.grid(row=1,column=4)
        sas.bind('<B1-ButtonRelease>',lambda event:self.SaveAsScene(editor))


        pref=Button(timelineFrame,width=11,bd=1,padx=5,pady=1,text="Preferences",font=iofont)
        pref.grid(row=1,column=5,padx=15)
        pref.bind('<Button-1>',lambda event:self.loadPreferences(preferencescanvas, "0000000"))


        TargetCanvas.create_window(8,18,window=timelineFrame,anchor='w')

    def _initMenuLineCanvas(self,TargetCanvas,TargetSide,preferencescanvas,editor):
        TargetCanvas = Canvas (self, width=1280, height=30,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
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
