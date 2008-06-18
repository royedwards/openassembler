#------------------------------------------------------------------------------------------------------------------------------------
#
#    Dbase management for OpenAssembler. XML is used to store date.
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#------------------------------------------------------------------------------------------------------------------------------------

from xml.dom import minidom


#------------------------------------------------------------------------------------------------------------------------------------
#    Global file structure variables
#------------------------------------------------------------------------------------------------------------------------------------

RUNTIME_NODELIST_FOLDER="/home/user/temp"
GUI_SETTINGS_FOLDER="/home/user/workspace/OpenAssembler/DBase/GUI"


#------------------------------------------------------------------------------------------------------------------------------------
#    General script to find a specific node in an XML file
#------------------------------------------------------------------------------------------------------------------------------------

def FindNamedNode(inBranch,nameToFind):
            outro=-1
            for  n in range  (0,inBranch.childNodes.length):
                if (str(inBranch.childNodes[n].nodeName))==nameToFind:
                    outro=n
            if outro==-1:
                print ("Error in segment: " +str(inBranch)+str(inBranch.parentNode)+str(inBranch.parentNode.parentNode))
                print "There is some problem with the xml structure... now quiting...."
                exit()
            return outro

#------------------------------------------------------------------------------------------------------------------------------------
#    Class to handle runtime data management
#------------------------------------------------------------------------------------------------------------------------------------
class openScene:

    def OpenCopyNode(self,openfile,Node):
        rootdoc=minidom.parse(openfile)
        root=rootdoc.documentElement
        tocopy = (root.childNodes[FindNamedNode(root,("Node"+str(Node)))].cloneNode(1))
        rootdoc2=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root_runtime=rootdoc2.documentElement
        root_runtime.appendChild(tocopy)
        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root_runtime.toxml())
        xmlfileoutput.close()
        root.unlink
        root_runtime.unlink


    def OpenexamineSettings(self,openfile,Node):
        returnvalue=[]
        rootdoc=minidom.parse(openfile)
        root=rootdoc.documentElement
        nodename = (root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("Name"))
        counter=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes.length
        for n in range (0,counter):
            attrname = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].nodeName
            attrvalu = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].firstChild.nodeValue
            attrtype = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].getAttribute("Type")
            set=(str(nodename),str(attrname),str(attrvalu),str(attrtype))
            returnvalue.append(set)
        root.unlink
        return returnvalue

    def OpenGetIDList(self,infile):
        rootdoc=minidom.parse(infile)
        root=rootdoc.documentElement
        IDList=[]
        runno=root.childNodes.length
        for n in range (0,runno):
            idval=str(root.childNodes[n].nodeName)
            if str(idval)=="Node0000000":
                pass
            else:
                IDList.append(idval[4:])
        return IDList

    def OpenGetFuncType(self,infile,ID):
        rootdoc=minidom.parse(infile)
        root=rootdoc.documentElement
        functy=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("FuncType")
        root.unlink
        return functy

    def OpenGetgenerationDataforLines(self,infile,ID):
        rootdoc=minidom.parse(infile)
        root=rootdoc.documentElement
        fromnode=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("FromNode")
        fromnodeout=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("FromNode-Output")
        fromnodeuni=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("Uni_Out")
        tonode=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("ToNode")
        tonodein=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("ToNode-Input")
        tonodeuni=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("Uni_In")
        root.unlink
        retu=(fromnode,fromnodeout,fromnodeuni,tonode, tonodein,tonodeuni)
        return retu

    def OpensettingsforGeneration(self,infile,ID,TargetCanvas):
        rootdoc=minidom.parse(infile)
        root=rootdoc.documentElement
        functy=root.childNodes[FindNamedNode(root,("Node"+str(ID)))].getAttribute("FuncType")
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(ID)))]
        actuelleGen=actuellenode.childNodes[FindNamedNode(actuellenode,("Generation"))]
        poss=actuelleGen.childNodes[FindNamedNode(actuelleGen,("Position"))]
        posix=poss.childNodes[FindNamedNode(poss,("X"))].firstChild.nodeValue
        posiy=poss.childNodes[FindNamedNode(poss,("Y"))].firstChild.nodeValue
        root.unlink
        generated=self.OpenGenerateVars(TargetCanvas,ID,int(posix),int(posiy),"MAIN",str(functy))
        return generated

class PreferencesManagement:

    def examineSettings(self,Node):
        returnvalue=[]
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        nodename = (root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("Name"))
        counter=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes.length
        for n in range (0,counter):
            attrname = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].nodeName
            attrvalu = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].firstChild.nodeValue
            attrtype = root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],"Data")].childNodes[n].getAttribute("Type")
            set=(str(nodename),str(attrname),str(attrvalu),str(attrtype))
            returnvalue.append(set)
            #print attrname +" -- "+attrvalu+"  --  "+attrtype
            #print root.toprettyxml()
        root.unlink
        return returnvalue

    def getNodeNote(self,Node):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        nodename = (root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("Name"))
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))]
        actuelleGen=actuellenode.childNodes[FindNamedNode(actuellenode,("Generation"))]
        labels=actuelleGen.childNodes[FindNamedNode(actuelleGen,("Labels"))]
        notevalue=labels.childNodes[FindNamedNode(labels,("Note"))].firstChild.nodeValue
        root.unlink
        set=(str(nodename),str(notevalue))
        return set

    def ChangeNote(self,Node,newvalue):
        if str(newvalue)=='':
            pass
        else:
            if Node=="0000000":
                rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
                root=rootdoc.documentElement
                actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))]
                actuelleGen=actuellenode.childNodes[FindNamedNode(actuellenode,("Data"))]
                notevalue=actuelleGen.childNodes[FindNamedNode(actuelleGen,("Note"))].firstChild.nodeValue=str(newvalue)
                xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
                xmlfileoutput.write(root.toxml())
                xmlfileoutput.close()
                root.unlink
            else:
                rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
                root=rootdoc.documentElement
                actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))]
                actuelleGen=actuellenode.childNodes[FindNamedNode(actuellenode,("Generation"))]
                labels=actuelleGen.childNodes[FindNamedNode(actuelleGen,("Labels"))]
                notevalue=labels.childNodes[FindNamedNode(labels,("Note"))].firstChild.nodeValue=str(newvalue)
                print "Node"+str(Node)+"."+"Note"+" set to: "+labels.childNodes[FindNamedNode(labels,("Note"))].firstChild.nodeValue
                xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
                xmlfileoutput.write(root.toxml())
                xmlfileoutput.close()
                root.unlink


    def ChangeSettings(self,Node,container,controller,newvalue):
        if str(newvalue)=='':
            pass
        else:
            rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
            root=rootdoc.documentElement
            actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,("Node"+str(Node)))],container)]
            controllerlink=actuellenode.childNodes[FindNamedNode(actuellenode,str(controller))]
            controllerlink.firstChild.nodeValue=str(newvalue)
            print "Node"+str(Node)+"."+str(controller)+" set to: "+controllerlink.firstChild.nodeValue
            xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
            xmlfileoutput.write(root.toxml())
            xmlfileoutput.close()
            root.unlink

