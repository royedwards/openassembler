######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from Tkinter import *
import tkFont

class old_preferences_interpreter:
		
	def old_gui_do(self,command):
		try:
			if command.split()[0]=="set":
				pass
			elif command.split()[0]=="showpreferences":
				node_datas=self.oas_gui_scenenode_show(command.split()[1])
				self.nodeInPreferences.set(node_datas[1])
				attrList=self.oas_gui_attributelist(node_datas[1])
				height=10
				string=[]
				inter=[]
				db=[]
				self.prefcanv.delete("all")
				ParameterFrame=Frame(self.prefcanv)
				ParameterFrame.grid()
				ParameterFrame.rowconfigure(0, weight=1)
				ParameterFrame.columnconfigure(0, weight=1)
				self.preferencecanvas=ParameterFrame
				self.prefcanv.create_window(0, 0, anchor=NW, window=ParameterFrame)
				self.prefcanv.config(scrollregion=self.prefcanv.bbox("all"))

				conchk="gray90"
				for n in range(0,len(attrList)):
					conchk="gray90"
					if (attrList[n][1]=="int") or (attrList[n][1]=="float"):
						string.append(StringVar())
						m=len(string)
						height=self.controllerNumberSimple(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],conchk)
					
					elif attrList[n][1]=="string":
						string.append(StringVar())
						m=len(string)
						height=self.controllerTextLine(ParameterFrame,node_datas[1],height,string[m-1],attrList[n][0],attrList[n][2],conchk)
				
				#self.preferencecanvas.update_idletasks()
				self.prefcanv.config(scrollregion=self.prefcanv.bbox("all"))

				
		except:
			pass

	def controllerNumberSimple(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		sstate="normal"
		if conchk=="darkred":
			sstate="disabled"
		fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
		fr.grid()
		
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
		e=Entry(fr,font=iofont,width=15,bg="gray55",state=sstate,relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
		e.grid(row=0,column=1,sticky=SW)
		variable.set(defaultvalue)
		#e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
		#TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
		return pos+30
		
		
		
	def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		sstate="normal"
		if conchk=="darkred":
			sstate="disabled"
		fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
		fr.grid()
		
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
		e=Entry(fr,font=iofont,width=20,bg="gray55",relief="groove",bd=1,state=sstate,textvariable=variable,highlightbackground="gray35",justify=LEFT)
		e.grid(row=0,column=1,sticky=SW)
		variable.set(defaultvalue)
		#e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
		#TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
		return pos+30
		
