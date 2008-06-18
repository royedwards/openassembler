###OpenAssembler Node python file###

class TXT_Combine:
#This is the main class to be imported

   def TXT_Combine_main(output, TXT_01, TXT_02):
      #This is the main definition to be called

      #--------------------
      #
      #   Your program code will be here
      #   If you keep the names, and the functions
      #   than everything have to be allright!!
      #
      #--------------------
     try:
         outTXT=str(TXT_01)+str(TXT_02)
     except:
         print "Error: Some error happened within the TXT_Combine!!!"
         return ":!:"

     if output=="TXT":
         return outTXT
     else:
         print "Error: Invalid output selected on TXT_Combine node!!!"
         return ":!:"


