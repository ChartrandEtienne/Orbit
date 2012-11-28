from pom import pom


class triangle(pom):
	def __init__(self, parRayon = 1):
		self.rayon = parRayon	
	def render(self, position):
		# print 'self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y'
		# print self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y
		glLoadIdentity()
		glTranslate(position.x, position.y, 0)
		r = self.rayon
		glBegin(GL_LINE_LOOP)
		glVertex2f(self.p.x, self.p.y + r)
		glVertex2f(self.p.x - r, self.p.y - r)
		glVertex2f(self.p.x + r, self.p.y - r)
		glEnd() 
