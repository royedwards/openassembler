#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    S. A.  conversion script....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import sys
import os
import shutil

#if '-h' in sys.argv or '--help' in sys.argv or '--help' in sys.argv:
#    print "This is a converter tool from SA to OpenAssembler"
#    print ""
#    print "Usage: SA_Converter <SA node file directory> <Directory for the node description file>"
#    print ""
#    print "Created by Laszlo Mates (laszlo.mates@gmail.com)"
#    print ""
#    sys.exit(0)
#
#if len(sys.argv)!=1:
#    print "Not enough arg given!!!"
#    print ""
#    print "Usage: SA_Converter <SA node file directory> <Directory for the node description file>"
#    print ""
#    sys.exit(0)
#
#if os.path.isdir(sys.argv[0])!=True:
#    print "Wrong arg given!!!"
#    print ""
#    print "Usage: SA_Converter <SA node file directory> <Directory for the node description file>"
#    print ""
#    sys.exit(0)
#else:
#    starterdir=sys.argv[0]
#
#if os.path.isdir(sys.argv[1])!=True:
#    print "Wrong arg given!!!"
#    print ""
#    print "Usage: SA_Converter <SA node file directory> <Directory for the node description file>"
#    print ""
#    sys.exit(0)
#else:
#    descrdir=sys.argv[1]

starterdir="/home/user/sacs"
dircontent=os.listdir(starterdir)
fileslist=[]
for i in range(0,len(dircontent)):
    if os.path.isfile(str(starterdir+"/"+dircontent[i]))==True:
        if dircontent[i].rsplit(".",1)[1][:2]=="sa":
            fileslist.append(str(starterdir+"/"+dircontent[i]))
        else:
            pass
    else:
        pass

for x in range(0,len(fileslist)):
    file=open(fileslist[x],"r")
    content=file.read()
    important_part=content.split("define\n{",1)[1].split("}",1)[0].split("\n")
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
            inputs.append((cleanpart[w][2],1,0,cleanpart[w][1]))
        if cleanpart[w][0]=="output":
            outputs.append((cleanpart[w][2],cleanpart[w][1]))

    if inputs==[] and outputs==[]:
        shape="SHAPE01"

    if inputs!=[] and outputs==[]:
        shape="SHAPE03"

    if inputs==[] and outputs!=[]:
        shape="SHAPE04"

    sname=raw_input("Short name for: "+name+" ?").strip()

    topc="gray30"
    midc="gray50"
    botc="gray40"

    if firsttag=="gizmo":
        topc="#468232"
        midc="#d3e8cc"
        botc="#9ecf8c"

    if firsttag=="locator":
        topc="#468232"
        midc="#d3e8cc"
        botc="#9ecf8c"

    if firsttag=="deformer":
        topc="#82324d"
        midc="#e8ccd5"
        botc="#cf8ca2"

    if firsttag=="field":
        topc="#825632"
        midc="#e8d9cc"
        botc="#cfaa8c"

    if firsttag=="math":
        topc="#326782"
        midc="#ccdfe8"
        botc="#8cb8cf"


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

