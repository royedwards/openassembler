#------------------------------------------------------------------------------------------------------------------------------------
#
#    MouseActions for OpenAssembler
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
#from Nodes.NodeList import NodeListCategoriser
#from Nodes.NodeElements import GUI_Elements_forNodes
#from Nodes.ConnectionLine import ConnectLine
#from WindowFrames.PreferencePanel import LoadPreferences


class SliderBarEvents:


    def B1ClickEvent(self,event,TargetCanvas):
        try:
		self.menulink.destroy()
	except:
		pass
		
    def B1DoubleClickEvent(self,event,SourceCanvas,TargetCanvas):
        try:
		self.menulink.destroy()
	except:
		pass
		
        EventTags=SourceCanvas.gettags(CURRENT)
        if len(EventTags)>0:
            NewNode=self.CreateNodefromList(TargetCanvas,self.lastx,self.lasty,EventTags[1],"MAIN")
        else:
            pass


    def mouseMove_SliderBar(self, event,TargetCanvas):
        try:
		self.menulink.destroy()
	except:
		pass
		
        try:
            Targettags = TargetCanvas.gettags(CURRENT)
            if event.y < 52:
                if (0 > (self.SliderBar_First_RowEnd+event.x - self.sliderlastx) > -((self.PreviewNodeNoumber[0]*90*.75)-(TargetCanvas.winfo_width()-20))):
                    TargetCanvas.move ("UP",event.x - self.sliderlastx,0)
                    self.SliderBar_First_RowEnd=self.SliderBar_First_RowEnd+(event.x - self.sliderlastx)
                else:
                    pass
            elif (52 < event.y < 98):
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



