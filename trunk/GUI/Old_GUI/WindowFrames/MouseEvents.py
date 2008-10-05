#------------------------------------------------------------------------------------------------------------------------------------
#
#    MouseActions for OpenAssembler
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
import tkFileDialog
import sys
from GUI.common.GUI_Interface import GUI_Interface_client
from GUI.Old_GUI.Nodes.ConnectionLine import ConnectLine


class NodeEditorCanvasEvents(GUI_Interface_client,ConnectLine):
    def CloseGUI(self):
    	try:
		self.nodePositions()
	except:
		pass
	self.oas_gui_interface_client(self.editorport,"server halt")
    	self.event_generate("<<cloose>>", when='tail')
            
    def NewScene(self):
	self.oas_gui_new()
	
    def Refresh(self):
    	self.nodePositions()
	self.oas_gui_refresh()


    def nodePositions(self):
	nodes=self.oas_gui_scenenodelist()
	for nds in nodes:
		realid=self.oas_gui_scenenode_show(nds)[0]
		bb=self.editorc.bbox(str(realid)+"select")
		self.oas_gui_set_positions(nds,int((bb[0]-5)*1/self.GlobalScale),int((bb[1]-5)*1/self.GlobalScale))	
	
    def SaveScene(self):
            self.nodePositions()
	    if self.savedfile=="":
	    	fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            	if fdiagback==():
                	pass
            	else:
			self.oas_gui_save(fdiagback)
			self.savedfile=fdiagback
	    else:
	    	self.oas_gui_save(self.savedfile)
			
    def SaveAsScene(self):
            self.nodePositions()
	    fdiagback=tkFileDialog.SaveAs(filetypes=[('OpenAsembler Scene','*.oas')],title="Save OpenAssembler scene file as:").show()
            if fdiagback==():
                pass
            else:
		self.oas_gui_save(fdiagback)
		self.savedfile=fdiagback
		
    def OpenScene(self):
            fdiagback=tkFileDialog.Open(filetypes=[('OpenAsembler Scene','*.oas')],title="Open OpenAssembler scene file as:").show()
            if fdiagback==():
                pass
            else:
		self.oas_gui_open(fdiagback)
		self.savedfile=fdiagback
		
		
    def AddNode(self,node):
    	self.oas_gui_addnode(node)
		
    
    def B1ClickNodeEditor(self,event,TargetCanvas,lasx,lasty,Eventtag):
        try:
		self.menulink.destroy()
	except:
		pass
        try:
            TargetCanvas.tag_raise(Eventtag[4])
        except:
            pass

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
                                        submenu.add_command(label=self.MenuNodeItems[g][h], command=lambda rty=self.MenuNodeItems[g][h]:self.AddNode(rty))
		menu.add_separator()
		menu.add_command(label="RUN!!!", command=lambda :self.runall())
		menu.add_command(label="Refresh", command=lambda :self.Refresh())
		menu.add_separator()
		menu.add_command(label="New", command=lambda :self.NewScene())
		menu.add_separator()
		menu.add_command(label="Open", command=lambda :self.OpenScene())
		menu.add_separator()
		menu.add_command(label="Save", command=lambda :self.SaveScene())
		menu.add_command(label="SaveAs", command=lambda :self.SaveAsScene())
		menu.add_separator()
		menu.add_command(label="Close Editor", command=lambda :self.CloseGUI())
		menu.post(event.x_root, event.y_root)
        else:
          pass
        self.menuopen="0"

    def delNodeFromMenu(self,TargetCanvas,EventTags):
    	self.oas_gui_deletenode(EventTags[0])

    def delLineFromMenu(self,TargetCanvas,EventTags):
    	self.oas_gui_deleteline(EventTags[0])

    def markEndFromMenu(self,EventTags):
	self.oas_gui_endnode(EventTags[0])

    def runall(self):
    	self.oas_gui_run()

    def preview(self,EventTags):
    	self.markEndFromMenu(EventTags)
	self.oas_gui_preview()
	
    def PopupMenuLine(self,TargetCanvas,event,Eventtag):

    	try:
		self.menulink.destroy()
	except:
		pass
        self.menulink=menu=Menu(TargetCanvas,tearoff=0,title=Eventtag[3])
        menu.add_command(label="Delete", command=lambda :self.delLineFromMenu(TargetCanvas,Eventtag))
        menu.post(event.x_root, event.y_root)

    def PopupMenuNode(self,TargetCanvas,event,Eventtag):

    	try:
		self.menulink.destroy()
	except:
		pass
        self.menulink=menu=Menu(TargetCanvas,tearoff=0,title=Eventtag[3])
	menu.add_command(label="Preview", command=lambda :self.preview(Eventtag))
	menu.add_command(label="Mark as EndNode", command=lambda :self.markEndFromMenu(Eventtag))
	menu.add_separator()
        menu.add_command(label="Delete", command=lambda :self.delNodeFromMenu(TargetCanvas,Eventtag))
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
	       elif Eventtag[3]=="line":
	       		self.PopupMenuLine(TargetCanvas,event,Eventtag)

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
                        if self.origin_node!="":
			    self.oas_gui_connect(self.origin_node,self.origin_out,EventTags[0],EventTags[2])
                except:
                    pass
        else:
            pass
        try:
            TargetCanvas.delete("LineUnderCreateTMP")
        except:
            pass
        self.origin_node=""


    def B1DoubleClickNodeEditor(self,event,TargetCanvas,lastx,lasty):
        try:
		self.menulink.destroy()
	except:
		pass
		
        EventTags=TargetCanvas.gettags(CURRENT)
        try:
            pass
	    #self.loadPreferences(preferencespanel,EventTags[0])
        except:
            pass


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
