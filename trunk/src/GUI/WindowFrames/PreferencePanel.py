#------------------------------------------------------------------------------------------------------------------------------------
#
#    Preference plane for OpenAssembler. 
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
from Dbase.DBaseManagement import PreferencesManagement
import tkFont
import tkFileDialog



class LoadPreferences(PreferencesManagement):

    def controllerBoolean(self,TargetCanvas,Node,pos,varriable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        ch=Checkbutton(fr,text=parametername,variable=varriable,onvalue="True",offvalue="False",state=sstate,font=iofont,anchor="w", fg=conchk,width=25,height=0)
        ch.grid()
        ch.var=varriable
        ch.bind('<B1-ButtonRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, varriable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerSeparator(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        plen=len(parametername)
        ta=int((50-plen)/2)
        tach=""
        for n in range(0,ta):
            tach=tach+"-"
        Label(fr,text=tach+parametername+tach,anchor="nw",width=28,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=0)
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerPassThrou(self,pos):
        return pos

    def controllerColor(self,TargetCanvas,Node,pos,v1,v2,v3,parametername,d1,d2,d3,conchk):
	sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v1,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW,padx=0)
        ee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v2,highlightbackground="gray35",justify=LEFT)
        ee.grid(row=0,column=2,sticky=SW,padx=1)
	eee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v3,highlightbackground="gray35",justify=LEFT)
        eee.grid(row=0,column=3,sticky=SW,padx=1)
	v1.set(d1)
	v2.set(d2)
	v3.set(d3)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	ee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	eee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerVectorPoint(self,TargetCanvas,Node,pos,v1,v2,v3,parametername,d1,d2,d3,conchk):
	sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v1,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW,padx=2)
        ee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v2,highlightbackground="gray35",justify=LEFT)
        ee.grid(row=0,column=2,sticky=SW,padx=1)
	eee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v3,highlightbackground="gray35",justify=LEFT)
        eee.grid(row=0,column=3,sticky=SW,padx=1)
	v1.set(d1)
	v2.set(d2)
	v3.set(d3)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	ee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	eee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=20,bg="gray55",relief="groove",bd=1,state=sstate,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerMatrix(self,TargetCanvas,Node,pos,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,parametername,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,conchk):
	sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=11,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
	
        e=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v1,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW,padx=3)
        ee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v2,highlightbackground="gray35",justify=LEFT)
        ee.grid(row=0,column=2,sticky=SW,padx=1)
	eee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v3,highlightbackground="gray35",justify=LEFT)
        eee.grid(row=0,column=3,sticky=SW,padx=1)
	eeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v4,highlightbackground="gray35",justify=LEFT)
        eeee.grid(row=0,column=4,sticky=SW,padx=1)
	
        re=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v5,highlightbackground="gray35",justify=LEFT)
        re.grid(row=1,column=1,sticky=SW,padx=3)
        ree=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v6,highlightbackground="gray35",justify=LEFT)
        ree.grid(row=1,column=2,sticky=SW,padx=1)
	reee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v7,highlightbackground="gray35",justify=LEFT)
        reee.grid(row=1,column=3,sticky=SW,padx=1)
	reeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v8,highlightbackground="gray35",justify=LEFT)
        reeee.grid(row=1,column=4,sticky=SW,padx=1)
	
        te=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v9,highlightbackground="gray35",justify=LEFT)
        te.grid(row=2,column=1,sticky=SW,padx=3)
        tee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v10,highlightbackground="gray35",justify=LEFT)
        tee.grid(row=2,column=2,sticky=SW,padx=1)
	teee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v11,highlightbackground="gray35",justify=LEFT)
        teee.grid(row=2,column=3,sticky=SW,padx=1)
	teeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v12,highlightbackground="gray35",justify=LEFT)
        teeee.grid(row=2,column=4,sticky=SW,padx=1)
	
        tre=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v13,highlightbackground="gray35",justify=LEFT)
        tre.grid(row=3,column=1,sticky=SW,padx=3)
        tree=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v14,highlightbackground="gray35",justify=LEFT)
        tree.grid(row=3,column=2,sticky=SW,padx=1)
	treee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v15,highlightbackground="gray35",justify=LEFT)
        treee.grid(row=3,column=3,sticky=SW,padx=1)
	treeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v16,highlightbackground="gray35",justify=LEFT)
        treeee.grid(row=3,column=4,sticky=SW,padx=1)
	
	
	v1.set(d1)
	v2.set(d2)
	v3.set(d3)
	v4.set(d4)
	v5.set(d5)
	v6.set(d6)
	v7.set(d7)
	v8.set(d8)
	v9.set(d9)
	v10.set(d10)
	v11.set(d11)
	v12.set(d12)
	v13.set(d13)
	v14.set(d14)
	v15.set(d15)
	v16.set(d16)
		
	
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        ee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        eee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        eeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        re.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        ree.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        reee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        reeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        te.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        tee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        teee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        teeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        tre.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        tree.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        treee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        treeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+100

    def controllerMassText(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Text(fr,font=iofont,width=30,height=8,bg="gray55",state=sstate,relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        e.grid(row=1,column=0,sticky=N)
        e.insert(CURRENT, defaultvalue)
        b=Button (fr,width=30,highlightcolor="gray35",bd=1,height=0,state=sstate,padx=0,pady=0,highlightbackground="gray35",text="Save",font=iofont)
        b.grid(row=2,column=0)
        b.bind('<B1-ButtonRelease>', lambda event: self._masTextSave(Node,e,parametername))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+210

    def _masTextSave(self,Node,textzone,parametername):
        a=str(textzone.get(1.0,END))[:-1]
        self.ChangeSettings(Node, "Data",parametername, a)

    def controllerSceneNote(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Text(fr,font=iofont,width=30,height=8,bg="gray55",relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        e.grid(row=1,column=0,sticky=N)
        e.insert(CURRENT, defaultvalue)
        b=Button (fr,width=30,highlightcolor="gray35",bd=1,height=0,padx=0,pady=0,highlightbackground="gray35",text="Save",font=iofont)
        b.grid(row=2,column=0)
        b.bind('<B1-ButtonRelease>', lambda event: self._sceneNoteSave(Node,e))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+210

    def _sceneNoteSave(self,Node,textzone):
        a=str(textzone.get(1.0,END))[:-1]
        self.ChangeNote(Node, a)

    def numval(self,event,v):
            if event.char in "1234567890.,":
                pass
            elif event.keycode==36:
                pass
            else:
                q=v.get()
                w=str(q)
                er=w[:-1]
                v.set(er)

    def controllerNumberSimple(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=15,bg="gray55",state=sstate,relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        #e.bind('<KeyRelease>',lambda event: self.numval(event,variable))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def SFGlobalnter(self,variable,Node,parametername,conchk):
        if int(variable.get())<int(self.endFrame.get()):
            self.ChangeSettings(Node, "Data",parametername, variable.get())
            self.startFrame.set(variable.get())
        else:
            self.ChangeSettings(Node, "Data",parametername, (self.endFrame.get()-1))
            self.startFrame.set((self.endFrame.get()-1))
            variable.set((self.endFrame.get()-1))

    def SFGlobal(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=15,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.SFGlobalnter(variable,Node,parametername))
        e.bind('<KeyRelease>',lambda event: self.numval(event,variable))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def EFGlobalnter(self,variable,Node,parametername,conchk):
        if int(variable.get())>int(self.startFrame.get()):
            self.ChangeSettings(Node, "Data",parametername, variable.get())
            self.endFrame.set(variable.get())
        else:
            self.ChangeSettings(Node, "Data",parametername, (self.startFrame.get()+1))
            self.endFrame.set((self.startFrame.get()+1))
            variable.set((self.startFrame.get()+1))

    def EOTTGlobalnter(self,variable,Node,parametername,conchk):
        self.ChangeSettings(Node, "Data",parametername, variable.get())
        self.eott.set(variable.get())

    def EOTTGlobal(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=15,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.EOTTGlobalnter(variable,Node,parametername))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def EFGlobal(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=15,bg="gray55",relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<Return>',lambda event:self.EFGlobalnter(variable,Node,parametername))
        e.bind('<KeyRelease>',lambda event: self.numval(event,variable))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30


    def openFile(self,TargetCanvas,Node, parametername, variable):
        fdiagback=tkFileDialog.Open(filetypes=[('Anyfile','*')]).show()
        if str(fdiagback)==(""):
            pass
        else:
            variable.set(fdiagback)
            self.ChangeSettings(Node,"Data", parametername, variable.get())
            self.loadPreferences(TargetCanvas,Node)
        return

    def controllerPath(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=9,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0)
        e=Entry(fr,font=iofont,width=14,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=N,padx=2)
        variable.set(defaultvalue)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        b=Button (fr,width=6,highlightcolor="gray35",bd=1,height=0,padx=0,state=sstate,pady=0,highlightbackground="gray35",text="Open",font=iofont)
        b.grid(row=0,column=3)
        b.bind('<B1-ButtonRelease>', lambda event:self.openFile(TargetCanvas,Node, parametername, variable))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

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
        height=35
        string=[]
        inter=[]
        db=[]
        conchk="gray90"
        for n in range(0,len(datas)):
	        conchk="gray90"
		datatogive=datas[n][2]
                if str(datatogive)[:1]==":":
		  datatogive=str(str(datas[n][2]).split("#",1)[1])
	    	  conchk="darkred"
		else:
		  datatogive=datas[n][2]
		        
        	if datas[n][3]=="Path" or datas[n][3]=="file":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerPath(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="color":
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
            	    m=len(string)
		    de=str(datatogive).strip(";").split(";")
		    if len(de)<3:
		    	de=["0","0","0"]
		    height=self.controllerColor(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],datas[n][1],de[0],de[1],de[2],conchk)

        	elif datas[n][3]=="vector" or datas[n][3]=="point" or datas[n][3]=="vvector" or datas[n][3]=="avector" or datas[n][3]=="vpoint" or datas[n][3]=="apoint" or datas[n][3]=="avvector":
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
            	    m=len(string)
		    de=str(datatogive).strip(";").split(";")
		    if len(de)<3:
		    	de=["0","0","0"]
		    height=self.controllerVectorPoint(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],datas[n][1],de[0],de[1],de[2],conchk)

        	elif datas[n][3]=="TextLine" or datas[n][3]=="string":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerTextLine(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="sceneNote":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerSceneNote(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="matrix" or datas[n][3]=="amatrix":
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    m=len(string)
		    dd=str(datatogive).strip(";").split(";")
		    if len(dd)<16:
		    	dd=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]		    
            	    height=self.controllerMatrix(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],string[m-4],string[m-5],string[m-6],string[m-7],string[m-8],string[m-9],string[m-10],string[m-11],string[m-12],string[m-13],string[m-14],string[m-15],string[m-16],datas[n][1],dd[0],dd[1],dd[2],dd[3],dd[4],dd[5],dd[6],dd[7],dd[8],dd[9],dd[10],dd[11],dd[12],dd[13],dd[14],dd[15],conchk)

        	elif datas[n][3]=="MassText":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerMassText(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="Separator":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerSeparator(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif (datas[n][3]=="SimpleNumber") or (datas[n][3]=="int") or (datas[n][3]=="vfloat") or (datas[n][3]=="aint") or (datas[n][3]=="afloat") or (datas[n][3]=="avfloat") or (datas[n][3]=="vint") or (datas[n][3]=="float"):
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerNumberSimple(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="SFGlobal":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.SFGlobal(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="EFGlobal":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.EFGlobal(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="endTree":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.EOTTGlobal(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="geo" or datas[n][3]=="curve" or datas[n][3]=="surface" or datas[n][3]=="mesh" or datas[n][3]=="amesh":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerPassThrou(height)

        	elif datas[n][3]=="Boolean" or datas[n][3]=="bool":
            	    inter.append(StringVar())
            	    z=len(inter)
            	    height=self.controllerBoolean(TargetCanvas,Node,height,inter[z-1],datas[n][1],None,conchk)
            	    if str(datatogive)=="True":
            	        inter[z-1].set("True")
            	    else:
            	        inter[z-1].set("False")
        	else:
            	    print "This type controller handler not available: "+str(datas[n][3])


class CanvasInitPreferencePanel:

    def controllerNodeHeader(self,TargetCanvas):
        fr=Frame(TargetCanvas,bg="gray35")
        fr.grid()
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize)+2 )
        label=Label(fr,textvariable=self.nodeInPreferences,anchor="nw",width=29,font=iofont,bg="gray15",relief="flat")
        label.grid()
        TargetCanvas.create_window(5,5,window=fr,anchor="nw",tag="header")

    def _initPreferencePanelCanvas(self,TargetSide):
        TargetCanvas = Canvas (self, width=300, height=792,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=2,rowspan=129,sticky=N)
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
