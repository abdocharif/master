class Voiture: 
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(self.__dict__)

v1 = Voiture("BMW", "M3", 2012)
v2 = Voiture("BMW", "M4", 2011)
v3 = Voiture("BMW", "M5", 2015)

v1.afficher_info()
v3.afficher_info()
v2.afficher_info()
