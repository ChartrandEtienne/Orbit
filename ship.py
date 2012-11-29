from math import *
from cercle import cercle
from vector import vector
from pom import pom
class ship:
	def __init__(self, parPom, parGra, parAngle=45):
		self.pom = parPom
		self.gra = parGra
		self.a = parAngle * pi / 180
	def render(self):
		self.gra.render(self.pom)
	def shoot(self, veloc):
		# nouveau = ship(self.pom.addShooty((veloc * sin(self.a)) (veloc * cos(self.a)), cercle()))
		nouveau = ship(self.pom.addShooty(veloc * sin(self.a), veloc * cos(self.a)), cercle())
		# Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
		return nouveau
