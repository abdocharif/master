import json

# Dictionnaire Python avec des informations sur des étudiants.
etudiants = [
    {"Nom": "gourramt", "Âge": 20, "Note": 16},
    {"Nom": "Charif", "Âge": 21, "Note": 17},
    {"Nom": "Ait gourramt", "Âge": 22, "Note": 18}
]

with open("etudiants.json", "w") as file:
    json.dump(etudiants, file)

# Lecture du fichier JSON
with open("etudiants.json", "r") as file:
    data = json.load(file)
    for etudiant in data:
        print(etudiant)
