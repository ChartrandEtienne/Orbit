from math import *
from pom import pom
from missileGra import missileGra

class missile:
	def __init__(self, parPom):
		self.pom = parPom
		self.gra = missileGra()
		self.age = 0
		self.rayon = 0.1
		# creve apres 10 secondes; sujet a changement
		self.dureeVie = 10
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
		self.age += tick
		if self.age > self.dureeVie:
			return 1
		return 0
	def collision(self, other):
		return False
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
		# l'angle est dependant du vecteur vitesse; le missile pointe la ou il va.
		self.age += tick
		self.pom.angleVeloc()
		if self.age > self.dureeVie:
			return 1
		return 0
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		# XXX: un putain de missile ne devrait pas avoir a shoot()
		return 0


