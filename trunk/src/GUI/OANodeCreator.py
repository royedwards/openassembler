#! /usr/bin/env python
#---------------------------------------------------------------------------------------------------------------------
#
#    Open Assembler Node Creator....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#---------------------------------------------------------------------------------------------------------------------
from Tkinter import *
from WindowFrames.NodeSliderBar import CanvasInitSliderBar
from GUI.Nodes.NodeList import NodeListCategoriser
from Dbase.DBaseManagement import SliderBarDbaseSupport
import tkFont


class _Application(Frame,CanvasInitSliderBar,NodeListCategoriser,SliderBarDbaseSupport):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=BOTH, expand=1)
        print "OpenAssembler Node Creator..."
        print "Owner: Laszlo Mates, laszlo.mates@gmail.com"
        self._createWidgets()

    def AddNodeButtons(self):
        TargetCanvas = Canvas (self, width=40, height=102,relief=GROOVE, cursor="sb_up_arrow", confine="false",bg="gray35",bd=2, scrollregion=(0,0,800,205))
        TargetCanvas.grid(row=130,column=0,rowspan=41)
        buttadd=Frame(TargetCanvas,height=100,width=38,bg="gray35")
        buttadd.grid_propagate(0)
        up= Button (buttadd,width=1,highlightcolor="gray35",bd=1,padx=10,pady=7,highlightbackground="gray35",text="+")
        up.grid(row=1,column=0)
        up.bind('<Button-1>',lambda event:self.upbutton())
        mid= Button(buttadd,width=1,highlightcolor="gray35",bd=1,padx=10,pady=7,highlightbackground="gray35",text="+")
        mid.grid(row=2,column=0)
        mid.bind('<Button-1>',lambda event:self.midbutton())
        butt= Button(buttadd,width=1,highlightcolor="gray35",bd=1,padx=10,pady=7,highlightbackground="gray35",text="+")
        butt.grid(row=3,column=0)
        #o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))
        TargetCanvas.create_window(5,5,window=buttadd,anchor='nw')
        return TargetCanvas

    def upbutton(self):
        self.Settingspanel()

    def midbutton(self):
        self.DeleteSliderBarNode("Image")

    def shownode(self,canvas,type):
        canvas.delete(ALL)
        VarInitReturn=[]
        VarInitReturn.append(canvas)
        VarInitReturn.append(str(00000))
        cord=(60,20)
        VarInitReturn.append(cord)
        VarInitReturn.append("MAIN")
        VarInitReturn.append("Mainfelirat")

        nodeshapestyle = "SHAPE02"
        topcolor="gray50"
        midcolor="gray60"
        botcolor="gray70"
        upperlabel="Test"
        Previewlabel="TST"
        Note="Ugyselaccik"
        inputs_out=[]
        inputs_out.append("In01")
        inputs_out.append("In02")
        outs_out=[]
        outs_out.append("Out01")
        outvalues=(str(nodeshapestyle),str(upperlabel),str(Previewlabel),str(Note),str(topcolor),str(midcolor),str(botcolor),(inputs_out),(outs_out))
        VarInitReturn.append(outvalues)
        self.PutNode(VarInitReturn)

    def Settingspanel(self):
        settingswindow = Toplevel(bg="gray35")
        settingswindow.wm_resizable(width=False ,height=False)
        settingswindow.title("Node Settings")
        placerowvar=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Row",anchor="w").grid(row=0,column=0)
        placerow = Entry(settingswindow,bg="gray35",width=10,textvariable=placerowvar,state="readonly")
        placerowvar.set("UP")
        placerow.grid(row=0,column=1)

        placecolumnvar=IntVar()
        Label(settingswindow,bg="gray35",width=10,text="Slot",anchor="w").grid(row=0,column=2)
        placecolumn = Entry(settingswindow,bg="gray35",width=10,textvariable=placecolumnvar,state="readonly")
        placecolumnvar.set(5)
        placecolumn.grid(row=0,column=3)

        name=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Name",anchor="w").grid(row=1,column=0)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=name)
        name.set("...")
        nameentry.grid(row=1,column=1)

        sname=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Short name",anchor="w").grid(row=1,column=2)
        sn = Entry(settingswindow,bg="gray35",width=10,textvariable=sname)
        sname.set("...")
        sn.grid(row=1,column=3)

        Label(settingswindow,bg="gray35",width=45,text="Note",anchor="c").grid(row=2,column=0, columnspan=4)
        notee=Text(settingswindow,width=45,height=5,bg="gray35",relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        notee.grid(row=3,column=0,columnspan=4)
        notee.insert(CURRENT, "SomeNote to here")

        Label(settingswindow,bg="gray35",width=45,text="Node-Shape-Style",anchor="c").grid(row=4,column=0, columnspan=4)
        shapetypes=Listbox(settingswindow,width=20,height=4,bg="gray35")
        shapetypes.grid(row=5,column=0,columnspan=2, sticky="nw")
        shapetypes.insert(END,"Normal")
        shapetypes.insert(END,"No-Input")
        shapetypes.insert(END,"No-Output")
        shapetypes.insert(END,"No-Input and No-Output")
        shapetypes.selection_set(0, 0)
        canv=Canvas(settingswindow,width=160,height=100,relief=GROOVE,bg="gray55",bd=2)
        canv.grid(row=5,column=2,columnspan=2,rowspan=3)
        self.shownode(canv,shapetypes.selection_get())
        shapetypes.bind("<ButtonRelease-1>",lambda event:self.shownode(canv,shapetypes.selection_get()))

        viewbutton=Button(settingswindow,text="View it !!!", padx=43,pady=5)
        viewbutton.grid(row=6,column=0,columnspan=2, sticky="w")

        topcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="TopColor",anchor="w").grid(row=0,column=4)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=topcolor)
        topcolor.set("gray70")
        nameentry.grid(row=1,column=4)

        bottcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="BottColor",anchor="w").grid(row=0,column=6)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=bottcolor)
        bottcolor.set("gray50")
        nameentry.grid(row=1,column=6)

        midcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="MidColor",anchor="w").grid(row=0,column=5)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=midcolor)
        midcolor.set("gray60")
        nameentry.grid(row=1,column=5)

        Label(settingswindow,bg="gray35",width=10,text="Outputs",anchor="c").grid(row=2,column=4)
        scrollout=Scrollbar(settingswindow)
        scrollout.grid(row=3,column=5,sticky=N+S+W)
        outs=Listbox(settingswindow,width=10,height=4,bg="gray35")
        outs.grid(row=3,column=4, sticky=N+S+W)
        outs.insert(END,"out01")
        outs.insert(END,"out02")
        outs.insert(END,"out03")
        outs.insert(END,"out04")
        outs.insert(END,"out05")
        outs.insert(END,"out06")
        outs.selection_set(0, 0)
        outs.config(yscrollcommand=scrollout.set)
        scrollout.config(command=outs.yview)
        newout=Button(settingswindow,text="NEW",width=4,pady=2)
        newout.grid(row=3,column=5,sticky="ne")
        editout=Button(settingswindow,text="EDIT",width=4,pady=2)
        editout.grid(row=3,column=5,sticky="e")
        delout=Button(settingswindow,text="DEL",width=4,pady=2)
        delout.grid(row=3,column=5,sticky="se")

        Label(settingswindow,bg="gray35",width=10,text="Settings",anchor="c").grid(row=4,column=4)
        scrollset=Scrollbar(settingswindow)
        scrollset.grid(row=5,column=5,sticky=N+S+W,rowspan=2)
        sets=Listbox(settingswindow,width=10,height=4,bg="gray35")
        sets.grid(row=5,column=4,rowspan=2,sticky=N+S+W)
        sets.insert(END,"set01")
        sets.insert(END,"set02")
        sets.insert(END,"set03")
        sets.insert(END,"set04")
        sets.insert(END,"set05")
        sets.insert(END,"set06")
        sets.selection_set(0, 0)
        sets.config(yscrollcommand=scrollset.set)
        scrollset.config(command=sets.yview)
        newset=Button(settingswindow,text="NEW",width=4,pady=2)
        newset.grid(row=5,column=5,sticky="ne")
        editset=Button(settingswindow,text="EDIT",width=4,pady=2)
        editset.grid(row=5,column=5,sticky="e")
        delset=Button(settingswindow,text="DEL",width=4,pady=2)
        delset.grid(row=5,column=5,sticky="se")

        scriptscroll=Scrollbar(settingswindow)
        scriptscroll.grid(row=9,column=5,sticky=N+S+W)
        textscript=Text(settingswindow,wrap=WORD,width=56,height=10,yscrollcommand=scriptscroll.set)
        textscript.grid(row=9, column=0,columnspan=6,sticky=N+W)
        scriptscroll.config(command=textscript.yview)

        scrsvar=StringVar()
        scryptent=Entry(settingswindow,width=18,textvariable=scrsvar)
        scrsvar.set("...")
        scryptent.grid(row=9, column=5,columnspan=2,sticky=N+E)

        genscr=Button(settingswindow,text="Generate",width=8,pady=2)
        genscr.grid(row=9,column=5,padx=25,pady=25,columnspan=2,rowspan=2,sticky="nw")
        openscr=Button(settingswindow,text="Open",width=8,pady=2)
        openscr.grid(row=9,column=5,padx=25,pady=50,columnspan=2,rowspan=2,sticky="nw")
        savescr=Button(settingswindow,text="Save",width=8,pady=2)
        savescr.grid(row=9,column=5,padx=25,columnspan=2,sticky="sw")

        mainsv=Button(settingswindow,text="SaveNode and Exit")
        mainsv.grid(row=10,columnspan=2,column=0)

        def canceller(win):
            win.destroy()
            return -1

        ccl=Button(settingswindow,text="Cancel")
        ccl.grid(row=10,column=6)
        ccl.bind("<Button-1>", lambda event:canceller(settingswindow))

    def Menuline(self):
        TargetCanvas = Canvas (self, width=585, height=20,relief=GROOVE, cursor="sb_up_arrow", confine="false",bg="gray35",bd=2, scrollregion=(0,0,800,205))
        TargetCanvas.grid(row=172,column=0,rowspan=41,columnspan=2)
        menuline=Frame(TargetCanvas,height=18,width=225,bg="gray35")
        menuline.grid_propagate(0)
        iofont = tkFont.Font ( family="mincho", size=8 )
        e=Entry(menuline,width=20,bd=1,font=iofont,textvariable=self.nodeinline,justify=LEFT,relief=GROOVE)
        e.grid(row=1,column=1)
        editb= Button (menuline,width=5,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Edit",font=iofont)
        editb.grid(row=1,column=2)
        #r.bind('<Button-1>',lambda event:(self.currentFrame.set(self.startFrame.get())))
        delb= Button(menuline,width=7,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Delete",fg="darkred",font=iofont)
        delb.grid(row=1,column=3,padx=25)
        #o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))
        TargetCanvas.create_window(5,13,window=menuline,anchor='w')
        return TargetCanvas

    def click(self,event,slider):
        tags = slider.gettags(CURRENT)
        if tags==():
            pass
        else:
            self.nodeinline.set(tags[1])

    def _createWidgets(self):
        self.lastx=30
        self.lasty=30
        self.GlobalScale=.5
        self.nodeinline=StringVar()
        slider=self.StartUpSliderBarCanvas("SliderBar", "bottom",None)
        slider.bind("<Double-Button-1>", lambda event: self.click(event,slider=slider))
        adder=self.AddNodeButtons()
        menulinne=self.Menuline()

app= _Application()
app.master.title("OpenAssembler Node Creator 0.01")
app.tk_strictMotif(1)
app.tk_setPalette("gray35")
app.master.wm_resizable(width=False ,height=False)
app.mainloop()
