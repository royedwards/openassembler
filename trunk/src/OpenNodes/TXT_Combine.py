###OpenAssembler Node python file###
'''

define
{
	name TXT_Combine
	tags oas:test
	input string TXT_01 "<input string>"
	input string TXT_02 "<input string>"
	output string TXT "<output string>"
}

'''

class TXT_Combine:
#This is the main class to be imported

   def TXT_Combine_main(self,output, TXT_01, TXT_02):
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


