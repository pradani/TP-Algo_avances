#!/usr/bin/python3

"""
Ce fichier contient tous les codes des sections du chapitre 2, algo avancés 2020/2021
Auteur: Prakasso Daniel 19B683FS
"""

def somme_entier(n):
	som = 0
	for i in range(n):
		som += i
	return som
class Element:
	"""docstring for Element"""
	def __init__(self):
		self.valeur = 0;
		self.suivant = None
class Liste:
	"""docstring for Liste"""
	def __init__(self):
		self.tete = None

	def ajouter(self, x):
		element = Element()
		element.valeur = x
		element.suivant = None
		if self.tete is None:
			self.tete = element
		else:
			el = self.tete
			self.tete = element
			element.suivant = el
def afficher(liste):
	d = liste.tete
	while (d is not None):
		print(d.valeur, end="--")
		d = d.suivant
	print("NULL")
if __name__ == '__main__':
	liste = Liste()
	x = 5
	liste.ajouter(x)
	liste.ajouter(3)
	liste.ajouter(10)
	afficher(liste)
		