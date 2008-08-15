#---------------------------------------------------------------------------------------------------------------------
#
#    Gui Starting script....
#
#    Created by: Laszlo Mates (laszlo.mates@gmail.com)
#    2007
#
#---------------------------------------------------------------------------------------------------------------------

import colorsys


class convertColors:
  def RGB2Hex(rgb_tuple):
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

  def Hex2RGB(colorstring):
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

