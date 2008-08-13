#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    S. A.  Gateway
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import sys
import os
import shutil
from DBaseManagement import SA_NodeConverter


class SA_Conversion(SA_NodeConverter):
    def CollectSAinFolder(self,starterdir):
	dircontent=os.listdir(starterdir)
        fileslist=[]
        for i in range(0,len(dircontent)):
            if os.path.isfile(str(starterdir+"/"+dircontent[i]))==True:
		    
		if os.path.splitext(dircontent[i])[1][1:][:2]=="sa" or os.path.splitext(dircontent[i])[1][1:][:2]=="py":
                    fileslist.append(str(starterdir+"/"+dircontent[i]))
                else:
                    pass
            else:
                pass
	    
	nodelist=[]
        duplicatednodes=[]
        for x in range(0,len(fileslist)):
            file=open(fileslist[x],"r")
            content=file.read()
            important_part=content.split("define\n{",1)[1].split("}",1)[0].split("\n\t")
            cleanpart=[]
            for z in range(0, len(important_part)):
                important_line=important_part[z].split(" ")
                cleanline=[]
                for y in range(0,len(important_line)):
                    if important_line[y]=="":
                        pass
                    else:
                        cleanline.append(important_line[y])
                if len(cleanline)!=0:
                    cleanpart.append(cleanline)
                else:
                    pass
            file.close()
            for w in range(0,len(cleanpart)):
                if cleanpart[w][0]=="name":
                    counter=0
                    for g in range(0,len(nodelist)):
                        if nodelist[g]==cleanpart[w][1]:
                            counter=1
                    if counter == 1:
                        duplicatednodes.append(cleanpart[w][1])
                    else:
			    
                        varibbbb=(cleanpart[w][1],str(fileslist[x]))
			nodelist.append(varibbbb)
        return nodelist

    def AddSAtoNodeDescription(self,path,fileslist):
        nodelistdir=os.path.split(path)[0]
	for x in range(0,len(fileslist)):
            file=open(fileslist[x],"r")
            content=file.read()
            important_part=content.split("define\n{",1)[1].split("}",1)[0].split("\n\t")
            cleanpart=[]
            for z in range(0, len(important_part)):
                important_line=important_part[z].split(" ")
                cleanline=[]
                for y in range(0,len(important_line)):
                    if important_line[y]=="":
                        pass
                    else:
                        cleanline.append(important_line[y])
                if len(cleanline)!=0:
                    cleanpart.append(cleanline)
                else:
                    pass
            file.close()
	    
            name=""
            firsttag=""
            shape="SHAPE02"
            scrpath=str(fileslist[x])
            notee="No note at this time.... sorry dude..."
            inputs=[]
            outputs=[]

            for w in range(0,len(cleanpart)):
                if cleanpart[w][0]=="name":
                    name=cleanpart[w][1]
                if cleanpart[w][0]=="tags":
                    firsttag=cleanpart[w][1].split(":")[0]
                if cleanpart[w][0]=="input":
                    inputs.append((cleanpart[w][2].split("\n")[0],"True","False",cleanpart[w][1].split("\n")[0]))
                if cleanpart[w][0]=="output":
                    outputs.append((cleanpart[w][2].split("\n")[0],cleanpart[w][1].split("\n")[0]))

            if inputs==[] and outputs==[]:
                shape="SHAPE01"
            elif inputs!=[] and outputs==[]:
                shape="SHAPE03"
            elif inputs==[] and outputs!=[]:
                shape="SHAPE04"


	    sname=""

            if len(name)>4:
		    sname=name[:2]+name[int(len(name)/2)]+name[(len(name)-1):]
	    else:
		    sname=name
		    

            topc="gray30"
            midc="gray50"
            botc="gray40"

            if firsttag=="mesh"or firsttag=="point" or firsttag=="curve" or firsttag=="object" or firsttag=="prim" or firsttag=="geo" or firsttag=="surface":
                topc="#468232"
                midc="#d3e8cc"
                botc="#9ecf8c"

            elif firsttag=="massive" or firsttag=="mass":
                topc="#328253"
                midc="#cce8d7"
                botc="#8ccfa7"

            elif firsttag=="dynamics" or firsttag=="field" or firsttag=="wind" or firsttag=="flow":
                topc="#82324d"
                midc="#e8ccd5"
                botc="#cf8ca2"

            elif firsttag=="shader" or firsttag=="renderman" or firsttag=="kdTree":
                topc="#823232"
                midc="#e8cccc"
                botc="#cf8c8c"

            elif firsttag=="math":
                topc="#326782"
                midc="#ccdfe8"
                botc="#8cb8cf"

            elif firsttag=="image":
                topc="#343282"
                midc="#cccce8"
                botc="#8d8ccf"

            elif firsttag=="locator" or firsttag=="gizmo" or firsttag=="bbox":
                topc="#5a8232"
                midc="#dae8cc"
                botc="#aecf8c"

            elif firsttag=="animation" or firsttag=="rigging" or firsttag=="playblast":
                topc="#613282"
                midc="#dccce8"
                botc="#b38ccf"

            else:
                pass

            collection=[]
            collection.append(name)
            collection.append(sname)
            collection.append(shape)
            collection.append(topc)
            collection.append(midc)
            collection.append(botc)
            collection.append(inputs)
            collection.append(outputs)
            collection.append(scrpath)
            collection.append(notee)


            if self.FindNamedNodeInFile(name, nodelistdir)==-1:
                self.AddNodeTypeSettingsToFile(collection, nodelistdir)
                if firsttag=="mesh" or firsttag=="massive" or firsttag=="image":
                    pass
		    #self.AddToSliderBarToFile("Upper_row", "SA"+str(x+1), name, nodelistdir)
                elif firsttag=="math" or firsttag=="mass" or firsttag=="gizmo" or firsttag=="field" or firsttag=="geo" or firsttag=="bbox":
                    pass
		    #self.AddToSliderBarToFile("Middle_row", "SA"+str(x+1), name, nodelistdir)
                else:
                    pass
		    #self.AddToSliderBarToFile("Bottom_row", "SA"+str(x+1), name, nodelistdir)

            for h in range (0,len(cleanpart)):
                if cleanpart[h][0]=="input":
                    if cleanpart[h][1]=="int" or cleanpart[h][1]=="float" or cleanpart[h][1]=="aint" or cleanpart[h][1]=="afloat" or cleanpart[h][1]=="vint" or cleanpart[h][1]=="vfloat" or cleanpart[h][1]=="avint" or cleanpart[h][1]=="avfloat":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "0")
                        else:
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a.split("\n")[0])

                    elif cleanpart[h][1]=="string" or cleanpart[h][1]=="file":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "...")
                        else:
                            if len(cleanpart[h])>3:
                                a=""
                                for q in range(3,len(cleanpart[h])):
                                    a+=str(cleanpart[h][q])+" "
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a.split("\n")[0])

                    elif cleanpart[h][1]=="bool":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "False")
                        else:
                            if a.split("\n")[0]=="0":
                                a="False"
                            else:
                                a="True"
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a)

                    elif cleanpart[h][1]=="vector" or cleanpart[h][1]=="point" or cleanpart[h][1]=="vvector" or cleanpart[h][1]=="color" or cleanpart[h][1]=="avector" or cleanpart[h][1]=="vpoint" or cleanpart[h][1]=="avvector" or cleanpart[h][1]=="apoint":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            a=";0;0;0;"
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a)
                        else:
                            if len(cleanpart[h])>3:
                                a=""
                                for q in range(3,len(cleanpart[h])):
                                    a+=str(cleanpart[h][q])+" "
                            a=str(a.strip(" "))
                            if a[:1]=="\"":
                                a=a.split("\"")[1]
                            if len(a.split(" "))>1:
                                a=a.split(" ")
                            elif len(a.split(","))>1:
                                a=a.split(",")
                            b=""
                            for qrt in range (0,len(a)):
                                b+=";"+a[qrt]
                            b+=";"
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], b)

                    elif cleanpart[h][1]=="matrix" or cleanpart[h][1]=="amatrix":
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], ";0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;")

                    else:
                            self.defaultSettings(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "...")



            for h in range (0,len(cleanpart)):
                if cleanpart[h][0]=="output":
                    if cleanpart[h][1]=="int" or cleanpart[h][1]=="float" or cleanpart[h][1]=="aint" or cleanpart[h][1]=="afloat" or cleanpart[h][1]=="vint" or cleanpart[h][1]=="vfloat" or cleanpart[h][1]=="avint" or cleanpart[h][1]=="avfloat":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "0")
                        else:
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a.split("\n")[0])

                    elif cleanpart[h][1]=="string" or cleanpart[h][1]=="file":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "...")
                        else:
                            if len(cleanpart[h])>3:
                                a=""
                                for q in range(3,len(cleanpart[h])):
                                    a+=str(cleanpart[h][q])+" "
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a.split("\n")[0])

                    elif cleanpart[h][1]=="bool":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "False")
                        else:
                            if a.split("\n")[0]=="0":
                                a="False"
                            else:
                                a="True"
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a)

                    elif cleanpart[h][1]=="vector" or cleanpart[h][1]=="point" or cleanpart[h][1]=="vvector" or cleanpart[h][1]=="color" or cleanpart[h][1]=="avector" or cleanpart[h][1]=="vpoint" or cleanpart[h][1]=="avvector" or cleanpart[h][1]=="apoint":
                        try:
                            a=cleanpart[h][3].split("\n")[0]
                        except:
                            a=""
                        if a=="" or a=="\"\"":
                            a=";0;0;0;"
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], a)
                        else:
                            if len(cleanpart[h])>3:
                                a=""
                                for q in range(3,len(cleanpart[h])):
                                    a+=str(cleanpart[h][q])+" "
                            a=str(a.strip(" "))
                            if a[:1]=="\"":
                                a=a.split("\"")[1]
                            if len(a.split(" "))>1:
                                a=a.split(" ")
                            elif len(a.split(","))>1:
                                a=a.split(",")
                            b=""
                            for qrt in range (0,len(a)):
                                b+=";"+a[qrt]
                            b+=";"
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], b)

                    elif cleanpart[h][1]=="matrix" or cleanpart[h][1]=="amatrix":
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], ";0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;")

                    else:
                            self.defaultOutputs(nodelistdir, name, str(cleanpart[h][2]).split("\n")[0], "0")
                    
		    
		    nlsmenu=open(self.nodeListMenu,"r")
		    nlsmcontent=nlsmenu.read()
		    nlsmenu.close()
		    nlsmcontent=nlsmcontent.strip("\n").split("\n")
		    menulist=[]
		    for lies in nlsmcontent:
			    lies=lies.strip(" ")
			    x=lies.split(" ")
			    menulist.append(x)
                    if firsttag.strip(" ").strip("\n")=="mesh":
                    		s=-1
				for xy in range(0,len(menulist)):
					if menulist[xy][0]=="Mesh":
						s=xy
					else:
						pass
				if s!=-1:
					t=-1
					for fgh in range (0,len(menulist[s])):
						if menulist[s][fgh]==name.strip(" ").strip("\n"):
							t=fgh
						else:
							pass
					if t==-1:
						menulist[s].append(name.strip(" ").strip("\n"))
					else:
						pass
				else:
					menulist.append(["Mesh",name.strip(" ").strip("\n")])
						
                    else:
                    		pass
		    #print menulist
		    kimfile=""
		    for lik in menulist:
			    kimline=""
			    for pif in lik:
				    kimline+=pif+" "
			    kimline+="\n"
			    kimfile+=kimline
				    
		    nlsmenu=open(self.nodeListMenu,"w")
		    nlsmenu.write(kimfile)
		    nlsmenu.close()
		    
		    
		    
