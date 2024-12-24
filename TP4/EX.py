# class Vehicule:

class Vehicule :
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.module=modele
        self.annee=annee

    def afficher_info(self):
        print(f"la marque : {self.marque} , module : {self.module} et annee : {self.annee}")

# class Moteur

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Puissance: {self.puissance} , Type de moteur: {self.type_moteur}")

#class voiture :

class Voiture (Vehicule,Moteur) :
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Nombre de places: {self.nombre_de_places}")

#class Moto :

class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Type de moto: {self.type_moto}")


# instance de Voiture

voiture = Voiture("Hyundai", "accent", 2018, 137, "Diesel", 6)
print("Infos du voiture :")
voiture.afficher_info()

print("\n")

# instance de Moto
moto = Moto("Peugeot", "Fox", 1995, 49, "Essence", "normal")
print("Infos du moto :")
moto.afficher_info()