from numpy import *
from vector import vector

import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

# a: acceleration (m/s**2)
# M: masse de la planete (kg)
# r: rayon depuis le centre de la planete (m)
# G: constante gravitationnelle universelle
# a = (GM) / r ** 2
# G = 6.6726 * 10 ** -11 
G = 6.6726 * 10 ** 1

# classe Point of Mass: 
# position en x et y, en metres
# vitesse vers x et y, en m/s
# masse, en kg (1kg pour une masse insignifiante (utile pour eviter le probleme des 3 corps))
# sert a implementer les operations physiques de base
# sera essentiellement la classe mere de toutes les planetes et vaiseaux
# 
# sim: prends un autre point de masse et calcule la position de self apres le temps tick selon l'attraction de pom. Possiblement d'un tableau de pom si j'en ai le courage
class pom:
	def __init__(self, parPosition, parVelocite, parMasse = 1):
		self.p = parPosition
		self.v = parVelocite
		self.m = parMasse	
	def sim(self, gravite, tick):
		global G
		deltax = -1 * (gravite.p.x - self.p.x)
		deltay = -1 * (gravite.p.y - self.p.y)
		r = sqrt(abs(deltax ** 2) + abs(deltay ** 2)) 
		xsurr = deltax / r
		ysurr = deltay / r
		a = (G * gravite.m) / (r ** 2)
		# pour eviter d'avoir un trou noir
		if r < 1:
			a = 10
		# composante x
		ax = a * xsurr
		newp = self.p.x + ((self.v.x * tick) - (ax * tick ** 2) / 2)
		newv = self.v.x - ax * tick
		self.p.x = newp
		self.v.x = newv
		ay = a * ysurr
		# composante y
		newp = self.p.y + ((self.v.y * tick) - (ay * tick ** 2) / 2)
		newv = self.v.y - ay * tick 
		self.p.y = newp 
		self.v.y = newv
