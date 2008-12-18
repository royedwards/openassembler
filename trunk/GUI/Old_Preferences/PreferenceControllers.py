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
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
		fr=Frame(TargetCanvas)
		fr.grid(sticky=SW)
		
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont).grid(row=0,column=0,pady=2)
		e=Entry(fr,font=iofont,width=15,state=sstate,textvariable=variable,justify=LEFT,bg="gray80")
		e.grid(row=0,column=1,sticky=SW)
		variable.set(defaultvalue)
		e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, variable.get()))
		return pos+30
		
	def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
		fr=Frame(TargetCanvas)
		fr.grid(sticky=SW)
		
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont).grid(row=0,column=0,pady=2)
		e=Entry(fr,font=iofont,width=25,state=sstate,textvariable=variable,justify=LEFT,bg="gray80")
		e.grid(row=0,column=1,sticky=SW)
		variable.set(defaultvalue)
		e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, variable.get()))
		return pos+30
		

    	def controllerBoolean(self,TargetCanvas,Node,pos,varriable,parametername,defaultvalue,conchk):
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
        	fr=Frame(TargetCanvas)
        	fr.grid(sticky=SW)
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
		Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont).grid(row=0,column=0,pady=2)
        	ch=Checkbutton(fr,text="",width=28,variable=varriable,onvalue="1.0",offvalue="0.0",state=sstate,font=iofont,anchor="w")
        	ch.grid(row=0,column=1)
		ch.var=varriable
        	ch.bind('<B1-ButtonRelease>',lambda event:self._boolhelp(self.nodeInPreferences.get(),parametername,varriable))
		return pos+30

	def _boolhelp(self,np,prn,varr):
		if varr.get()=="0.0":
			va="1.0"
		else:
			va="0.0"
		self.oas_gui_set(np,prn, va )


    	def controllerPassThrou(self,pos):
        	return pos
	

    	def controllerVectorPoint(self,TargetCanvas,Node,pos,v1,v2,v3,parametername,d1,d2,d3,conchk):
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
        	fr=Frame(TargetCanvas)
        	fr.grid(sticky=SW)
        
		iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont).grid(row=0,column=0,pady=2)
        	e=Entry(fr,font=iofont,width=6,state=sstate,textvariable=v1,justify=LEFT,bg="gray80")
        	e.grid(row=0,column=1,sticky=SW,padx=2)
        	ee=Entry(fr,font=iofont,width=6,state=sstate,textvariable=v2,justify=LEFT,bg="gray80")
        	ee.grid(row=0,column=2,sticky=SW,padx=1)
		eee=Entry(fr,font=iofont,width=6,state=sstate,textvariable=v3,justify=LEFT,bg="gray80")
        	eee.grid(row=0,column=3,sticky=SW,padx=1)
		v1.set(d1)
		v2.set(d2)
		v3.set(d3)
        	e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, str("("+str(v1.get())+","+str(v2.get())+","+ str(v3.get())+")"  ) ))
		ee.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, str("("+str(v1.get())+","+str(v2.get())+","+ str(v3.get())+")"  )  ))
		eee.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, str("("+str(v1.get())+","+str(v2.get())+","+ str(v3.get())+")"  )   ))
        	return pos+30


    	def _masTextSave(self,Node,textzone,parametername):
        	a=str(textzone.get(1.0,END))[:-1]
        	self.oas_gui_set(self.nodeInPreferences.get(),parametername, a)

    	def controllerMassText(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
        	fr=Frame(TargetCanvas)
        	fr.grid(sticky=SW)
        	iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont).grid(row=0,column=0,pady=2,sticky=NW)
        	e=Text(fr,font=iofont,width=25,height=14,state=sstate,wrap="word",bg="gray80",bd=2)
        	e.grid(row=0,column=1,sticky=NW)
        	e.insert(CURRENT, defaultvalue)
        	b=Button (fr,width=25,height=0,state=sstate,padx=0,pady=0,text="Save",font=iofont)
        	b.grid(row=1,column=1,columnspan=2)
        	b.bind('<B1-ButtonRelease>', lambda event: self._masTextSave(Node,e,parametername))
        	return pos+210



    	def openFile(self,TargetCanvas,Node, parametername, variable):
        	fdiagback=tkFileDialog.Open(filetypes=[('Anyfile','*')]).show()
        	if str(fdiagback)==(""):
        	    pass
        	else:
        	    variable.set(fdiagback)
        	    self.oas_gui_set(self.nodeInPreferences.get(),parametername, variable.get())
        	return

	    
	def controllerPath(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
		if str(conchk)=="1":
			sstate="disabled"
		else:
			sstate="normal"
        	fr=Frame(TargetCanvas)
        	fr.grid(sticky=SW)
        	iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        	Label(fr,text=parametername+":",anchor="nw",width=9,font=iofont).grid(row=0,column=0)
        	e=Entry(fr,font=iofont,width=14,state=sstate,textvariable=variable,justify=LEFT,bg="gray80")
        	e.grid(row=0,column=1,sticky=N,padx=2)
        	variable.set(defaultvalue)
        	e.bind('<Return>',lambda event:self.oas_gui_set(self.nodeInPreferences.get(),parametername, varriable.get()))
        	b=Button (fr,width=6,bd=1,height=0,padx=0,state=sstate,pady=0,text="Open",font=iofont)
        	b.grid(row=0,column=3)
        	b.bind('<B1-ButtonRelease>', lambda event:self.openFile(TargetCanvas,Node, parametername, variable))
        	return pos+30

