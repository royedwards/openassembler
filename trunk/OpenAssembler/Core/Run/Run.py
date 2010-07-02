# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

import time, sys, os, shutil, time
from Core.Dbase.Data_handler import oas_data_handler
from Core.Dbase.FileIO import oas_fileio

class oas_execute(oas_data_handler,oas_fileio):
        def oas_run_execute(self,save_file="",runmode="normal",softwarename=""):
                self.runmode=runmode
                self.softwarename=softwarename
                if os.name=="nt":
                        self.oas_userhome=os.environ.get("USERPROFILE") 
                        self.realPath="C:\OpenTools\bin"
                else:
                        self.oas_userhome=os.environ.get("HOME")
                        self.realPath="/opt/OpenTools/bin"

                self.oas_tmp=str(self.oas_userhome)+"/tmp_opentools"
                if os.path.isdir(self.oas_tmp):
                        pass
                else:
                        os.makedirs(self.oas_tmp)

                back=None

                self.node_cross_list={}
                for nds in self.oas_rt.keys():
                        self.node_cross_list[self.oas_rt[nds]['name']]=nds

                if self.node_cross_list!={}:

                        arrangement={}
                        for key in self.oas_rt.keys():
                                if arrangement.has_key(self.oas_rt[key]["nodetype"]):
                                        arrangement[self.oas_rt[key]["nodetype"]].append(self.oas_rt[key]["name"])
                                else:
                                        arrangement[self.oas_rt[key]["nodetype"]]=[self.oas_rt[key]["name"]]

                        chk=0
                        if arrangement.has_key("_def"):
                                for item in arrangement["_def"]:
                                        if item == "__init__":
                                                chk=1
                        if chk==0:
                                print "No __init__ node!!"
                                return 0

                        piramids={}
                        for item in arrangement["_def"]:
                                piramid=self.oas_make_piramid(item)
                                optimized=self.oas_make_optimization(piramid)
                                piramids[item]=optimized

                        for key in piramids.keys():
                                piramids[key].remove(key)

                        paths={}
                        for key in arrangement.keys():
                                paths[key]=self.oas_node_list[key]['path']

                        to_inport={}

                        for key in paths.keys():
                                if paths[key]=="OpenAssembler internal function":
                                        pass
                                else:
                                        for p in self.manualPath:
                                                if paths[key].find(p)>-1:
                                                        to_inport[key]=paths[key].split(p)[1][1:].split(".")[0].replace("/",".").replace("\\",".")

                        js=self.oas_create_jobfile(piramids,to_inport)

                        if save_file!="":
                                try:
                                        jsfile=""
                                        jsfile=save_file
                                        jf=open(jsfile,"w")
                                        jf.write(js)
                                        jf.close()
                                except:
                                        print "Filename is invalid... or other problem during the file save..."
                                        return 0
                        else:
                                lt=time.localtime()
                                loct=""
                                for i in lt:
                                        loct+=str(i)
                                if self.runmode=="houdini":
                                        loct="h"+loct
                                jsfile=""
                                jsfile=self.oas_tmp+"/"+loct+".py"
                                jf=open(jsfile,"w")
                                jf.write(js)
                                jf.close()
                                if self.runmode=="houdini":
                                        emp="__all__=[]"
                                        fi=open(self.oas_tmp+"/__init__.py","w")
                                        fi.write(emp)
                                        fi.close()
                                        return [self.oas_tmp,loct]
                                else:
                                        pyhy="python"
                                        if str(self.oas_rt[self.node_cross_list["__init__"]]["inputs"]["Hython"]["value"])==str(1):
                                                pyhy="hython"
                                        elif str(self.oas_rt[self.node_cross_list["__init__"]]["inputs"]["Nuke"]["value"])==str(1):
                                                pyhy="nuke -t"
                                        else:
                                                pyhy="python"
                                        if os.name=="nt":
                                                back=os.popen(pyhy+" \""+str(jsfile)+"\"")
                                        else:
                                                back=os.popen(pyhy+" "+str(jsfile)+" ")
                                        print >> sys.stdout, back.read()
                                        os.remove(jsfile)
                                        return back
                else:
                        print "There is no node in the scene."
                        return 0
                
        def oas_make_piramid(self,fin_node):
                level=[]
                level_number=0
                next_level_counter=1
                level.append([fin_node])
                while next_level_counter!=0:
                        tmp=self.oas_input_connections(level[level_number])
                        if tmp==[]:
                                next_level_counter=0
                        else:
                                level.append(tmp)
                                level_number+=1
                                next_level_counter=len(level[level_number])                             
                return level
                
