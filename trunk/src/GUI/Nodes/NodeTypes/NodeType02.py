from Tkinter import *
import tkFont


class NodeType02:
    def __init__(self):
        pass

    def _name(self):
        return "NodeType02"

    def BasicShape02(self,InputParameters):
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
        iofont = tkFont.Font ( family="Keyboard", size=4 )
        sizex=150
        if len(Input)>len(Output):
            sizey=40+len(Input)*30+20
        elif len(Input)<len(Output):
            sizey=40+len(Output)*30+20
        else:
            sizey=40+len(Output)*30+20

        if sizey<70:
            sizey=70

        TargetCanvas.create_polygon(x,y,x,y,x+sizex-20,y,x+sizex-20,y,x+sizex,y,x+sizex,y+20,x+sizex,y+20,x,y+20,x,y+20,smooth=1,splinesteps=12,width=1,fill=BaseColorTop,outline="gray20",tag=(str(ID),"UPPERPART",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_text(x+int(sizex/2),y+10,text=NodeUpperLabel,font=iofont,tag=(str(ID),"UPPERLABEL",str(FuctionType),NodeUpperLabel,NodeUpperLabel+"select"))

        TargetCanvas.create_polygon(x,y+sizey-20,x,y+sizey-20,x+sizex,y+sizey-20,x+sizex,y+sizey-20,x+sizex,y+sizey,x+sizex,y+sizey,x+20,y+sizey,x+20,y+sizey,x,y+sizey,smooth=1,splinesteps=12,width=1,fill=BaseColorBottom,outline="gray20",tag=(str(ID),"BOTTOMPART",str(FuctionType),"",NodeUpperLabel+"select"))

        TargetCanvas.create_rectangle(x,y+20,x+sizex,y+sizey-21,fill=BaseColorCenter,width=1,outline="",tag=(str(ID),"CENTERPART",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_line(x,y+20,x,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"LEFTLINE",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_line(x+7,y+20,x+7,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"LEFTSeparatorLINE",str(FuctionType),"",NodeUpperLabel+"select"))

        TargetCanvas.create_line(x+sizex,y+20,x+sizex,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"RIGHTLINE",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_line(x+sizex-7,y+20,x+sizex-7,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"RIGHTSeparatorLINE",str(FuctionType),"",NodeUpperLabel+"select"))

        n=1
        while n<=len(Input):
                    TargetCanvas.create_rectangle(x,y+n*30,x+7,y+n*30+20,fill=BaseColorTop,width=1,outline="black",tag=(str(ID),str(ID)+Input[n-1],Input[n-1],"IN",NodeUpperLabel+"select"))
                    TargetCanvas.create_text(x+10,y+n*30+10,anchor="w",justify="center",font=iofont,text=Input[n-1],tag=(str(ID),"INPUTTEXT"+str(n),str(FuctionType),NodeUpperLabel+"in",NodeUpperLabel+"select"))
                    n=n+1

        n=1
        while n<=len(Output):
                    TargetCanvas.create_rectangle(x+sizex-7,y+n*30,x+sizex,y+n*30+20,fill=BaseColorBottom,width=1,outline="black",tag=(str(ID),str(ID)+Output[n-1],Output[n-1],"OUT",NodeUpperLabel+"select"))
                    TargetCanvas.create_text(x+sizex-10,y+n*30+10,anchor="e",justify="center",font=iofont,text=Output[n-1],tag=(str(ID),"OUTPUTTEXT"+str(n),str(FuctionType),NodeUpperLabel+"out",NodeUpperLabel+"select"))
                    n=n+1


        TargetCanvas.create_oval(x+4,y+4,x+16,y+16,fill="red",width=2,outline="darkred",tag=(str(ID),"CLOSEBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+sizex-16,y+4,x+sizex-4,y+16,fill="grey55",width=2,outline="gray25",tag=(str(ID),"NOTEBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+sizex-16,y+sizey-16,x+sizex-4,y+sizey-4,fill="orange",width=2,outline="darkorange",tag=(str(ID),"PREFERENCESBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))
        TargetCanvas.create_oval(x+4,y+sizey-16,x+16,y+sizey-4,fill="green",width=2,outline="darkgreen",tag=(str(ID),"RUNBUTTON",str(FuctionType),"",NodeUpperLabel+"select"))

        TargetCanvas.scale((NodeUpperLabel+"select"),self.lastx,self.lasty,self.GlobalScale,self.GlobalScale)

    def PreviewShape02(self,InputParameters):
        TargetCanvas=InputParameters[0]
        ID=InputParameters[1]
        x=InputParameters[2][0]
        y=InputParameters[2][1]
        Ident=InputParameters[3]
        #Type=InputParameters[4]
        Note=InputParameters[5][3]
        NodeCenterLabel=InputParameters[5][2]
        BaseColorBottom=InputParameters[5][6]
        BaseColorTop=InputParameters[5][5]
        BaseColorCenter=InputParameters[5][4]

        FunctionType=InputParameters[4]

        TargetCanvas.create_polygon(x,y,x,y,x+65,y,x+65,y,x+80,y,x+80,y+15,x+80,y+15,x,y+15,x,y+15,smooth=1,splinesteps=1,width=2,fill=BaseColorTop,outline="gray20",tag=(ID,FunctionType,Ident,Note))
        TargetCanvas.create_polygon(x+80,y+65,x+80,y+65,x+80,y+80,x+80,y+80,x+15,y+80,x+15,y+80,x,y+80,x,y+65,x,y+65,smooth=1,splinesteps=1,width=2,fill=BaseColorBottom,outline="gray20",tag=(ID,FunctionType,Ident,Note))

        TargetCanvas.create_rectangle(x,y+15,x+80,y+65,fill=BaseColorCenter,width=2,outline="",tag=(ID,FunctionType,Ident,Note))
        TargetCanvas.create_line(x,y+15,x,y+65,width=2,fill="gray20",tag=(ID,FunctionType,Ident,Note))
        TargetCanvas.create_line(x+80,y+15,x+80,y+65,width=2,fill="gray20",tag=(ID,FunctionType,Ident,Note))
        TargetCanvas.create_text(x+40,y+42,text=NodeCenterLabel,tag=(ID,FunctionType,Ident,Note))










