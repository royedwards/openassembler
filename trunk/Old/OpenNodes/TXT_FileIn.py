###OpenAssembler Node python file###

'''
define
{
	name TXT_FileIn
	tags oas:test
	input file Text_File "~"
	output string TXT "<text output>"


}
'''



class TXT_FileIn:
#This is the main class to be imported

   def TXT_FileIn_main(self, output, Text_File):
      #This is the main definition to be called

      #--------------------
      #
      #   Your program code will be here
      #   If you keep the names, and the functions
      #   than everything have to be allright!!
      #
      #--------------------
     try:
         filein=open(str(Text_File),"r")
         text=filein.read()
         filein.close()
     except:
         print "Error: Some error happened within the TXT_FileIn!!!"
         return ":!:"

     if output=="TXT":
         return text
     else:
          print "Error: Invalid output selected on TXT_FileIn node!!!"
          return ":!:"
