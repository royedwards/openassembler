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
import tkFileDialog
from GUI.common.GUI_Gateway import gui_gateway

class old_gui_controllers(gui_gateway):

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
		e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, variable.get()))
		return pos+30
		
	def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		sstate="normal"
		if conchk=="darkred":
			sstate="disabled"
		fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
		fr.grid()
		
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
		e=Entry(fr,font=iofont,width=25,bg="gray55",relief="groove",bd=1,state=sstate,textvariable=variable,highlightbackground="gray35",justify=LEFT)
		e.grid(row=0,column=1,sticky=SW)
		variable.set(defaultvalue)
		e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, variable.get()))
		return pos+30
		

    	def controllerBoolean(self,TargetCanvas,Node,pos,varriable,parametername,defaultvalue,conchk):
        	sstate="normal"
        	if conchk=="darkred":
        	  sstate="disabled"
        	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        	fr.grid
        	
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	ch=Checkbutton(fr,text=parametername,variable=varriable,onvalue="True",offvalue="False",state=sstate,font=iofont,anchor="w", fg=conchk,width=25,height=0)
        	ch.grid()
        	ch.var=varriable
        	ch.bind('<B1-ButtonRelease>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, varriable.get()))
        	TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        	return pos+30


    	def controllerPassThrou(self,pos):
        	return pos
	

    	def controllerVectorPoint(self,TargetCanvas,Node,pos,v1,v2,v3,parametername,d1,d2,d3,conchk):
		sstate="normal"
        	if conchk=="darkred":
        	  sstate="disabled"
        	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        	fr.grid
        
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        	e=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v1,highlightbackground="gray35",justify=LEFT)
        	e.grid(row=0,column=1,sticky=SW,padx=2)
        	ee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v2,highlightbackground="gray35",justify=LEFT)
        	ee.grid(row=0,column=2,sticky=SW,padx=1)
		eee=Entry(fr,font=iofont,width=6,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v3,highlightbackground="gray35",justify=LEFT)
        	eee.grid(row=0,column=3,sticky=SW,padx=1)
		v1.set(d1)
		v2.set(d2)
		v3.set(d3)
        	e.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
		ee.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
		eee.bind('<Return>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
        	TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        	return pos+30


    	def _masTextSave(self,Node,textzone,parametername):
        	a=str(textzone.get(1.0,END))[:-1]
        	self.ChangeSettings(Node, "Data",parametername, a)

    	def controllerMassText(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        	sstate="normal"
        	if conchk=="darkred":
        	  sstate="disabled"
        	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        	fr.grid
        	iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=28,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        	e=Text(fr,font=iofont,width=30,height=8,bg="gray55",state=sstate,relief="sunken",wrap="word",bd=2,highlightbackground="gray35")
        	e.grid(row=1,column=0,sticky=N)
        	e.insert(CURRENT, defaultvalue)
        	b=Button (fr,width=30,highlightcolor="gray35",bd=1,height=0,state=sstate,padx=0,pady=0,highlightbackground="gray35",text="Save",font=iofont)
        	b.grid(row=2,column=0)
        	b.bind('<B1-ButtonRelease>', lambda event: self._masTextSave(Node,e,parametername))
        	TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        	return pos+210



    	def openFile(self,TargetCanvas,Node, parametername, variable):
        	fdiagback=tkFileDialog.Open(filetypes=[('Anyfile','*')]).show()
        	if str(fdiagback)==(""):
        	    pass
        	else:
        	    variable.set(fdiagback)
        	    self.ChangeSettings(Node,"Data", parametername, variable.get())
        	    self.loadPreferences(TargetCanvas,Node)
        	return

	    
	def controllerPath(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        	sstate="normal"
        	if conchk=="darkred":
        	  sstate="disabled"
        	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        	fr.grid
        	iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=9,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0)
        	e=Entry(fr,font=iofont,width=14,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        	e.grid(row=0,column=1,sticky=N,padx=2)
        	variable.set(defaultvalue)
        	e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        	b=Button (fr,width=6,highlightcolor="gray35",bd=1,height=0,padx=0,state=sstate,pady=0,highlightbackground="gray35",text="Open",font=iofont)
        	b.grid(row=0,column=3)
        	b.bind('<B1-ButtonRelease>', lambda event:self.openFile(TargetCanvas,Node, parametername, variable))
        	TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        	return pos+30

