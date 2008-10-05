######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

import colorsys
from Tkinter import *
import sys

class convertColors:
  def Rgb2Hex(self,rgb_tuple):
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

  def Hex2RGB(self,colorstring):
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

class OAssemblerColorPicker(Frame):
	def OpenAssemblerColorPicker(self,inputcolor):
		Frame.__init__(self,master=None)
		self.grid()
		b=Button(self,text="f",command=lambda :sys.exit(0))
		b.grid()


class _run(OAssemblerColorPicker):
	def __init__(self):
		self.OpenAssemblerColorPicker("")


class Picker:
	def __init__(self):
		app=_run()
		app.mainloop()

#Picker()
