#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pyglet

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout = 3.0)  #el ttyACM0 puede depender, se mira en el Arduino abajo a la derecha
song1 = pyglet.media.load('verse2.aif')
player = pyglet.media.Player();
player.queue(song1);

def reproducir(id):
	if (id == "2"):
		player.play()
	elif(id == '3'):
		player.play()
	elif(id == '4'):
		player.play()



while True:
   lineaLeida = arduino.readline()												  
   if lineaLeida:
   		if (lineaLeida == '2\r\n'):
   			reproducir('2')
   		elif lineaLeida == '3\r\n':
   			reproducir('3')
   		elif lineaLeida == '4\r\n':
   			reproducir('4')
   		else:
   			print lineaLeida,

   		

