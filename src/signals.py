import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Signals:

	def __init__(self, zp):
		self.zPlane = zp

	def onDestroy(self, *args):
        	Gtk.main_quit()
	
	def onClick(self, widget, button):
		print("onClick: ", button.x, button.y)
		cr = widget.get_child().cairo_create()
		cr.set_line_width(9)
        	cr.set_source_rgb(0.7, 0.2, 0.0)
                
        	cr.arc(button.x, button.y, 50, 0, 2*math.pi)
        	cr.stroke_preserve()
        
        	cr.set_source_rgb(0.3, 0.4, 0.6)
        	cr.fill()

