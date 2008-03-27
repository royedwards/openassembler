from Tkinter import *
from GUI.Nodes.NodeList import NodeListCategoriser
from GUI.Nodes.NodeElements import GUI_Elements_forNodes
from GUI.Nodes.ConnectionLine import ConnectLine
from GUI.WindowFrames.PreferencePanel import LoadPreferences
from Dbase.DBaseManagement import RuntimeNodeRegister


class SliderBarEvents(NodeListCategoriser):


    def B1ClickEvent(self,event,TargetCanvas):
        pass

    def B1DoubleClickEvent(self,event,SourceCanvas,TargetCanvas):
        EventTags=SourceCanvas.gettags(CURRENT)
        if len(EventTags)>0:
            NewNode=self.CreateNodefromList(TargetCanvas,self.lastx,self.lasty,EventTags[1],"MAIN")
        else:
            pass


    def mouseMove_SliderBar(self, event,TargetCanvas):
        try:
            Targettags = TargetCanvas.gettags(CURRENT)
            if event.y < 77:
                if (0 > (self.SliderBar_First_RowEnd+event.x - self.sliderlastx) > -((self.PreviewNodeNoumber[0]*90*.75)-(TargetCanvas.winfo_width()-20))):
                    TargetCanvas.move ("UP",event.x - self.sliderlastx,0)
                    self.SliderBar_First_RowEnd=self.SliderBar_First_RowEnd+(event.x - self.sliderlastx)
                else:
                    pass
            elif (77 < event.y < 143):
                if (0 > (self.SliderBar_Secound_RowEnd+event.x - self.sliderlastx) > -((self.PreviewNodeNoumber[1]*90*.75)-(TargetCanvas.winfo_width()-20))):
                    TargetCanvas.move ("MID",event.x - self.sliderlastx,0)
                    self.SliderBar_Secound_RowEnd=self.SliderBar_Secound_RowEnd+(event.x - self.sliderlastx)
                else:
                    pass
            else:
                if (0 > (self.SliderBar_Third_RowEnd+event.x - self.sliderlastx) > -((self.PreviewNodeNoumber[2]*90*.75)-(TargetCanvas.winfo_width()-20))):
                    TargetCanvas.move ("BOT",event.x - self.sliderlastx,0)
                    self.SliderBar_Third_RowEnd=self.SliderBar_Third_RowEnd+(event.x - self.sliderlastx)
                else:
                    pass
        except:
            pass



class NodeEditorCanvasEvents(GUI_Elements_forNodes,ConnectLine,LoadPreferences,RuntimeNodeRegister):

    def B1ClickNodeEditor(self,event,TargetCanvas,lasx,lasty,Eventtag,preferencespanel):
        try:
            if str(Eventtag[1])=="CLOSEBUTTON":
                self.DeleteItem(TargetCanvas,Eventtag[0])
                TargetCanvas.delete(Eventtag[4])
            if str(Eventtag[1])=="PREFERENCESBUTTON":
                self.loadPreferences(preferencespanel,Eventtag[0])
            else:
                pass
        except:
            pass

        if str(TargetCanvas.cget('cursor'))=="pirate":
            EventTags=TargetCanvas.gettags(CURRENT)
            if len(EventTags)>0:
                self.DeleteItem(TargetCanvas,EventTags[0])
                TargetCanvas.delete(EventTags[4])
            TargetCanvas.configure(cursor="draft_large")
        try:
            TargetCanvas.tag_raise(Eventtag[4])
        except:
            pass

    def ReleaseNodeEditor(self,event,TargetCanvas,lasx,lasty):
        EventTags=TargetCanvas.gettags(CURRENT)
        if len(EventTags)>0:
            if EventTags[0]=="LineUnderCreateTMP":
                pass
            elif self.origin_node == "":
                pass
            else:
                try:
                    if EventTags[3]=="IN":
                        self.DrawNewLine(TargetCanvas, self.origin_node,self.origin_out,self.origin_uni, EventTags[0],EventTags[2],EventTags[1])
                except:
                    pass
        else:
            pass
        try:
            TargetCanvas.delete("LineUnderCreateTMP")
        except:
            pass

        self.origin_node=""


    def B1DoubleClickNodeEditor(self,event,TargetCanvas,lastx,lasty,preferencespanel):
        EventTags=TargetCanvas.gettags(CURRENT)
        try:
            if EventTags[1]=='UPPERLABEL':
                self.AddNodeRenamer(event, TargetCanvas,EventTags)
            else:
                self.loadPreferences(preferencespanel,EventTags[0])
        except:
            pass


    def NodeEditorPan_Move(self, event,TargetCanvas,lastx,lasty,Eventtag):
        try:
            TargetCanvas.tag_raise(Eventtag[4])
        except:
            pass
        if Eventtag == "":
            TargetCanvas.move (ALL,event.x - lastx, event.y - lasty)
        elif Eventtag[3]=="OUT":
            self.origin_node=Eventtag[0]
            self.origin_out=Eventtag[2]
            self.origin_uni=Eventtag[1]
            self.DrawTMPLine(TargetCanvas, Eventtag,lastx,lasty)
        else:
            if len(Eventtag)==8:
                TargetCanvas.tag_lower((str(Eventtag[0])+"select"))
            else:
                TargetCanvas.move(Eventtag[4],event.x - lastx, event.y - lasty)
                self.RedrawLines(TargetCanvas, Eventtag[0])

    def NodeEditorZoom(self, event,TargetCanvas):
        try:
            BoundingBoxAll= TargetCanvas.bbox(ALL)
            BoundingBoxAllCenter_X= ((BoundingBoxAll[2]-BoundingBoxAll[0])/2)+BoundingBoxAll[0]
            BoundingBoxAllCenter_Y= ((BoundingBoxAll[3]-BoundingBoxAll[1])/2)+BoundingBoxAll[1]
        except:
            pass
        if (event.x - self.lastx) > 0:
            TargetCanvas.scale(ALL,BoundingBoxAllCenter_X,BoundingBoxAllCenter_Y,1.05,1.05)
            self.GlobalScale=self.GlobalScale*1.05
            BoundingBoxAllCenter_X=0
            BoundingBoxAllCenter_Y=0
        elif (event.x - self.lastx) < 0:
            TargetCanvas.scale(ALL,BoundingBoxAllCenter_X,BoundingBoxAllCenter_Y,.952381,.952381)
            self.GlobalScale=self.GlobalScale*.952381
            BoundingBoxAllCenter_X=0
            BoundingBoxAllCenter_Y=0
        else:
            pass
        BoundingBoxAllCenter_X=0
        BoundingBoxAllCenter_Y=0

    def NodeEditorScaleToCanvasDefault(self, event,TargetCanvas):
        TargetCanvas.scale(ALL,event.x,event.y,1/self.GlobalScale,1/self.GlobalScale)
        self.GlobalScale=1

    def NodeEditorMoveCanvasCenterToCursor(self, event,TargetCanvas):
        try:
            BoundingBoxAll= TargetCanvas.bbox(ALL)
            BoundingBoxAllCenter_X= ((BoundingBoxAll[2]-BoundingBoxAll[0])/2)+BoundingBoxAll[0]
            BoundingBoxAllCenter_Y= ((BoundingBoxAll[3]-BoundingBoxAll[1])/2)+BoundingBoxAll[1]
            TargetCanvas.move(ALL,-(BoundingBoxAllCenter_X-event.x),-(BoundingBoxAllCenter_Y-event.y))
            BoundingBoxAllCenter_X=0
            BoundingBoxAllCenter_Y=0
        except:
            pass



