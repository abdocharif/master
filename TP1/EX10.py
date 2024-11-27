def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()  # Crée une copie du premier dictionnaire
    for cle, valeur in dict2.items():
        if cle in fusion:
            fusion[cle] += valeur  # Additionne les valeurs si la clé existe
        else:
            fusion[cle] = valeur  # Ajoute une nouvelle clé
    return fusion
# Exemple d'utilisation
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
resultat = fusionner_dicts(dict1, dict2)
print(resultat)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
