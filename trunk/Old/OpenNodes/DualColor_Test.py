###OpenAssembler Node python file###

'''
define
{
	name DualColor_Test
	tags oas:test
	input string Text "put some text here"
	input color Color1 "1 0 0"
	input color Color2 "0 1 0"
	input color Color3 "0 0 1"
	output string TXT "here we are"

}
'''


class TXT_In:
#This is the main class to be imported

   def TXT_In_main(self,output, Text):
      #This is the main definition to be called

      #--------------------
      #
      #   Your program code will be here
      #   If you keep the names, and the functions
      #   than everything have to be allright!!
      #
      #--------------------

      if output=="TXT":
         return Text
      else:
          print "Error: Invalid output selected on TXT_In node!!!"
          return ":!:"

