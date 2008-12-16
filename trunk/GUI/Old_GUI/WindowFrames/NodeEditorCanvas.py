#------------------------------------------------------------------------------------------------------------------------------------
#
#    Main Node editor canvas for OpenAssembler
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------

from Tkinter import *
from MouseEvents import NodeEditorCanvasEvents

class CanvasInitNodeEditor(NodeEditorCanvasEvents):

    def StartUpNodeEditorCanvas(self):
        TargetCanvas = Canvas (self, width=640, height=480,relief=GROOVE, cursor="draft_large", confine="false",bg="gray45",bd=2, scrollregion=(0,0,2048,1536))
	TargetCanvas.pack(expand=1,fill=BOTH)

        def handlerB1Click(event, self=self, TargetCanvas=TargetCanvas):
            EventTags=TargetCanvas.gettags(CURRENT)
            self.lastx=event.x
            self.lasty=event.y
            self.B1ClickNodeEditor(event, TargetCanvas,self.lastx,self.lasty,EventTags)
        TargetCanvas.bind("<Button-1>", handlerB1Click)

        def handlerB3Click(event, self=self, TargetCanvas=TargetCanvas):
            EventTags=TargetCanvas.gettags(CURRENT)
            self.lastx=event.x
            self.lasty=event.y
            self.B3ClickNodeEditor(event, TargetCanvas,self.lastx,self.lasty,EventTags)
        TargetCanvas.bind("<Button-3>", handlerB3Click)
	TargetCanvas.bind("<Control-Button-1>", handlerB3Click)

        def handlerRelease(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
            self.ReleaseNodeEditor(event, TargetCanvas,self.lastx,self.lasty)

        TargetCanvas.bind("<B1-ButtonRelease>", handlerRelease)
        TargetCanvas.bind("<B2-ButtonRelease>", handlerRelease)
        TargetCanvas.bind("<Control-B1-ButtonRelease>", handlerRelease)
	TargetCanvas.bind("<B3-ButtonRelease>", handlerRelease)

        def handlerB1DoubleClick(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
            self.B1DoubleClickNodeEditor(event, TargetCanvas,self.lastx,self.lasty)

        TargetCanvas.bind("<Double-Button-1>", handlerB1DoubleClick)

        def handlerB1Move(event, self=self, TargetCanvas=TargetCanvas):
            EventTags=TargetCanvas.gettags(CURRENT)
            if len(EventTags)>0:
                self.NodeEditorPan_Move(event, TargetCanvas, self.lastx, self.lasty, EventTags)
            else:
                self.NodeEditorPan_Move(event, TargetCanvas, self.lastx, self.lasty, "")
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B1-Motion>", handlerB1Move)

        def handlerB2Move(event, self=self, TargetCanvas=TargetCanvas):
            self.NodeEditorZoom(event, TargetCanvas)
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B2-Motion>", handlerB2Move)

        def Aevent(event, self=self, TargetCanvas=TargetCanvas):
            if str(event.widget) ==".":
                self.NodeEditorScaleToCanvasDefault(event, TargetCanvas)
            else:
                pass
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind_all("a", Aevent)

        def Fevent(event, self=self, TargetCanvas=TargetCanvas):
            if str(event.widget) ==".":
                self.NodeEditorMoveCanvasCenterToCursor(event, TargetCanvas)
            else:
                pass
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind_all("f", Fevent)

        return TargetCanvas

