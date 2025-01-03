from abc import ABC,abstractmethod
class Vehicule(ABC):
    def __init__(self,marque):
        self.marque= marque

    @abstractmethod
    def Deplacer(self):
        pass

class Voiture(Vehicule):
    def Deplacer(self):
        return f"{self.marque} a 4 roues."
    
class Bicyclette(Vehicule):
    def Deplacer(self):
        return f"{self.marque} a 2 roues."
    
V1=Voiture("BMW")
V2=Voiture("audi")
B1=Bicyclette("Santacruz")
B2=Bicyclette("VTT")

vehicules =[V1, V2, B1, B2]

for vehicule in vehicules :
      print(vehicule.Deplacer())