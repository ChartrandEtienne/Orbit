import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

from pom import pom

# tracer les planetes
class cercle:
	def __init__(self, parRayon=1, parSmoothness = 10):
		self.rayon = parRayon
		self.smoothness = parSmoothness
        def render(self, position):
                glLoadIdentity()
                glBegin(GL_LINE_LOOP)
                for i in range(0, self.smoothness):
                        angle = i * math.pi * 2.0 / self.smoothness
                        glVertex2f(position.x + self.rayon * math.cos(angle), position.y + self.rayon * math.sin(angle))
                glEnd()
