from pom import pom
# tracer les planetes
class cercle(pom):
        rayon = 1
        smoothness = 10
        def render(self):
                glLoadIdentity()
                glBegin(GL_LINE_LOOP)
                for i in range(0, self.smoothness):
                        angle = i * math.pi * 2.0 / self.smoothness
                        glVertex2f(self.p.x + self.rayon * math.cos(angle), self.p.y + self.rayon * math.sin(angle))
                glEnd()
