###OpenAssembler Node python file###

'''
define
{
	name readSetup
	tags opsw
	output file ProjectROOT "" ""
	output file VaultROOT "" ""
	output file AdminROOT "" ""
	output file DevROOT "" ""

}
'''
import os, sys, platform,string

class readSetup():
   def readSetup_main(self, **connections):
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="ProjectROOT"
	try:

		if os.name=="nt":
			opdb_userhome=os.environ.get("USERPROFILE")
			opdb_home=str(opdb_userhome)+"/OpenAssembler"
		else:
			opdb_userhome=os.environ.get("HOME")
			opdb_home=str(opdb_userhome)+"/.OpenAssembler"
	    	
		if os.path.isdir(opdb_home):
			pass
	    	else:
			return ""
		
		opdb_setupFile=opdb_home+"/OpenProjectDb.ini"
		setup_contents_opdb=[]
		
		
		if os.path.isfile(opdb_setupFile)==True:
			path=opdb_setupFile
			file=open(path,"r")
			setupFile_Content=file.read()
			setupFile_Content=setupFile_Content.replace("\r\n","\n")
			file.close()
			setupFile_Content=setupFile_Content.split("\n")
			parsed=[]
			for rws in setupFile_Content:
				ret=rws.split()
				if len(ret)>0:
					if str(rws[:1])!=str("#"):
						parsed.append(ret)

			if oas_output=="ProjectROOT":
				pr=""
				for liness in parsed:
					if liness[0]=="project_root":
						pr=liness[1]
				return pr

			if oas_output=="VaultROOT":
				vr=""
				for liness in parsed:
					if liness[0]=="vault_root":
						vr=liness[1]
				return vr

			if oas_output=="AdminROOT":
				ar=""
				for liness in parsed:
					if liness[0]=="admin_root":
						ar=liness[1]
				return ar

			if oas_output=="DevROOT":
				dv=""
				for liness in parsed:
					if liness[0]=="dev_root":
						dv=liness[1]
				return dv
		
		else:
			return ""
	except:
		return ""
