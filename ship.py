from math import *
from cercle import cercle
from pom import pom
class ship:
	def __init__(self, parPom, parGra):
		self.pom = parPom
		self.gra = parGra
		self.age = 0
		self.rayon = 0.5
#	def commande(nouveauPom):
#		self.pom.
	def collision(self, other):
		if self.pom.distance(other.pom) < (self.rayon + other.rayon):
			# nombre arbitraire: un missile devient actif des qu'il a 4 secondes
			# sinon, on a une collision avec le tireur
			# ce qui est emmerdant pour plusieurs raisons
			if other.age > 4:
				return True
		else:
			return False	
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
		self.age += tick 
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		# nouveau = ship(self.pom.addShooty((veloc * sin(self.a)) (veloc * cos(self.a)), cercle()))
		# nouveau = ship(self.pom.addShooty(veloc * sin(self.a), veloc * cos(self.a)), cercle())
		nouveau = ship(self.pom.addShooty(sin(self.pom.a), veloc * cos(self.pom.a)), cercle())
		# Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
		return nouveau
