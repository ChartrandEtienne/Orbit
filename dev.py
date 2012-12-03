#!/usr/bin/python -O
import sys
import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from numpy import *

from galaxy import galaxy
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
	galaxie.Tick()
 	glutPostRedisplay()
 	glutTimerFunc(50, tick, 0)



def init():
	glClearColor(0, 0, 0, 0)
	glLoadIdentity()

galaxie = galaxy()
	
centre = ship(pom(0, 0, 0, 0, 10 ** 2), cercle(10,20))
galaxie.planetes.append(centre)

# orbite rond
Test = ship(pom(-30, 0, 0, 14.8), triangle(), "hiro p.")
Test2 = ship(pom(-20, 0, 0, 18.166), triangle())

galaxie.vaisseaux.append(Test)
galaxie.vaisseaux.append(Test2)
# escape velocity
# Test = ship(pom(-10, 0, 0, 36.33), triangle())




# centre.rayon = 10
# centre.smoothness = 20
# systemeSolaire = []
# Test = cercle(vector(-20, 0), vector(0, 20))
#print len(systemeSolaire)
# systemeSolaire.append(Test)
# systemeSolaire.append(Test2)
# systemeSolaire.append(cercle(vector(10, 0), vector(0, 25)))
#print len(systemeSolaire)
# weird shit
# systemeSolaire.append(cercle(vector(15, 10), vector(5, 15)))
#print len(systemeSolaire)

def keyboard(key, x, y):
	# cette salete...
	# Je vais devoir inventer un format d'interface entre l'objet clavier
	# et l'objet galaxie. 
	if key == 'q':
		sys.exit(0)
	if key == 'p':
		# mhhhh... Le append ne devrait pas reellement etre la.
		galaxie.armes.append(galaxie.vaisseaux[0].shoot(10))
	if key == 'd':
		galaxie.vaisseaux[0].commande(pom(0, 0, 0, 0, 0, 0.1))
	if key == 'a':
		galaxie.vaisseaux[0].commande(pom(0, 0, 0, 0, 0, -0.1))
		


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
	glutDisplayFunc(galaxie.display)
	glutKeyboardFunc(keyboard)
	glutTimerFunc(25, tick, 0)
	glutMainLoop()
	return	

main()
