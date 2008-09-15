#------------------------------------------------------------------------------------------------------------------------------------
#
#    SliderBar for OpenAssembler.
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
#from Nodes.NodeList import NodeListCategoriser
from MouseEvents import SliderBarEvents

class CanvasInitSliderBar(SliderBarEvents):

    def _initSliderbarCanvas(self):
        TargetCanvas = Canvas (self, width=1280, height=int(140/3*int(self.sliderbarrows)),relief=GROOVE, cursor="sb_up_arrow", confine="false",bg="gray35",bd=2, scrollregion=(0,0,1280,204))
        TargetCanvas.grid(row=130,column=1,rowspan=41, sticky=N)

        def handlerB1Click(event, self=self, TargetCanvas=TargetCanvas):
            self.sliderlastx=event.x
            self.sliderlasty=event.y
            return self.B1ClickEvent(event, TargetCanvas)

            TargetCanvas.bind("<Button-1>", handlerB1Click)

        def handlerB1DoubleClick(event, self=self, TargetCanvas=TargetCanvas):
            self.sliderlastx=event.x
            self.sliderlasty=event.y
            return self.B1DoubleClickEvent(event, TargetCanvas,EditorCanvas)

            TargetCanvas.bind("<Double-Button-1>", handlerB1DoubleClick)

        def handlerB1Move(event, self=self, TargetCanvas=TargetCanvas):
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
        tmp_db=self.SliderBarNodeList
        self.PreviewNodeNoumber=(len(tmp_db[0]),len(tmp_db[1]),len(tmp_db[2]))
        return TargetCanvas

    def restartSliderbarCanvas(self,TargetCanvas):
        TargetCanvas.delete(ALL)
        self._placePreviewNodes(TargetCanvas)

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
        TargetCanvas.scale(ALL,0,0,.5,.5)
        print "SliderBar Filled width PreviewNodes"

    def StartUpSliderBarCanvas(self):
        TargetCanvas=self._initSliderbarCanvas()
        #self._placePreviewNodes(TargetCanvas)
        return TargetCanvas
