import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onDraw(self, x, y):
        print("onDraw: ", x, y)

    def onEvent(self, x, y):
        print("onEvent: ", x, y)

builder = Gtk.Builder()
builder.add_from_file("zPlane.glade")
builder.connect_signals(Handler())

window = builder.get_object("zPlane")
window.show_all()

Gtk.main()
