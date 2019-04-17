import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from signals import Signals
from coord import Coord

class zPlane:
	def __init__(self, g):
		self.gladeFile = g
		self.signals = Signals(self)
		self.setup()
		self.coords = []
		
	def setup(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(self.gladeFile)
		self.builder.connect_signals(self.signals)
		self.window = self.builder.get_object("zPlane")
		self.drawing_area = self.builder.get_object("drawingArea")

	def show(self):
		self.window.show_all()

	def main(self):
		Gtk.main()

	def addCoord(self, x, y):
		self.coords.append(Coord(x, y))
