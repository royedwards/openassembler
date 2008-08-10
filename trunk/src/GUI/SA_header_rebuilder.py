#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    S. A.  conversion script.... (header rebuilder)
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import sys
import os
import shutil

enddir="/home/user/trysax"
startfile="/home/user/sacs/collection.txt"

file=open(startfile,"r")
content=file.read()
file.close()
fl=content.split("%FileNode:\n")
for i in range(1,len(fl)):
    files=fl[i].split("\n",1)
    of=enddir+"/"+files[0].rsplit("/",1)[1]
    filcon="\ndefine\n{"+files[1]+"\n}\n"
    fle=open(of,"w")
    fle.write(filcon)
    fle.close()
