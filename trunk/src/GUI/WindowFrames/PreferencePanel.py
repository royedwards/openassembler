from Tkinter import *
from Dbase.DBaseManagement import PreferencesManagement
import tkFont
import tkFileDialog



class LoadPreferences(PreferencesManagement):

    def controllerBoolean(self,TargetCanvas,Node,pos,varriable,parametername,defaultvalue):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        ch=Checkbutton(fr,text=parametername,variable=varriable,onvalue="True",offvalue="False",font=iofont,anchor="w",width=25,height=0)
        ch.grid()
        ch.var=varriable
        ch.bind('<B1-ButtonRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, varriable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+15

    def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35").grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=28,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=1,column=0,sticky=N,pady=0)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+35

    def controllerMassText(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35").grid(row=0,column=0,pady=2)
        e=Text(fr,font=iofont,width=28,height=26,bg="gray55",relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        e.grid(row=1,column=0,sticky=N)
        e.insert(CURRENT, defaultvalue)
        b=Button (fr,width=28,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Save",font=iofont)
        b.grid(row=2,column=0)
        b.bind('<B1-ButtonRelease>', lambda event: self._masTextSave(Node,e))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+35

    def _masTextSave(self,Node,textzone):
        a=str(textzone.get(1.0,END))[:-1]
        self.ChangeNote(Node, str(a))


    def controllerNumberSimple(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35").grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=28,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=1,column=0,sticky=N,pady=0)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+35


    def openFile(self,TargetCanvas,Node, parametername, variable):
        fdiagback=tkFileDialog.Open(filetypes=[('Anyfile','*')]).show()
        if str(fdiagback)==(""):
            pass
        else:
            variable.set(fdiagback)
            self.ChangeSettings(Node,"Data", parametername, variable.get())
            self.loadPreferences(TargetCanvas,Node)
        return

    def controllerPath(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35").grid(row=0,column=0,columnspan=2,pady=2)
        e=Entry(fr,font=iofont,width=23,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=1,column=0,sticky=N,pady=0)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        b=Button (fr,width=4,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Open",font=iofont)
        b.grid(row=1,column=1)
        b.bind('<B1-ButtonRelease>', lambda event:self.openFile(TargetCanvas,Node, parametername, variable))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+35

    def loadNote(self,TargetCanvas,Node):
        TargetCanvas.delete(ALL)
        self.controllerNodeHeader(TargetCanvas)
        def killer(self):
            pass
        TargetCanvas.bind("<B1-Motion>",killer)
        datas=self.getNodeNote(Node)
        self.nodeInPreferences.set(datas[0])
        height=20
        string=[]
        self.controllerMassText(TargetCanvas, Node, 20, None, "Note", datas[1])

    def resetPreferencePlane(self,TargetCanvas):
        TargetCanvas.delete(ALL)
        self.controllerNodeHeader(TargetCanvas)
        self.nodeInPreferences.set("OpenAssembler")
        def killer(self):
            pass
        TargetCanvas.bind("<B1-Motion>",killer)

    def loadPreferences(self,TargetCanvas,Node):
        TargetCanvas.delete(ALL)
        self.controllerNodeHeader(TargetCanvas)
        def handlerRelease(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B1-ButtonRelease>", handlerRelease)

        def handlerB1Move(event, self=self, TargetCanvas=TargetCanvas):
            if (TargetCanvas.bbox(ALL)[3]>=(10-(event.y - self.lasty))) and (TargetCanvas.bbox(ALL)[1]<=(260-(event.y - self.lasty))):
                TargetCanvas.move (ALL,0, event.y - self.lasty)
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B1-Motion>",handlerB1Move)
        datas=self.examineSettings(Node)
        self.nodeInPreferences.set(datas[0][0])
        height=20
        string=[]
        inter=[]
        for n in range(0,len(datas)):
            if datas[n][3]=="Path":
                string.append(StringVar())
                m=len(string)
                height=self.controllerPath(TargetCanvas,Node,height,string[m-1],datas[n][1],datas[n][2])

            if datas[n][3]=="TextLine":
                string.append(StringVar())
                m=len(string)
                height=self.controllerNumberSimple(TargetCanvas,Node,height,string[m-1],datas[n][1],datas[n][2])

            if datas[n][3]=="SimpleNumber":
                db.append(DoubleVar())
                m=len(db)
                height=self.controllerTextLine(TargetCanvas,Node,height,db[m-1],datas[n][1],datas[n][2])

            if datas[n][3]=="Boolean":
                inter.append(StringVar())
                z=len(inter)
                height=self.controllerBoolean(TargetCanvas,Node,height,inter[z-1],datas[n][1],None)
                if str(datas[n][2])=="True":
                    inter[z-1].set("True")
                else:
                    inter[z-1].set("False")
            else:
                pass


class CanvasInitPreferencePanel:

    def controllerNodeHeader(self,TargetCanvas):
        fr=Frame(TargetCanvas,bg="gray35")
        fr.grid()
        iofont = tkFont.Font ( family="Keyboard", size=6 )
        label=Label(fr,textvariable=self.nodeInPreferences,anchor="nw",width=28,font=iofont,bg="gray15",relief="flat")
        label.grid()
        TargetCanvas.create_window(5,5,window=fr,anchor="nw",tag="header")

    def _initPreferencePanelCanvas(self,TargetSide):
        TargetCanvas = Canvas (self, width=150, height=267,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=61,column=2,rowspan=110,sticky=S)
        def handlerB1Click(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<Button-1>", handlerB1Click)
        self.controllerNodeHeader(TargetCanvas)
        print "PreferencePanel Initialised."
        return TargetCanvas

    def _ForgetPreferencePanelCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "PreferencePanel Closed."

    def StartUpPreferencePanelCanvas(self,Name,Side):
        TargetCanvas=self._initPreferencePanelCanvas(Side)
        return TargetCanvas