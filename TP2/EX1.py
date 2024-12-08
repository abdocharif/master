class chien:
    def __init__(self,nom,race,age):
        self.nom=nom
        self.race=race
        self.age=age
    def aboyer(self):
        print("woof")

ch = chien("hawhaw","tt",16)
ch.aboyer()