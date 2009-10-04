###OpenAssembler Node python file###

'''
define
{
	name upload_imgs
	tags opsub
	input dbPath Path "" ""
	input file Folder "" ""
	input string Type "" ""
	input string Comment "" ""
	output int result "" ""

}
'''
import os, sys,time, Image,shutil
from OpenProject.getElementType import getElementType
from OpenProject.createNewVersion import createNewVersion
from OpenProject.getVaultPath import getVaultPath
from OpenProject.getCleanPath import getCleanPath

class upload_imgs(getElementType,createNewVersion,getVaultPath,getCleanPath):
   def upload_imgs_main(self, **connections):
	try:
		Path=connections["Path"]
	except:
		Path=""
	try:
		Folder=connections["Folder"]
	except:
		Folder=""
	try:
		Type=connections["Type"]
	except:
		Type=""
	try:
		Comment=connections["Comment"]
	except:
		Comment=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"

	if oas_output=="result":
		try:
			if self.getElementType_main(Path=Path)==0 or self.getElementType_main(Path=Path)=="":
				return 0
			if os.path.isdir(Folder):
				pass
			else:
				return 0
			if str(Type)=="Art":
				newversion=self.createNewVersion_main(Path=Path,ReviewType=Type,Comment=Comment)
			else:
				newversion=self.createNewVersion_main(Path=Path)
			if newversion==0 or newversion=="":
				return 0
			cp=self.getCleanPath_main(Path=Path)
			newpath=cp+"@"+newversion
			vpath=self.getVaultPath_main(Path=newpath)
			content=os.listdir(Folder)
			for c in content:
				shutil.copytree(Folder+"/"+c,vpath+"/"+c)
			return 1
		except:
			return 0
			
	else:
		return 0


if __name__ == "__main__":
	print upload_imgs().upload_imgs_main( Path=":sandbox:Art:References", Folder="/home/simanlaci/tmp_opentools/testeles/result", Type="Art", Comment="Test imgSubm.", oas_output="result")
 
