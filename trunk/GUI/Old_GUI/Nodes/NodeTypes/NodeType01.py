from Tkinter import *
import tkFont

class NodeType01:
    def BasicShape01(self,TargetCanvas,ID,NodeUpperLabel,FuctionType,Input,Output,Color,x,y):
        BaseColorBottom="gray80"
        BaseColorTop="gray20"
        BaseColorCenter=Color
        iofont = tkFont.Font ( family=self.font, size=self.fontsize-4 )
        sizex=150
        if len(Input)>len(Output):
            sizey=40+len(Input)*30+20
        elif len(Input)<len(Output):
            sizey=40+len(Output)*30+20
        else:
            sizey=40+len(Output)*30+20

        if sizey<70:
            sizey=70

        TargetCanvas.create_polygon(x,y,x,y,x+sizex-20,y,x+sizex-20,y,x+sizex,y,x+sizex,y+20,x+sizex,y+20,x,y+20,x,y+20,smooth=1,splinesteps=12,width=1,fill=BaseColorTop,outline="gray20",tag=(str(ID),"UPPERPART",str(FuctionType),"",ID+"select"))
        TargetCanvas.create_text(x+int(sizex/2),y+10,text=NodeUpperLabel,font=iofont,fill="gray95",tag=(str(ID),"UPPERLABEL",str(FuctionType),NodeUpperLabel,ID+"select"))

        TargetCanvas.create_polygon(x,y+sizey-20,x,y+sizey-20,x+sizex,y+sizey-20,x+sizex,y+sizey-20,x+sizex,y+sizey,x+sizex,y+sizey,x+20,y+sizey,x+20,y+sizey,x,y+sizey,smooth=1,splinesteps=12,width=1,fill=BaseColorBottom,outline="gray20",tag=(str(ID),"BOTTOMPART",str(FuctionType),"",ID+"select"))

        TargetCanvas.create_rectangle(x,y+20,x+sizex,y+sizey-20,fill=BaseColorCenter,width=1,outline="",tag=(str(ID),"CENTERPART",str(FuctionType),"",ID+"select"))
        TargetCanvas.create_line(x,y+20,x,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"LEFTLINE",str(FuctionType),"",ID+"select"))
        TargetCanvas.create_line(x+7,y+20,x+7,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"LEFTSeparatorLINE",str(FuctionType),"",ID+"select"))

        TargetCanvas.create_line(x+sizex,y+20,x+sizex,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"RIGHTLINE",str(FuctionType),"",ID+"select"))
        TargetCanvas.create_line(x+sizex-7,y+20,x+sizex-7,y+sizey-20,width=1,fill="gray20",tag=(str(ID),"RIGHTSeparatorLINE",str(FuctionType),"",ID+"select"))

        n=1
        while n<=len(Input):
                    kockacolor="gray80"
                    TargetCanvas.create_rectangle(x,y+n*30,x+7,y+n*30+20,fill=kockacolor,width=1,outline="black",tag=(str(ID),str(ID)+Input[n-1],Input[n-1],"IN",ID+"select"))
                    TargetCanvas.create_text(x+10,y+n*30+10,anchor="w",justify="center",font=iofont,text=Input[n-1],tag=(str(ID),"INPUTTEXT"+str(n),str(FuctionType),NodeUpperLabel+"in",ID+"select"))
                    n=n+1

        n=1
        while n<=len(Output):
                    kockacolor="gray80"
                    TargetCanvas.create_rectangle(x+sizex-7,y+n*30,x+sizex,y+n*30+20,fill=kockacolor,width=1,outline="black",tag=(str(ID),str(ID)+Output[n-1],Output[n-1],"OUT",ID+"select"))
                    TargetCanvas.create_text(x+sizex-10,y+n*30+10,anchor="e",justify="center",font=iofont,text=Output[n-1],tag=(str(ID),"OUTPUTTEXT"+str(n),str(FuctionType),NodeUpperLabel+"out",ID+"select"))
                    n=n+1

        #TargetCanvas.create_oval(x+4,y+4,x+16,y+16,fill="red",width=2,outline="darkred",tag=(str(ID),"CLOSEBUTTON",str(FuctionType),"",ID+"select"))
        #TargetCanvas.create_oval(x+sizex-16,y+4,x+sizex-4,y+16,fill="grey55",width=2,outline="gray25",tag=(str(ID),"NOTEBUTTON",str(FuctionType),"",ID+"select"))
        #TargetCanvas.create_oval(x+sizex-16,y+sizey-16,x+sizex-4,y+sizey-4,fill="orange",width=2,outline="darkorange",tag=(str(ID),"PREFERENCESBUTTON",str(FuctionType),"",ID+"select"))
        #TargetCanvas.create_oval(x+4,y+sizey-16,x+16,y+sizey-4,fill="green",width=2,outline="darkgreen",tag=(str(ID),"RUNBUTTON",str(FuctionType),"",ID+"select"))

        TargetCanvas.scale((ID+"select"),self.lastx,self.lasty,self.GlobalScale,self.GlobalScale)











