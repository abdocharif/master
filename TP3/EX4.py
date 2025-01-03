class Produit():
    def __init__(self,nom,prix):
        self.__nom=nom
        self.__prix=prix
    def getnom(self):
        return self.__nom
    def getprix(self):
        return self.__prix
    def calculer_prix(self,remise):
        if self.__prix> 100 :
            return self.__prix * (1 - remise / 100)
        else:
            return self.__prix
produit = Produit("Telephone", 120)
print(produit.calculer_prix(10))