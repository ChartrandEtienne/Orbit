import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *

def printCaption(px, py, caption):
	glLoadIdentity()
	glTranslate(px + 3, py, 0)
	glScale(0.015, 0.015, 1)
	for i in caption:
		glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(i))

