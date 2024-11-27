def compte_occurences(liste):
    occurrences = {}
    for mot in liste:
        if mot in occurrences:
            occurrences[mot] += 1
        else:
            occurrences[mot] = 1
    return occurrences
liste_mots = ["chat", "chien", "chat", "oiseau", "chien", "chien"]
resultat = compte_occurences(liste_mots)
print(resultat)
