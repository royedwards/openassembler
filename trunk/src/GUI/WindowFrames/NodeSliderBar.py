from Tkinter import *
from Dbase.DBaseManagement import SliderBarDbaseSupport
from GUI.Nodes.NodeList import NodeListCategoriser
from MouseEvents import SliderBarEvents

class CanvasInitSliderBar(SliderBarDbaseSupport,NodeListCategoriser,SliderBarEvents):
    def __init__(self):
        pass
    def _name(self):
        return "NodeSliderBarCanvasInit"

    def _initSliderbarCanvas(self,TargetCanvas,TargetSide,EditorCanvas):
        TargetCanvas = Canvas (self, width=540, height=102,relief=GROOVE, cursor="sb_up_arrow", confine="false",bg="gray35",bd=2, scrollregion=(0,0,800,205))
        TargetCanvas.grid(row=130,column=1,rowspan=41)

        def handlerB1Click(event, self=self, TargetCanvas=TargetCanvas):
            self.sliderlastx=event.x
            self.sliderlasty=event.y
            return self.B1ClickEvent(event, TargetCanvas)
        if EditorCanvas==None:
            pass
        else:
            TargetCanvas.bind("<Button-1>", handlerB1Click)

        def handlerB1DoubleClick(event, self=self, TargetCanvas=TargetCanvas,EditorCanvas=EditorCanvas):
            self.sliderlastx=event.x
            self.sliderlasty=event.y
            return self.B1DoubleClickEvent(event, TargetCanvas,EditorCanvas)
        if EditorCanvas==None:
            pass
        else:
            TargetCanvas.bind("<Double-Button-1>", handlerB1DoubleClick)

        def handlerB1Move(event, self=self, TargetCanvas=TargetCanvas,EditorCanvas=EditorCanvas):
            tmp=self.mouseMove_SliderBar(event, TargetCanvas)
            self.sliderlastx=event.x
            self.sliderlasty=event.y
            return tmp
        TargetCanvas.bind("<B1-Motion>", handlerB1Move)

        self.sliderlastx=30
        self.sliderlasty=30
        self.SliderBar_First_RowEnd=0
        self.SliderBar_Secound_RowEnd=0
        self.SliderBar_Third_RowEnd=0
        tmp_db=self.GetSliderBarNodeList()
        self.PreviewNodeNoumber=(len(tmp_db[0]),len(tmp_db[1]),len(tmp_db[2]))

        print "SliderBar Initialised."
        return TargetCanvas

    def _ForgetSliderbarCanvas(self,TargetCanvas):
        TargetCanvas.forget()
        print "SliderBar Closed."

    def _placePreviewNodes(self,TargetCanvas):
        list=self.GetSliderBarNodeList()
        tmpvar=0
        x=20
        y=15
        while tmpvar<3:
            count=len(list[tmpvar])
            i= 0
            if tmpvar is 0:
                row="UP"
            elif tmpvar is 1:
                row="MID"
            else:
                row="BOT"
            while i<count:
                self.CreateNodefromList(TargetCanvas,x,y,list[tmpvar][i],row)
                i += 1
                x += 90
            x=20
            y +=90
            tmpvar +=1
        TargetCanvas.scale(ALL,0,0,.375,.375)
        print "SliderBar Filled width PreviewNodes"

    def StartUpSliderBarCanvas(self,Name,Side,EditorCanvas):
        TargetCanvas=self._initSliderbarCanvas(Name,Side,EditorCanvas)
        self._placePreviewNodes(TargetCanvas)
        return TargetCanvas
