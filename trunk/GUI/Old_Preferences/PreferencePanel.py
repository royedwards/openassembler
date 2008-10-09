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
    def Preferences_Loader(self):
    	pass

class CanvasInitPreferencePanel:

    def StartUpPreferencePanelCanvas(self):
        
        fr=Frame(self,bg="gray35",relief=GROOVE,bd=2)
        fr.grid(column=0,row=0)
        iofont = tkFont.Font ( family=self.font, size=int(self.fontsize)+2 )
        label=Label(fr,textvariable=self.nodeInPreferences,anchor="nw",width=44,font=iofont,bg="gray15",fg="gray90",relief="flat")
        label.grid()	

	prefscroll=Scrollbar(self,orient="vertical")
	prefscroll.grid(column=1,row=0,rowspan=2,sticky=N+S)
	TargetCanvas = Canvas (self, width=445, height=500,bg="gray35",yscrollcommand=prefscroll.set)
     	TargetCanvas.grid(column=0,row=1, sticky=N+S+E+W)
	prefscroll.config(command=TargetCanvas.yview)

	self.grid_rowconfigure(1, weight=1)
	self.grid_columnconfigure(0, weight=1)

	ParameterFrame=Frame(TargetCanvas)
	ParameterFrame.rowconfigure(0, weight=1)
	ParameterFrame.columnconfigure(0, weight=1)
	
	# here the stuff comes... it is important!!!
			
	TargetCanvas.create_window(0, 0, anchor=NW, window=ParameterFrame)
	
	# and this is the msot important.... it takes me 1 hour to find out why it is not working
	
	ParameterFrame.update_idletasks()

	TargetCanvas.config(scrollregion=TargetCanvas.bbox("all"))

        return ParameterFrame

