###OpenAssembler Node python file###

'''
define
{
	name get_TextEdit
	tags qtmod
	input uiItem Entry "" ""
	output string toPlainText "" ""
	output html toHtml "" ""

}
'''
import os, sys, platform

class get_TextEdit():
	def get_TextEdit_main(self, **connections):
		Entry=connections["Entry"]
		try: 
		    oas_output=connection["oas_output"]
		except:
		    oas_output="toPlainText"
		if Entry=="":
			return 0
		if oas_output=="toPlainText":
			return str(Entry.toPlainText())
		if oas_output=="toHtml":
			return str(Entry.toHtml())


