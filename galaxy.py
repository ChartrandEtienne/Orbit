import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *


class galaxy:
	def __init__(self):
		self.vaisseaux = []
		self.armes = []
		self.planetes = []	
		self.tick = 0.032
		self.viseur = None
		self.vise = None
	def Tick(self):
		# self.vaisseaux[0].planTir(self.planetes[0].pom, self.tick, 40)
		# self.vaisseaux[1].planSim(self.planetes[0].pom, self.tick, 40)
		self.viseur = self.vaisseaux[0]
		self.vise = self.vaisseaux[1]
		# Mhkay
		self.viseur.planTir(self.planetes[0].pom, self.tick, 160)
		self.vise.planSim(self.planetes[0].pom, self.tick, 160)
		
		positionCollision = self.viseur.collisionFuture(self.vise)

		print positionCollision
		# if self.viseur.collisionFuture(self.
		# et c'est tout.
		for i in xrange(len(self.vaisseaux) - 1, -1, -1):
			if self.vaisseaux[i].sim(self.planetes[0].pom, self.tick):
				del self.vaisseaux[i]
		for i in xrange(len(self.armes) - 1, -1, -1):
			if self.armes[i].sim(self.planetes[0].pom, self.tick):
				del self.armes[i]
		cvp = [] # collisions vaisseaux-planetes
		cvm = [] # collisions vaisseaux-missiles
		cpm = [] # collisions planetes-missiles
		for i in self.planetes:
			for j in self.vaisseaux:
				if j.collision(i):
					cvp.append(j)
		for i in self.vaisseaux:
			for j in self.armes:
				if i.collision(j):
					cvm.append((i, j))
		for i in self.planetes:
			for j in self.armes:
				if j.collision(i):
					cpm.append(j)	

		# missile + planete = plus de missile.
		for i in cpm:
			self.armes.remove(i)
		# vaisseau + planete = plus de vaisseau 
		for i in cvp:
			self.vaisseaux.remove(i)
		# vaisseau + missle = ambigu. Disons destruction, pour le moment.
		for i in cvm:
			# bug ici: pour deux collisions detectees, tente d'enlever le vaisseau 2 fois
			self.vaisseaux.remove(i[0])
			self.armes.remove(i[1])
	def display(self):
		glMatrixMode(GL_MODELVIEW)
		glEnableClientState(GL_VERTEX_ARRAY)
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1, 0, 0)
		glLoadIdentity()
		for i in self.planetes:
			i.render()
		for i in self.vaisseaux:
			i.render()
		for i in self.armes:
			i.render()
#		glLoadIdentity()
#		glScale(0.015, 0.015, 1)
#		banane = "banane"
#		for i in banane:
#			glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(i)) 
		glFlush()
