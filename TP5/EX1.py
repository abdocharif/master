# Créez le fichier "exemple.txt" et ajoutez des lignes de texte manuellement.

# Script Python pour lire le fichier :
with open("Exemple.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Ligne {i}: {line.strip()}")
