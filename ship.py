from math import *
from cercle import cercle
from pom import pom
class ship:
	def __init__(self, parPom, parGra):
		self.pom = parPom
		self.gra = parGra
#	def commande(nouveauPom):
#		self.pom.
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
		for i in range(0, len(
		return False
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		# nouveau = ship(self.pom.addShooty((veloc * sin(self.a)) (veloc * cos(self.a)), cercle()))
		# nouveau = ship(self.pom.addShooty(veloc * sin(self.a), veloc * cos(self.a)), cercle())
		nouveau = ship(self.pom.addShooty(sin(self.pom.a), veloc * cos(self.pom.a)), cercle())
		# Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
		return nouveau
