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

    def getNodeName(self,Node):
        rootdoc=minidom.parse(RUNTIME_NODELIST_FOLDER + "/RuntimeNodeList.xml")
        root=rootdoc.documentElement
        actuellenode=root.childNodes[FindNamedNode(root,("Node"+str(Node)))].getAttribute("Name")
        root.unlink
        return actuellenode

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
        return inp

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
                inputs_out.append((str(data_root.childNodes[n].nodeName)))

        outputs=generation_root.childNodes[FindNamedNode(generation_root,"Outputs")]
        outno=outputs.childNodes.length
        outs_out=[]
        for n in range (0,outno):
            tmp=((str(outputs.childNodes[n].nodeName)),(str(outputs.childNodes[n].getAttribute("Type"))))
            outs_out.append((str(outputs.childNodes[n].nodeName)))

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
        ntlabelattr.value="String"
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