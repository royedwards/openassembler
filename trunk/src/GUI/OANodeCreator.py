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

import tkFont


class _Application(Frame,CanvasInitSliderBar):
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
        #o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))

        butt= Button(buttadd,width=1,highlightcolor="gray35",bd=1,padx=10,pady=7,highlightbackground="gray35",text="+")
        butt.grid(row=3,column=0)
        #o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))

        TargetCanvas.create_window(5,5,window=buttadd,anchor='nw')
        return TargetCanvas

    def upbutton(self):
        self.Settingspanel()

    def Settingspanel(self):
        settingswindow = Toplevel(bg="gray35")
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
        canv=Canvas(settingswindow,width=200,height=100,relief=GROOVE,bg="gray55",bd=2)
        canv.grid(row=5,column=2,columnspan=2,rowspan=3)


        settingswindow.master.wm_resizable(width=False ,height=False)

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
        #slider.bind("<Button-1>", lambda event: self.click(event,slider=slider))
        adder=self.AddNodeButtons()
        menulinne=self.Menuline()



app= _Application()
app.master.title("OpenAssembler Node Creator 0.01")
app.tk_strictMotif(1)
app.tk_setPalette("gray35")
app.master.wm_resizable(width=False ,height=False)
app.mainloop()
