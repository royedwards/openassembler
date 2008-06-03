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
import os
from WindowFrames.NodeSliderBar import CanvasInitSliderBar
from GUI.Nodes.NodeList import NodeListCategoriser
from Dbase.DBaseManagement import SliderBarDbaseSupport
import tkFont
import tkFileDialog

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
        self.Settingspanel("",("up","new"))

    def midbutton(self):
        pass

    def writethesettingsbacktofile(self,name,sname,nodeshape,topc,midc,botc,ins,outs,scrpath,state,notee):
        collection=[]
        collection.append(name)
        collection.append(sname)
        if nodeshape.selection_get()=="Normal":
            collection.append("SHAPE02")
        else:
            print "You must select a node shape style!!!"
            return 0
        collection.append(topc)
        collection.append(midc)
        collection.append(botc)
        collection.append(ins)
        collection.append(outs)
        collection.append(scrpath)
        collection.append(notee)

        print state

        if state=="edit":
            #delete reginode
            #kiir ujnode
            pass
        else:
            #kiir ujnode
            #kiir rowlistbe
            pass


    def outputsettings(self,out_area,originallist):
        outputwindow = Toplevel(bg="gray35")
        outputwindow.wm_resizable(width=False ,height=False)
        outputwindow.title("Output Settings")
        paramname=StringVar()
        Label(outputwindow,bg="gray35",width=10,text="Output Name:",anchor="w").grid(row=0,column=0)
        param = Entry(outputwindow,bg="gray35",width=10,textvariable=paramname)
        paramname.set("name")
        param.grid(row=0,column=1)

        scrollout=Scrollbar(outputwindow)
        scrollout.grid(row=1,column=2,sticky=N+S+W)
        Label(outputwindow,bg="gray35",text="Parameter type:",anchor="c").grid(row=1,column=0)
        outypes=Listbox(outputwindow,height=4,bg="gray35")
        outypes.grid(row=1,column=1, sticky="nw")
        outypes.config(yscrollcommand=scrollout.set)
        scrollout.config(command=outypes.yview)
        outypes.insert(END,"Path")
        outypes.insert(END,"TextLine")
        outypes.insert(END,"MassText")
        outypes.insert(END,"Separator")
        outypes.insert(END,"SimpleNumber")
        outypes.insert(END,"Boolean")
        outypes.insert(END,"--None--")
        outypes.insert(END,"--None--")
        def okbuttrun(outputwindow,out_area,paramname,outypes,originallist):
            try:
                x=outypes.selection_get()
                if x!="Normal":
                    out_area.append((paramname.get(),outypes.selection_get()))
                    originallist.insert(END,str(paramname.get()))
                    outputwindow.destroy()
                else:
                    print "You must select a parameter type!!!!"
            except:
                print "You must select a parameter type!!!!"


        okbutt=Button(outputwindow,text="OK, save it!", padx=43,pady=5)
        okbutt.grid(row=2,column=0, sticky="w")
        try:
            okbutt.bind("<Button-1>",lambda event:okbuttrun(outputwindow,out_area,paramname,outypes,originallist))
        except:
            pass
        cancelbutton=Button(outputwindow,text="Cancel!!!", padx=43,pady=5)
        cancelbutton.grid(row=2,column=1, columnspan=2,sticky="e")
        try:
            cancelbutton.bind("<Button-1>",lambda event:outputwindow.destroy())
        except:
            pass

    def deloutput(self,outvar,listbox):
        for n in range(0,len(outvar)):
            try:
                if outvar[n][0]==listbox.selection_get():
                    del outvar[n]
                    listbox.delete(listbox.curselection()[0])
            except:
                pass

    def generatescript(self,textscript,snvar,name,settings_tmp,output_tmp):
        textscript.delete(1.0,END)
        textscript.insert(END,"###OpenAssembler Node python file###\n")
        textscript.insert(END,"\n")

        textscript.insert(END,str("class "+str(name.get())+"()\n"))
        textscript.insert(END,"#This is the main class to be imported\n")
        textscript.insert(END,"\n")
        textscript.insert(END,str("   def "+str(name.get())+"_main("))
        textscript.insert(END,str("output, "))
        for n in range (0,len(settings_tmp)):
            if n==(len(settings_tmp)-1):
                textscript.insert(END,str(str(settings_tmp[n][0])))
            else:
                textscript.insert(END,str(str(settings_tmp[n][0])+", "))
        textscript.insert(END,str(")\n"))
        textscript.insert(END,"      #This is the main definition to be called\n")
        textscript.insert(END,str("\n"))
        textscript.insert(END,str("      #--------------------\n"))
        textscript.insert(END,str("      #\n"))
        textscript.insert(END,str("      #   Your program code will be here\n"))
        textscript.insert(END,str("      #   If you keep the names, and the functions\n"))
        textscript.insert(END,str("      #   than everything have to be allright!!\n"))
        textscript.insert(END,str("      #\n"))
        textscript.insert(END,str("      #--------------------\n"))
        textscript.insert(END,str("\n"))

        for n in range (0,len(output_tmp)):
            textscript.insert(END,"      if "+"output==\""+str(output_tmp[n][0])+"\":\n")
            textscript.insert(END,"         return \"[put a variable here]\"\n")
            textscript.insert(END,str("\n"))
        fback=tkFileDialog.SaveAs(filetypes=[('Python file','*.py')], title="Save python file::",defaultextension="py").show()
        if os.path.exists(str(fback)):
            snvar.set(str(fback))
            outfilescript=open(fback,"w")
            outfilescript.write(str(textscript.get(1.0,END)))
            outfilescript.close()

    def func_savescript(self,scryptent,textscript):
        fback=tkFileDialog.SaveAs(filetypes=[('Python file','*.py')], title="Save python file::",defaultextension="py").show()
        if os.path.exists(str(fback)):
            snvar.set(str(fback))
            outfilescript=open(fback,"w")
            outfilescript.write(str(textscript.get(1.0,END)))
            outfilescript.close()
            scryptent.set(str(fback))

    def func_openscript(self,scryptent,textscript):
        fback=tkFileDialog.Open(filetypes=[('Python file','*.py')], title="Open python file::",defaultextension="py").show()
        if os.path.exists(str(fback)):
            textscript.delete(1.0,END)
            file=open(fback)
            rfile=file.read()
            textscript.insert(1.0, rfile)
            file.close()
            scryptent.set(str(fback))

    def inputsettings(self,out_area,originallist):
        outputwindow = Toplevel(bg="gray35")
        outputwindow.wm_resizable(width=False ,height=False)
        outputwindow.title("Settings editor")
        paramname=StringVar()
        Label(outputwindow,bg="gray35",width=10,text="Output Name:",anchor="w").grid(row=0,column=0)
        param = Entry(outputwindow,bg="gray35",width=10,textvariable=paramname)
        paramname.set("name")
        param.grid(row=0,column=1)

        scrollout=Scrollbar(outputwindow)
        scrollout.grid(row=1,column=2,sticky=N+S+W)
        Label(outputwindow,bg="gray35",text="Parameter type:",anchor="c").grid(row=1,column=0)
        outypes=Listbox(outputwindow,height=4,bg="gray35")
        outypes.grid(row=1,column=1, sticky="nw")
        outypes.config(yscrollcommand=scrollout.set)
        scrollout.config(command=outypes.yview)
        outypes.insert(END,"Path")
        outypes.insert(END,"TextLine")
        outypes.insert(END,"MassText")
        outypes.insert(END,"Separator")
        outypes.insert(END,"SimpleNumber")
        outypes.insert(END,"Boolean")
        outypes.insert(END,"--None--")
        outypes.insert(END,"--None--")
        def okbuttrun(outputwindow,out_area,paramname,outypes,originallist):
            try:
                x=outypes.selection_get()
                if x!="Normal":
                    out_area.append((paramname.get(),varriableconnect.get(),mvarriableconnect.get(),outypes.selection_get()))
                    originallist.insert(END,str(paramname.get()))
                    outputwindow.destroy()
                else:
                    print "You must select a parameter type!!!!"
            except:
                print "You must select a parameter type!!!!"
        varriableconnect=StringVar()
        ch=Checkbutton(outputwindow,text="Connectable?",variable=varriableconnect,onvalue="True",offvalue="False",anchor="w")
        ch.grid(row=2,column=0)
        varriableconnect.set("True")
        ch.var=varriableconnect

        mvarriableconnect=StringVar()
        mch=Checkbutton(outputwindow,text="MultipleConnections?",variable=mvarriableconnect,onvalue="True",offvalue="False",anchor="w")
        mch.grid(row=2,column=1)
        mvarriableconnect.set("False")
        mch.var=mvarriableconnect

        okbutt=Button(outputwindow,text="OK, save it!", padx=43,pady=5)
        okbutt.grid(row=3,column=0, sticky="w")
        try:
            okbutt.bind("<Button-1>",lambda event:okbuttrun(outputwindow,out_area,paramname,outypes,originallist))
        except:
            pass
        cancelbutton=Button(outputwindow,text="Cancel!!!", padx=43,pady=5)
        cancelbutton.grid(row=3,column=1, columnspan=2,sticky="e")
        try:
            cancelbutton.bind("<Button-1>",lambda event:outputwindow.destroy())
        except:
            pass



    def shownode(self,canvas,name,sname,nodeshape,topc,midc,botc,ins,outs):
        canvas.delete(ALL)
        VarInitReturn=[]
        VarInitReturn.append(canvas)
        VarInitReturn.append(str(00000))
        cord=(60,20)
        VarInitReturn.append(cord)
        VarInitReturn.append("MAIN")
        VarInitReturn.append(name)
        try:
            tmmp=nodeshape.selection_get()
        except:
            tmmp="Normal"
        if tmmp=="Normal":
            nodeshapestyle = "SHAPE02"
        else:
            nodeshapestyle = "SHAPE02"
            print "You must select a node shape to view it!!! Normal node shape is used in this case..."
        topcolor=topc
        midcolor=midc
        botcolor=botc
        upperlabel=name
        Previewlabel=sname
        Note="..."
        iinnss=[]
        for n in range(0,len(ins)):
            if ins[n][1]=="True":
                iinnss.append(ins[n])
        outvalues=(str(nodeshapestyle),str(upperlabel),str(Previewlabel),str(Note),str(topcolor),str(midcolor),str(botcolor),iinnss,outs)
        VarInitReturn.append(outvalues)
        self.PutNode(VarInitReturn)

    def Settingspanel(self, invars,posvars,state):
        if invars==[()]:
            return 1
        settingswindow = Toplevel(bg="gray35")
        settingswindow.wm_resizable(width=False ,height=False)
        settingswindow.title("Node Settings")
        placerowvar=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Row",anchor="w").grid(row=0,column=0)
        placerow = Entry(settingswindow,bg="gray35",width=10,textvariable=placerowvar,state="readonly")
        placerowvar.set(posvars[0])
        placerow.grid(row=0,column=1)

        placecolumnvar=IntVar()
        Label(settingswindow,bg="gray35",width=10,text="Slot",anchor="w").grid(row=0,column=2)
        placecolumn = Entry(settingswindow,bg="gray35",width=10,textvariable=placecolumnvar,state="readonly")
        placecolumnvar.set(posvars[1])
        placecolumn.grid(row=0,column=3)

        name=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Name",anchor="w").grid(row=1,column=0)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=name,state="readonly")
        name.set(invars[1])
        nameentry.grid(row=1,column=1)
        #def nameback():
           # pass
        #nameentry.bind("<Return>",lambda event: nameback())


        sname=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="Short name",anchor="w").grid(row=1,column=2)
        sn = Entry(settingswindow,bg="gray35",width=10,textvariable=sname)
        sname.set(invars[2])
        sn.grid(row=1,column=3)

        Label(settingswindow,bg="gray35",width=45,text="Note",anchor="c").grid(row=2,column=0, columnspan=4)
        notee=Text(settingswindow,width=45,height=5,bg="gray35",relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        notee.grid(row=3,column=0,columnspan=4)
        notee.insert(CURRENT, invars[3])

        Label(settingswindow,bg="gray35",width=45,text="Node-Shape-Style",anchor="c").grid(row=4,column=0, columnspan=4)
        shapetypes=Listbox(settingswindow,width=20,height=4,bg="gray35")
        shapetypes.grid(row=5,column=0,columnspan=2, sticky="nw")
        shapetypes.insert(END,"Normal")
        shapetypes.insert(END,"No-Input")
        shapetypes.insert(END,"No-Output")
        shapetypes.insert(END,"No-Input and No-Output")
        canv=Canvas(settingswindow,width=160,height=100,relief=GROOVE,bg="gray55",bd=2)
        canv.grid(row=5,column=2,columnspan=2,rowspan=3)
        if invars[0]=="SHAPE02":
            shapetypes.selection_set(0, 0)
        #shapetypes.bind("<ButtonRelease-1>",lambda event:self.shownode(canv,shapetypes.selection_get()))

        viewbutton=Button(settingswindow,text="View it !!!", padx=43,pady=5)
        viewbutton.grid(row=6,column=0,columnspan=2, sticky="w")
        try:
            viewbutton.bind("<Button-1>",lambda event:self.shownode(canv,name.get(),sname.get(),shapetypes,topcolor.get(),midcolor.get(),bottcolor.get(),settings_tmp,output_tmp))
        except:
            pass

        topcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="TopColor",anchor="w").grid(row=0,column=4)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=topcolor)
        topcolor.set(invars[4])
        nameentry.grid(row=1,column=4)

        bottcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="BottColor",anchor="w").grid(row=0,column=6)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=bottcolor)
        bottcolor.set(invars[6])
        nameentry.grid(row=1,column=6)

        midcolor=StringVar()
        Label(settingswindow,bg="gray35",width=10,text="MidColor",anchor="w").grid(row=0,column=5)
        nameentry = Entry(settingswindow,bg="gray35",width=10,textvariable=midcolor)
        midcolor.set(invars[5])
        nameentry.grid(row=1,column=5)

        output_tmp=[]
        Label(settingswindow,bg="gray35",width=10,text="Outputs",anchor="c").grid(row=2,column=4)
        scrollout=Scrollbar(settingswindow)
        scrollout.grid(row=3,column=5,sticky=N+S+W)
        outs=Listbox(settingswindow,width=10,height=4,bg="gray35")
        outs.grid(row=3,column=4, sticky=N+S+W)
        for n in range(0,len(invars[8])):
            nam= invars[8][n][0]
            typ= invars[8][n][1]
            output_tmp.append((nam,typ))
        for n in range(0,len(output_tmp)):
            outs.insert(END,output_tmp[n][0])
        outs.config(yscrollcommand=scrollout.set)
        scrollout.config(command=outs.yview)
        newout=Button(settingswindow,text="NEW",width=4,pady=2)
        newout.grid(row=3,column=5,sticky="ne")
        newout.bind("<Button-1>", lambda event:self.outputsettings(output_tmp,outs))
        delout=Button(settingswindow,text="DEL",width=4,pady=2)
        delout.grid(row=3,column=5,sticky="se")
        delout.bind("<Button-1>", lambda event:self.deloutput(output_tmp,outs))

        settings_tmp=[]
        Label(settingswindow,bg="gray35",width=10,text="Settings",anchor="c").grid(row=4,column=4)
        scrollset=Scrollbar(settingswindow)
        scrollset.grid(row=5,column=5,sticky=N+S+W,rowspan=2)
        sets=Listbox(settingswindow,width=10,height=4,bg="gray35")
        sets.grid(row=5,column=4,rowspan=2,sticky=N+S+W)
        for n in range(0,len(invars[7])):
            param0=invars[7][n][0]
            param1=invars[7][n][1]
            param2=invars[7][n][2]
            param3=invars[7][n][3]
            settings_tmp.append((param0,param1,param2,param3))
        for n in range(0,len(settings_tmp)):
            sets.insert(END,settings_tmp[n][0])
        sets.config(yscrollcommand=scrollset.set)
        scrollset.config(command=sets.yview)
        newset=Button(settingswindow,text="NEW",width=4,pady=2)
        newset.grid(row=5,column=5,sticky="ne")

        newset.bind("<Button-1>", lambda event:self.inputsettings(settings_tmp,sets))
        delset=Button(settingswindow,text="DEL",width=4,pady=2)
        delset.grid(row=5,column=5,sticky="se")
        delset.bind("<Button-1>", lambda event:self.deloutput(settings_tmp,sets))

        scriptscroll=Scrollbar(settingswindow)
        scriptscroll.grid(row=9,column=5,sticky=N+S+W)
        textscript=Text(settingswindow,wrap=WORD,width=56,height=10,yscrollcommand=scriptscroll.set)
        textscript.grid(row=9, column=0,columnspan=6,sticky=N+W)
        scriptscroll.config(command=textscript.yview)

        scrsvar=StringVar()
        scryptent=Entry(settingswindow,width=18,textvariable=scrsvar)
        scrsvar.set(invars[9])
        scryptent.grid(row=9, column=5,columnspan=2,sticky=N+E)

        if os.path.exists(str(invars[9])):
            textscript.delete(1.0,END)
            file=open(invars[9])
            textscript.insert(1.0, file)
            file.close()

        genscr=Button(settingswindow,text="Generate",width=8,pady=2)
        genscr.grid(row=9,column=5,padx=25,pady=25,columnspan=2,rowspan=2,sticky="nw")
        genscr.bind("<B1-ButtonRelease>", lambda event:self.generatescript(textscript,scrsvar,name,settings_tmp,output_tmp))

        openscr=Button(settingswindow,text="Open",width=8,pady=2)
        openscr.grid(row=9,column=5,padx=25,pady=50,columnspan=2,rowspan=2,sticky="nw")
        openscr.bind("<B1-ButtonRelease>", lambda event:self.func_openscript(scrsvar, textscript))

        savescr=Button(settingswindow,text="Save",width=8,pady=2)
        savescr.grid(row=9,column=5,padx=25,columnspan=2,sticky="sw")
        savescr.bind("<B1-ButtonRelease>", lambda event:self.func_savescript(scrsvar, textscript))

        mainsv=Button(settingswindow,text="SaveNode and Exit")
        mainsv.grid(row=10,columnspan=2,column=0)
        mainsv.bind("<Button-1>", lambda event:self.writethesettingsbacktofile(name.get(),sname.get(),shapetypes,topcolor.get(),midcolor.get(),bottcolor.get(),settings_tmp,output_tmp,scrsvar.get(),state,notee.get(1.0,END)))

        def canceller(win):
            win.destroy()
            return -1

        ccl=Button(settingswindow,text="Cancel")
        ccl.grid(row=10,column=6)
        ccl.bind("<Button-1>", lambda event:canceller(settingswindow))

    def editbutt(self):
        self.Settingspanel(self.getNodeSettings(self.nodeinline.get()), self.getRowAndPosition(self.nodeinline.get()),"edit")
        #print self.getNodeSettings(self.nodeinline.get())

    def Menuline(self):
        TargetCanvas = Canvas (self, width=585, height=20,relief=GROOVE, cursor="sb_up_arrow", confine="false",bg="gray35",bd=2, scrollregion=(0,0,800,205))
        TargetCanvas.grid(row=172,column=0,rowspan=41,columnspan=2)
        menuline=Frame(TargetCanvas,height=18,width=225,bg="gray35")
        menuline.grid_propagate(0)
        iofont = tkFont.Font ( family="mincho", size=8 )
        e=Label(menuline,width=20,bd=1,font=iofont,textvariable=self.nodeinline,justify=LEFT,relief=GROOVE,state='normal')
        e.grid(row=1,column=1)
        editb= Button (menuline,width=5,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Edit",font=iofont)
        editb.grid(row=1,column=2)
        editb.bind('<Button-1>',lambda event:self.editbutt())
        delb= Button(menuline,width=7,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="Delete",fg="darkred",font=iofont)
        delb.grid(row=1,column=3,padx=25)
        delb.bind('<Button-1>',lambda event:self.DeleteSliderBarNode(self.nodeinline.get()))
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
