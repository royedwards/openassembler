#------------------------------------------------------------------------------------------------------------------------------------
#
#    Node Elements for OpenAssembler.
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------


from Tkinter import *
from Dbase.DBaseManagement import RuntimeNodeRegister


class GUI_Elements_forNodes(RuntimeNodeRegister):

    def AddNodeRenamer(self,event,TargetCanvas,Eventtag):
        startText=Eventtag[3]
        print startText
        print Eventtag
        ID=Eventtag[0]
        askwindow = Toplevel(bg="gray55")
        askwindow.title('Change '+startText+' to:')
        askentry = Entry(askwindow,bg="gray55",width=60)
        askentry.grid(row=1)
        askentry.master.wm_resizable(width=False ,height=False)
        def enterEvent(event):
            if askentry.get() == "":
                pass
            else:
                if self.ChangeRuntimeNodeName(ID, askentry.get()) == "true":
                    if self.nodeInPreferences.get()==startText:
                       self.nodeInPreferences.set(askentry.get())
                    print "Node " + ID + " has new name: " + askentry.get()
                    TargetCanvas.itemconfig(startText, text=askentry.get(),tag=(Eventtag[0],Eventtag[1],Eventtag[2],askentry.get(),Eventtag[4]))
                    TargetCanvas.dtag(startText)
                    askwindow.destroy()
                else:
                    pass
        def escEvent(event):
            askwindow.destroy()
        askwindow.bind("<Return>", enterEvent)
        askwindow.bind("<Escape>",escEvent)


    def RemoveNodeRenamer(self,event,TargetCanvas):
        TargetCanvas.delete('RENAMERENTRY')