# petite classe vecteur. Pratique pour stocker une position ou une velocite
class vector:
	def __init__(self, parX=0, parY=0):
		self.x = parX
		self.y = parY
	def add(self, autre):
		self.x += autre.x
		self.y += autre.y
