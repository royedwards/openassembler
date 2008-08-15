#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    S. A.  conversion script.... (header collector)
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import sys
import os
import shutil

starterdir="/home/user/sacs"
endfile="/home/user/sacs/collection.txt"
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
collection=""
for x in range(0,len(fileslist)):
    file=open(fileslist[x],"r")
    content=file.read()
    important_part=content.split("define\n{",1)[1].split("}",1)[0]
    collection += ("%FileNode:\n"+str(fileslist[x])+"\n"+str(important_part)+"\n")
    file.close()

end=open(endfile,"w")
end.write(collection)
end.close()