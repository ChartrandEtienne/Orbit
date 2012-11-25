#!/usr/bin/python -O
import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

from pom import pom
from vector import vector
from triangle import triangle
from cercle import cercle

class matrice:
	def __init__(self):
		self.m = projection = matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	def projection(self, width, height):
		self.m[0][0] = 0.5 / width
		self.m[1][1] = 0.5 / height


def tick(foo):
	# Tri.sim(centre, 0.032)
	Test.sim(centre, 0.01)	
	glutPostRedisplay()
	glutTimerFunc(5, tick, 0)

def display():
	glMatrixMode(GL_MODELVIEW)
	glEnableClientState(GL_VERTEX_ARRAY)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 0, 0)
	glLoadIdentity()
	Test.render()
	centre.render()
	glFlush()	

def init():
	glClearColor(0, 0, 0, 0)
	glLoadIdentity()
	
centre = cercle(vector(0, 0), vector(0, 0), 10 ** 2)
centre.rayon = 10
centre.smoothness = 20
systemeSolaire = []
Test = cercle(vector(-10, 0), vector(0, 20))
#print len(systemeSolaire)
# systemeSolaire.append(cercle(vector(10, 0), vector(0, 25)))
#print len(systemeSolaire)
# weird shit
# systemeSolaire.append(cercle(vector(15, 10), vector(5, 15)))
#print len(systemeSolaire)

def main():
	print "This. Is. Orbit."
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(250, 250)
	glutCreateWindow("test")
	init()
	glMatrixMode(GL_PROJECTION)
	matrice1 = matrice()
	matrice1.projection(100, 100)
	glLoadMatrixf(matrice1.m)
	glutDisplayFunc(display)
	glutTimerFunc(25, tick, 0)
	glutMainLoop()
	return	

main()
