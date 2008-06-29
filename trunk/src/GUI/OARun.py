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


        # check the inputs in a cycle if it is written than: none ,and copy it to the priority list the change the input collection to the string: done
        # in the same cycle, change all the inputs with the copied node before to none

         # get the collection of nodes
         #filter booth list  if they are used at all

         #filter: minden nodre vegig kell futtatni
         # lepes 1: ez maga a kimeneti node? ha igen hozza kell adni a listahoz, es a ciklus lep ha nem:
         # lepes 2:??????????

         #el kell indulni a kiindulasi ponttol viszafele: leveleket kell epiteni, level0 kiindulasi node, level 1 ennek a bemenetei, level 2 a level 1 bemenetei
         #es igy tovabb....
         #talan ugy, hogy csinalunk egy ideiglenes tombot, ami mindig a bemenet a kovetkezo ciklusnak, ebben regisztraljuk a bemeneteekt, es van egy kulon lista, ahol regisztraljuk az oszeset... nem torodve a duplikacioval...
         #utanna az eredeti node-gyujtemeny minden tagjara meg kell vizsgalni, hogy szerepele a "nagy tombben, ha igen, akkor maradhat, ha nem akkormennie kell.

         #legelegansabb megoldas, hogyha kulon layer tomboket hozunk letre, mindig eget lepunk a ciklus bemenetenel, es igy kapjuk meg a hasznalt nodokat, es egyben a prioritasi listat is...

        #WE NEED TO HANLE THAT WHICH NODE IS CONNECTED TO THE TREE
        #get end of the tree node settings separetly or atleast we have to be sure it is not dropped by the nonuseable notconnected filter

        # after the priority list is done, a next cycle can make an extended list with the necessary memory freeing up deletion

        collectedFinalList=[]

        #generate the job-script depending on the final list like the followings: variable_node_output=Function(output,input1,input2.....)


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