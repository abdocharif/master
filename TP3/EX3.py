from abc import ABC,abstractmethod
from math import pi
class Forme(ABC):
    def __init__(self,list):
       self.list=list
    @abstractmethod
    def calculer_surface():
        pass
class Cercle(Forme):
    def __init__(self,r):
        self.r=r
    def calculer_surface(self):
        return pi*self.r**2
        
class Rectangle(Forme):
    def __init__(self,largeur,longeur):
        self.largeur=largeur
        self.longeur=longeur
    def calculer_surface(self):
       Sr= self.largeur*self.longeur
       return Sr
def afficher_surface(formes):
    for forme in formes:
         print(f"Surface de {type(forme).__name__}: {forme.calculer_surface()}")

# Exemple d'utilisation
formes = [Cercle(5), Rectangle(4, 6)]
afficher_surface(formes)



