list=[1,2,3,4]
def somme_liste(list):
    somme=0
    i=0
    for i in range(list[3]):
        somme=somme+list[i]
    return somme

print(somme_liste(list))