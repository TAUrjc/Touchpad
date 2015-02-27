#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pygame
pygame.mixer.init()
flanco = True
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)  #el ttyACM0 puede depender, se mira en el Arduino abajo a la derecha

#player = pyglet.media.Player();
#player.queue(song1);


		
	#pyglet.app.run()
	
while True:
   lineaLeida = arduino.readline()												  
   if lineaLeida:
   		if (lineaLeida == '2\r\n'):
			pygame.mixer.music.load("verse1.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
			    continue

   		elif lineaLeida == '3\r\n':
			pygame.mixer.music.load("verse2.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
			    continue
   		elif lineaLeida == '4\r\n':
   			pygame.mixer.music.load("verse3.mp3")
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
			    continue
