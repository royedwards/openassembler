You can istall OpenAssembler several way:

  1. You download the executeable-package from this site
  1. You download the python scripts from this site, and you running them
  1. svn checkout http://openassembler.googlecode.com/svn/trunk/ openassembler-read-only

[requirements](requirements.md)

After you get it, you can copy it somewhere, and it is ready to use.

It is worth to include its path to the global environment.

Maybe you need to edit the setup file (was generated automaticaly on the first run)

The setup file is in your home directory under the folder: **.OpenAssembler**

This file is looks like this:

```
#environments   SA_SCRIPT_PATH
font Helvetica
fontsize 12

port server 23345
port editor 23346
			
manualpath <path to your oas copy>/OpenAssembler/OpenNodes


menucategory Math math
menucategory Viewer viewer
menucategory OpenAssembler oas
   
   
variablecategory red path,string
variablecategory blue int,aint,vint,avint,float,afloat,vfloat,avfloat
variablecategory green matrix,amatrix,vmatrix,avmatrix
variablecategory black color,point,vector,avector,vvector,avvector


```