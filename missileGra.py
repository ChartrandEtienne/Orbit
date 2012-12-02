import OpenGL

from OpenGL.GL import *

from numpy import *

from pom import pom

class missileGra:
	def __init__(self):
		self.grandeur = 1 # pour ajuster la grandeur du machin, etc...
	def render(self, position):
		glLoadIdentity()
		glTranslate(position.px, position.py, 0)
		glRotate(position.getAngleDeg(), 0, 0, 1)
		glBegin(GL_LINE_STRIP)
		glVertex2f(0, self.grandeur)
		glVertex2f(0, 0)
		glVertex2f(self.grandeur / -3.0, self.grandeur / -2.0)
		glVertex2f(self.grandeur / 3.0, self.grandeur / -2.0)
		glVertex2f(0, 0)
		glEnd()
				
