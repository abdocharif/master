# Script pour enregistrer des phrases dans un fichier :
phrases = [input(f"Entrez la phrase {i + 1}: ") for i in range(3)]

with open("phrases.txt", "w") as file:
    for phrase in phrases:
        file.write(phrase + "\n")
