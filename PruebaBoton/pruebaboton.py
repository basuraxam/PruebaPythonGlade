#!/usr/bin/env python
# -*- coding: utf-8 -*-



import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def onBotonClicked(builder):
    print("Hola Mundo")

def mainQuit(builder):
    Gtk.main_quit()


builder = Gtk.Builder()
builder.add_from_file("pruebaboton.glade")


signals = { "on_boton1_clicked" : onBotonClicked,
            "gtk_main_quit" : mainQuit }


builder.connect_signals(signals)

window = builder.get_object("window1")
window.show_all()

Gtk.main()