# ##############################################################################
# calculate the final order from the levels, check vhen the node firs appear
# ##############################################################################

        def oas_make_optimization(self,level):  
                finallist=[]
                for x in range(0,len(level)):
                        reverse_x=len(level)-x-1
                        exist_chk=0
                        for lev in level[reverse_x]:
                                for flm in finallist:
                                        if flm==lev:
                                                exist_chk=1
                                if exist_chk==1:
                                        exist_chk=0
                                else:
                                        finallist.append(lev)
                                        exist_chk=0
                return finallist
        
        def oas_input_connections(self,node_ins):
                ret=[]
                for node in node_ins:
                        for con in self.oas_rt_connections.keys():
                                if self.oas_rt[self.oas_rt_connections[con]['in_node']]['name']==str(node):
                                        ret.append(self.oas_rt[self.oas_rt_connections[con]['out_node']]['name'])
                return ret
                
        def oas_create_jobfile(self,piramids,to_inport):
                js="""#! /usr/bin/env python
# ################################
# OpenAssembler Job Script
# Created with OpenAssembler V3
#
# ################################

import sys, os

"""
                if os.path.isfile(str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])):
                        js+="from PyQt4 import QtGui,QtCore,uic,QtOpenGL \n"

                if self.runmode=="finalize":
                        pass
                else:
                        js+="""
def AddSysPath(new_path):
        new_path = os.path.abspath(new_path)
        if os.name == 'nt':
                new_path = new_path.lower()
        do = -1
        if os.path.exists(new_path):
                do = 1
                for x in sys.path:
                        x = os.path.abspath(x)
                        if sys.platform == 'win32':
                                x = x.lower()
                        if new_path in (x, x + os.sep):
                                do = 0
                if do:
                        sys.path.append(new_path)
                        pass
        return do

"""

                        for pa in self.manualPath:
                                js+="AddSysPath(\""+str(pa)+"\")\n"

                js+="\n"

                for key in to_inport.keys():
                        js+="from "+str(to_inport[key])+" import "+str(key)+"\n"

                js+="\n"
                self.lastoutput=""

                if os.path.isfile(str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])):
                        js+="class main_app_start(QtGui.QMainWindow):\n\n"
                else:
                        js+="class main_app_start():\n\n"
                
                for definition in piramids.keys():
                        js+="\tdef "+str(definition)+"(self,**args):\n"
                        if definition=="__init__":
                                if os.path.isfile(str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])):
                                        js+="\t\tQtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowFlags())\n"
                                        if self.runmode=="finalize":
                                                js+="\t\tif os.name==\"nt\":\n"
                                                js+="\t\t\tuic.loadUi(\"C:/OpenTools/bin/"+str(self.softwarename)+"/ui/main.ui"+"\",self)\n"
                                                js+="\t\telse:\n"
                                                js+="\t\t\tuic.loadUi(\"/opt/OpenTools/bin/"+str(self.softwarename)+"/ui/main.ui"+"\",self)\n"
                                        else:
                                                js+="\t\tuic.loadUi(\""+str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])+"\",self)\n"
                                        js+="\t\tself.show()\n"
                                js+="\t\tself._cache={}\n"
                                js+="\t\tself._startframe="+str(self.oas_scene_setup['startframe'])+"\n"
                                js+="\t\tself._endframe="+str(self.oas_scene_setup['endframe'])+"\n"
                                js+="\t\t_frame="+str(self.oas_scene_setup['frame'])+"\n"
                        elif definition=="__exit__":
                                if os.path.isfile(str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])):
                                        js+="\t\tself.close()\n"
                                else:
                                        js+="\t\tsys.exit()\n"
                        else:
                                js+="\t\ttry:\n"
                                js+="\t\t\t_frame=args[\"_frame\"]\n"
                                js+="\t\texcept:\n"
                                js+="\t\t\t_frame=self._startframe\n"

                        nodelist=piramids[definition]

                        for n in range (0,len(nodelist)):
                                outs=[]
                                for cns in self.oas_rt_connections.keys():
                                        if self.oas_rt_connections[cns]['out_node']==str(self.node_cross_list[nodelist[n]]):
                                                c=0
                                                for o in outs:
                                                        if str(o)==str(self.oas_rt_connections[cns]['out_value']):
                                                                c=1
                                                if c==0:
                                                        outs.append(str(self.oas_rt_connections[cns]['out_value']))
                                if outs==[]:
                                        outs=["out"]
                                for out in outs:
                                        js+="\t\t"+str(nodelist[n])+"_variable_"+str(out)+"="+str(self.oas_rt[self.node_cross_list[nodelist[n]]]["nodetype"])+"()."+str(self.oas_rt[self.node_cross_list[nodelist[n]]]["nodetype"])+"_main(oas_output=\""+str(out)+"\""
                                        self.lastoutput=str(nodelist[n])+"_variable_"+str(out)
                                        for ins in self.oas_rt[self.node_cross_list[nodelist[n]]]['inputs'].keys():
                                                js+=","+str(ins)+"="
                                                hascon=""
                                                for cns in self.oas_rt_connections.keys():
                                                        
                                                        if (self.oas_rt_connections[cns]['in_node']==str(self.node_cross_list[nodelist[n]])) and (self.oas_rt_connections[cns]['in_value']==str(ins)):
                                                                hascon=self.oas_rt[self.oas_rt_connections[cns]['out_node']]['name']+"_variable_"+self.oas_rt_connections[cns]['out_value']
                                                        else:
                                                                pass 
                                                if hascon=="":
                                                        vl=str(self.oas_rt[self.node_cross_list[nodelist[n]]]['inputs'][ins]['value'])
                                                        if vl[:1]=="=":
                                                                vl=vl[1:]
                                                        elif vl[:1]=="$":
                                                                if piramids.has_key(vl[1:]):
                                                                        vl="self."+str(vl[1:])+"(_frame=_frame,_cache=self._cache)"
                                                                else:
                                                                        vl="self."+str(vl[1:])+"()"
                                                        elif vl[:1]==">":
                                                                vl="self."+str(vl[1:])
                                                        elif self.oas_variablecategory[str(self.oas_rt[self.node_cross_list[nodelist[n]]]['inputs'][ins]['variable_type'])]=="Text" or str(self.oas_rt[self.node_cross_list[nodelist[n]]]['inputs'][ins]['variable_type'])=="any":
                                                                vl="\""+vl+"\""
                                                        js+=vl
                                                else:
                                                        js+=hascon
                                        for setts in self.oas_rt[self.node_cross_list[nodelist[n]]]['settings'].keys():
                                                js+=","+str(setts)+"="+self.oas_rt[self.node_cross_list[nodelist[n]]]['settings'][setts]
                                        js+=", _frame=_frame, _cache=self._cache)\n"
                                if (n+1)==len(nodelist):
                                        if definition!="__init__":
                                                js+="\t\t"+"return "+str(self.lastoutput)+"\n"
                        js+="\n"
                if os.path.isfile(str(self.oas_rt[self.node_cross_list["__init__"]]["settings"]["QtMainWindowUi"])):
                        js+="""

def main():
        app = QtGui.QApplication(sys.argv)
        mas=main_app_start()
        sys.exit(app.exec_())

if __name__ == "__main__":
        main()
"""
                else:
                        js+="""

def main():
        app = main_app_start()
        sys.exit()

if __name__ == "__main__":
        main()

"""
                return js