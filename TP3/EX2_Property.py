class Personne():
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom=nom
    nom = property(getnom,setnom)
    def getprenom(self):
        return self.__prenom
    def setprenom(self,prenom):
        self.__prenom=prenom
    prenom = property(getprenom,setprenom)
    def getage(self):
        return self.__age
    def setage(self,age):
        self.__age=age
    age = property(getage,setage)

p1=Personne("charif","abdo",20)
print(p1.nom,p1.prenom,p1.age)