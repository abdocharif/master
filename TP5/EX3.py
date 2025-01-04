with open("phrases.txt", "a") as file:
    while input("Voulez-vous ajouter une phrase (oui/non)? ").lower() == "oui":
        phrase = input("Entrez une nouvelle phrase: ")
        file.write(phrase  + "\n")
