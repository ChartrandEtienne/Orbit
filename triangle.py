from pom import pom


class triangle(pom):
	def render(self):
		# print 'self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y'
		# print self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y
		glLoadIdentity()
		glTranslate(self.p.x, self.p.y, 0)
		r = 1
		glBegin(GL_LINE_LOOP)
		glVertex2f(self.p.x, self.p.y + r)
		glVertex2f(self.p.x - r, self.p.y - r)
		glVertex2f(self.p.x + r, self.p.y - r)
		glEnd() 
