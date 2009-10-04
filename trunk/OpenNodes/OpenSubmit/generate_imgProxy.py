###OpenAssembler Node python file###

'''
define
{
	name generate_imgProxy
	tags opsub
	input array1D Images "" ""
	input file Folder "" ""
	output int result "" ""

}
'''
import os, sys,time, Image,shutil
from Setup import opdb_setup

class generate_imgProxy(opdb_setup):
   def generate_imgProxy_main(self, **connections):
	try:
		Images=connections["Images"]
	except:
		Images=""
	try:
		Folder=connections["Folder"]
	except:
		Folder=""
	try:
		oas_output=connections["oas_output"]
	except:
		oas_output="result"
	if oas_output=="result":
		try:
			if os.path.isdir(Folder):
				pass
			else:
				os.makedirs(Folder)
			if os.path.isdir(Folder+"/full"):
				pass
			else:
				os.makedirs(Folder+"/full")
			if os.path.isdir(Folder+"/half"):
				pass
			else:
				os.makedirs(Folder+"/half")
			if os.path.isdir(Folder+"/proxy"):
				pass
			else:
				os.makedirs(Folder+"/proxy")
			if os.path.isdir(Folder+"/thumbnail"):
				pass
			else:
				os.makedirs(Folder+"/thumbnail")

			for n in range(0,len(Images)):
					if os.path.isfile(Images[n]):
							ofile=os.path.basename(Images[n])
							pngof=ofile.split(".")[0]+".png"
							shutil.copy(Images[n],Folder+"/full/"+ofile)
							imorig=Image.open(Images[n])
							osize=imorig.size
							hsize=(int(osize[0]/2),int(osize[1]/2))
							psize=(int(osize[0]/5),int(osize[1]/5))
							tsize=(int(osize[0]/10),int(osize[1]/10))
							imh=imorig.resize(hsize)
							imp=imorig.resize(psize)
							imt=imorig.resize(tsize)
							imh.save(Folder+"/half/"+ofile)
							imp.save(Folder+"/proxy/"+ofile)
							imt.save(Folder+"/thumbnail/"+pngof)
					else:
							return 0

			return 1
		except:
			return 0
			
	else:
		return 0


if __name__ == "__main__":
	print generate_imgProxy().generate_imgProxy_main( Images=['/home/simanlaci/tmp_opentools/0001.jpg', '/home/simanlaci/tmp_opentools/0002.jpg'], Folder="/home/simanlaci/tmp_opentools/result", oas_output="result")
 
