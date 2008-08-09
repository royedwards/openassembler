#! /usr/bin/env python

#---------------------------------------------------------------------------------------------------------------------
#
#    OpenAssembler run script....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2008
#
#---------------------------------------------------------------------------------------------------------------------

import os
import sys
import time
import shutil
from Dbase.DBaseManagement import OARun_dB_tools


class OARun_main(OARun_dB_tools):
    def __init__(self,splt):
        prepareddir=self.prep_folders(splt)
        nodelist=self.collect_nodes(prepareddir[0],prepareddir[1])
        self.compute_priorityorder(nodelist)

    def prep_folders(self,splt):
        timmee = time.gmtime()
        fintime=""
        for n in range (0, len(timmee)):
            fintime+="_"+str(timmee[n])
        try:
            os.makedirs(str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)
            print "--  --  TMP cache folder are created..."
            print "--  --  TMP cache folder: "+str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime
        except:
            print "Error: Problem with the temp dir creation!!"
            sys.exit(1)
        try:
            shutil.copy(str(splt[0])+"/"+str(splt[1]), (str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime))
            print "--  --  OAS copied..."
        except:
            print "Error: Problem with copying files!!!"
            sys.exit(1)
        jobscriptvar="#! /usr/bin/env python\n"
        jobscriptvar+=("# OpenAssembler Job-Script\n")
        try:
            jsfile=open((str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/jobscript.py","w")
            jsfile.write(jobscriptvar)
            jsfile.close()
            print "--  --  Job-script are created..."
            print "--  --  Job-script: "+(str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/jobscript.py"
        except:
            print "Error: Problem with js file!!!"
            sys.exit(1)
        return (((str(splt[0])+"/temp/"+str(splt[1][:-4])+fintime)+"/"),str(splt[1]))


    def collect_nodes(self,dir,inFile):

        collectedFuncionList=self.collectFunctionList(dir+inFile)

        print "--  --  Functions are collected..."
        for n in range(0,len(collectedFuncionList)):
            shutil.copy(str(collectedFuncionList[n][1]), str(dir))
            ff=open(str(dir+"jobscript.py"),"r")
            oldffvar=ff.read()
            ff.close()
            oldffvar+="import "+str(collectedFuncionList[n][0])+"\n"
            ff=open(str(dir+"jobscript.py"),"w")
            ff.write(str(oldffvar))
            ff.close()
        print "--  --  Functions are imported to the job-script..."

        collectedNodeList=self.collectNodeList_with_settings(str(dir+inFile))
        return collectedNodeList

    def compute_priorityorder(self,collectedNodeList):

        fin_node=self.final_node()
        level=[]
        level_number=0
        while next_level_counter==0:
            if level_number==0:
                level.append(fin_node)
            else:
                level.append(self.get_back_inputs(level[level_number]))
            level_number+=1
            next_level_counter=len(level[level_number])

        check_list=[]
        ll=len(level)-1
        for i in range(0,ll):
            for m in range(0,(len(level[ll-i])-1)):
                er=0
                for k in range(0,(len(check_list)-1)):
                                if check_list[k]==level[(ll-i)][m]:
                                   er=1
                                else:
                                    er=0
                if er==1:
                    level[(ll-i)][m]="*"+str(level[(ll-i)][m])
                else:
                    check_list.append(str(level[(ll-i)][m]))


        for z in range(0,ll):
            for x in range(0,(len(level[ll-z])-1)):
                if level[ll-z][x][:1]=="*":
                    pass
                else:
                    nou=0
                    for f in range(0,(len(collectedNodeList)-1)):
                        if collectedNodeList[f]==level[ll-z][x]:
                            nou=f
                        else:
                            pass
                #     1, kikeresni a kigyujtott tombbol hogy melyikaz (ha csillaggal kezdodik nem foglalkozni vele)
                #2, atvenni az ertekeket, hogyha :243535 akkor kikeresni a konnekciot, es rekonstrualni a valtozonevet
                #3, mrgnezni milyen kimeneti kotesek vannak a nodbol, es letrehozni annyi valtozot, ahany csak van
                #4, kiirni a jobscriptbe
                #5, megnezni hogy az egyel magasabb szamu levelen torolhetok e a valtozok... (van e csillagozott felljebb)

                #megjegyzes, hogyha szamolnanak, hogy hanyszor szerepel mindenegyes node, mikor csinaljuk a piramist,
                #marmint a leveleket, akkor konyen szurni lehetne, hogyha az elofordulasa nagyonn, mint az oszes kimeno kapcsolatanak a szama
                #akkor az mar egy loop, es akkor megall a feldolgozas

        #generate the job-script: variable_node_output=Function(output,input1,input2.....)


        # run the job-script

#-----------------------------------------------------Main------------------------------------------------------------------------------#

#read the arguments, check them...
print "OpenAssembler Script Running Mechanism starting up...."
print "Owner: Laszlo Mates, laszlo.mates@gmail.com"
print ""

arginput="/home/user/testfile_for_run.oas"
if arginput[-3:] != "oas":
    print "Error: This file is not an OAS"
    os.abort()
else:
    splt=arginput.rsplit("/",1)
    masterfile_path=arginput
    if len(splt)>1:
        masterfile_file=splt[1]
        masterfile_dir=splt[0]+"/"
    else:
        masterfile_file=splt[0]
        forcedir=os.path.realpath(arginput)
        fd=forcedir.rsplit("/",1)
        masterfile_dir=fd[0]+"/"
    try:
        openit=open(arginput,"r")
    except:
        print "Error: No such file or directory!!! (input oas)"
        os.abort()
print "--  --  Input is checked..."
print "--  --  Input: "+ str(arginput)
print "--  --  Input looks fine!!!"
OARun_main(splt)