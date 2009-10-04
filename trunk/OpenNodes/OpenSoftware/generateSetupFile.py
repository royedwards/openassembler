###OpenAssembler Node python file###

'''
define
{
	name generateSetupFile
	tags opsw
	input file ProjectPath "" ""
	input file VaultPath "" ""
	input file AdminPath "" ""
	input file DevPath "" ""
	output int result "" ""

}
'''
import os, sys, platform

class generateSetupFile():
   def generateSetupFile_main(self, **connections):
		ProjectPath=str(connections["ProjectPath"])
		VaultPath=str(connections["VaultPath"])
		AdminPath=str(connections["AdminPath"])
		DevPath=str(connections["DevPath"])
		opdb_userhome=""
		opdb_home=""
		soft_dir=""
		if os.name=="nt":
			opdb_userhome=os.environ.get("USERPROFILE")
			opdb_home=str(opdb_userhome)+"/OpenAssembler"
			soft_dir="C:\OpenTools"
		else:
			opdb_userhome=os.environ.get("HOME")
			opdb_home=str(opdb_userhome)+"/.OpenAssembler"
			soft_dir="/opt/OpenTools"

		
		
		oas_setup="""
menucategory OpenProject opdb
menucategory OpenEdit oped
menucategory OpenCoOrdination ocoo
menucategory OpenModules opm
menucategory OpenSubmit opsub
menucategory QtModules qtmod
menucategory PyModules pymod
menucategory Misc  msc 
menucategory Math math
menucategory OpenSoftware opsw
menucategory customQtWidgets qtwidg
   
variablecategory Text file,string
variablecategory Number int,float
variablecategory 1DArray array1D
variablecategory 2DArray array2D
variablecategory ShotInfo shotInfo
variablecategory MultyShedule multyShedule
variablecategory MultyUser multyUsers
variablecategory MultyEdit multyEdit

manualpath /home/[USER]/Development/OpenNodes

"""

		proj_setup="project_root "+ProjectPath+"\n"
		proj_setup+="vault_root "+VaultPath+"\n"
		proj_setup+="admin_root "+AdminPath+"\n"
		proj_setup+="dev_root "+DevPath+"\n"

		try:
			os.makedirs(opdb_home)

		except:
			print "There is some problem with the OpenAssembler-setup-directory creation!"

		try:
			os.makedirs(opdb_userhome+"/tmp_opentools/img_cache")
			if os.name!="nt":
				os.system("chmod -R 777 "+opdb_userhome+"/tmp_opentools/")
		except:
			print "There is some problem with the tmp-dir creation!"

		try:
			if os.name=="nt":
				os.makedirs("C:\OpenTools\bin")
			else:
				os.makedirs("/opt/OpenTools/bin")
		except:
			print "There is some problem with the OpenTools-dir creation!"

		try:
			if os.name=="nt":
				os.makedirs("C:\OpenTools\Icons")
			else:
				os.makedirs("/opt/OpenTools/Icons")
		except:
			print "There is some problem with the OpenTools-dir creation!"

		try:
			if os.name=="nt":
				os.makedirs("C:\OpenTools\OpenNodes")
			else:
				os.makedirs("/opt/OpenTools/OpenNodes")
		except:
			print "There is some problem with the OpenTools-dir creation!"

		fl=open(opdb_home+"/OpenAssembler.ini","w")
		fl.write(str(oas_setup))
		fl.close()

		fl=open(opdb_home+"/OpenProjectDb.ini","w")
		fl.write(str(proj_setup))
		fl.close()

		if os.name!="nt":
			os.system("chmod -R 777 "+opdb_home)


