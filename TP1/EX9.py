def analyse_texte(texte):

    # Supprimer les espaces superflus et diviser en mots
    mots = texte.split()
    # Compter les caractères (sans les espaces)
    caracteres = len(texte.replace(" ", ""))
    # Construire le dictionnaire des résultats
    resultat = {
        "nombre_de_mots": len(mots),
        "nombre_de_caracteres": caracteres
    }
    return resultat

texte = " Python est un langage de programmation puissant."
resultat = analyse_texte(texte)
print(resultat)
