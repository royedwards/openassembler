import os,sys

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


AddSysPath("/W/Projects/projectDb/Softwares/bin/OpenAssembler")

from Core.Console.Console import oas_console
from Core.Dbase.Dbase_init import dBase_Init
from Core.Gateway.Gateway import oas_gateway

class oas_loader(dBase_Init,oas_console,oas_gateway):
	def i(self,args):

		self.dBase_builder()


		oas_template=args[0]
		target=args[1]
		project=args[2]
		shot=args[3]
		node_pass=args[4]
		parm_setup=args[5]
		ff=args[6]
		ef=args[7]

		inc=args[8]
		ht=args[9]
		type=args[10]
		pathOverride=args[11]

		comm=""
		for n in range(12,len(args)):
			comm+=args[n]+" "

		comm=comm.strip()

		self.oas_open(filename=oas_template,filetype="oas")

		self.oas_set(nodevalue="dataNode.Project",value=project)
		self.oas_set(nodevalue="dataNode.Shot",value=shot)

		self.oas_set(nodevalue="dataNode.Node_Pass",value=node_pass)
		self.oas_set(nodevalue="dataNode.Param_Setup",value=parm_setup)
	
		self.oas_set(nodevalue="dataNode.pathOverride",value=pathOverride)

		self.oas_set(nodevalue="_HnT_._in",value=ht)
		self.oas_set(nodevalue="_firstFrame_._in",value=ff)
		self.oas_set(nodevalue="_endFrame_._in",value=ef)
		self.oas_set(nodevalue="dataNode.Increment",value=inc)

		self.oas_set(nodevalue="_Type_._in",value=type)
		self.oas_set(nodevalue="comment_in._in",value=comm)

		self.oas_set(nodevalue="_LorF_._in",value=target)

		return self.oas_houdini()
	   

app = oas_loader().i(sys.argv[1:])

AddSysPath(app[0])
exec("from "+app[1]+" import main_app_start")

main_app_start()

os.remove(app[0]+"/"+app[1]+".py")
try:
    os.remove(app[0]+"/"+app[1]+".pyc")
except:
    pass
