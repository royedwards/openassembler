###OpenAssembler Node python file###

class TXT_Replace:
#This is the main class to be imported

   def TXT_Replace_main(output, Original, InputA, InputB):
      #This is the main definition to be called

      #--------------------
      #
      #   Your program code will be here
      #   If you keep the names, and the functions
      #   than everything have to be allright!!
      #
      #--------------------
      try:
          text_to_replace=str(Original)
          text_to_replace.replace(str(InputA),str(InputB))
      except:
         print "Error: Some error happened within the TXT_Replace!!!"
         return ":!:"

      if output=="TXT":
         return text_to_replace
      else:
          print "Error: Invalid output selected on TXT_Replace node!!!"
          return ":!:"


