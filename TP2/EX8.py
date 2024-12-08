class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        print("Liste d'amis :")
        for ami in self.amis:
            print("-",ami)

# Test
personne = Personne("abdelhamid", "Aitgourramt", 20)
personne.ajouter_ami("Abdo")
personne.ajouter_ami("charif")
personne.afficher_amis()
