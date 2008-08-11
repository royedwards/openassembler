#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    S. A.  conversion script.... (header statistics module)
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import sys
import os
import shutil

endfile="/home/user/Munka/SwissArmy/statistics.txt"
startfile="/home/user/Munka/SwissArmy/collection.txt"

starterdir="/home/user/Munka/SwissArmy/scripts"
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

nodelist=[]
duplicatednodes=[]
firsttaglist=[]
tgslist=[]
variabletypes=[]


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
                nodelist.append(cleanpart[w][1])

        if cleanpart[w][0]=="tags":

            counter=0
            for g in range(0,len(firsttaglist)):
                if str(firsttaglist[g])==str(cleanpart[w][1].split(":")[0]):
                    counter=1
            if counter != 0:
                tgslist.append(str(cleanpart[w][1].split(":")[0]))
            else:
                firsttaglist.append(str(cleanpart[w][1].split(":")[0]))
                tgslist.append(str(cleanpart[w][1].split(":")[0]))
            counter =0

        if cleanpart[w][0]=="input":

            counter=0
            for g in range(0,len(variabletypes)):
                if variabletypes[g]==cleanpart[w][1]:
                    counter=1
            if counter == 1:
                pass
            else:
                variabletypes.append(cleanpart[w][1])


        if cleanpart[w][0]=="output":

            counter=0
            for g in range(0,len(variabletypes)):
                if variabletypes[g]==cleanpart[w][1]:
                    counter=1
            if counter == 1:
                pass
            else:
                variabletypes.append(cleanpart[w][1])

print "Statistic results:"
print "All nodes: "+str(len(nodelist))
print "\nTags:"
for i in range (0,len(firsttaglist)):
    no=tgslist.count(str(firsttaglist[i]))
    print "  "+firsttaglist[i]+" :  "+str(no)
print "\nVariables:"
for i in range (0,len(variabletypes)):
    print "  "+variabletypes[i]
print "\nDuplicated nodes:"
for i in range (0,len(duplicatednodes)):
    print "  "+duplicatednodes[i]