#------------------------------------------------------------------------------------------------------------------------------------
#
#    Timeline for OpenAssembler. 
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
from MouseEvents import NodeEditorCanvasEvents
import tkFont


class CanvasInitTimeLine(NodeEditorCanvasEvents):

    def delItemPress(self,editorcanvas):
        editorcanvas.configure(cursor="pirate")

    def endTreePress(self,editorcanvas):
        editorcanvas.configure(cursor="cross")

    def timeLine_init(self,TargetCanvas,editorcanvas):
        timelineFrame=Frame(TargetCanvas,height=22,width=865,bg="gray35")
        timelineFrame.grid_propagate(0)

        iofont = tkFont.Font ( family="Helvetica", size=10 )
        e=Entry(timelineFrame,width=4,bd=1,state="readonly",font=iofont,textvariable=self.startFrame,fg="gray15",justify=RIGHT,relief=GROOVE)
        e.grid(row=1,column=1)

        r= Button (timelineFrame,width=2,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="<<",font=iofont)
        r.grid(row=1,column=2)
        r.bind('<Button-1>',lambda event:(self.currentFrame.set(self.startFrame.get())))
        o= Button(timelineFrame,width=2,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="<-",font=iofont)
        o.grid(row=1,column=3)
        o.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()-1)))

        e2=Entry(timelineFrame,width=4,bd=0,state="readonly",font=iofont,textvariable=self.currentFrame,highlightbackground="gray35",fg="red",bg="lightblue",justify=RIGHT)
        e2.grid(row=1,column=4)
        b=backfor=Button(timelineFrame,width=2,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text="->",font=iofont)
        b.grid(row=1,column=5)
        b.bind('<Button-1>',lambda event:(self.currentFrame.set(self.currentFrame.get()+1)))
        o2=onefor=Button(timelineFrame,width=2,highlightcolor="gray35",bd=1,padx=5,pady=1,highlightbackground="gray35",text=">>",font=iofont)
        o2.grid(row=1,column=6)
        o2.bind('<Button-1>',lambda event:(self.currentFrame.set(self.endFrame.get())))

        e3=Entry(timelineFrame,width=4,bd=1,state="readonly",font=iofont,textvariable=self.endFrame,fg="gray15",justify=RIGHT,relief=GROOVE)
        e3.grid(row=1,column=7)

        delitem=Button(timelineFrame,width=3,bd=1,padx=5,pady=1,bg="darkred",activebackground="darkred",activeforeground="gray75",text="Del",font=iofont)
        delitem.grid(row=1,column=8,padx=15)
        delitem.bind('<Button-1>', lambda event: self.delItemPress(editorcanvas))

        duplicate=Button(timelineFrame,width=5,bd=1,padx=5,pady=1,text="Dupl.",font=iofont)
        duplicate.grid(row=1,column=9)
        #dulicate.bind('<Button-1>', lambda event: self.delItemPress(editorcanvas))

        instance=Button(timelineFrame,width=5,bd=1,padx=5,pady=1,text="Inst.",font=iofont)
        instance.grid(row=1,column=10)
        #dulicate.bind('<Button-1>', lambda event: self.delItemPress(editorcanvas))

        endtree=Button(timelineFrame,width=7,bd=1,padx=5,pady=1,text="EndNode",font=iofont,activeforeground="darkgreen",fg="lightgreen")
        endtree.grid(row=1,column=11,padx=15)
        endtree.bind('<Button-1>', lambda event: self.endTreePress(editorcanvas))

        etente=Entry(timelineFrame,width=30,bd=1,state="readonly",font=iofont,textvariable=self.eott,fg="gray15",justify=LEFT,relief=GROOVE)
        etente.grid(row=1,column=12)

        rururun=Button(timelineFrame,width=12,bd=1,padx=5,pady=1,text="- - - RUN - - -",font=iofont,bg="darkgreen",activebackground="darkgreen",activeforeground="gray75")
        rururun.grid(row=1,column=13)

        TargetCanvas.create_window(8,18,window=timelineFrame,anchor='w')

    def _initTimeLineCanvas(self,TargetCanvas,TargetSide,editorcanvas):
        TargetCanvas = Canvas (self, width=1280, height=30,relief=GROOVE, cursor="draft_large",bg="gray35",bd=2)
        TargetCanvas.grid(row=124,column=1,rowspan=6, sticky=N)
        self.timeLine_init(TargetCanvas,editorcanvas)

        print "TimeLine Initialised."
        return TargetCanvas

    def _ForgetTimeLineCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "TimeLine Closed."

    def StartUpTimeLineCanvas(self,Name,Side,editorcanvas):
        TargetCanvas=self._initTimeLineCanvas(Name,Side,editorcanvas)
        return TargetCanvas