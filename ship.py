from math import *
from cercle import cercle
from pom import pom
from missile import missile
from caption import printCaption 
from previsionGra import previsionGra
from itertools import *

# pas sur que je veut faire ca.
class ship:
	def __init__(self, parPom, parGra, parCaption = ""):
		self.pom = parPom
		self.gra = parGra
		self.age = 0
		self.rayon = 4
		self.caption = parCaption
		self.tirPrevu = None
	def commande(self, nouveauPom):
		self.pom.addCommande(nouveauPom)
	def collision(self, other):
		if self.pom.distance(other.pom) < (self.rayon + other.rayon):
			# nombre arbitraire: un missile devient actif des qu'il a 4 secondes
			# sinon, on a une collision avec le tireur
			# ce qui est emmerdant pour plusieurs raisons
			if other.age > 1:
				return True
		else:
			return False	
	def collisionFuture(self, autre):
		for a, b in izip(self.tirPrevu.pom.previsions, autre.pom.previsions):
			if a.distance(b) < (self.rayon + autre.rayon):
				return a
		return None
	def planTir(self, centre, tick, instances):
		self.tirPrevu = missile(self.pom.addShooty(10))
		self.tirPrevu.pom.prevision(centre, tick, instances)			
		# print self.tirPrevu.pom.previsions
	def planSim(self, centre, tick, instances):
		self.pom.prevision(centre, tick, instances)	
		# print self.pom.previsions
	def sim(self, gravite, tick):
		self.pom.sim(gravite, tick)
		self.age += tick 
		return 0
	def render(self):
		self.gra.render(self.pom)
		printCaption(self.pom.px, self.pom.py, self.caption)
		if self.tirPrevu:
			previsionGra(self.tirPrevu.pom.previsions)
		if self.pom.previsions:
			previsionGra(self.pom.previsions)
	def shoot(self, veloc):
		if self.tirPrevu:
			nouveau = self.tirPrevu
			self.tirPrevu = []
		else:
			nouveau = missile(self.pom.addShooty(veloc))
		return nouveau
