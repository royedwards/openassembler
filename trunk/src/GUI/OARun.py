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

class OARun_main:
    def __init__(self):
        pass

    def prep_folders(self):

        #Create a tmp work dir, for the workfiles into the same folder where the oas was...
            #copy the oas there too
            #create the jos-script here with header


        #collect a list about the used functions in the oas
            #copy the py scrits to the tmpdir
            #write the import modules lines to the job-script

        collectedFuncionList=[]

        #collect the list of the presented nodes with their inputs and their outputs

        collectedNodeList=[]

        # check the inputs in a cycle if it is written than: none ,and copy it to the priority list the change the input collection to the string: done
        # in the same cycle, change all the inputs with the copied node before to none

        # after the priority list is done, a next cycle can make an extended list with the necessary memory freeing up deletion

        collectedFinalList=[]

        #generate the job-script depending on the final list like the followings: variable_node_output=Function(output,input1,input2.....)


        # run the job-script



# check the argments, set the wariables: maindir, workfile

#OARun_main()

arginput="/home/user/testfile_for_run.oas"
if arginput[-3:] != "oas":
    print "This file is not an OAS"
else:
    splt=arginput.rsplit("/",1)
    masterfile_path=arginput
    masterfile_file=splt[1]
    masterfile_dir=splt[0]+"/"