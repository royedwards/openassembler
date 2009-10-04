###OpenAssembler Node python file###

'''
define
{
	name get_LineEntry
	tags qtmod
	input uiItem Entry "" ""
	output string text "" ""
	output string selectedText "" ""

}
'''
import os, sys, platform

class get_LineEntry():
	def get_LineEntry_main(self, **connections):
		Entry=connections["Entry"]
		try: 
		    oas_output=connection["oas_output"]
		except:
		    oas_output="text"
		if Entry=="":
			return 0
		if oas_output=="text":
			return str(Entry.text())
		if oas_output=="selectedText":
			return str(Entry.selectedText())


