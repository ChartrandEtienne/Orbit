from pom import pom
import OpenGL
from OpenGL.GL import *

def previsionGra(previsions):
	glLoadIdentity()
	glBegin(GL_LINE_STRIP)
	for i in previsions:
		glVertex2f(i.px, i.py)
	glEnd()
