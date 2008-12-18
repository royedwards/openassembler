######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################


from Tkinter import *
import tkFont,sys
from GUI.common.GUI_Interface import GUI_Interface_client
from PreferenceControllers import old_gui_controllers


class LoadPreferences(old_gui_controllers):
	
	def old_preferences_refresh(self):
		self.prefcanv.delete("all")
		ParameterFrame=Frame(self.prefcanv)
		ParameterFrame.grid()
		ParameterFrame.rowconfigure(0, weight=1)
		ParameterFrame.columnconfigure(0, weight=1)
		self.preferencecanvas=ParameterFrame
		self.prefcanv.create_window(0, 0, anchor=NW, window=ParameterFrame)
		self.prefcanv.config(scrollregion=self.prefcanv.bbox("all"))
		self.nodeInPreferences.set("OpenAssembler")
		self.nip.set("OpenAssembler")
		return ParameterFrame
		
	def old_preferences_build(self,command):
		node_datas=self.oas_gui_scenenode_show(command.split()[1])
		self.nodeInPreferences.set(node_datas[1])
		self.nip.set(node_datas[1])
		attrList=self.oas_gui_attributelist(node_datas[1])
		return attrList,node_datas	
			
	def  old_preferences_addattributes(self,ParameterFrame,attrList,node_datas):
		height=10
		string=[]
		inter=[]
		db=[]				
		for n in range(0,len(attrList)):
								
			if (attrList[n][1]=="int") or (attrList[n][1]=="float"):
				string.append(StringVar())
				m=len(string)
				height=self.controllerNumberSimple(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],attrList[n][4])		
			elif attrList[n][1]=="string":
				string.append(StringVar())
				m=len(string)
				height=self.controllerTextLine(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],attrList[n][4])
				
        		elif attrList[n][1]=="boolean":
            			string.append(StringVar())
            			m=len(string)
            			height=self.controllerBoolean(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],attrList[n][4])
				string[m-1].set(str(attrList[n][2]))
					
			elif attrList[n][1]=="text":
				string.append(StringVar())
				m=len(string)
				height=self.controllerMassText(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],attrList[n][4])		
			
			elif attrList[n][1]=="path":
				string.append(StringVar())
				m=len(string)
				height=self.controllerPath(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],attrList[n][4])
			
			elif attrList[n][1]=="vector":
		    		string.append(StringVar())
		    		string.append(StringVar())
		    		string.append(StringVar())
            	    		m=len(string)
		    		de=str(attrList[n][2]).strip(")").lstrip("(").split(",")
		    		if len(de)<3:
		    			de=["0","0","0"]
			
				height=self.controllerVectorPoint(ParameterFrame,node_datas[1],height,string[m-1],string[m-2],string[m-3],attrList[n][0],de[0],de[1],de[2],attrList[n][4])
				
		self.prefcanv.config(scrollregion=self.prefcanv.bbox("all"))

	
class CanvasInitPreferencePanel(GUI_Interface_client):

    def exit_button(self):
	sys.exit()
	
    def namechange_event(self,old, new):
	ret=self.oas_gui_interface_client(self.main_serverport,"rename "+str(old)+" "+str(new))
	if ret==str(0):
		self.nip.set(old)
		
    def StartUpPreferencePanelCanvas(self):
        fr=Frame(self,relief=GROOVE,bd=2)
        fr.grid(column=0,row=0)
	
	iofont = tkFont.Font ( family=self.font, size=int(self.fontsize)+2 )
        label=Entry(fr,textvariable=self.nip,width=44,font=iofont,bg="gray80")
        label.grid()	
	label.bind('<Return>',lambda event:self.namechange_event(self.nodeInPreferences.get(),self.nip.get()))
	prefscroll=Scrollbar(self,orient="vertical")
	prefscroll.grid(column=1,row=0,rowspan=3,sticky=N+S)
	TargetCanvas = Canvas (self,height=400,width=200,yscrollcommand=prefscroll.set)
     	TargetCanvas.grid(column=0,row=1, sticky=N+S+E+W)
	self.prefcanv=TargetCanvas
	
	prefscroll.config(command=TargetCanvas.yview)
	
	self.grid_rowconfigure(1, weight=1)
	self.grid_columnconfigure(0, weight=1)

