#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pygame
#import thread

pygame.mixer.init()
flanco = True
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)  #el ttyACM0 puede depender, se mira en el Arduino abajo a la derecha
sound1 = pygame.mixer.Sound('base.ogg')
sound2 = pygame.mixer.Sound('verse2.ogg')
sound3 = pygame.mixer.Sound('verse3.ogg')



def sonido(lineaLeida):
    try:
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
	    print "ESTOY LEYENDO BASURA"
    except OSError:
	print "Se me ha fastidiao el OS"
    except serial.serialutil.SerialException:
	print "Se me ha fastidiao el SERIAL"
    	
while True:
   lineaLeida = arduino.readline()												  
   if lineaLeida:
	try:
	    sonido(lineaLeida)
	    #thread.start_new_thread(sonido, (lineaLeida, ))
	except:
	    print "error: fallo al lanzar el thread"
