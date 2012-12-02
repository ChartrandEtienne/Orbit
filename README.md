Space shooter basé sur une simulation physique rigoureuse. 

Codé en Python 2.7, avec PyOpenGL pour la partie graphique, et numpy pour quelques détails

url: https://github.com/ChartrandEtienne/Orbit.git

Si j'ai bien compris, voici l'ordre d'operation d'un commit: avant de commencer, cloner le projet dans un directory, commit quand une quantite raisonnable de travail a ete fait, puis pousser le projet sur le serveur une fois le travail termine. 

cloner le projet: git clone <url du projet>
avoir les updates: git pull
"commit" un changement: git commit -a
pousser les updates sur le serveur: git push -u

pour ajouter un fichier au projet, il suffit de creer un fichier, puis de faire: git add <nom du fichier>, puis de commit



DESING

Le point central du programme est (alors que le monde est toujours simple et ne comporte qu'un seul centre gravitationnel) le tableau "systemeSolaire". Chaque element qui veut faire partie de ce club select doit implementer les suivantes:

- Constructeur prenant un pom et une representation graphique, qui renvoie de toute evidence un objet valide selon les principes de cette liste. Habituellement, passe les arguments a la methode sim de son champ pom, qui veut dire point-of-mass. Il est parfois pratique d'utiliser tick pour une minuterie ou quelque chose du genre, mais self.pom.phy fait en general tout le boulot:
	def __init__(self, pom, gra):

- Methode sim, qui prends un pom qui va faire office de masse qui va exercer une gravitation sur self, et un tick qui est la periode de temps qui sera simulee durant un seul "frame". Accessoirement, sert a comminquer des messages en dehors du tableau: ceux qui revoient True (ou une autre valeur predeterminee) vont etre traites plus tard, et par cela je veut dire pour le moment supprimes du tableau:
	def sim(self, gravite, tick):

- Methode render, qui ne prends aucun param, et qui prends lui-meme en charge la tache de dessiner la representation graphique de self a l'ecran, selon sa position et son angle(pour le moment). Habituellement, passe le pom a la methode render de son champ gra, qui signifie "graphique", ou "graph" ou ce que vous voulez. 
	def render(self):

- Fonction collision, qui detecte si self touche a un autre objet: renvoie un bool, donc de toute evidence vrai si un collision s'est produite, faux si non:
	def collision(self, other):
	return bool

- Fonction shoot, qui va renvoyer un projectile quelconque; celui-ci aura tout d'abord la meme position et velocite que self, plus un vecteur specifique a l'arme en question, qui dependera d'ailleurs de l'angle de tir de self. L'objet retourne doit etre valide selon cette liste; il sera ajoute au tableau systemeSolaire. Aussi remarquer qu'il ne doit pas causer de collision avec self au lancement. Il n'est pas encore clair s'il est prerefable de rapporter une collision qui arrive plus tard, ou de rendre self immunise contre ses propres tirs; dans le doute, j'ai implemente le premier avec une simple minuterie. Les parametres ne sont absolument pas definitifs, mais toujours, mais pour le moment, je passe la vitesse de tir du nouveau projectile. 
	def shoot(self, vitesse):
	return (un vaisseau valide)

- Fonction command, qui va prendre un objet point-of-mass et modifier self.pom en consequence. Si l'utilisateur veut accelerer de x vers l'avant et tourner de y vers la gauche, lui passer un pom avec vy = x, a = y, et la fonction command va additionner le pom a self.pom. (aucune implementation valide encore) (va probablement changer vu que les donnees de pom ne sont pas les seules commandes que je vais envoyer a un vaisseau)


UPDATE: Je vais separer les vaisseaux et les armes. 
