from Nodes.NodeTypes.NodeVarInit import NodeVarInit
from Dbase.DBaseManagement import RuntimeNodeRegister
from WindowFrames.PreferencePanel import LoadPreferences



class ConnectLine(NodeVarInit,RuntimeNodeRegister,LoadPreferences):

    def DrawLine(self,TargetCanvas,x1,y1,x2,y2,tagger):
        px1=x1
        px2=((x1+x2)/2)
        px4=x2

        py1=y1
        py4=y2

        TargetCanvas.create_line(px1,py1,px1+px2/5,py1,(px4-px2/5),py4, px4,py4,fill="gray25",width=2,smooth=1,tag=tagger)
        TargetCanvas.tag_lower(tagger)


    def DrawTMPLine(self,TargetCanvas,Eventtag,lastx,lasty):
        try:
            TargetCanvas.delete("LineUnderCreateTMP")
        except:
            pass

        tmp_BB=TargetCanvas.bbox(Eventtag[1])
        tmp_center_x= tmp_BB[0]+(tmp_BB[2]-tmp_BB[0])/2
        tmp_center_y= tmp_BB[1]+(tmp_BB[3]-tmp_BB[1])/2
        self.DrawLine(TargetCanvas, tmp_center_x,tmp_center_y,lastx,lasty,"LineUnderCreateTMP")

    def DrawNewLine(self,TargetCanvas,Fromnode,output,uni_out,Tonode,input,uni_in):
        if Fromnode==Tonode:
            print "Redundant connections not allowed!!!"
        else:
            tmp_BB_out=TargetCanvas.bbox((str(uni_out)))
            tmp_out_center_x= tmp_BB_out[0]+(tmp_BB_out[2]-tmp_BB_out[0])/2
            tmp_out_center_y= tmp_BB_out[1]+(tmp_BB_out[3]-tmp_BB_out[1])/2
            tmp_BB_in=TargetCanvas.bbox((str(uni_in)))
            tmp_in_center_x= tmp_BB_in[0]+(tmp_BB_in[2]-tmp_BB_in[0])/2
            tmp_in_center_y= tmp_BB_in[1]+(tmp_BB_in[3]-tmp_BB_in[1])/2
            lineID=self._NewNodeID()
            for n in range (0,(len(self.RuntimeLines))):
                if (str(self.RuntimeLines[n][6])== str(uni_in)):
                    if self.checkIfMultiNode(Tonode, input)=="False":
                        self.DeleteItem(TargetCanvas,self.RuntimeLines[n][0])
                    else:
                        pass
                else:
                    pass
            self.RegisterLine(lineID,Fromnode,output,uni_out,Tonode,input,uni_in)
            self.writeConnections(Tonode, input,Fromnode,output ,lineID)
            self.DrawLine(TargetCanvas, tmp_out_center_x,tmp_out_center_y,tmp_in_center_x,tmp_in_center_y,(lineID,Fromnode,Tonode,"line",(str(lineID)+"select")))
            TargetCanvas.tag_lower((str(lineID)+"select"))
            print "Connect(" +str(lineID)+ "): " + uni_out + " ---> " + uni_in

    def _reDrawLine(self,TargetCanvas,lineID,Fromnode,output,uni_out,Tonode,input,uni_in):
            tmp_BB_out=TargetCanvas.bbox(str(uni_out))
            tmp_out_center_x= tmp_BB_out[0]+(tmp_BB_out[2]-tmp_BB_out[0])/2
            tmp_out_center_y= tmp_BB_out[1]+(tmp_BB_out[3]-tmp_BB_out[1])/2
            tmp_BB_in=TargetCanvas.bbox(str(uni_in))
            tmp_in_center_x= tmp_BB_in[0]+(tmp_BB_in[2]-tmp_BB_in[0])/2
            tmp_in_center_y= tmp_BB_in[1]+(tmp_BB_in[3]-tmp_BB_in[1])/2
            self.DrawLine(TargetCanvas, tmp_out_center_x,tmp_out_center_y,tmp_in_center_x,tmp_in_center_y,(lineID,Fromnode,Tonode,"line",(str(lineID)+"select")))
            TargetCanvas.tag_lower((str(lineID)+"select"))

    def RedrawLines(self,TargetCanvas,ActionNode):
        for n in range (0,(len(self.RuntimeLines))):
            if self.RuntimeLines[n][1]== ActionNode:
                    TargetCanvas.delete((str(self.RuntimeLines[n][0])+"select"))
                    self._reDrawLine(TargetCanvas, str(self.RuntimeLines[n][0]), self.RuntimeLines[n][1], self.RuntimeLines[n][2], self.RuntimeLines[n][3], self.RuntimeLines[n][4], self.RuntimeLines[n][5], self.RuntimeLines[n][6])

            else:
                pass

        for n in range (0,(len(self.RuntimeLines))):
            if str(self.RuntimeLines[n][4])== str(ActionNode):
                    TargetCanvas.delete((str(self.RuntimeLines[n][0])+"select"))
                    self._reDrawLine(TargetCanvas, self.RuntimeLines[n][0], self.RuntimeLines[n][1], self.RuntimeLines[n][2], self.RuntimeLines[n][3], self.RuntimeLines[n][4], self.RuntimeLines[n][5], self.RuntimeLines[n][6])

            else:
                pass

