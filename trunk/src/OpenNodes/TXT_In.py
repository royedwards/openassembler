###OpenAssembler Node python file###

class TXT_In:
#This is the main class to be imported

   def TXT_In_main(output, Text):
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

