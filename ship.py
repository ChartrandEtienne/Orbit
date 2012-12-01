from math import *
from cercle import cercle
from pom import pom
class ship:
	def __init__(self, parPom, parGra):
		self.pom = parPom
		self.gra = parGra
#	def commande(nouveauPom):
#		self.pom.
	def collision(self, other):
		if self.pom.distance(other.pom) < 5:
			return True
		else:
			return False	
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		# nouveau = ship(self.pom.addShooty((veloc * sin(self.a)) (veloc * cos(self.a)), cercle()))
		# nouveau = ship(self.pom.addShooty(veloc * sin(self.a), veloc * cos(self.a)), cercle())
		nouveau = ship(self.pom.addShooty(sin(self.pom.a), veloc * cos(self.pom.a)), cercle())
		# Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
		return nouveau
