from cercle import cercle
from vector import vector
from pom import pom
class ship:
	def __init__(self, parPom, parGra):
		self.pom = parPom
		self.gra = parGra
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, nouveaux, nouveauy):
		nouveau = ship(self.pom.addShooty(nouveaux, nouveauy), cercle())
		# Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
		return nouveau
