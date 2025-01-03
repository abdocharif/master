class Employe():
    def __init__(self,nom,prenom,salaire):
        self.nom=nom
        self.prenom=prenom
        self.salaire=salaire
class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.emp_supervises = []

    def ajouter_emp(self,employe):
        if isinstance (employe, Employe):
            self.emp_supervises.append(employe)
        else :
            raise ValueError("L'objet doit être une instance de la classe Employe.")
    def afficher_emp_supervises(self):
        if self.emp_supervises :
             print(f"Employés supervisés par {self.prenom} {self.nom} :")
             for employe in self.emp_supervises:
                print(f"- {employe.prenom} {employe.nom}, Salaire: {employe.salaire:.2f}MAD")
        else :
            print(f"{self.prenom} {self.nom} ne supervise aucun employé.")

em1 = Employe("Ait gourramt","Abdelhamid",10000)
em2 = Employe("Charif","abdo",3000)


M = Manager("Bennani","Achraf",5000)

M.ajouter_emp(em1)
M.ajouter_emp(em2)

print(M.afficher_emp_supervises())


