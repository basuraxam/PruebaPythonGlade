#!/usr/bin/env python
# -*- coding: utf-8 -*-



import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def onAnadirClicked(builder):
#    texto = eIdNom.get_text()
#    lIdRes.set_text("Hola %s" % texto)
#    model.append(["prueba"])
    print("Añadir Texto")

def mainQuit(builder):
    Gtk.main_quit()


builder = Gtk.Builder()
builder.add_from_file("pruebaboton2.glade")


signals = { "on_bAñadir_clicked" : onAnadirClicked,
            "gtk_main_quit" : mainQuit }


builder.connect_signals(signals)

#eIdNom = builder.get_object("eIdNombre")
#lIdRes = builder.get_object("lIdResultado")

#model = Gtk.ListStore(str)
#lstWeb = builder.get_object("listaweb")
#lstWeb.
window = builder.get_object("window1")
window.show_all()

Gtk.main()
