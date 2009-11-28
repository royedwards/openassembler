###OpenAssembler Node python file###

'''
define
{
	name copyFileToVault
	tags opdb
	input dbPath dbPath "" ""
	input file filePath "" ""
	input string forcename "" ""
	input string memo "" ""
	output any result "" ""

}
'''
import os, sys,shutil
from OpenProject.getVaultPath import getVaultPath

class copyFileToVault():
   def copyFileToVault_main(self, **connections):
	try:
		dbPath=connections["dbPath"]
	except:
		dbPath=""
	try:
		filePath=connections["filePath"]
	except:
		filePath=""
	try:
		forcename=connections["forcename"]
	except:
		forcename=""
	try:
		memo=connections["memo"]
	except:
		memo=""


	if os.path.isfile(filePath):
		pass
	else:
		return 0

	vPath=gVP(dbPath)
	if vPath=="" or vPath==0:
		return 0

	try:
		shutil.copy(filePath,vPath+"/"+forcename)
	except:
		return 0

	try:
		fl=open(vPath+"/memo.atr","w")
		fl.write(memo)
		fl.close()
	except:
		return 0
	return 1

def gVP(Path):
	return getVaultPath().getVaultPath_main(Path=Path)