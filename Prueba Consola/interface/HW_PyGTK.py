import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.say_hello, None)
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

    def say_hello(self, widget, data=None):
        print "Hello World"


hello = HelloWorld()
hello.main()
