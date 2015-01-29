#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import serial
import time
import pyglet

arduino = serial.Serial('/dev/ttyACM2', 9600, timeout = 3.0)
song1 = pyglet.media.load('zombieprueba.mp3')
player = pyglet.media.Player();
player.queue(song1);

def reproducir(id):
	if (id == "1"):
		player.play()

while True:
    lineaLeida = arduino.readline()												  
    if lineaLeida:
    	reproducir('1')

