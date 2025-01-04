try:
    with open("inexistant.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")

