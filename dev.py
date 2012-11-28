#!/usr/bin/python -O
import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

from pom import pom
from triangle import triangle
from cercle import cercle
from ship import ship

class matrice:
	def __init__(self):
		self.m = projection = matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
	def projection(self, width, height):
		self.m[0][0] = 0.5 / width
		self.m[1][1] = 0.5 / height


def tick(foo):
	# Tri.sim(centre, 0.032)
	# Test.sim(centre, 0.032)	
	# Test.phy.sim(centre.phy, 0.032)
	for i in range(0, len(systemeSolaire)):
		systemeSolaire[i].phy.sim(centre.phy, 0.032)	
	glutPostRedisplay()
	glutTimerFunc(50, tick, 0)


def display():
	glMatrixMode(GL_MODELVIEW)
	glEnableClientState(GL_VERTEX_ARRAY)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 0, 0)
	glLoadIdentity()
	centre.render()
	for i in range(0, len(systemeSolaire)):
		systemeSolaire[i].render()
	# Test.render()
	# centre.render()
	glFlush()	

def init():
	glClearColor(0, 0, 0, 0)
	glLoadIdentity()
	
# centre = cercle(vector(0, 0), vector(0, 0), 10 ** 2)
centre = ship(pom(vector(0, 0), vector(0, 0), 10 ** 2), cercle(10, 20))
Test = ship(pom(vector(-20, 0), vector(0, 20)), cercle())
# centre.rayon = 10
# centre.smoothness = 20
systemeSolaire = []
# Test = cercle(vector(-20, 0), vector(0, 20))
#print len(systemeSolaire)
systemeSolaire.append(Test)
# systemeSolaire.append(cercle(vector(10, 0), vector(0, 25)))
#print len(systemeSolaire)
# weird shit
# systemeSolaire.append(cercle(vector(15, 10), vector(5, 15)))
#print len(systemeSolaire)

def keyboard(key, x, y):

	if key == 'q':
		sys.exit(0)
	if key == 's':
		systemeSolaire.append(systemeSolaire[0].shoot(vector(0, 5)))


def main():
	print "This. Is. Orbit."
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(250, 250)
	glutCreateWindow("test")
	init()
	glMatrixMode(GL_PROJECTION)
	matrice1 = matrice()
	matrice1.projection(50, 50)
	glLoadMatrixf(matrice1.m)
	glutDisplayFunc(display)
	glutKeyboardFunc(keyboard)
	glutTimerFunc(25, tick, 0)
	glutMainLoop()
	return	

main()
