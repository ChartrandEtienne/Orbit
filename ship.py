from math import *
from cercle import cercle
from pom import pom
from missile import missile
class ship:
	def __init__(self, parPom, parGra):
		self.pom = parPom
		self.gra = parGra
		self.age = 0
		self.rayon = 0.5
	def commande(self, nouveauPom):
		self.pom.addCommande(nouveauPom)
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
		return 0
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		nouveau = missile(self.pom.addShooty(veloc))
		return nouveau
