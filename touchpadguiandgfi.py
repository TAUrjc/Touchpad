#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pygame
import gtk, sys
import threading

threads = list()
pygame.mixer.init()
flanco = True
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)  #el ttyACM0 puede depender, se mira en el Arduino abajo a la derecha
sound1 = pygame.mixer.Sound('base.ogg')
sound2 = pygame.mixer.Sound('verse2.ogg')
sound3 = pygame.mixer.Sound('verse3.ogg')


def sonido(lineaLeida):
    if (lineaLeida == '2\r\n'):
	try:
	    sound1.play(loops = -1);
	    print "ESCRIBO DESPUES DE LA BASE"
	except pygame.error, message:
	    print "base" + sound1.name
	    

    elif lineaLeida == '3\r\n':
	try:
	    sound2.play(loops = 0);
	except pygame.error, message:
	    print "sound2" + sound2.name
	    
    elif lineaLeida == '4\r\n':
	try:
	    sound3.play(loops = 0);
	except pygame.error, message:
	    print "sound3" + sound3.name
    else:
	print "Error de lectura (Leo cosas raras)"


class PyApp(gtk.Window):
   
    def __init__(self):
        super(PyApp, self).__init__()

        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)

        def b1(b):
	 print "boton 1"
         sonido('3\r\n')

        def b2(b):
	 print "boton 2"  
         sonido('4\r\n')

        def base(b):
	 print "base"    
         sonido('2\r\n')
        
        self.set_title("Buttons")
        self.set_size_request(400, 300)
        self.set_position(gtk.WIN_POS_CENTER)

        btn1 = gtk.Button("Sound1")
        btn1.set_sensitive(True)
        btn1.set_size_request(80, 80)
        btn2 = gtk.Button("Sound2")
        btn2.set_sensitive(True)
        btn2.set_size_request(80, 80)
        btn3 = gtk.Button("Base")
        btn3.set_sensitive(True)
        btn3.set_size_request(80, 80)
        btn1.connect('clicked', b1)
        btn2.connect('clicked', b2)
        btn3.connect('clicked', base)

        fixed = gtk.Fixed()

        fixed.put(btn1, 50, 93)
        fixed.put(btn2, 150, 93)
        fixed.put(btn3, 260, 93)
        
        self.connect("destroy", gtk.main_quit)
        
        self.add(fixed)
        self.show_all()

def gui():
    PyApp()
    gtk.main()


def gfi():    	
    while True:
       print "EHEHE ME METO EN EL BUCLE"
       try:
	   lineaLeida = arduino.readline()												  
	   if lineaLeida:
		try:
		    sonido(lineaLeida)
		    #thread.start_new_thread(sonido, (lineaLeida, ))
		except:
		    print "error: fallo al lanzar el thread"
       except serial.serialutil.SerialException:
	    print "Error del serial"
	    pass
       except OSError:
	    print "Error del OS"
	    pass

t1 = threading.Thread(target=gui, args=( ))
threads.append(t1)
t1.start()
t2 = threading.Thread(target=gfi, args=( ))
threads.append(t2)
t2.start()
