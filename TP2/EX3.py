class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if montant <= self.solde:
            self.solde -= montant
        else:
            print("Solde insuffisant.")

    def afficher_solde(self):
        print(f"Solde actuel: {self.solde}DH")

compte = CompteBancaire("Abdelhamid", 1000)
compte.deposer(500)
compte.retirer(300)
compte.afficher_solde()
