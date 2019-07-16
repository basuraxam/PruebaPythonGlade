#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def onAnadirClicked(builder):
    texto = lText.get_text()
#    lIdRes.set_text("Hola %s" % texto)
    lstWeb.append([texto,"masTxt5"])

    print("Añadir ( %s ) Texto" % texto)

def mainQuit(builder):
    Gtk.main_quit()


builder = Gtk.Builder()
builder.add_from_file("/home/sykey/Documentos/Python_Glade_GTK/PruebaBoton2/pruebaboton2.glade")


signals = { "on_bAñadir_clicked" : onAnadirClicked,
            "gtk_main_quit" : mainQuit }


builder.connect_signals(signals)

lText  = builder.get_object("lTexto")
lstWeb = builder.get_object("liststore1")

window = builder.get_object("window1")
window.show_all()

Gtk.main()

