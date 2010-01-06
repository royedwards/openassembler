###OpenAssembler Node python file###

'''
define
{
	name clipboardCopy
	tags pymod
	input any toCopy "" ""
	output any copied "" ""

}
'''
try:
	import pygtk
	import gtk
except:
	print "PyGTK will not work!"

class clipboardCopy():
	def clipboardCopy_main(self, **connections):
		try:
			clipboard=gtk.clipboard_get()
			clipboard.set_text(str(connections["toCopy"]))
			return str(connections["toCopy"])
		except:
			return 0
