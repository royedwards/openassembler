from Tkinter import *
import tkFont

#
#   no-input no-output node
#
#


class NodeType01:
    def __init__(self):
        pass

    def _name(self):
        return "NodeType01"

    def BasicShape01(self,InputParameters):
        ID=InputParameters[1]
        TargetCanvas=InputParameters[0]
        Input=InputParameters[5][7]
        Output=InputParameters[5][8]
        NodeUpperLabel=str(InputParameters[5][1])+str(InputParameters[1])
        NodeCenterLabel=InputParameters[5][2]
        BaseColorBottom=InputParameters[5][6]
        BaseColorTop=InputParameters[5][4]
        BaseColorCenter=InputParameters[5][5]
        x=InputParameters[2][0]
        y=InputParameters[2][1]
        FuctionType=InputParameters[4]
        iofont = tkFont.Font ( family="system", size=4 )
        sizex=180
        sizey=70

        TargetCanvas.create_polygon(x,y,x,y,x+sizex-20,y,x+sizex-20,y,x+sizex,y,x+sizex,y,x+sizex,y+20,x+sizex,y+20,x,y+20,x,y+20,smooth=1,splinesteps=12,width=1,fill=BaseColorTop,outline="gray20",tag=(str(ID),"UPPERPART",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_text(x+int(sizex/2),y+10,text=NodeUpperLabel,font=iofont,tag=(str(ID),"UPPERLABEL",str(FuctionType),NodeUpperLabel,NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+4,y+4,x+16,y+16,fill="red",width=2,outline="darkred",tag=(str(ID),"CLOSEBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+sizex-16,y+4,x+sizex-4,y+16,fill="grey55",width=2,outline="gray25",tag=(str(ID),"NOTEBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+sizex-32,y+4,x+sizex-20,y+16,fill="orange",width=2,outline="darkorange",tag=(str(ID),"PREFERENCESBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+20,y+4,x+32,y+16,fill="green",width=2,outline="darkgreen",tag=(str(ID),"RUNBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))

        TargetCanvas.scale((NodeUpperLabel+"select"),self.lastx,self.lasty,self.GlobalScale,self.GlobalScale)

    def PreviewShape01(self,InputParameters):
        TargetCanvas=InputParameters[0]
        ID=InputParameters[1]
        x=InputParameters[2][0]
        y=InputParameters[2][1]
        Ident=InputParameters[3]
        Note=InputParameters[5][3]
        NodeCenterLabel=InputParameters[5][2]
        BaseColorBottom=InputParameters[5][6]
        BaseColorTop=InputParameters[5][5]
        BaseColorCenter=InputParameters[5][4]

        FunctionType=InputParameters[4]

        TargetCanvas.create_polygon(x,y,x,y,x+65,y,x+65,y,x+80,y,x+80,y,x+80,y+15,x+80,y+15,x,y+15,x,y+15,smooth=1,splinesteps=1,width=2,fill=BaseColorTop,outline="gray20",tag=(ID,FunctionType,Ident,Note))

        TargetCanvas.create_text(x+40,y+42,text=NodeCenterLabel,tag=(ID,FunctionType,Ident,Note))










