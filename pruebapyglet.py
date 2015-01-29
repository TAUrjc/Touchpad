#!/usr/bin/env python
import pyglet
song = pyglet.media.load('zombieprueba.mp3')
player = pyglet.media.Player();
player.queue(song);


while True:
	player.play()
	