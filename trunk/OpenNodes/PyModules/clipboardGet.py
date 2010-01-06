###OpenAssembler Node python file###

'''
define
{
	name clipboardGet
	tags pymod
	output any content "" ""

}
'''
try:
	import pygtk
	import gtk
except:
	print "PyGTK will not work!"

class clipboardGet():
	def clipboardGet_main(self, **connections):
		try:
			clipboard=gtk.clipboard_get()
			x=clipboard.wait_for_text()
			return x
		except:
			return 0