class RuntimeNodeRegister:

    def runtimeDBasePath(self):
        x=(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        return x


    def CreateGlobalPreferences(self,startframe,endframe,note,etr):
        ID="Node0000000"

        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root_runtime=rootruntimedoc.documentElement

        runtimeNodeList_trick=minidom.getDOMImplementation()
        root_trick=runtimeNodeList_trick.createDocument("", "OpenAssemblerRuntimersx", "")

        mdn=root_trick.createElement(str(ID))
        root_trick.firstChild.appendChild(mdn)
        attr=root_trick.createAttribute("Name")
        attr.value="GlobalScenePreferences"
        mdn.setAttributeNode(attr)
        attr2=root_trick.createAttribute("FuncType")
        attr2.value="GlobalScenePreferences"
        mdn.setAttributeNode(attr2)

        data=root_trick.createElement("Data")
        mdn.appendChild(data)

        sf=root_trick.createElement("EndOfTheTree")
        sfx=root_trick.createTextNode(str(etr))
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="endTree"
        sf.setAttributeNode(attr3)


        sf=root_trick.createElement("Timing")
        sfx=root_trick.createTextNode("...")
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="Separator"
        sf.setAttributeNode(attr3)

        sf=root_trick.createElement("StartFrame")
        sfx=root_trick.createTextNode(str(startframe))
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="SFGlobal"
        sf.setAttributeNode(attr3)

        sf=root_trick.createElement("EndFrame")
        sfx=root_trick.createTextNode(str(endframe))
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="EFGlobal"
        sf.setAttributeNode(attr3)

        sf=root_trick.createElement("Misc")
        sfx=root_trick.createTextNode("...")
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="Separator"
        sf.setAttributeNode(attr3)

        sf=root_trick.createElement("Note")
        sfx=root_trick.createTextNode(str(note))
        sf.appendChild(sfx)
        data.appendChild(sf)
        attr3=root_trick.createAttribute("Type")
        attr3.value="sceneNote"
        sf.setAttributeNode(attr3)

        mroot=root_trick.firstChild.firstChild.cloneNode(1)
        root_runtime.appendChild(mroot)

        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root_runtime.toxml())
        xmlfileoutput.close()
        root_trick.unlink
        root_runtime.unlink

    def Create_RuntimeDBase(self):
        runtimeNodeList=minidom.getDOMImplementation()
        root=runtimeNodeList.createDocument("", "OpenAssemblerRuntimers", "")
        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root.toxml())
        xmlfileoutput.close()

    def GetIDList(self):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        IDList=[]
        runno=root.childNodes.length
        for n in range (0,runno):
            idval=str(root.childNodes[n].nodeName)
            if str(idval)=="Node0000000":
                pass
            else:
                IDList.append(idval[4:])
        return IDList

    def IDChc(self,NewID):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        NewIDd=("Node"+str(NewID))
        checker=-1
        runno=root.childNodes.length
        for n in range (0,runno):
            if (str(root.childNodes[n].nodeName))==str(NewIDd):
                checker=1
        if checker==1:
            return "false"
        else:
            return "true"

    def writeBackOneNodePosition(self,TargetCanvas,ID):
        functype=self.getNodeFuncType(ID)
        bb=TargetCanvas.bbox((str(functype)+str(ID)+"select"))
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(ID)))]
        actuelleGen=actuellenode.childNodes[FindNamedNode(actuellenode,("Generation"))]
        poss=actuelleGen.childNodes[FindNamedNode(actuelleGen,("Position"))]
        posix=poss.childNodes[FindNamedNode(poss,("X"))].firstChild.nodeValue=str(bb[0]*2-25)
        posiy=poss.childNodes[FindNamedNode(poss,("Y"))].firstChild.nodeValue=str(bb[1]*2-25)
        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root.toxml())
        xmlfileoutput.close()
        root.unlink

    def writeBackNodePositions(self,TargetCanvas):
        IDs=self.GetIDList()
        iis=self.GetIDList()
        for f in range(0,len(iis)):
            for h in range (0,len(self.RuntimeLines)):
                if str(self.RuntimeLines[h][0])==str(iis[f]):
                    IDs.remove(iis[f])


        for n in range (0,len(IDs)):
            self.writeBackOneNodePosition(TargetCanvas, IDs[n])

    def RegisterRuntimeNode(self,InputParameters):
        ID=("Node" + str(InputParameters[1]))
        Ident=InputParameters[3]
        NodeUpperLabel=(str(InputParameters[5][1])+str(InputParameters[1]))
        FunctionType=Functype=InputParameters[4]

        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root_runtime=rootruntimedoc.documentElement

        runtimeNodeList_trick=minidom.getDOMImplementation()
        root_trick=runtimeNodeList_trick.createDocument("", "OpenAssemblerRuntimersx", "")

        mdn=root_trick.createElement(str(ID))
        root_trick.firstChild.appendChild(mdn)
        attr=root_trick.createAttribute("Name")
        attr.value=NodeUpperLabel
        mdn.setAttributeNode(attr)
        attr2=root_trick.createAttribute("FuncType")
        attr2.value=Functype
        mdn.setAttributeNode(attr2)
        mroot=root_trick.firstChild.firstChild.cloneNode(1)
        root_runtime.appendChild(mroot)

        rootsettingdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
        root=rootsettingdoc.documentElement
        generation_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Generation")].cloneNode(1))
        Data_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Data")].cloneNode(1))
        source_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Source")].cloneNode(1))
        mroot.appendChild(generation_root)
        mroot.appendChild(Data_root)
        mroot.appendChild(source_root)
        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root_runtime.toxml())
        xmlfileoutput.close()
        root.unlink
        root_trick.unlink
        root_runtime.unlink
        del root, root_trick, root_runtime, xmlfileoutput, mroot, source_root, Data_root, generation_root

    def getNodeName(self,Node):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("Name")
        root.unlink
        del rootdoc, root
        return actuellenode

    def getNodeFuncType(self,Node):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("FuncType")
        root.unlink
        del rootdoc, root
        return actuellenode

    def getFrameRange(self):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node0000000"))]
        dta=actuellenode.childNodes[FindNamedNode(actuellenode,("Data"))]
        sf=dta.childNodes[FindNamedNode(dta,("StartFrame"))].firstChild.nodeValue
        ef=dta.childNodes[FindNamedNode(dta,("EndFrame"))].firstChild.nodeValue
        root.unlink
        del actuellenode, root, rootdoc, dta
        return (sf,ef)

    def _CHCRuntimeNodeName(self,ID,NewName):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        checker=-1
        runno=root.childNodes.length
        for n in range (0,runno):
            if (str(root.childNodes[n].getAttribute("Name")))==str(NewName):
                checker=1
        if checker==1:
            return "false"
        else:
            return "true"

    def DeleteLines(self,TargetCanvas,LineList):
        for n in range(0,len(LineList)):
            rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
            root_runtime=rootruntimedoc.documentElement
            for m in range (0,len(self.RuntimeLines)):
                if self.RuntimeLines[m][0]==LineList[n]:
                    if self.IDChc((self.RuntimeLines[m][4]))=="false":
                        actuellenode=root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(self.RuntimeLines[m][4])))]
                        datapart=actuellenode.childNodes[FindNamedNode(actuellenode,"Data")]
                        inp=datapart.childNodes[FindNamedNode(datapart,str(self.RuntimeLines[m][5]))].firstChild.nodeValue
                        if inp==(":"+str(LineList[n])):
                            datapart.childNodes[FindNamedNode(datapart,str(self.RuntimeLines[m][5]))].firstChild.nodeValue="..."
                        else:
                            pos=inp.find((":"+str(LineList[n])))
                            cc=len((":"+str(LineList[n])))
                            ret=inp[:pos]+inp[(pos+cc):]
                            datapart.childNodes[FindNamedNode(datapart,str(self.RuntimeLines[m][5]))].firstChild.nodeValue=inp[:pos]+inp[(pos+cc):]
                    else:
                        pass
            print str(root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(LineList[n])))].getAttribute('FuncType'))+ ' ('+ str(LineList[n]) + ') deleted...'
            root_runtime.removeChild(root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(LineList[n])))])
            xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
            xmlfileoutput.write(root_runtime.toxml())
            xmlfileoutput.close()
            root_runtime.unlink
            TargetCanvas.delete((str(LineList[n])+"select"))
        temp=[]
        for n in range(0,len(self.RuntimeLines)):
            ident=0
            for m in range(0,len(LineList)):
                if LineList[m]==self.RuntimeLines[n][0]:
                    ident=1
            if ident ==1:
                pass
            else:
                temp.append(self.RuntimeLines[n])

        self.RuntimeLines=temp

    def DeleteItem(self,TargetCanvas,itemToDelete):

        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root_runtime=rootruntimedoc.documentElement
        tester=root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(itemToDelete)))].getAttribute('FuncType')
        root_runtime.unlink
        if tester=="NodeConnectionLine":
            list=[]
            list.append(int(itemToDelete))
            self.DeleteLines(TargetCanvas,list)
        else:
            rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
            root_runtime=rootruntimedoc.documentElement
            print root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(itemToDelete)))].getAttribute('FuncType')+ ' ('+ itemToDelete + ') deleted...'
            root_runtime.removeChild(root_runtime.childNodes[FindNamedNode(root_runtime,("Node"+str(itemToDelete)))])
            xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
            xmlfileoutput.write(root_runtime.toxml())
            xmlfileoutput.close()
            root_runtime.unlink
            theList=[]
            for n in range (0,(len(self.RuntimeLines))):
                if ((str(self.RuntimeLines[n][1])== str(itemToDelete) or (str(self.RuntimeLines[n][4])== str(itemToDelete) or (str(self.RuntimeLines[n][0])== str(itemToDelete))))):
                    theList.append(self.RuntimeLines[n][0])
                else:
                    pass
            if len(theList)==0:
                pass
            else:
                self.DeleteLines(TargetCanvas,theList)

    def checkIfMultiNode(self,Node,Input):
        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root=rootruntimedoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))]
        datapart=actuellenode.childNodes[FindNamedNode(actuellenode,"Data")]
        inp=datapart.childNodes[FindNamedNode(datapart,str(Input))].getAttribute("MultiConnection")
        root.unlink
        return inp

    def writeConnections(self,Node,input,newID):
        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root=rootruntimedoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))]
        datapart=actuellenode.childNodes[FindNamedNode(actuellenode,"Data")]
        inp=str(datapart.childNodes[FindNamedNode(datapart,str(input))].firstChild.nodeValue)
        if inp[:1]==":":
            datapart.childNodes[FindNamedNode(datapart,str(input))].firstChild.nodeValue=str(datapart.childNodes[FindNamedNode(datapart,str(input))].firstChild.nodeValue)+":"+str(newID)
        else:
            datapart.childNodes[FindNamedNode(datapart,str(input))].firstChild.nodeValue=":"+str(newID)
        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root.toxml())
        xmlfileoutput.close()
        root.unlink

    def checkMultipleSelfConnection(self,fromnode,output,tonode,input):
        if len(self.RuntimeLines)==0:
            return 0
        else:
            for n in range(0,len(self.RuntimeLines)):
                if self.RuntimeLines[n][3]==(str(fromnode)+str(output)) and self.RuntimeLines[n][6]==(str(tonode)+str(input)):
                    return self.RuntimeLines[n][0]
                else:
                    return 0

    def RegisterLine(self,lineID,Fromnode,output,uni_out,Tonode,input,uni_in):
        rootruntimedoc=minidom.parse((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"))
        root_runtime=rootruntimedoc.documentElement

        runtimeNodeList_trick=minidom.getDOMImplementation()
        root_trick=runtimeNodeList_trick.createDocument("", "SetEditorRuntimersx", "")


        newLine=root_trick.createElement("Node"+str(lineID))
        root_trick.firstChild.appendChild(newLine)

        ftattr=root_trick.createAttribute("FuncType")
        ftattr.value="NodeConnectionLine"
        newLine.setAttributeNode(ftattr)

        fromattr=root_trick.createAttribute("FromNode")
        fromattr.value=Fromnode
        newLine.setAttributeNode(fromattr)

        fromoutattr=root_trick.createAttribute("FromNode-Output")
        fromoutattr.value=output
        newLine.setAttributeNode(fromoutattr)

        unioutattr=root_trick.createAttribute("Uni_Out")
        unioutattr.value=uni_out
        newLine.setAttributeNode(unioutattr)

        toattr=root_trick.createAttribute("ToNode")
        toattr.value=Tonode
        newLine.setAttributeNode(toattr)

        toinattr=root_trick.createAttribute("ToNode-Input")
        toinattr.value=input
        newLine.setAttributeNode(toinattr)

        uniinattr=root_trick.createAttribute("Uni_In")
        uniinattr.value=uni_in
        newLine.setAttributeNode(uniinattr)

        mroot=root_trick.firstChild.firstChild.cloneNode(1)
        root_runtime.appendChild(mroot)

        xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
        xmlfileoutput.write(root_runtime.toxml())
        xmlfileoutput.close()
        self.RuntimeLines.append((lineID,Fromnode,output,uni_out,Tonode,input,uni_in))
        root_trick.unlink
        root_runtime.unlink

    def ChangeRuntimeNodeName(self,ID,NewName):
        x = self._CHCRuntimeNodeName(ID,NewName)
        IDd=("Node"+ID)
        if  x=="true":
            rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
            root=rootdoc.documentElement
            root.childNodes[FindNamedNode(root,IDd)].setAttribute("Name",NewName)
            xmlfileoutput=open((RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml"),"w")
            xmlfileoutput.write(root.toxml())
            xmlfileoutput.close()
            return "true"
        else:
            return "false"

#------------------------------------------------------------------------------------------------------------------------------------
#    Class to handle SliderBar data enquery
#------------------------------------------------------------------------------------------------------------------------------------

class SliderBarDbaseSupport:

    def CountRowMember(self,row):
        rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml")
        root_final=rootdoc.documentElement

        uprow=root_final.childNodes[0].childNodes.length
        midrow=root_final.childNodes[1].childNodes.length
        bottrow=root_final.childNodes[2].childNodes.length

        if row==1:
            return uprow
        if row==2:
            return midrow
        if row==3:
            return bottrow


    def DeleteSliderBarNode(self,nodeName):
        if nodeName=="":
            pass
        else:
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml")
            root=rootdoc.documentElement
            b=None
            for n in range(0,root.childNodes.length):
                for m in range(0,root.childNodes[n].childNodes.length):
                    if str(root.childNodes[n].childNodes[m].firstChild.nodeValue)==str(nodeName):
                        print root.childNodes[n].childNodes[m].nodeName +" : "+ str(root.childNodes[n].childNodes[m].firstChild.nodeValue)
                        b=root.childNodes[n].childNodes[m]
                try:
                    root.childNodes[n].removeChild(b)
                    files=open((GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml"),"w")
                    files.write(str(root.toxml()))
                    files.close()
                except:
                    pass
            root.unlink
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
            root=rootdoc.documentElement
            b=None
            for n in range(0,root.childNodes.length):
                if str(root.childNodes[n].nodeName)==str(nodeName):
                        b=root.childNodes[n]
                try:
                    root.removeChild(b)
                    files=open((GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml"),"w")
                    files.write(str(root.toxml()))
                    files.close()
                except:
                    pass
            root.unlink

    def getRowAndPosition(self,nodeName):
        slot=None
        row=None
        if nodeName=="":
            pass
        else:
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml")
            root=rootdoc.documentElement
            for n in range(0,root.childNodes.length):
                for m in range(0,root.childNodes[n].childNodes.length):
                    if str(root.childNodes[n].childNodes[m].firstChild.nodeValue)==str(nodeName):
                        row= root.childNodes[n].nodeName
                        slot=root.childNodes[n].childNodes[m].nodeName
            root.unlink
            return (row,slot)


    def getNodeSettings(self,Functype,state):

        if state=="edit":
            if Functype=="":
                return [()]
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
            root=rootdoc.documentElement
            generation_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Generation")])
            data_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Data")])
            source_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Source")])

            nodeshapestyle = generation_root.childNodes[FindNamedNode(generation_root,"NodeShapeStyle")].firstChild.nodeValue

            colors=generation_root.childNodes[FindNamedNode(generation_root,"Colors")]
            topcolor=colors.childNodes[FindNamedNode(colors,"TopColor")].firstChild.nodeValue
            midcolor=colors.childNodes[FindNamedNode(colors,"MiddleColor")].firstChild.nodeValue
            botcolor=colors.childNodes[FindNamedNode(colors,"BottomColor")].firstChild.nodeValue

            labels=generation_root.childNodes[FindNamedNode(generation_root,"Labels")]
            upperlabel=labels.childNodes[FindNamedNode(labels,"UpperLabel")].firstChild.nodeValue
            Previewlabel=labels.childNodes[FindNamedNode(labels,"PreviewLabel")].firstChild.nodeValue
            Note=labels.childNodes[FindNamedNode(labels,"Note")].firstChild.nodeValue

            inpno=data_root.childNodes.length
            inputs_out=[]
            for n in range (0,inpno):
                    inpnname=str(data_root.childNodes[n].nodeName)
                    inpconn=str(data_root.childNodes[n].getAttribute("Connection"))
                    inpmulti=str(data_root.childNodes[n].getAttribute("MultiConnection"))
                    inptyp=str(data_root.childNodes[n].getAttribute("Type"))
                    inpp=(inpnname,inpconn,inpmulti,inptyp)
                    inputs_out.append((inpp))

            outputs=generation_root.childNodes[FindNamedNode(generation_root,"Outputs")]
            outno=outputs.childNodes.length
            outs_out=[]
            for n in range (0,outno):
                tmp=((str(outputs.childNodes[n].nodeName)),(str(outputs.childNodes[n].getAttribute("Type"))))
                outs_out.append((tmp))

            sourcefile=str(source_root.firstChild.firstChild.nodeValue)

            outvalues=(str(nodeshapestyle),str(upperlabel),str(Previewlabel),str(Note),str(topcolor),str(midcolor),str(botcolor),(inputs_out),(outs_out),sourcefile)
            root.unlink
        if state!="edit":
            inputs_out=[]
            inpnname="InputToDefine"
            inpconn="True"
            inpmulti="True"
            inptyp="Path"
            inpp=(inpnname,inpconn,inpmulti,inptyp)
            inputs_out.append((inpp))
            outs_out=[]
            outs_out.append(("SettingsToDefine","True"))
            outvalues=("SHAPE02","NewNode","NN","Put some note here!","gray60","gray45","gray35",(inputs_out),(outs_out),"...")

        return outvalues

    def GetSliderBarNodeList(self):
       rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml")
       root=rootdoc.documentElement
       up=[]
       mid=[]
       but=[]
       if  root.childNodes[0].hasChildNodes()==True:
           for  n in range  (0,root.childNodes[0].childNodes.length):
               up.append(str(root.childNodes[0].childNodes[n].firstChild.nodeValue))
       else:
            pass

       if  root.childNodes[1].hasChildNodes()==True:
            for  n in range  (0,root.childNodes[1].childNodes.length):
                mid.append(str(root.childNodes[1].childNodes[n].firstChild.nodeValue))
       else:
            pass

       if  root.childNodes[2].hasChildNodes()==True:
            for  n in range  (0,root.childNodes[2].childNodes.length):
                but.append(str(root.childNodes[2].childNodes[n].firstChild.nodeValue))
       else:
            pass
       x=(up,mid,but)
       return x

#------------------------------------------------------------------------------------------------------------------------------------
#    Class to initialize the startup variables
#------------------------------------------------------------------------------------------------------------------------------------

class VarDefs:

    def GetVars(self,Functype):
        rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
        root=rootdoc.documentElement
        generation_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Generation")])
        data_root=(root.childNodes[FindNamedNode(root,Functype)].childNodes[FindNamedNode(root.childNodes[FindNamedNode(root,Functype)],"Data")])

        nodeshapestyle = generation_root.childNodes[FindNamedNode(generation_root,"NodeShapeStyle")].firstChild.nodeValue

        colors=generation_root.childNodes[FindNamedNode(generation_root,"Colors")]
        topcolor=colors.childNodes[FindNamedNode(colors,"TopColor")].firstChild.nodeValue
        midcolor=colors.childNodes[FindNamedNode(colors,"MiddleColor")].firstChild.nodeValue
        botcolor=colors.childNodes[FindNamedNode(colors,"BottomColor")].firstChild.nodeValue

        labels=generation_root.childNodes[FindNamedNode(generation_root,"Labels")]
        upperlabel=labels.childNodes[FindNamedNode(labels,"UpperLabel")].firstChild.nodeValue
        Previewlabel=labels.childNodes[FindNamedNode(labels,"PreviewLabel")].firstChild.nodeValue
        Note=labels.childNodes[FindNamedNode(labels,"Note")].firstChild.nodeValue

        inpno=data_root.childNodes.length
        inputs_out=[]
        for n in range (0,inpno):
            if ((str(data_root.childNodes[n].getAttribute("Connection"))))=="False":
                pass
            else:
                inputs_out.append([(str(data_root.childNodes[n].nodeName)),str(data_root.childNodes[n].getAttribute("Type"))])

        outputs=generation_root.childNodes[FindNamedNode(generation_root,"Outputs")]
        outno=outputs.childNodes.length
        outs_out=[]
        for n in range (0,outno):
            tmp=((str(outputs.childNodes[n].nodeName)),(str(outputs.childNodes[n].getAttribute("Type"))))
            outs_out.append([(str(outputs.childNodes[n].nodeName)),(str(outputs.childNodes[n].getAttribute("Type")))])

        outvalues=(str(nodeshapestyle),str(upperlabel),str(Previewlabel),str(Note),str(topcolor),str(midcolor),str(botcolor),(inputs_out),(outs_out))

        return outvalues

#------------------------------------------------------------------------------------------------------------------------------------
#    Definitions for initial data strucutre creation
#
#    _createSliderBarNodeList()                 Generates the xml for the SliderBar node list
#    _createNodeTypeSettings()                Generates the base node style description xml and the first data entry.
#
#------------------------------------------------------------------------------------------------------------------------------------





def _createSliderBarNodeList():
        nodeListDoc=minidom.getDOMImplementation()
        root=nodeListDoc.createDocument("", "SliderBarNodes", "")
        xmlfileoutput=open((GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml"),"w")
        upp=root.createElement("Upper_row")
        root.firstChild.appendChild(upp)

        uslot1=root.createElement("slot1")
        upp.appendChild(uslot1)
        uslot1txt=root.createTextNode("Image")
        uslot1.appendChild(uslot1txt)

        uslot2=root.createElement("slot2")
        upp.appendChild(uslot2)
        uslot2txt=root.createTextNode("Image")
        uslot2.appendChild(uslot2txt)

        midd=root.createElement("Middle_row")
        root.firstChild.appendChild(midd)

        bott=root.createElement("Bottom_row")
        root.firstChild.appendChild(bott)

        print root.toprettyxml()
        xmlfileoutput.write(root.toxml())
        xmlfileoutput.close()

def _createNodeTypeSettings():

        testdoc=minidom.getDOMImplementation()
        root=testdoc.createDocument("","NodeTypes","")
        files=open((GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml"),"w")

        Image=root.createElement("Image")
        root.firstChild.appendChild(Image)
        imattr=root.createAttribute("Type")
        imattr.value="MainCategory"
        Image.setAttributeNode(imattr)

        Generation_image=root.createElement("Generation")
        Image.appendChild(Generation_image)
        genattr=root.createAttribute("Type")
        genattr.value="SubCategory"
        Generation_image.setAttributeNode(genattr)
        nss=root.createElement("NodeShapeStyle")
        nssattr=root.createAttribute("Type")
        nssattr.value="String"
        nss.setAttributeNode(nssattr)
        Generation_image.appendChild(nss)
        nsstext=root.createTextNode("SHAPE02")
        nss.appendChild(nsstext)
        colors=root.createElement("Colors")
        Generation_image.appendChild(colors)
        colattr=root.createAttribute("Type")
        colattr.value="SubCategory"
        colors.setAttributeNode(colattr)
        topcol=root.createElement("TopColor")
        colors.appendChild(topcol)
        topcolattr=root.createAttribute("Type")
        topcolattr.value="ColorHEX"
        topcol.setAttributeNode(topcolattr)
        topcolhex=root.createTextNode("gray60")
        topcol.appendChild(topcolhex)
        midcol=root.createElement("MiddleColor")
        colors.appendChild(midcol)
        midcolattr=root.createAttribute("Type")
        midcolattr.value="ColorHEX"
        midcol.setAttributeNode(midcolattr)
        midcolhex=root.createTextNode("gray40")
        midcol.appendChild(midcolhex)
        botcol=root.createElement("BottomColor")
        colors.appendChild(botcol)
        botcolattr=root.createAttribute("Type")
        botcolattr.value="ColorHEX"
        botcol.setAttributeNode(botcolattr)
        botcolhex=root.createTextNode("gray75")
        botcol.appendChild(botcolhex)
        labels=root.createElement("Labels")
        Generation_image.appendChild(labels)
        labattr=root.createAttribute("Type")
        labattr.value="SubCategory"
        labels.setAttributeNode(labattr)
        uplabel=root.createElement("UpperLabel")
        labels.appendChild(uplabel)
        uplabelattr=root.createAttribute("Type")
        uplabelattr.value="String"
        uplabel.setAttributeNode(uplabelattr)
        upperlabeltext=root.createTextNode("Image")
        uplabel.appendChild(upperlabeltext)
        prlabel=root.createElement("PreviewLabel")
        labels.appendChild(prlabel)
        prlabelattr=root.createAttribute("Type")
        prlabelattr.value="String"
        prlabel.setAttributeNode(prlabelattr)
        prlabeltext=root.createTextNode("IMG")
        prlabel.appendChild(prlabeltext)
        ntlabel=root.createElement("Note")
        labels.appendChild(ntlabel)
        ntlabelattr=root.createAttribute("Type")
        ntlabelattr.value="MassText"
        ntlabel.setAttributeNode(ntlabelattr)
        ntlabeltext=root.createTextNode("Note to Image node...")
        ntlabel.appendChild(ntlabeltext)
        oups=root.createElement("Outputs")
        Generation_image.appendChild(oups)
        oupattr=root.createAttribute("Type")
        oupattr.value="SubCategory"
        oups.setAttributeNode(oupattr)
        out1=root.createElement("ImageOut")
        oups.appendChild(out1)
        out1attr=root.createAttribute("Type")
        out1attr.value="Path"
        out1.setAttributeNode(out1attr)
        out1txt=root.createTextNode("")
        out1.appendChild(out1txt)
        out2=root.createElement("TexOut")
        oups.appendChild(out2)
        out2attr=root.createAttribute("Type")
        out2attr.value="Path"
        out2.setAttributeNode(out2attr)
        out2txt=root.createTextNode("")
        out2.appendChild(out2txt)
        pos=root.createElement("Position")
        Generation_image.appendChild(pos)
        posattr=root.createAttribute("Type")
        posattr.value="SubCategory"
        pos.setAttributeNode(posattr)
        xpos=root.createElement("X")
        pos.appendChild(xpos)
        xposattr=root.createAttribute("Type")
        xposattr.value="Integer"
        xpos.setAttributeNode(xposattr)
        xpostxt=root.createTextNode("100")
        xpos.appendChild(xpostxt)
        ypos=root.createElement("Y")
        pos.appendChild(ypos)
        yposattr=root.createAttribute("Type")
        yposattr.value="Integer"
        ypos.setAttributeNode(yposattr)
        ypostxt=root.createTextNode("100")
        ypos.appendChild(ypostxt)

        Data=root.createElement("Data")
        Image.appendChild(Data)
        datattr=root.createAttribute("Type")
        datattr.value="SubCategory"
        Data.setAttributeNode(datattr)
        impath=root.createElement("ImageIn")
        Data.appendChild(impath)
        impathattr=root.createAttribute("Type")
        impathattr.value="Path"
        impath.setAttributeNode(impathattr)

        impathattr2=root.createAttribute("Connection")
        impathattr2.value="True"
        impath.setAttributeNode(impathattr2)

        impathattr2=root.createAttribute("MultiConnection")
        impathattr2.value="True"
        impath.setAttributeNode(impathattr2)

        impathtext=root.createTextNode("...")
        impath.appendChild(impathtext)

        ctt=root.createElement("ConvertToTex")
        Data.appendChild(ctt)
        cttattr=root.createAttribute("Type")
        cttattr.value="Boolean"
        ctt.setAttributeNode(cttattr)

        cttattr2=root.createAttribute("Connection")
        cttattr2.value="False"
        ctt.setAttributeNode(cttattr2)

        cttattr2=root.createAttribute("MultiConnection")
        cttattr2.value="False"
        ctt.setAttributeNode(cttattr2)

        ctttext=root.createTextNode("True")
        ctt.appendChild(ctttext)

        clt=root.createElement("CleanTex")
        Data.appendChild(clt)
        cltattr=root.createAttribute("Type")
        cltattr.value="Boolean"
        clt.setAttributeNode(cltattr)

        cltattr2=root.createAttribute("Connection")
        cltattr2.value="False"
        clt.setAttributeNode(cltattr2)

        cltattr2=root.createAttribute("MultiConnection")
        cltattr2.value="False"
        clt.setAttributeNode(cltattr2)

        clttext=root.createTextNode("False")
        clt.appendChild(clttext)


        source=root.createElement("Source")
        Image.appendChild(source)
        sattr=root.createAttribute("Type")
        sattr.value="SubCategory"
        source.setAttributeNode(sattr)
        sfile=root.createElement("Sourcecode")
        source.appendChild(sfile)
        sfa=root.createAttribute("Type")
        sfa.value="pyc"
        sfile.setAttributeNode(sfa)
        tart=root.createTextNode("...")
        sfile.appendChild(tart)

        files.write(root.toxml())
        files.close()

class NodeEditordbTools:

    def DeleteNodeTypeSettings(self,node):
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
            root=rootdoc.documentElement
            root.removeChild(root.childNodes[FindNamedNode(root,str(node))])
            files=open((GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml"),"w")
            files.write(str(root.toxml()))
            files.close()

    def AddToSliderBar(self,row,position,name):

        rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml")
        root_final=rootdoc.documentElement

        uprow=root_final.childNodes[0].cloneNode(1)
        midrow=root_final.childNodes[1].cloneNode(1)
        bottrow=root_final.childNodes[2].cloneNode(1)

        nodeListDoc=minidom.getDOMImplementation()
        root=nodeListDoc.createDocument("", "SliderBarNodes", "")
        if row=="Upper_row":
            slotname= (str(position))
            slo=root.createElement(slotname)
            uprow.appendChild(slo)
            nat=root.createTextNode(str(name))
            slo.appendChild(nat)
        if row=="Middle_row":
            slotname= (str(position))
            slo=root.createElement(slotname)
            midrow.appendChild(slo)
            nat=root.createTextNode(str(name))
            slo.appendChild(nat)
        if row=="Bottom_row":
            slotname= (str(position))
            slo=root.createElement(slotname)
            bottrow.appendChild(slo)
            nat=root.createTextNode(str(name))
            slo.appendChild(nat)

        root.firstChild.appendChild(uprow)
        root.firstChild.appendChild(midrow)
        root.firstChild.appendChild(bottrow)

        files=open((GUI_SETTINGS_FOLDER + "/SliderBarNodeList.xml"),"w")

        files.write(str(root.toxml()))
        files.close()


    def AddNodeTypeSettings(self, ns):
            rootdoc=minidom.parse(GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml")
            root_final=rootdoc.documentElement
            try:
                if root_final.childNodes[FindNamedNode(root_final,str(ns[0]))].nodeName==ns[0]:
                    print "This node already exist!!!!!"
                    return 1
            except:
                print "Ignore the error, every software need to drop some error, so here we go..."
                print "Sorry Dude :) "
            runtimeNodeList_trick=minidom.getDOMImplementation()
            root=runtimeNodeList_trick.createDocument("", "NodeTypeSettings", "")

            image=root.createElement(str(ns[0]))
            root.firstChild.appendChild(image)
            imattr=root.createAttribute("Type")
            imattr.value="MainCategory"
            image.setAttributeNode(imattr)

            Generation_image=root.createElement("Generation")
            image.appendChild(Generation_image)
            genattr=root.createAttribute("Type")
            genattr.value="SubCategory"
            Generation_image.setAttributeNode(genattr)
            nss=root.createElement("NodeShapeStyle")
            nssattr=root.createAttribute("Type")
            nssattr.value="String"
            nss.setAttributeNode(nssattr)
            Generation_image.appendChild(nss)
            nsstext=root.createTextNode(str(ns[2]))
            nss.appendChild(nsstext)
            colors=root.createElement("Colors")
            Generation_image.appendChild(colors)
            colattr=root.createAttribute("Type")
            colattr.value="SubCategory"
            colors.setAttributeNode(colattr)
            topcol=root.createElement("TopColor")
            colors.appendChild(topcol)
            topcolattr=root.createAttribute("Type")
            topcolattr.value="ColorHEX"
            topcol.setAttributeNode(topcolattr)
            topcolhex=root.createTextNode(str(ns[3]))
            topcol.appendChild(topcolhex)
            midcol=root.createElement("MiddleColor")
            colors.appendChild(midcol)
            midcolattr=root.createAttribute("Type")
            midcolattr.value="ColorHEX"
            midcol.setAttributeNode(midcolattr)
            midcolhex=root.createTextNode(str(ns[4]))
            midcol.appendChild(midcolhex)
            botcol=root.createElement("BottomColor")
            colors.appendChild(botcol)
            botcolattr=root.createAttribute("Type")
            botcolattr.value="ColorHEX"
            botcol.setAttributeNode(botcolattr)
            botcolhex=root.createTextNode(str(ns[5]))
            botcol.appendChild(botcolhex)
            labels=root.createElement("Labels")
            Generation_image.appendChild(labels)
            labattr=root.createAttribute("Type")
            labattr.value="SubCategory"
            labels.setAttributeNode(labattr)
            uplabel=root.createElement("UpperLabel")
            labels.appendChild(uplabel)
            uplabelattr=root.createAttribute("Type")
            uplabelattr.value="String"
            uplabel.setAttributeNode(uplabelattr)
            upperlabeltext=root.createTextNode(str(ns[0]))
            uplabel.appendChild(upperlabeltext)
            prlabel=root.createElement("PreviewLabel")
            labels.appendChild(prlabel)
            prlabelattr=root.createAttribute("Type")
            prlabelattr.value="String"
            prlabel.setAttributeNode(prlabelattr)
            prlabeltext=root.createTextNode(str(ns[1]))
            prlabel.appendChild(prlabeltext)
            ntlabel=root.createElement("Note")
            labels.appendChild(ntlabel)
            ntlabelattr=root.createAttribute("Type")
            ntlabelattr.value="MassText"
            ntlabel.setAttributeNode(ntlabelattr)
            ntlabeltext=root.createTextNode(str(ns[9]))
            ntlabel.appendChild(ntlabeltext)
            oups=root.createElement("Outputs")
            Generation_image.appendChild(oups)
            oupattr=root.createAttribute("Type")
            oupattr.value="SubCategory"
            oups.setAttributeNode(oupattr)

            for n in range(0,len(ns[7])):
                out1=root.createElement(str(ns[7][n][0]))
                oups.appendChild(out1)
                out1attr=root.createAttribute("Type")
                out1attr.value=str(ns[7][n][1])
                out1.setAttributeNode(out1attr)
                out1txt=root.createTextNode("")
                out1.appendChild(out1txt)

            pos=root.createElement("Position")
            Generation_image.appendChild(pos)
            posattr=root.createAttribute("Type")
            posattr.value="SubCategory"
            pos.setAttributeNode(posattr)
            xpos=root.createElement("X")
            pos.appendChild(xpos)
            xposattr=root.createAttribute("Type")
            xposattr.value="Integer"
            xpos.setAttributeNode(xposattr)
            xpostxt=root.createTextNode("100")
            xpos.appendChild(xpostxt)
            ypos=root.createElement("Y")
            pos.appendChild(ypos)
            yposattr=root.createAttribute("Type")
            yposattr.value="Integer"
            ypos.setAttributeNode(yposattr)
            ypostxt=root.createTextNode("100")
            ypos.appendChild(ypostxt)

            Data=root.createElement("Data")
            image.appendChild(Data)
            datattr=root.createAttribute("Type")
            datattr.value="SubCategory"
            Data.setAttributeNode(datattr)

            for m in range(0,len(ns[6])):
                impath=root.createElement(str(ns[6][m][0]))
                Data.appendChild(impath)
                impathattr=root.createAttribute("Type")
                impathattr.value=str(ns[6][m][3])
                impath.setAttributeNode(impathattr)

                impathattr2=root.createAttribute("Connection")
                impathattr2.value=str(ns[6][m][1])
                impath.setAttributeNode(impathattr2)

                impathattr2=root.createAttribute("MultiConnection")
                impathattr2.value=str(ns[6][m][2])
                impath.setAttributeNode(impathattr2)

                impathtext=root.createTextNode("...")
                impath.appendChild(impathtext)

            source=root.createElement("Source")
            image.appendChild(source)
            sattr=root.createAttribute("Type")
            sattr.value="SubCategory"
            source.setAttributeNode(sattr)
            sfile=root.createElement("Sourcecode")
            source.appendChild(sfile)
            sfa=root.createAttribute("Type")
            sfa.value="py"
            sfile.setAttributeNode(sfa)
            tart=root.createTextNode(str(ns[8]))
            sfile.appendChild(tart)

            x=root.firstChild.firstChild.cloneNode(1)
            root_final.appendChild(x)
            files=open((GUI_SETTINGS_FOLDER + "/NodeTypeSettings.xml"),"w")

            files.write(str(root_final.toxml()))
            files.close()



#**************************************************************************************************************************************************************
#    Fuction call handlers to direct run this file
#
#_createSliderBarNodeList()
#_createNodeTypeSettings()
#GetVars(1,"Image")
#
#
#
#**************************************************************************************************************************************************************