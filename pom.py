from numpy import *


import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *
from math import *

from copy import *

# a: acceleration (m/s**2)
# M: masse de la planete (kg)
# r: rayon depuis le centre de la planete (m)
# G: constante gravitationnelle universelle
# a = (GM) / r ** 2
# G = 6.6726 * 10 ** -11 
G = 6.6726 * 10 ** 1

# NOTE
# orbite rond pour une velocite v, un rayon R et une masse M:
# v = sqrt(M * G / r)

# escape velocity:
# v = sqrt(2 * M * G / r)

# classe Point of Mass: 
# position en x et y, en metres
# vitesse vers x et y, en m/s
# masse, en kg (1kg pour une masse insignifiante (utile pour eviter le probleme des 3 corps))
# sert a implementer les operations physiques de base
# sera essentiellement la classe mere de toutes les planetes et vaiseaux
# 
# sim: prends un autre point de masse et calcule la position de self apres le temps tick selon l'attraction de pom. Possiblement d'un tableau de pom si j'en ai le courage
class pom:
	def __init__(self, parPx, parPy, parVx, parVy, parMasse = 1, parAngle = 0):
		self.previsions = []
		self.px = parPx
		self.py = parPy
		self.vx = parVx
		self.vy = parVy
		self.m = parMasse
		self.a = parAngle
	def __copy__(objet):
		return pom(objet.px, objet.py, objet.vx, objet.vy, objet.m, objet.a)
	def prevision(self, gravite, tick, iterations):
		if not self.previsions:
			self.previsions = [copy(self)]
		for i in range(len(self.previsions), iterations):
			prevision = copy(self.previsions[-1])
			prevision.sim(gravite, tick)
			self.previsions.append(prevision)
	def addCommande(self, commande):
		self.px += commande.px
		self.py += commande.py
		self.vx += commande.vx
		self.vy += commande.vy
		self.a += commande.a
	def getAngleDeg(self):
		return (self.a * 180 / pi) - 90
	def addShooty(self, veloc):
		velocx = veloc * cos(self.a)
		velocy = veloc * sin(self.a)
		nouveau = pom(self.px, self.py, self.vx + velocx, self.vy + velocy, 0, self.a)
		return nouveau
	def angleVeloc(self):
		if self.vx == 0:
			if self.vy > 0:
				self.a = pi / 2
				return 
			if self.vy < 0:
				self.a = 3 * pi / 2
				return
		if self.vy == 0:
			if self.vx > 0:
				self.a = 0
				return 
			if self.vx < 0:
				self.a = pi
				return
		if self.vx == 0 and self.vy == 0:
			return	
		angle = atan(self.vy / self.vx)
		if self.vx < 0:
			self.a = angle + pi
		else:
			self.a = angle
		# print self.a
		return
	def distance(self, autre):
		deltax = -1 * (autre.px - self.px)
		deltay = -1 * (autre.py - self.py)
		return sqrt(abs(deltax ** 2) + (deltay ** 2))
	def sim(self, gravite, tick):
		if self.previsions:
			elem = self.previsions.pop(0)
			self.px = elem.px
			self.py = elem.py
			self.vx = elem.vx
			self.vy = elem.vy
			return
		global G
		deltax = -1 * (gravite.px - self.px)
		deltay = -1 * (gravite.py - self.py)
		r = sqrt(abs(deltax ** 2) + abs(deltay ** 2)) 
		xsurr = deltax / r
		ysurr = deltay / r
		a = (G * gravite.m) / (r ** 2)
		# pour eviter d'avoir un trou noir
		if r < 1:
			a = 10
		# composante x
		ax = a * xsurr
		newpx = self.px + ((self.vx * tick) - (ax * tick ** 2) / 2)
		# newv = self.vx - ax * tick
		# self.px = newp
		# self.vx = newv
		ay = a * ysurr
		# composante y
		newpy = self.py + ((self.vy * tick) - (ay * tick ** 2) / 2)
		# rayon a la position estimee
		r2 = sqrt(abs((deltax + newpx) ** 2) + (abs((deltay + newpy) ** 2)))
		# acceleration a la position estimmee
		a2 = (G * gravite.m) / (r ** 2)
		# moyenne
		# a = (a + a2) / 2
		a = a2
		ax = a * xsurr
		ay = a * ysurr
		# positions et vitesses selon l'acceleration moyenne
		newvx = self.vx - (ax * tick) / 2
		newvy = self.vy - (ay * tick) / 2
		newpx = self.px + ((newvx * tick) - (ax * tick ** 2) / 2)
		newpy = self.py + ((newvy * tick) - (ay * tick ** 2) / 2)
		newvx = newvx - (ax * tick) / 2
		newvy = newvy - (ay * tick) / 2
		self.px = newpx
		self.py = newpy
		self.vx = newvx
		self.vy = newvy
		# newv = self.vy - ay * tick 
		# self.py = newp 
		# self.vy = newv
