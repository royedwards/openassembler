###OpenAssembler Node python file###

'''
define
{
	name collect_imgs
	tags opsub
	input array1D Images "" ""
	input file Folder "" ""
	input file Master "" ""
	output array1D result "" ""

}
'''
import os, sys,time, Image
from Setup import opdb_setup

class collect_imgs(opdb_setup):
   def collect_imgs_main(self, **connections):
	try:
		Images=connections["Images"]
	except:
		Images=""
	try:
		Folder=connections["Folder"]
	except:
		Folder=""
	try:
		Master=connections["Master"]
	except:
		Master=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			ret=[]
			if Master=="":
				pass
			else:
				if os.path.isfile(Master):
					tee=[Master]
					Images.remove(Master)
					for im in Images:
						tee.append(im)
					Images=tee
				else:
					return 0
			for n in range(0,len(Images)):
					if os.path.isfile(str(Images[n])):
						if os.path.isdir(Folder):
							tm=str(n+1).zfill(4)
							ofile=Folder+"/"+tm+".jpg"
							Image.open(str(Images[n])).save(ofile)
							ret.append(ofile)
						else:
							return 0
					else:
							return 0

			return ret
		except:
			return 0
			
	else:
		return 0


if __name__ == "__main__":
	print collect_imgs().collect_imgs_main( Images=["/home/simanlaci/teste.tif","/home/simanlaci/test.jpg"], Folder="/home/simanlaci/tmp_opentools", Master="/home/simanlaci/teste.tif", oas_output="result")
 
