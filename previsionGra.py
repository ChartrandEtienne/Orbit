from pom import pom
import OpenGL
from OpenGL.GL import *

def previsionGra(objet):
	glLoadIdentity()
	glBegin(GL_LINE_STRIP)
	for i in objet.previsions:
		glVertex2f(i.px, i.py)
	glEnd()
