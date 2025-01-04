import csv

# Création du fichier CSV avec des données d'exemple
fichier_csv = "contacts.csv"

# Données d'exemple
contacts = [
    ["Nom", "Age", "Ville"],
    ["Abdelhamid", "20", "Paris"],
    ["abdo", "25", "LA"],
    ["ait gourramt", "28", "new york"]
]
# Écriture des données dans le fichier CSV
with open(fichier_csv, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(contacts)
print(f"Le fichier '{fichier_csv}' a été créé avec succès !")

