from abc import ABC,abstractmethod
from math import pi
class Forme(ABC):
    def __init__(self):
       pass
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


R = Rectangle(1,1)
C = Cercle(2)
print("",R.calculer_surface())