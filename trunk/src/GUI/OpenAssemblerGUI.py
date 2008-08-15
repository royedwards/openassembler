#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    Gui Starting script....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#---------------------------------------------------------------------------------------------------------------------

from Tkinter import *
from WindowFrames.NodeSliderBar import CanvasInitSliderBar
from WindowFrames.NodeEditorCanvas import CanvasInitNodeEditor
from WindowFrames.TimeLine import CanvasInitTimeLine
from WindowFrames.MenuLine import CanvasInitMenuLine
from WindowFrames.PreferencePanel import CanvasInitPreferencePanel
from WindowFrames.MicroViewer import CanvasInitMicroViewer
from Dbase.DBaseManagement import RuntimeNodeRegister, SA_NodeConverter
from Dbase.SA_Gateway import SA_Conversion

import os
from xml.dom import minidom


class _Application(Frame,CanvasInitSliderBar,CanvasInitNodeEditor,CanvasInitTimeLine,CanvasInitMenuLine,CanvasInitPreferencePanel,CanvasInitMicroViewer,SA_Conversion,SA_NodeConverter):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        print "OpenAssembler Starting up...."
        print "Owner: Laszlo Mates, laszlo.mates@gmail.com"
        self.Startup()
	self._createWidgets()
	
    def MenuVarBuilder(self,path):
        nlsmenu=open(path,"r")
        nlsmcontent=nlsmenu.read()
        nlsmenu.close()
        nlsmcontent=nlsmcontent.strip("\n").split("\n")
        menulist=[]
        for lies in nlsmcontent:
                lies=lies.strip(" ")
                x=lies.split(" ")
                menulist.append(x)
        return menulist    
        
    def FileCreator(self,path, filetype):
	    if filetype=="nodedescription":
		   testdoc=minidom.getDOMImplementation()
        	   root=testdoc.createDocument("","NodeTypes","")
        	   files=open(path,"w")
        	   files.write(root.toxml())
        	   files.close()
		   
	    elif filetype=="sliderbarsettings":
        	   nodeListDoc=minidom.getDOMImplementation()
        	   root=nodeListDoc.createDocument("", "SliderBarNodes", "")
        	   xmlfileoutput=open(path,"w")
        	   upp=root.createElement("Upper_row")
        	   root.firstChild.appendChild(upp)

        	   midd=root.createElement("Middle_row")
        	   root.firstChild.appendChild(midd)

        	   bott=root.createElement("Bottom_row")
        	   root.firstChild.appendChild(bott)

        	   xmlfileoutput.write(root.toxml())
        	   xmlfileoutput.close()
		   
	    elif filetype=="ini":
        	   files=open(path,"w")
		   
		   initext="environments OASPATH\n"
		   initext+="font Helvetica\n"
		   initext+="fontsize 10\n"
		   initext+="sliderbarrows 1\n"
		   initext+="menucategory Math math\n"
		   initext+="menucategory Mass mass\n"
		   initext+="menucategory Dynamics dynamics:field:wind:flow\n"
		   initext+="menucategory OpenAssembler oas\n"
		   
		   initext+="menucategory Massive massive\n"
		   initext+="menucategory Mesh mesh:geo:surface:curve\n"
		   initext+="manualpath /net/homes/lmates/OpenAssembler/src/OpenNodes\n"
		   
        	   files.write(initext)
        	   files.close()
		   
	    elif filetype=="menu":
        	   files=open(path,"w")
		   
		   initext=""

        	   files.write(initext)
        	   files.close()
		   
    def iniFileMapper(self,path):
	    files=open(path,"r")
	    ifm=str(files.read()).strip("\n").strip(" ")
	    ifm=ifm.split("\n")
	    out=[]
	    for i in range(0,len(ifm)):
		    if ifm[i]==" " or ifm[i]=="\"\"" or ifm[i]=="\n" or ifm[i]=="":
			    pass
		    else:
			    out.append(ifm[i].strip(" ").split(" "))
	    files.close()
	    return out

    def iniFileAnalizer(self,path,type):
	    if type=="environments":
        	   in_ini=self.iniFileMapper(path)
		   filestoreturn=[]
        	   for f in range(0,len(in_ini)):
			   if in_ini[f][0]==type:
				   filestoreturn=in_ini[f][1].split(":")
        	   return filestoreturn
	    elif type=="font":
        	   in_ini=self.iniFileMapper(path)
        	   x=""
		   for f in range(0,len(in_ini)):
			   if in_ini[f][0]==type:
				   x=in_ini[f][1]
        	   return x
	    elif type=="fontsize":
        	   in_ini=self.iniFileMapper(path)
        	   x=""
		   for f in range(0,len(in_ini)):
			   if in_ini[f][0]==type:
				   x=in_ini[f][1]
        	   return x
	    elif type=="sliderbarrows":
        	   in_ini=self.iniFileMapper(path)
        	   x=""
		   for f in range(0,len(in_ini)):
			   if in_ini[f][0]==type:
				   x=in_ini[f][1]
        	   return x
            if type=="menucategory":
                   in_ini=self.iniFileMapper(path)
                   filestoreturn=[]
                   for f in range(0,len(in_ini)):
                           if in_ini[f][0]==type:
                                   filestoreturn.append([in_ini[f][1],in_ini[f][2].split(":")])
                   return filestoreturn
	    if type=="manualpath":
        	   in_ini=self.iniFileMapper(path)
		   filestoreturn=[]
        	   for f in range(0,len(in_ini)):
			   if in_ini[f][0]==type:
				   filestoreturn=in_ini[f][1].split(":")
        	   return filestoreturn                         
                           
                           
    def collectNodesFromFolders(self,folder):
	    if str(folder)=="None":
		    pass
	    else:
		    folder=folder.strip(" ").split(":")
		    return folder
	    

    def Startup(self):

	    self.homedirectory=os.environ.get("HOME")
	    self.OAHome=str(self.homedirectory)+"/.OpenAssembler"
	    self.nodeDescriptionFile=self.OAHome+"/NodeTypeSettings.xml"
	    self.sliderbarDescriptionFile=self.OAHome+"/SliderBarNodeList.xml"
	    self.OASini=self.OAHome+"/OpenAssembler.ini"
	    self.nodeListMenu=self.OAHome+"/NodeListMenu.ini"
	    self.menulink=""


	    if os.path.isdir(self.OAHome):
		    pass
	    else:
		    os.mkdir(self.OAHome)
		    print "OpenAssembler userfolder created."

	    if os.path.isfile(self.nodeDescriptionFile):
		    pass
	    else:
		    self.FileCreator(self.nodeDescriptionFile,"nodedescription")
		    print "Node-description file created."

	    if os.path.isfile(self.sliderbarDescriptionFile):
		    pass
	    else:
		    self.FileCreator(self.sliderbarDescriptionFile,"sliderbarsettings")
		    print "SliderBar-description file created."

	    if os.path.isfile(self.OASini):
		    pass
	    else:
		    self.FileCreator(self.OASini,"ini")
		    print "OpenAssembler.ini file created."

	    if os.path.isfile(self.nodeListMenu):
		    pass
	    else:
		    self.FileCreator(self.nodeListMenu,"menu")
		    print "NodeListMenu.ini file created."



    	    self.font=self.iniFileAnalizer(self.OASini,"font")
    	    self.fontsize=self.iniFileAnalizer(self.OASini,"fontsize")
	    self.sliderbarrows=self.iniFileAnalizer(self.OASini,"sliderbarrows")
	    self.menucats=self.iniFileAnalizer(self.OASini,"menucategory")
            
            checkfolders=[]
	    for envs in self.iniFileAnalizer(self.OASini,"environments"):
		    folder=os.environ.get(str(envs))
		    for dirs in self.collectNodesFromFolders(folder):
			    if os.path.isdir(dirs)==True:
			    	checkfolders.append(dirs)
	    mpath=self.iniFileAnalizer(self.OASini,"manualpath")
	    for patcc in mpath:
	    	checkfolders.append(str(patcc))	
	    bigfilelist=[]
	    for folds in checkfolders:
		    for nds in self.CollectSAinFolder(folds):
			    bigfilelist.append(nds)
	
	    existance=self.GetNameList(self.nodeDescriptionFile)
	    
            toADD=[]
	    toDELETE=[]	
	    for nam in bigfilelist:
		    checkerke=0
		    for k in range(0,len(existance)):
			    if nam[0]==existance[k]:
				    checkerke=1
			    else:
				    pass
		    if checkerke==1:
			    pass
		    else:
			    toADD.append(nam[1])

	    for item in existance:
		    checkerke=0
		    for k in range(0,len(bigfilelist)):
			    if item==bigfilelist[k]:
				    checkerke=1
			    else:
				    pass
		    if checkerke==0:
			    pass
		    else:
			    toDELETE.append(nam[1])

    	    if len(toADD)>0:
		    print "We will generate nodes for you, this may take a while.... (but you need to do it just once) :)"
	            self.AddSAtoNodeDescription(self.nodeDescriptionFile,toADD)
		    
	    if len(toDELETE)>0:
		    print "We will delete some nodes from your description, this may take a while...."
		    self.DeleteNodeTypeSettings(self.nodeDescriptionFile,toDELETE)
	    
            self.MenuNodeItems=self.MenuVarBuilder(self.nodeListMenu)
	    
	    self.rt=""
    	    self.lastx=30
            self.lasty=30
            self.GlobalScale=.75
            self.origin_node=""
            self.origin_out=""
            self.origin_uni=""
            self.sceneFileName=""
            self.Create_RuntimeDBase()
            self.CreateGlobalPreferences(1, 100, "Basic scene setup...","...")
            self.RuntimeLines=[]
            self.startFrame=IntVar()
            self.startFrame.set(self.getFrameRange()[0])
            self.endFrame=IntVar()
            self.endFrame.set(self.getFrameRange()[1])
            self.currentFrame=IntVar()
            self.currentFrame.set(self.startFrame.get())
            self.nodeInPreferences=StringVar()
            self.nodeInPreferences.set("OpenAssembler")
            self.eott=StringVar()
            self.eott.set("...")
    	    self.GUI_definition=""
    	    self.GUI_slider=""
            self.menuopen="0"
    	    nodesettingsfile=open(self.nodeDescriptionFile,"r")
    	    self.GUI_definition=nodesettingsfile.read()
    	    nodesettingsfile.close()

    	    sliderfile=open(self.sliderbarDescriptionFile,"r")
    	    self.GUI_slider=sliderfile.read()
    	    sliderfile.close()


    def _createWidgets(self):

    	    mview=self.StartUpMicroViewerCanvas("MicroViewer", "right")
            ppanel=self.StartUpPreferencePanelCanvas("PreferencePanel", "right")
            editorcanvas=self.StartUpNodeEditorCanvas("NodeEditorCanvas", "top",ppanel)
            menuline=self.StartUpMenuLineCanvas("MenuLineCanvas","top",ppanel,editorcanvas)
            tline=self.StartUpTimeLineCanvas("TimeLineCanvas", "bottom",editorcanvas)
            slider=self.StartUpSliderBarCanvas("SliderBar", "bottom",editorcanvas)            
            self.sldr=slider
	    self.pplane=ppanel

            print "Application Started!"



app= _Application()
app.master.title("OpenAssembler 0.04beta")
app.tk_strictMotif(1)
app.tk_setPalette("gray35")
app.master.wm_resizable(width=False ,height=False)
app.mainloop()
print "OpenAssembler Closed."
print "---Thank You!---"

