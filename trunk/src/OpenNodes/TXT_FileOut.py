###OpenAssembler Node python file###

class TXT_FileOut:
#This is the main class to be imported

   def TXT_FileOut_main(self, output, Filename, TXT):
      #This is the main definition to be called

      #--------------------
      #
      #   Your program code will be here
      #   If you keep the names, and the functions
      #   than everything have to be allright!!
      #
      #--------------------
     try:
         fileout=open(str(Filename),"w")
         fileout.write(str(TXT))
         fileout.close()
         print "File: " + Filename + " saved!!!"
     except:
         print "Error: Some error happened within the TXT_FileOut!!!"
         return ":!:"