class NodeEditorCanvasEvents:

    def B1ClickNodeEditor(self,event,TargetCanvas,lasx,lasty,Eventtag,preferencespanel):
        try:
		self.menulink.destroy()
	except:
		pass
		
        try:
            if str(Eventtag[1])=="CLOSEBUTTON":
                if self.getNodeName(Eventtag[0])==self.nodeInPreferences.get():
                    self.resetPreferencePlane(preferencespanel)
                self.DeleteItem(TargetCanvas,Eventtag[0])
                TargetCanvas.delete(Eventtag[4])
            if str(Eventtag[1])=="PREFERENCESBUTTON":
                self.loadPreferences(preferencespanel,Eventtag[0])
            if str(Eventtag[1])=="NOTEBUTTON":
                self.loadNote(preferencespanel, Eventtag[0])
            else:
                pass
        except:
            pass

        if str(TargetCanvas.cget('cursor'))=="pirate":
            EventTags=TargetCanvas.gettags(CURRENT)
            if len(EventTags)>0:
                if self.getNodeName(EventTags[0])==self.nodeInPreferences.get():
                    self.resetPreferencePlane(preferencespanel)
                self.DeleteItem(TargetCanvas,EventTags[0])
                TargetCanvas.delete(EventTags[4])
            TargetCanvas.configure(cursor="draft_large")
        try:
            TargetCanvas.tag_raise(Eventtag[4])
        except:
            pass

        if str(TargetCanvas.cget('cursor'))=="cross":
            EventTags=TargetCanvas.gettags(CURRENT)
            if len(EventTags)>0:
                self.eott.set(str(self.getNodeName(EventTags[0])))
                self.ChangeSettings("0000000", "Data","EndOfTheTree", str(self.getNodeName(EventTags[0])))
            TargetCanvas.configure(cursor="draft_large")
        try:
            TargetCanvas.tag_raise(Eventtag[4])
        except:
            pass

    def hello(self,a):
	print a


    def PopupMenuMain(self,TargetCanvas,event):
    	try:
		self.menulink.destroy()
	except:
		pass	
        if self.menuopen=="0":
	        self.menuopen="1"
                self.menulink=menu=Menu(TargetCanvas,tearoff=0,title="NodeList")
                for g in range(0,len(self.MenuNodeItems)):
                  if self.MenuNodeItems[g][0]!="":
                        submenu=Menu(menu,tearoff=0,title=self.MenuNodeItems[g][0])
                        menu.add_cascade(label=self.MenuNodeItems[g][0],menu=submenu)
                        for h in range(1,len(self.MenuNodeItems[g])):
                                if self.MenuNodeItems[g][h]!="":
                                        submenu.add_command(label=self.MenuNodeItems[g][h], command=lambda rty=self.MenuNodeItems[g][h]:self.CreateNodefromList(TargetCanvas,self.lastx,self.lasty,rty,"MAIN"))

	        #menu.add_separator()
                #menu.add_command(label="Cancel")
	        menu.post(event.x_root, event.y_root)
        else:
          pass
        self.menuopen="0"

    def delNodeFromMenu(self,TargetCanvas,EventTags):
    		self.resetPreferencePlane(self.pplane)
                self.DeleteItem(TargetCanvas,EventTags[0])
                TargetCanvas.delete(EventTags[4])

    def markEndFromMenu(self,TargetCanvas,EventTags):
                self.eott.set(str(self.getNodeName(EventTags[0])))
                self.ChangeSettings("0000000", "Data","EndOfTheTree", str(self.getNodeName(EventTags[0])))

    def addToSliderFromMenu(self,TargetCanvas,EventTags, row):
                self.AddToSliderBarToFile(row,"noneimportant",EventTags[2],self.sliderbarDescriptionFile)
                sliderfile=open(self.sliderbarDescriptionFile,"r")
                self.GUI_slider=sliderfile.read()
                sliderfile.close()
                self.restartSliderbarCanvas(self.sldr)


    def PopupMenuNode(self,TargetCanvas,event,Eventtag):

    	try:
		self.menulink.destroy()
	except:
		pass

        self.menulink=menu=Menu(TargetCanvas,tearoff=0,title=Eventtag[3])
	menu.add_command(label="Mark as EndNode", command=lambda :self.markEndFromMenu(TargetCanvas,Eventtag))
        
        subm=Menu(menu,tearoff=0)
        menu.add_cascade(label="Add to the SliderBar",menu=subm)
        subm.add_command(label="Row 1", command=lambda :self.addToSliderFromMenu(TargetCanvas,Eventtag,"Upper_row"))
        subm.add_command(label="Row 2", command=lambda :self.addToSliderFromMenu(TargetCanvas,Eventtag,"Middle_row"))
        subm.add_command(label="Row 3", command=lambda :self.addToSliderFromMenu(TargetCanvas,Eventtag,"Bottom_row"))
        menu.add_command(label="Delete", command=lambda :self.delNodeFromMenu(TargetCanvas,Eventtag))
        
        #menu.add_separator()
        #menu.add_command(label="Cancel")
        menu.post(event.x_root, event.y_root)


    def B3ClickNodeEditor(self,event,TargetCanvas,lasx,lasty,Eventtag):
        try:
		self.menulink.destroy()
	except:
		pass
		
        if len(Eventtag)==0:
	       self.PopupMenuMain(TargetCanvas,event)
        else:
               if Eventtag[3]!="line":
	       	self.PopupMenuNode(TargetCanvas,event,Eventtag)

    def ReleaseNodeEditor(self,event,TargetCanvas,lasx,lasty,preferencespanel):
        EventTags=TargetCanvas.gettags(CURRENT)
        if len(EventTags)>0:
            if EventTags[0]=="LineUnderCreateTMP":
                pass
            elif self.origin_node == "":
                pass
            else:
                try:
                    if EventTags[3]=="IN":
                        if self.checkMultipleSelfConnection(self.origin_node, self.origin_out, EventTags[0], EventTags[2])==0:
                            tst1=TargetCanvas.itemcget(EventTags[1],"fill")
                            tst2=TargetCanvas.itemcget(self.origin_uni,"fill")
                            if tst1==tst2:
                                self.DrawNewLine(TargetCanvas, self.origin_node,self.origin_out,self.origin_uni, EventTags[0],EventTags[2],EventTags[1])
                                if self.getNodeName(EventTags[0]) == self.nodeInPreferences.get():
                                    self.loadPreferences(preferencespanel, EventTags[0])
                            else:
                                print "The connection types does not match!!!"
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
        try:
		self.menulink.destroy()
	except:
		pass
		
        EventTags=TargetCanvas.gettags(CURRENT)
        try:
            if EventTags[1]=='UPPERLABEL':
                if self.getNodeName(EventTags[0])==self.nodeInPreferences.get():
                    pass
                else:
                    self.AddNodeRenamer(event, TargetCanvas,EventTags)
            else:
                self.loadPreferences(preferencespanel,EventTags[0])
        except:
            self.resetPreferencePlane(preferencespanel)


    def NodeEditorPan_Move(self, event,TargetCanvas,lastx,lasty,Eventtag):
        try:
		self.menulink.destroy()
	except:
		pass
		
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
	elif Eventtag[3]=="line":
	    TargetCanvas.tag_lower(Eventtag[4])
        else:
            if len(Eventtag)==8:
                TargetCanvas.tag_lower((str(Eventtag[0])+"select"))
            else:
                TargetCanvas.move(Eventtag[4],event.x - lastx, event.y - lasty)
                self.RedrawLines(TargetCanvas, Eventtag[0])

    def NodeEditorZoom(self, event,TargetCanvas):
        try:
		self.menulink.destroy()
	except:
		pass
		
        BoundingBoxAllCenter_X=600
	BoundingBoxAllCenter_Y=360
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
