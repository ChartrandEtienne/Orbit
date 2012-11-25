import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

from pom import pom

# tracer les planetes
class cercle(pom):
	def __init__(self, parPosition, parVelocite, parMasse=1, parRayon=1, parSmoothness = 10):
		self.p = parPosition
		self.v = parVelocite
		self.m = parMasse
		self.rayon = parRayon
		self.smoothness = parSmoothness
        def render(self):
                glLoadIdentity()
                glBegin(GL_LINE_LOOP)
                for i in range(0, self.smoothness):
                        angle = i * math.pi * 2.0 / self.smoothness
                        glVertex2f(self.p.x + self.rayon * math.cos(angle), self.p.y + self.rayon * math.sin(angle))
                glEnd()
