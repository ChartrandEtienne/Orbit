from pom import pom
import OpenGL
from OpenGL.GL import *


class triangle(pom):
	def __init__(self, parRayon = 1):
		self.rayon = parRayon	
	def render(self, position):
		# print 'self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y'
		# print self.p.x, ',', self.p.y, ', ', self.v.x, ', ', self.v.y
		glLoadIdentity()
		glTranslate(position.px, position.py, 0)
		glRotate(position.getAngleDeg(), 0, 0, 1)
		r = self.rayon
		glBegin(GL_LINE_LOOP)
		glVertex2f(0, 0 + 2 * r)
		glVertex2f(0 - r, 0 - r)
		glVertex2f(0 + r, 0 - r)
		glEnd() 
		if position.previsions:
			glBegin(GL_LINE)
			for i in position.previsions:
				glVertex2f(i.px, i.py)
			glEnd()
			
