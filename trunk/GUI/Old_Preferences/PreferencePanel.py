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
import tkFileDialog
from ColorConversions import convertColors
import colorsys


class LoadPreferences(convertColors):

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
        ch.bind('<B1-ButtonRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, varriable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerSeparator(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        plen=len(parametername)
        ta=int((50-plen)/2)
        tach=""
        for n in range(0,ta):
            tach=tach+"-"
        Label(fr,text=tach+parametername+tach,anchor="nw",width=28,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=0)
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerPassThrou(self,pos):
        return pos
	
	
    def crossPos(self,canvasMainColor,canvasLumin,h,s,v):
	try:
		canvasMainColor.delete("hor_col")
		canvasMainColor.delete("vert_col")
		canvasLumin.delete("lumaline")
	except:
		pass
    	apply(canvasLumin.tk.call,(canvasLumin._w,'create','line') + (0,(v*128),17,(v*128)) + ('-width',2,'-fill',"red", "-tags", "lumaline"))
    	apply(canvasMainColor.tk.call,(canvasMainColor._w,'create','line') + (0,(s*128),129,(s*128)) + ('-width',1,'-fill',"black", "-tags", "hor_col"))
    	apply(canvasMainColor.tk.call,(canvasMainColor._w,'create','line') + ((h*128),0,(h*128),129) + ('-width',1,'-fill',"black", "-tags", "vert_col"))


    def rgb_headed_update(self,Node ,parametername, canvasMainColor,canvasLumin,rvar,gvar,bvar,hvar,svar,vvar):
    
    	self.ChangeSettings(Node, "Data",parametername, str(";"+str(rvar.get())+";"+str(gvar.get())+";"+ str(bvar.get())+";"  ))
	
	try:
    		if float(rvar.get())>1 or float(gvar.get())>1 or float(bvar.get())>1:
			rvar.set(float(rvar.get())/255)
			gvar.set(float(gvar.get())/255)
			bvar.set(float(bvar.get())/255)
	
		hsv_comb=colorsys.rgb_to_hsv(float(rvar.get()),float(gvar.get()),float(bvar.get()))
		hvar.set(hsv_comb[0])
		svar.set(hsv_comb[1])
		vvar.set(hsv_comb[2])
		self.drawColorPicker(canvasMainColor,float(vvar.get()))
		self.crossPos(canvasMainColor,canvasLumin,float(hvar.get()),float(svar.get()),float(vvar.get()))
	except:
		self.crossPos(canvasMainColor,canvasLumin,0.5,0.5,0.5)
		self.drawColorPicker(canvasMainColor,0.5)


    def hsv_headed_update(self,Node ,parametername, canvasMainColor,canvasLumin,rvar,gvar,bvar,hvar,svar,vvar):
    
	try:
		rgb_comb=colorsys.hsv_to_rgb(float(hvar.get()),float(svar.get()),float(vvar.get()))
		rvar.set(float(rgb_comb[0]))
		gvar.set(float(rgb_comb[1]))
		bvar.set(float(rgb_comb[2]))
		self.drawColorPicker(canvasMainColor,float(vvar.get()))
		self.crossPos(canvasMainColor,canvasLumin,float(hvar.get()),float(svar.get()),float(vvar.get()))
		self.ChangeSettings(Node, "Data",parametername, str(";"+str(rvar.get())+";"+str(gvar.get())+";"+ str(bvar.get())+";"  ))
	except:
		self.crossPos(canvasMainColor,canvasLumin,0.5,0.5,0.5)
		self.drawColorPicker(canvasMainColor,0.5)

    def drawColorPicker(self, bugcanvas,v):
    	try:
		bugcanvas.delete("colorbig")
	except:
		pass
	for ha in range(0,32):
		for es in range(0,32):
			colget=""
			hval=ha/32.000
			sval=es/32.000
			cctv=colorsys.hsv_to_rgb(hval,sval,v)
			err=int(cctv[0]*255)
			gee=int(cctv[1]*255)
			bee=int(cctv[2]*255)
			colget=str(self.Rgb2Hex((err,gee,bee)))
			apply(bugcanvas.tk.call,(bugcanvas._w,'create','line') + (ha*4,es*4,(ha+1)*4,(es+1)*4) + ('-width',8,'-fill',colget,"-tags","colorbig"))
	
    def drawLumaPicker(self,smallcanvas):
    	try:
		smallcanvas.delete("colorsmall")
	except:
		pass
	for j in range (0,25):
		apply(smallcanvas.tk.call,(smallcanvas._w,'create','line') + (1,j*4*1.28,17,j*4*1.28) + ('-width',8,'-fill',("grey"+str(j*4)),"-tags","colorsmall"))
		

    def getLumaPicker(self,Node,param,smallcanvas,bigcanvas,event,hval,sval,vval,rval,gval,bval):
	value_was_geted=0
	if 128>=event.y>=1:
		value_was_geted=event.y
	elif 128<event.y:
		value_was_geted	= 128
	elif 1>event.y:
		value_was_geted	= 1
	vval.set(str(value_was_geted/128.0000))
	self.hsv_headed_update(Node ,param, bigcanvas,smallcanvas,rval,gval,bval,hval,sval,vval)
	
	
	
    def getColorPicker(self,Node,param,smallcanvas,bigcanvas,event,hval,sval,vval,rval,gval,bval):
	value_was_geted_y=0
	if 128>=event.y>=1:
		value_was_geted_y=event.y
	elif 128<event.y:
		value_was_geted_y= 128
	elif 1>event.y:
		value_was_geted_y= 1
	sval.set(str(value_was_geted_y/128.0000))

	value_was_geted_x=0
	if 128>=event.x>=1:
		value_was_geted_x=event.x
	elif 128<event.x:
		value_was_geted_x = 128
	elif 1>event.x:
		value_was_geted_x = 1
	hval.set(str(value_was_geted_x/128.0000))
	
	self.hsv_headed_update(Node ,param, bigcanvas,smallcanvas,rval,gval,bval,hval,sval,vval)
	
	
	

    def controllerColor(self,TargetCanvas,Node,pos,valr,valg,valb,parametername,d1,d2,d3,conchk,valh,vals,valve):
	if float(d1)>1 or float(d2)>1 or float(d3)>1:
		d1=d1/255
		d2=d2/255
		d3=d3/255
	sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=13,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2,sticky=N)
        self.bigc.append(Canvas(fr,width=128, height=128,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=0))
	impno=len(self.bigc)-1
	self.bigc[impno].grid(row=0,column=1,rowspan=2,columnspan=4,sticky=N)
        self.smallc.append(Canvas(fr,width=16, height=128,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=0))
	impsmno=len(self.smallc)-1
	self.smallc[impsmno].grid(row=0,column=5,rowspan=2,sticky=N)
	self.drawLumaPicker(self.smallc[impsmno])

	labelrgb=Label(fr,text="rgb",anchor="nw",width=3,font=iofont,bg="gray35", fg=conchk).grid(row=2,column=1,sticky=N)
        rgbr=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=valr,highlightbackground="gray35",justify=LEFT)
        rgbr.grid(row=2,column=2,sticky=SW,padx=1)
        rgbg=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=valg,highlightbackground="gray35",justify=LEFT)
        rgbg.grid(row=2,column=3,sticky=SW,padx=1)
	rgbb=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=valb,highlightbackground="gray35",justify=LEFT)
        rgbb.grid(row=2,column=4,sticky=SW,padx=1)

	labelhsv=Label(fr,text="hsv",anchor="nw",width=3,font=iofont,bg="gray35", fg=conchk).grid(row=3,column=1,sticky=N)

        hsvh=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=valh,highlightbackground="gray35",justify=LEFT)
        hsvh.grid(row=3,column=2,sticky=SW,padx=1)
        hsvs=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=vals,highlightbackground="gray35",justify=LEFT)
        hsvs.grid(row=3,column=3,sticky=SW,padx=1)
	hsvv=Entry(fr,font=iofont,width=3,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=valve,highlightbackground="gray35",justify=LEFT)
        hsvv.grid(row=3,column=4,sticky=SW,padx=1)
	
	conversion=colorsys.rgb_to_hsv(float(d1),float(d2),float(d3))

	self.drawColorPicker(self.bigc[impno],float(conversion[2]))
	self.crossPos(self.bigc[impno],self.smallc[impsmno],conversion[0],conversion[1],conversion[2])
	valr.set(d1)
	valg.set(d2)
	valb.set(d3)

	valh.set(str(conversion[0]))
	vals.set(str(conversion[1]))
	valve.set(str(conversion[2]))	


        rgbr.bind('<KeyRelease>',lambda event:self.rgb_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	rgbg.bind('<KeyRelease>',lambda event:self.rgb_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	rgbb.bind('<KeyRelease>',lambda event:self.rgb_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	
	
        hsvh.bind('<KeyRelease>',lambda event:self.hsv_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	hsvs.bind('<KeyRelease>',lambda event:self.hsv_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	hsvv.bind('<KeyRelease>',lambda event:self.hsv_headed_update(Node,parametername, self.bigc[impno],self.smallc[impsmno],valr,valg,valb,valh,vals,valve)   )
	
	self.smallc[impsmno].bind('<ButtonRelease-1>',lambda event:self.getLumaPicker(Node,parametername,self.smallc[impsmno],self.bigc[impno],event,valh,vals,valve,valr,valg,valb)   )
	self.bigc[impno].bind('<ButtonRelease-1>',lambda event:self.getColorPicker(Node,parametername,self.smallc[impsmno],self.bigc[impno],event,valh,vals,valve,valr,valg,valb)   )
	
        TargetCanvas.create_window(5,pos+5,window=fr,anchor="nw")
        return pos+190

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
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	ee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
	eee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";"  )   ))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerTextLine(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
	fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=10,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=20,bg="gray55",relief="groove",bd=1,state=sstate,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

    def controllerMatrix(self,TargetCanvas,Node,pos,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,parametername,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,conchk):
	sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=30,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=11,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
	
        e=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v1,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW,padx=3)
        ee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v2,highlightbackground="gray35",justify=LEFT)
        ee.grid(row=0,column=2,sticky=SW,padx=1)
	eee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v3,highlightbackground="gray35",justify=LEFT)
        eee.grid(row=0,column=3,sticky=SW,padx=1)
	eeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v4,highlightbackground="gray35",justify=LEFT)
        eeee.grid(row=0,column=4,sticky=SW,padx=1)
	
        re=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v5,highlightbackground="gray35",justify=LEFT)
        re.grid(row=1,column=1,sticky=SW,padx=3)
        ree=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v6,highlightbackground="gray35",justify=LEFT)
        ree.grid(row=1,column=2,sticky=SW,padx=1)
	reee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v7,highlightbackground="gray35",justify=LEFT)
        reee.grid(row=1,column=3,sticky=SW,padx=1)
	reeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v8,highlightbackground="gray35",justify=LEFT)
        reeee.grid(row=1,column=4,sticky=SW,padx=1)
	
        te=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v9,highlightbackground="gray35",justify=LEFT)
        te.grid(row=2,column=1,sticky=SW,padx=3)
        tee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v10,highlightbackground="gray35",justify=LEFT)
        tee.grid(row=2,column=2,sticky=SW,padx=1)
	teee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v11,highlightbackground="gray35",justify=LEFT)
        teee.grid(row=2,column=3,sticky=SW,padx=1)
	teeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v12,highlightbackground="gray35",justify=LEFT)
        teeee.grid(row=2,column=4,sticky=SW,padx=1)
	
        tre=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v13,highlightbackground="gray35",justify=LEFT)
        tre.grid(row=3,column=1,sticky=SW,padx=3)
        tree=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v14,highlightbackground="gray35",justify=LEFT)
        tree.grid(row=3,column=2,sticky=SW,padx=1)
	treee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v15,highlightbackground="gray35",justify=LEFT)
        treee.grid(row=3,column=3,sticky=SW,padx=1)
	treeee=Entry(fr,font=iofont,width=4,bg="gray55",relief="groove",state=sstate,bd=1,textvariable=v16,highlightbackground="gray35",justify=LEFT)
        treeee.grid(row=3,column=4,sticky=SW,padx=1)
	
	
	v1.set(d1)
	v2.set(d2)
	v3.set(d3)
	v4.set(d4)
	v5.set(d5)
	v6.set(d6)
	v7.set(d7)
	v8.set(d8)
	v9.set(d9)
	v10.set(d10)
	v11.set(d11)
	v12.set(d12)
	v13.set(d13)
	v14.set(d14)
	v15.set(d15)
	v16.set(d16)
		
	
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        ee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        eee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        eeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        re.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        ree.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        reee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        reeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        te.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        tee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        teee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        teeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        tre.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        tree.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        treee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))
        treeee.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, str(";"+str(v1.get())+";"+str(v2.get())+";"+ str(v3.get())+";" + str(v4.get())+";"+ str(v5.get())+";"+ str(v6.get())+";"+ str(v7.get())+";"+ str(v8.get())+";"+ str(v9.get())+";"+ str(v10.get())+";"+ str(v11.get())+";"+ str(v12.get())+";"+ str(v13.get())+";"+ str(v14.get())+";"+ str(v15.get())+";"+ str(v16.get())+";" )   ))

        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+100

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

    def _masTextSave(self,Node,textzone,parametername):
        a=str(textzone.get(1.0,END))[:-1]
        self.ChangeSettings(Node, "Data",parametername, a)

    def numval(self,event,v):
            if event.char in "1234567890.,":
                pass
            elif event.keycode==36:
                pass
            else:
                q=v.get()
                w=str(q)
                er=w[:-1]
                v.set(er)

    def controllerNumberSimple(self,TargetCanvas,Node,pos,variable,parametername,defaultvalue,conchk):
        sstate="normal"
        if conchk=="darkred":
          sstate="disabled"
        fr=Frame(TargetCanvas,height=10,width=145,bg="gray35",bd=0)
        fr.grid
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize) )
        Label(fr,text=parametername+":",anchor="nw",width=15,font=iofont,bg="gray35", fg=conchk).grid(row=0,column=0,pady=2)
        e=Entry(fr,font=iofont,width=15,bg="gray55",state=sstate,relief="groove",bd=1,textvariable=variable,highlightbackground="gray35",justify=LEFT)
        e.grid(row=0,column=1,sticky=SW)
        variable.set(defaultvalue)
        e.bind('<KeyRelease>',lambda event:self.ChangeSettings(Node, "Data",parametername, variable.get()))
        TargetCanvas.create_window(5,pos,window=fr,anchor="nw")
        return pos+30

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

    def resetPreferencePlane(self,TargetCanvas):
        TargetCanvas.delete(ALL)
        self.controllerNodeHeader(TargetCanvas)
        self.nodeInPreferences.set("OpenAssembler")
        def killer(self):
            pass
        TargetCanvas.bind("<B1-Motion>",killer)

    def loadPreferences(self,TargetCanvas,Node):
        TargetCanvas.delete(ALL)
        self.controllerNodeHeader(TargetCanvas)
        def handlerRelease(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B1-ButtonRelease>", handlerRelease)

        def handlerB1Move(event, self=self, TargetCanvas=TargetCanvas):
            if (TargetCanvas.bbox(ALL)[3]>=(10-(event.y - self.lasty))) and (TargetCanvas.bbox(ALL)[1]<=(260-(event.y - self.lasty))):
                TargetCanvas.move (ALL,0, event.y - self.lasty)
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<B1-Motion>",handlerB1Move)
        datas=self.examineSettings(Node)
        self.nodeInPreferences.set(datas[0][0])
        height=35
        string=[]
        inter=[]
        db=[]
        conchk="gray90"
        for n in range(0,len(datas)):
	        conchk="gray90"
		datatogive=datas[n][2]
                if str(datatogive)[:1]==":":
		  datatogive=str(str(datas[n][2]).split("#",1)[1])
	    	  conchk="darkred"
		else:
		  datatogive=datas[n][2]
		        
        	if datas[n][3]=="Path" or datas[n][3]=="file":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerPath(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="color":
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())		    
            	    m=len(string)
		    de=str(datatogive).strip(";").split(";")
		    if len(de)<3:
		    	de=["0","0","0"]
		    height=self.controllerColor(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],datas[n][1],de[0],de[1],de[2],conchk,string[m-4],string[m-5],string[m-6])


        	elif datas[n][3]=="vector" or datas[n][3]=="point" or datas[n][3]=="vvector" or datas[n][3]=="avector" or datas[n][3]=="vpoint" or datas[n][3]=="apoint" or datas[n][3]=="avvector":
		    string.append(StringVar())
		    string.append(StringVar())
		    string.append(StringVar())
            	    m=len(string)
		    de=str(datatogive).strip(";").split(";")
		    if len(de)<3:
		    	de=["0","0","0"]
		    height=self.controllerVectorPoint(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],datas[n][1],de[0],de[1],de[2],conchk)

        	elif datas[n][3]=="string":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerTextLine(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="matrix" or datas[n][3]=="amatrix":
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    string.append(StringVar())
            	    m=len(string)
		    dd=str(datatogive).strip(";").split(";")
		    if len(dd)<16:
		    	dd=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]		    
            	    height=self.controllerMatrix(TargetCanvas,Node,height,string[m-1],string[m-2],string[m-3],string[m-4],string[m-5],string[m-6],string[m-7],string[m-8],string[m-9],string[m-10],string[m-11],string[m-12],string[m-13],string[m-14],string[m-15],string[m-16],datas[n][1],dd[0],dd[1],dd[2],dd[3],dd[4],dd[5],dd[6],dd[7],dd[8],dd[9],dd[10],dd[11],dd[12],dd[13],dd[14],dd[15],conchk)

        	elif datas[n][3]=="longstring":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerMassText(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif datas[n][3]=="Separator":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerSeparator(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)

        	elif (datas[n][3]=="int") or (datas[n][3]=="vfloat") or (datas[n][3]=="aint") or (datas[n][3]=="afloat") or (datas[n][3]=="avfloat") or (datas[n][3]=="vint") or (datas[n][3]=="float"):
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerNumberSimple(TargetCanvas,Node,height,string[m-1],datas[n][1],datatogive,conchk)
		    
        	elif datas[n][3]=="geo" or datas[n][3]=="curve" or datas[n][3]=="surface" or datas[n][3]=="mesh" or datas[n][3]=="amesh":
            	    string.append(StringVar())
            	    m=len(string)
            	    height=self.controllerPassThrou(height)

        	elif datas[n][3]=="bool":
            	    inter.append(StringVar())
            	    z=len(inter)
            	    height=self.controllerBoolean(TargetCanvas,Node,height,inter[z-1],datas[n][1],None,conchk)
            	    if str(datatogive)=="True":
            	        inter[z-1].set("True")
            	    else:
            	        inter[z-1].set("False")
        	else:
			pass


class CanvasInitPreferencePanel:

    def controllerNodeHeader(self,TargetCanvas):
        fr=Frame(TargetCanvas,bg="gray35")
        fr.grid()
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize)+2 )
        label=Label(fr,textvariable=self.nodeInPreferences,anchor="nw",width=29,font=iofont,bg="gray15",fg="gray90",relief="flat")
        label.grid()
        TargetCanvas.create_window(5,5,window=fr,anchor="nw",tag="header")

    def StartUpPreferencePanelCanvas(self):
        TargetCanvas = Canvas (self, width=300, height=792,relief=GROOVE, cursor="draft_large", confine="false",bg="gray35",bd=2)
        TargetCanvas.grid(row=1,column=2,rowspan=129,sticky=N)
        def handlerB1Click(event, self=self, TargetCanvas=TargetCanvas):
            self.lastx=event.x
            self.lasty=event.y
        TargetCanvas.bind("<Button-1>", handlerB1Click)
        self.controllerNodeHeader(TargetCanvas)
        return TargetCanvas

