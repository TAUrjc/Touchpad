#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pyglet

flanco = True
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)  #el ttyACM0 puede depender, se mira en el Arduino abajo a la derecha
#song1 = pyglet.media.load('verse2.aif')
song1 = pyglet.resource.media('verse1.mp3')
song2 = pyglet.resource.media('verse2.mp3')
song3 = pyglet.resource.media('verse3.mp3')

#player = pyglet.media.Player();
#player.queue(song1);

def reproducir(id):
	global flanco
	if (id == "2"):
		song1.play()
	elif(id == '3' ):
		song2.play()
	elif(id == '4'):
		song3.play()
		
	#pyglet.app.run()
	
while True:
   lineaLeida = arduino.readline()												  
   if lineaLeida:
   		if (lineaLeida == '2\r\n'):
   			reproducir('2')
   		elif lineaLeida == '3\r\n':
   			reproducir('3')
   		elif lineaLeida == '4\r\n':
   			reproducir('4')
